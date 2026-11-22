# Statement Audit report

Run: 2026-11-19T18:07 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM · ET at first dump: 11/19/2026, 6:02:51 PM

Verdicts: PASS 3849 · WRONG 2 (CRITICAL) · MISLEADING 3 (HIGH) · UNVERIFIED 337 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| RBOT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 2 signals, 0 up, 2 down, 0 flat | WRONG | CRITICAL | change 0.00%, close location 0.21, OBV falling |
| RBOT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.41× / 0.00× | 0.41× / 0.00× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| AVGC | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.3 | 19.1 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| COPX | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.9 | 28.7 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| DRAL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.3 | 34.6 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AAPL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.94× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.52× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AAPU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.00× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ABBV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.12× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AIPO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.07× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ALAB | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.5× 2.46× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.6× 2.64× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.23× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 229 252. 2025 -12 -22 1.6× 1.55× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| ANET.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.51× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASTL.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.26× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ATD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | U1 | numbers on the card no statement above claimed (exhaustive scan) | 101 252. 1.3× 1.28× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AVGC | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.9× 2.89× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AVGO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 229 252. 2025 -12 -22 1.9× 1.88× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| AVGO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.77× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BDT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.69× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BOTZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.14× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRK-B | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.67× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRKU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.95× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.3× 3.25× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.95× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CEG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.50× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CGY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.49× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.71× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.70× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COP | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.64× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.4× 2.42× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 192 252. 2.1× 2.09× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| COPZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.90× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COST | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.53× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COTG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.03× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CSU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.98× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CVX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 104 252. 4.7× 4.65× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 161 252. 1.5× 1.47× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.75× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DRIV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.00× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DUK | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.70× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ELIL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.93× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| EQIX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.23× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ETN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.2× 2.18× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| FCX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | X0 | Technical Read card | not found | card text | UNVERIFIED | INFO | card did not render |
| GDX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.31× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.69× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDXU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GEV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 229 252. 2025 -12 -22 1.4× 1.45× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| GEV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.22× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GGLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.61× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GIB-A.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.48× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GOOGL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.89× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GRID | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.92× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.81× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HURA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.48× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HXQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.32× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JNJ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.90× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JPM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.8× 1.80× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| KEYS | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.19× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| LIN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.22× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| LLY | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.62× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MDA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.71× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| META | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.43× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| METU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.22× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MRVL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.18× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MSFT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.68× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MSFU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 211 252. 2026 -01 -20 1.0× 1.02× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| MTRX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.60× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.76× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.48× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.93× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NFLX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NFXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.45× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NTR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.86× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NVDA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.6× 2.56× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NVDL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.89× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ONTO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 141 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ORBX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.75× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ORCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.87× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.95× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PLD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.34× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PNG.V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.02× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QCOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.32× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QPUX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.94× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QTUM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.90× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RTX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.84× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.26× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SETM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 148 252. 0.6× 0.55× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SGRD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.10× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SMH | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 135 252. 1.7× 1.69× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SNDK.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.80× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.4× 2.43× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.33× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 158 252. 1.2× 1.18× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SPCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.73× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.70× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.37× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.04× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UBOT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.49× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UFO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.37× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| URA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.11× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| URAA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.24× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.87× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| VFV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.09× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| VRT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 135 252. 1.2× 1.20× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| WDC.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.18× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WELL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.46× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.33× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XCHP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.1× 2.12× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XEQT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 211 252. 2026 -01 -20 3.0× 3.05× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| XETM.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.78× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XGD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.91× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $349.21 | $349.21 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $347.77 | $347.77 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 0.4% above | 0.4% above | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.75 | $7.75 (sr=7.7459) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.9 | -5.9 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $347.77, 0.4% | $347.77, 0.4% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $349.21 · Nov 19 | $349.21 · Nov 19 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $349.21 "After hours" | $349.21 "after hours" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $302.45, 15.5% | $302.45, 15.5% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $341.37, 2.3% | $341.37, 2.3% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $349.21 / entry $349.21 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.2 | 53.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +30.5% vs +9.2% | 30.5% vs 9.2% | PASS |  |  |
| AAPL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPL | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.2 | 17.2 | PASS |  | Wilder, completed bars |
| AAPL | T4w | words "20 or more / below 20" | below 20 | ADX 17.2 | PASS |  |  |
| AAPL | T5 | "counted at the last close ($X, date)" = last completed bar | $349.21, Nov 19 | $349.21, Nov 19 | PASS |  |  |
| AAPL | T6 | price vs 200-day average (S1 pattern sma values) | $349.21 vs $302.45 · +15.5% | $349.21 vs $302.45 · 15.5% | PASS |  |  |
| AAPL | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T7 | price vs 50-day average (S1 pattern sma values) | $349.21 vs $341.37 · +2.3% | $349.21 vs $341.37 · 2.3% | PASS |  |  |
| AAPL | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.3% over 30 td | +4.3% over 30 td | PASS |  |  |
| AAPL | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.2% below $360.83 | 3.2% below $360.83 | PASS |  | closing high would be 356.27 |
| AAPL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.2% below | PASS |  |  |
| AAPL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $360.83 | $360.8299865722656 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.92%, close location 0.31, OBV falling |
| AAPL | V2 | day change of the last completed bar | down 0.9% | -0.92% | PASS |  |  |
| AAPL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.94× / 0.41× | 0.94× / 0.41× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 39881727) | 20 bars, last ('2026-11-19', 39881727) | PASS |  |  |
| AAPU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $47.68 | $47.68 | PASS |  |  |
| AAPU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $47.63 | $47.63 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPU | E3 | percent from the 21-day average | 0.1% above | 0.1% above | PASS |  |  |
| AAPU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AAPU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.02 | $2.03 (sr=2.0246) | PASS |  | Wilder ATR14 |
| AAPU | E5 | distance in normal day-moves | 0.0 | 0.0 | PASS |  | gauge dot note uses the same number:  · 0.0 day-moves above |
| AAPU | L-ema21 | ladder row ema21: price and gap = price vs average | $47.63, 0.1% | $47.63, 0.1% | PASS |  |  |
| AAPU | L-note | "Last close $X · date" note = last completed bar | Last close $47.68 · Nov 19 | $47.68 · Nov 19 | PASS |  |  |
| AAPU | L-now | ladder price row = compared price; name = the basis label | $47.68 "After hours" | $47.68 "after hours" | PASS |  |  |
| AAPU | L-sma200 | ladder row sma200: price and gap = price vs average | $38.27, 24.6% | $38.27, 24.6% | PASS |  |  |
| AAPU | L-sma50 | ladder row sma50: price and gap = price vs average | $46.26, 3.1% | $46.26, 3.1% | PASS |  |  |
| AAPU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $47.68 / entry $47.68 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.5 | 51.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +45.9% vs +9.2% | 45.9% vs 9.2% | PASS |  |  |
| AAPU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPU | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.7 | 16.7 | PASS |  | Wilder, completed bars |
| AAPU | T4w | words "20 or more / below 20" | below 20 | ADX 16.7 | PASS |  |  |
| AAPU | T5 | "counted at the last close ($X, date)" = last completed bar | $47.68, Nov 19 | $47.68, Nov 19 | PASS |  |  |
| AAPU | T6 | price vs 200-day average (S1 pattern sma values) | $47.68 vs $38.27 · +24.6% | $47.68 vs $38.27 · 24.6% | PASS |  |  |
| AAPU | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T7 | price vs 50-day average (S1 pattern sma values) | $47.68 vs $46.26 · +3.1% | $47.68 vs $46.26 · 3.1% | PASS |  |  |
| AAPU | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.9% over 30 td | +6.9% over 30 td | PASS |  |  |
| AAPU | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.6% below $51.04 | 6.6% below $51.04 | PASS |  | closing high would be 49.81 |
| AAPU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.6% below | PASS |  |  |
| AAPU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $51.04 | $51.040000915527344 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.87%, close location 0.29, OBV falling |
| AAPU | V2 | day change of the last completed bar | down 1.9% | -1.87% | PASS |  |  |
| AAPU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.52× / 0.44× | 0.52× / 0.44× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 400372) | 20 bars, last ('2026-11-19', 400372) | PASS |  |  |
| ABBV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $283.54 | $283.54 | PASS |  |  |
| ABBV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $288.39 | $288.39 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ABBV | E3 | percent from the 21-day average | 1.7% below | 1.7% below | PASS |  |  |
| ABBV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ABBV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.71 | $6.71 (sr=6.7056) | PASS |  | Wilder ATR14 |
| ABBV | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| ABBV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -7.3 | -7.3 | PASS |  |  |
| ABBV | L-ema21 | ladder row ema21: price and gap = price vs average | $288.39, -1.7% | $288.39, -1.7% | PASS |  |  |
| ABBV | L-note | "Last close $X · date" note = last completed bar | Last close $283.54 · Nov 19 | $283.54 · Nov 19 | PASS |  |  |
| ABBV | L-now | ladder price row = compared price; name = the basis label | $283.54 "After hours" | $283.54 "after hours" | PASS |  |  |
| ABBV | L-sma200 | ladder row sma200: price and gap = price vs average | $239.6, 18.3% | $239.60, 18.3% | PASS |  |  |
| ABBV | L-sma50 | ladder row sma50: price and gap = price vs average | $277.64, 2.1% | $277.64, 2.1% | PASS |  |  |
| ABBV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $283.54 / entry $283.54 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ABBV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ABBV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.8 | 45.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ABBV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.4% vs +9.2% | 25.4% vs 9.2% | PASS |  |  |
| ABBV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ABBV | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.3 | 27.3 | PASS |  | Wilder, completed bars |
| ABBV | T4w | words "20 or more / below 20" | 20 or more | ADX 27.3 | PASS |  |  |
| ABBV | T5 | "counted at the last close ($X, date)" = last completed bar | $283.54, Nov 19 | $283.54, Nov 19 | PASS |  |  |
| ABBV | T6 | price vs 200-day average (S1 pattern sma values) | $283.54 vs $239.60 · +18.3% | $283.54 vs $239.60 · 18.3% | PASS |  |  |
| ABBV | T6w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T7 | price vs 50-day average (S1 pattern sma values) | $283.54 vs $277.64 · +2.1% | $283.54 vs $277.64 · 2.1% | PASS |  |  |
| ABBV | T7w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.6% over 30 td | +4.6% over 30 td | PASS |  |  |
| ABBV | T8r | word "rising" | still rising | rising | PASS |  |  |
| ABBV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ABBV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.4% below $302.93 | 6.4% below $302.93 | PASS |  | closing high would be 295.03 |
| ABBV | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.4% below | PASS |  |  |
| ABBV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.93 | $302.92999267578125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ABBV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.86%, close location 0.59, OBV falling |
| ABBV | V2 | day change of the last completed bar | down 0.9% | -0.86% | PASS |  |  |
| ABBV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ABBV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.00× / 0.36× | 1.00× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ABBV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4976690) | 20 bars, last ('2026-11-19', 4976690) | PASS |  |  |
| AIPO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $22.08 | $22.08 | PASS |  |  |
| AIPO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.0 | $24.00 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AIPO | E3 | percent from the 21-day average | 8.0% below | 8.0% below | PASS |  |  |
| AIPO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AIPO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.11 | $1.11 (sr=1.1057) | PASS |  | Wilder ATR14 |
| AIPO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| AIPO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.0 | +4.0 | PASS |  |  |
| AIPO | L-ema21 | ladder row ema21: price and gap = price vs average | $24, -8.0% | $24.00, -8.0% | PASS |  |  |
| AIPO | L-note | "Last close $X · date" note = last completed bar | Last close $22.08 · Nov 19 | $22.08 · Nov 19 | PASS |  |  |
| AIPO | L-now | ladder price row = compared price; name = the basis label | $22.08 "After hours" | $22.08 "after hours" | PASS |  |  |
| AIPO | L-sma200 | ladder row sma200: price and gap = price vs average | $28.48, -22.5% | $28.48, -22.5% | PASS |  |  |
| AIPO | L-sma50 | ladder row sma50: price and gap = price vs average | $26.3, -16.1% | $26.30, -16.1% | PASS |  |  |
| AIPO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $22.08 / entry $22.08 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AIPO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AIPO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.3 | 36.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AIPO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.2% vs +9.2% | -2.2% vs 9.2% | PASS |  |  |
| AIPO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AIPO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.6 | 32.6 | PASS |  | Wilder, completed bars |
| AIPO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.6 | PASS |  |  |
| AIPO | T5 | "counted at the last close ($X, date)" = last completed bar | $22.08, Nov 19 | $22.08, Nov 19 | PASS |  |  |
| AIPO | T6 | price vs 200-day average (S1 pattern sma values) | $22.08 vs $28.48 · -22.5% | $22.08 vs $28.48 · -22.5% | PASS |  |  |
| AIPO | T6w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T7 | price vs 50-day average (S1 pattern sma values) | $22.08 vs $26.30 · -16.0% | $22.08 vs $26.30 · -16.1% | PASS |  |  |
| AIPO | T7w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.6% over 30 td | +0.5% over 30 td | PASS |  |  |
| AIPO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AIPO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AIPO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.5% below $34.79 | 36.5% below $34.79 | PASS |  | closing high would be 34.77 |
| AIPO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.5% below | PASS |  |  |
| AIPO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $34.79 | $34.79 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AIPO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.69%, close location 0.02, OBV falling |
| AIPO | V2 | day change of the last completed bar | down 2.7% | -2.69% | PASS |  |  |
| AIPO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0234) | PASS |  |  |
| AIPO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AIPO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.12× / 0.54× | 1.12× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AIPO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1842571) | 20 bars, last ('2026-11-19', 1842571) | PASS |  |  |
| ALAB | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $211.60 | $211.60 | PASS |  |  |
| ALAB | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $236.32 | $236.32 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ALAB | E3 | percent from the 21-day average | 10.5% below | 10.5% below | PASS |  |  |
| ALAB | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ALAB | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $23.31 | $23.31 (sr=23.3111) | PASS |  | Wilder ATR14 |
| ALAB | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| ALAB | L-ema21 | ladder row ema21: price and gap = price vs average | $236.32, -10.5% | $236.32, -10.5% | PASS |  |  |
| ALAB | L-note | "Last close $X · date" note = last completed bar | Last close $211.60 · Nov 19 | $211.60 · Nov 19 | PASS |  |  |
| ALAB | L-now | ladder price row = compared price; name = the basis label | $211.6 "After hours" | $211.60 "after hours" | PASS |  |  |
| ALAB | L-sma200 | ladder row sma200: price and gap = price vs average | $258.64, -18.2% | $258.64, -18.2% | PASS |  |  |
| ALAB | L-sma50 | ladder row sma50: price and gap = price vs average | $287.43, -26.4% | $287.43, -26.4% | PASS |  |  |
| ALAB | S5-price | S5: the same live price reads the same on the header and the Entry block | header $211.60 / entry $211.60 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ALAB | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ALAB | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.5 | 39.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ALAB | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.0% vs +9.2% | 49.0% vs 9.2% | PASS |  |  |
| ALAB | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ALAB | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.0 | 28.0 | PASS |  | Wilder, completed bars |
| ALAB | T4w | words "20 or more / below 20" | 20 or more | ADX 28.0 | PASS |  |  |
| ALAB | T5 | "counted at the last close ($X, date)" = last completed bar | $211.60, Nov 19 | $211.60, Nov 19 | PASS |  |  |
| ALAB | T6 | price vs 200-day average (S1 pattern sma values) | $211.60 vs $258.64 · -18.2% | $211.60 vs $258.64 · -18.2% | PASS |  |  |
| ALAB | T6w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T7 | price vs 50-day average (S1 pattern sma values) | $211.60 vs $287.43 · -26.4% | $211.60 vs $287.43 · -26.4% | PASS |  |  |
| ALAB | T7w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.3% over 30 td | +5.3% over 30 td | PASS |  |  |
| ALAB | T8r | word "rising" | still rising | rising | PASS |  |  |
| ALAB | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ALAB | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 57.6% below $499.48 | 57.6% below $499.48 | PASS |  | closing high would be 483.02 |
| ALAB | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 57.6% below | PASS |  |  |
| ALAB | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $499.48 | $499.4762 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ALAB | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.38%, close location 0.01, OBV falling |
| ALAB | V2 | day change of the last completed bar | down 2.4% | -2.38% | PASS |  |  |
| ALAB | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0111) | PASS |  |  |
| ALAB | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ALAB | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.07× / 0.22× | 1.07× / 0.22× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ALAB | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4937851) | 20 bars, last ('2026-11-19', 4937851) | PASS |  |  |
| AMD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $489.19 | $489.19 | PASS |  |  |
| AMD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $520.9 | $520.90 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD | E3 | percent from the 21-day average | 6.1% below | 6.1% below | PASS |  |  |
| AMD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $43.48 | $43.48 (sr=43.4822) | PASS |  | Wilder ATR14 |
| AMD | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| AMD | L-ema21 | ladder row ema21: price and gap = price vs average | $520.9, -6.1% | $520.90, -6.1% | PASS |  |  |
| AMD | L-note | "Last close $X · date" note = last completed bar | Last close $489.19 · Nov 19 | $489.19 · Nov 19 | PASS |  |  |
| AMD | L-now | ladder price row = compared price; name = the basis label | $489.19 "After hours" | $489.19 "after hours" | PASS |  |  |
| AMD | L-sma200 | ladder row sma200: price and gap = price vs average | $428.63, 14.1% | $428.63, 14.1% | PASS |  |  |
| AMD | L-sma50 | ladder row sma50: price and gap = price vs average | $554.93, -11.8% | $554.93, -11.8% | PASS |  |  |
| AMD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $489.19 / entry $489.19 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.2 | 45.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +118.8% vs +9.2% | 118.8% vs 9.2% | PASS |  |  |
| AMD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.3 | 17.3 | PASS |  | Wilder, completed bars |
| AMD | T4w | words "20 or more / below 20" | below 20 | ADX 17.3 | PASS |  |  |
| AMD | T5 | "counted at the last close ($X, date)" = last completed bar | $489.19, Nov 19 | $489.19, Nov 19 | PASS |  |  |
| AMD | T6 | price vs 200-day average (S1 pattern sma values) | $489.19 vs $428.63 · +14.1% | $489.19 vs $428.63 · 14.1% | PASS |  |  |
| AMD | T6w | word "Above" | Above | Above | PASS |  |  |
| AMD | T7 | price vs 50-day average (S1 pattern sma values) | $489.19 vs $554.93 · -11.8% | $489.19 vs $554.93 · -11.8% | PASS |  |  |
| AMD | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.8% over 30 td | +11.8% over 30 td | PASS |  |  |
| AMD | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 25.7% below $658.52 | 25.7% below $658.52 | PASS |  | closing high would be 649.42 |
| AMD | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 25.7% below | PASS |  |  |
| AMD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $658.52 | $658.52 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -7.72%, close location 0.22, OBV flat |
| AMD | V2 | day change of the last completed bar | down 7.7% | -7.72% | PASS |  |  |
| AMD | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2206) | PASS |  |  |
| AMD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| AMD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.46× / 0.87× | 2.46× / 0.87× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 71050784) | 20 bars, last ('2026-11-19', 71050784) | PASS |  |  |
| AMD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.59 | $12.59 | PASS |  |  |
| AMD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.41 | $13.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD.TO | E3 | percent from the 21-day average | 6.1% below | 6.1% below | PASS |  |  |
| AMD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AMD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.10 | $1.10 (sr=1.0987) | PASS |  | Wilder ATR14 |
| AMD.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| AMD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $13.41, -6.1% | $13.41, -6.1% | PASS |  |  |
| AMD.TO | L-now | ladder price row = compared price; name = the basis label | $12.59 "Last close" | $12.59 "last close" | PASS |  |  |
| AMD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $11.06, 13.8% | $11.06, 13.8% | PASS |  |  |
| AMD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $14.25, -11.7% | $14.25, -11.7% | PASS |  |  |
| AMD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.1 | 45.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +113.4% vs +9.2% | 113.4% vs 9.2% | PASS |  |  |
| AMD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.8 | 17.8 | PASS |  | Wilder, completed bars |
| AMD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 17.8 | PASS |  |  |
| AMD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $12.59 vs $11.06 · +13.8% | $12.59 vs $11.06 · 13.8% | PASS |  |  |
| AMD.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| AMD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $12.59 vs $14.25 · -11.6% | $12.59 vs $14.25 · -11.7% | PASS |  |  |
| AMD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.5% over 30 td | +11.6% over 30 td | PASS |  |  |
| AMD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 25.8% below $16.97 | 25.8% below $16.97 | PASS |  | closing high would be 16.73 |
| AMD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 25.8% below | PASS |  |  |
| AMD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $16.97 | $16.968570709228516 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -7.56%, close location 0.22, OBV rising |
| AMD.TO | V2 | day change of the last completed bar | down 7.6% | -7.56% | PASS |  |  |
| AMD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2222) | PASS |  |  |
| AMD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AMD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.64× / 0.87× | 2.64× / 0.87× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 6134838) | 20 bars, last ('2026-11-19', 6134838) | PASS |  |  |
| AMZN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $257.37 | $257.37 | PASS |  |  |
| AMZN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $259.53 | $259.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZN | E3 | percent from the 21-day average | 0.8% below | 0.8% below | PASS |  |  |
| AMZN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.61 | $9.61 (sr=9.6081) | PASS |  | Wilder ATR14 |
| AMZN | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| AMZN | L-ema21 | ladder row ema21: price and gap = price vs average | $259.53, -0.8% | $259.53, -0.8% | PASS |  |  |
| AMZN | L-note | "Last close $X · date" note = last completed bar | Last close $257.37 · Nov 19 | $257.37 · Nov 19 | PASS |  |  |
| AMZN | L-now | ladder price row = compared price; name = the basis label | $257.37 "After hours" | $257.37 "after hours" | PASS |  |  |
| AMZN | L-sma200 | ladder row sma200: price and gap = price vs average | $245.03, 5.0% | $245.03, 5.0% | PASS |  |  |
| AMZN | L-sma50 | ladder row sma50: price and gap = price vs average | $255.23, 0.8% | $255.23, 0.8% | PASS |  |  |
| AMZN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $257.37 / entry $257.37 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.0 | 49.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.6% vs +9.2% | 15.6% vs 9.2% | PASS |  |  |
| AMZN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZN | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.5 | 11.5 | PASS |  | Wilder, completed bars |
| AMZN | T4w | words "20 or more / below 20" | below 20 | ADX 11.5 | PASS |  |  |
| AMZN | T5 | "counted at the last close ($X, date)" = last completed bar | $257.37, Nov 19 | $257.37, Nov 19 | PASS |  |  |
| AMZN | T6 | price vs 200-day average (S1 pattern sma values) | $257.37 vs $245.03 · +5.0% | $257.37 vs $245.03 · 5.0% | PASS |  |  |
| AMZN | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T7 | price vs 50-day average (S1 pattern sma values) | $257.37 vs $255.23 · +0.8% | $257.37 vs $255.23 · 0.8% | PASS |  |  |
| AMZN | T7w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| AMZN | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMZN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.4% below $287.20 | 10.4% below $287.20 | PASS |  | closing high would be 284.02 |
| AMZN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.4% below | PASS |  |  |
| AMZN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $287.20 | $287.20001220703125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.87%, close location 0.04, OBV falling |
| AMZN | V2 | day change of the last completed bar | down 3.9% | -3.87% | PASS |  |  |
| AMZN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0359) | PASS |  |  |
| AMZN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.23× / 1.04× | 1.23× / 1.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 52082830) | 20 bars, last ('2026-11-19', 52082830) | PASS |  |  |
| AMZU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $34.95 | $34.95 | PASS |  |  |
| AMZU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $36.01 | $36.01 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZU | E3 | percent from the 21-day average | 2.9% below | 2.9% below | PASS |  |  |
| AMZU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.65 | $2.65 (sr=2.6462) | PASS |  | Wilder ATR14 |
| AMZU | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| AMZU | L-ema21 | ladder row ema21: price and gap = price vs average | $36.01, -2.9% | $36.01, -2.9% | PASS |  |  |
| AMZU | L-note | "Last close $X · date" note = last completed bar | Last close $34.95 · Nov 19 | $34.95 · Nov 19 | PASS |  |  |
| AMZU | L-now | ladder price row = compared price; name = the basis label | $34.95 "After hours" | $34.95 "after hours" | PASS |  |  |
| AMZU | L-sma200 | ladder row sma200: price and gap = price vs average | $34.93, 0.0% | $34.93, 0.0% | PASS |  |  |
| AMZU | L-sma50 | ladder row sma50: price and gap = price vs average | $35.31, -1.0% | $35.31, -1.0% | PASS |  |  |
| AMZU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $34.95 / entry $34.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.4 | 47.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +7.5% vs +9.2% | 7.5% vs 9.2% | PASS |  |  |
| AMZU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZU | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.4 | 11.4 | PASS |  | Wilder, completed bars |
| AMZU | T4w | words "20 or more / below 20" | below 20 | ADX 11.4 | PASS |  |  |
| AMZU | T5 | "counted at the last close ($X, date)" = last completed bar | $34.95, Nov 19 | $34.95, Nov 19 | PASS |  |  |
| AMZU | T6 | price vs 200-day average (S1 pattern sma values) | $34.95 vs $34.93 · +0.1% | $34.95 vs $34.93 · 0.0% | PASS |  |  |
| AMZU | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZU | T7 | price vs 50-day average (S1 pattern sma values) | $34.95 vs $35.31 · -1.0% | $34.95 vs $35.31 · -1.0% | PASS |  |  |
| AMZU | T7w | word "Below" | Below | Below | PASS |  |  |
| AMZU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.2% over 30 td | -0.2% over 30 td | PASS |  |  |
| AMZU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AMZU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 25.1% below $46.64 | 25.1% below $46.64 | PASS |  | closing high would be 45.45 |
| AMZU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 25.1% below | PASS |  |  |
| AMZU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.64 | $46.64482080439608 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.81%, close location 0.02, OBV falling |
| AMZU | V2 | day change of the last completed bar | down 7.8% | -7.81% | PASS |  |  |
| AMZU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0205) | PASS |  |  |
| AMZU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 1.03× | 0.88× / 1.03× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1692366) | 20 bars, last ('2026-11-19', 1692366) | PASS |  |  |
| ANET.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $33.90 | $33.90 | PASS |  |  |
| ANET.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.46 | $33.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ANET.TO | E3 | percent from the 21-day average | 1.3% above | 1.3% above | PASS |  |  |
| ANET.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ANET.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.98 | $1.98 (sr=1.9823) | PASS |  | Wilder ATR14 |
| ANET.TO | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| ANET.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $33.46, 1.3% | $33.46, 1.3% | PASS |  |  |
| ANET.TO | L-now | ladder price row = compared price; name = the basis label | $33.9 "Last close" | $33.90 "last close" | PASS |  |  |
| ANET.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $30.22, 12.2% | $30.22, 12.2% | PASS |  |  |
| ANET.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $34.4, -1.4% | $34.40, -1.4% | PASS |  |  |
| ANET.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.2 | 51.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ANET.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +42.2% vs +9.2% | 42.2% vs 9.2% | PASS |  |  |
| ANET.TO | T3w | words "past year" vs the window used | 228 / 251 bars back | 250-253 bars | PASS |  |  |
| ANET.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.3 | 17.3 | PASS |  | Wilder, completed bars |
| ANET.TO | T4w | words "20 or more / below 20" | below 20 | ADX 17.3 | PASS |  |  |
| ANET.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.19%, close location 0.00, OBV falling |
| ANET.TO | V2 | day change of the last completed bar | down 2.2% | -2.19% | PASS |  |  |
| ANET.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| ANET.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ANET.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.55× / 0.37× | 1.55× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ANET.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 75262) | 20 bars, last ('2026-11-19', 75262) | PASS |  |  |
| ANET.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.55, OBV falling | condition true | PASS |  |  |
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
| ASML.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +47.6% vs +9.2% | 47.6% vs 9.2% | PASS |  |  |
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
| ASML.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-18 | 0.88× from 2026-11-18 | PASS |  | window "50 bars" includes the bar itself |
| ASML.TO | V6 | Volume detail: last session date and RVOL | 2026-11-18 0.88× | 2026-11-18 0.88× | PASS |  |  |
| ASML.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.24× | 0.88× / 0.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASML.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 39767) | 20 bars, last ('2026-11-18', 39767) | PASS |  |  |
| ASTL.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $6.90 | $6.90 | PASS |  |  |
| ASTL.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $7.21 | $7.21 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASTL.TO | E3 | percent from the 21-day average | 4.2% below | 4.2% below | PASS |  |  |
| ASTL.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ASTL.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.42 | $0.42 (sr=0.4201) | PASS |  | Wilder ATR14 |
| ASTL.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| ASTL.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $7.21, -4.2% | $7.21, -4.2% | PASS |  |  |
| ASTL.TO | L-note | "Last close $X · date" note = last completed bar | Last close $6.90 · Nov 19 | $6.90 · Nov 19 | PASS |  |  |
| ASTL.TO | L-now | ladder price row = compared price; name = the basis label | $6.9 "After hours" | $6.90 "after hours" | PASS |  |  |
| ASTL.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $6.27, 10.1% | $6.27, 10.1% | PASS |  |  |
| ASTL.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $6.54, 5.5% | $6.54, 5.5% | PASS |  |  |
| ASTL.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $6.90 / entry $6.90 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ASTL.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASTL.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.8 | 46.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASTL.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +42.6% vs +9.2% | 42.6% vs 9.2% | PASS |  |  |
| ASTL.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASTL.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.9 | 25.0 | PASS |  | Wilder, completed bars |
| ASTL.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.0 | PASS |  |  |
| ASTL.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $6.90, Nov 19 | $6.90, Nov 19 | PASS |  |  |
| ASTL.TO | T6 | price vs 200-day average (S1 pattern sma values) | $6.90 vs $6.27 · +10.0% | $6.90 vs $6.27 · 10.1% | PASS |  |  |
| ASTL.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| ASTL.TO | T7 | price vs 50-day average (S1 pattern sma values) | $6.90 vs $6.54 · +5.5% | $6.90 vs $6.54 · 5.5% | PASS |  |  |
| ASTL.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| ASTL.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.5% over 30 td | +2.4% over 30 td | PASS |  |  |
| ASTL.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASTL.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASTL.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.0% below $8.31 | 17.0% below $8.31 | PASS |  | closing high would be 8.22 |
| ASTL.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.0% below | PASS |  |  |
| ASTL.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $8.31 | $8.3100004196167 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASTL.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.58%, close location 0.32, OBV falling |
| ASTL.TO | V2 | day change of the last completed bar | down 0.6% | -0.58% | PASS |  |  |
| ASTL.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASTL.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.51× / 0.10× | 0.51× / 0.09× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASTL.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 306753) | 20 bars, last ('2026-11-19', 306753) | PASS |  |  |
| ATD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $80.14 | $80.14 | PASS |  |  |
| ATD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $82.31 | $82.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ATD.TO | E3 | percent from the 21-day average | 2.6% below | 2.6% below | PASS |  |  |
| ATD.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ATD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.77 | $1.77 (sr=1.7668) | PASS |  | Wilder ATR14 |
| ATD.TO | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| ATD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $82.31, -2.6% | $82.31, -2.6% | PASS |  |  |
| ATD.TO | L-note | "Last close $X · date" note = last completed bar | Last close $80.14 · Nov 19 | $80.14 · Nov 19 | PASS |  |  |
| ATD.TO | L-now | ladder price row = compared price; name = the basis label | $80.14 "After hours" | $80.14 "after hours" | PASS |  |  |
| ATD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $82.46, -2.8% | $82.46, -2.8% | PASS |  |  |
| ATD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $80.82, -0.8% | $80.82, -0.8% | PASS |  |  |
| ATD.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $80.14 / entry $80.14 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ATD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ATD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.7 | 41.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ATD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +17.1% vs +9.2% | 17.1% vs 9.2% | PASS |  |  |
| ATD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ATD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.5 | 15.5 | PASS |  | Wilder, completed bars |
| ATD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.5 | PASS |  |  |
| ATD.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $80.14, Nov 19 | $80.14, Nov 19 | PASS |  |  |
| ATD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $80.14 vs $82.46 · -2.8% | $80.14 vs $82.46 · -2.8% | PASS |  |  |
| ATD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| ATD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $80.14 vs $80.82 · -0.8% | $80.14 vs $80.82 · -0.8% | PASS |  |  |
| ATD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| ATD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| ATD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ATD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ATD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 15.4% below $94.68 | 15.4% below $94.68 | PASS |  | closing high would be 93.29 |
| ATD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 15.4% below | PASS |  |  |
| ATD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $94.68 | $94.67526234045502 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ATD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.45%, close location 0.07, OBV falling |
| ATD.TO | V2 | day change of the last completed bar | down 3.5% | -3.45% | PASS |  |  |
| ATD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0702) | PASS |  |  |
| ATD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ATD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.26× / 1.56× | 1.26× / 1.56× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ATD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1659480) | 20 bars, last ('2026-11-19', 1659480) | PASS |  |  |
| AVGC | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $18.88 | $18.88 | PASS |  |  |
| AVGC | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.42 | $18.42 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGC | E3 | percent from the 21-day average | 2.5% above | 2.5% above | PASS |  |  |
| AVGC | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AVGC | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.71 | $1.71 (sr=1.7114) | PASS |  | Wilder ATR14 |
| AVGC | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| AVGC | L-ema21 | ladder row ema21: price and gap = price vs average | $18.42, 2.5% | $18.42, 2.5% | PASS |  |  |
| AVGC | L-note | "Last close $X · date" note = last completed bar | Last close $18.88 · Nov 19 | $18.88 · Nov 19 | PASS |  |  |
| AVGC | L-now | ladder price row = compared price; name = the basis label | $18.88 "After hours" | $18.88 "after hours" | PASS |  |  |
| AVGC | L-sma50 | ladder row sma50: price and gap = price vs average | $19.58, -3.6% | $19.58, -3.6% | PASS |  |  |
| AVGC | S5-price | S5: the same live price reads the same on the header and the Entry block | header $18.88 / entry $18.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AVGC | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.8 | 50.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGC | T4w | words "20 or more / below 20" | below 20 | ADX 19.1 | PASS |  |  |
| AVGC | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -4.07%, close location 0.00, OBV rising |
| AVGC | V2 | day change of the last completed bar | down 4.1% | -4.07% | PASS |  |  |
| AVGC | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| AVGC | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGC | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.28× / 0.45× | 1.28× / 0.45× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGC | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4018) | 20 bars, last ('2026-11-19', 4018) | PASS |  |  |
| AVGO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $346.65 | $346.65 | PASS |  |  |
| AVGO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $338.31 | $338.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO | E3 | percent from the 21-day average | 2.5% above | 2.5% above | PASS |  |  |
| AVGO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AVGO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $18.04 | $18.04 (sr=18.0376) | PASS |  | Wilder ATR14 |
| AVGO | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| AVGO | L-ema21 | ladder row ema21: price and gap = price vs average | $338.31, 2.5% | $338.31, 2.5% | PASS |  |  |
| AVGO | L-note | "Last close $X · date" note = last completed bar | Last close $346.55 · Nov 19 | $346.55 · Nov 19 | PASS |  |  |
| AVGO | L-now | ladder price row = compared price; name = the basis label | $346.65 "After hours" | $346.65 "after hours" | PASS |  |  |
| AVGO | L-sma200 | ladder row sma200: price and gap = price vs average | $366.94, -5.5% | $366.94, -5.5% | PASS |  |  |
| AVGO | L-sma50 | ladder row sma50: price and gap = price vs average | $343.79, 0.8% | $343.79, 0.8% | PASS |  |  |
| AVGO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $346.65 / entry $346.65 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AVGO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AVGO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 52.5 | 52.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.5% vs +9.2% | -1.5% vs 9.2% | PASS |  |  |
| AVGO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.2 | 19.2 | PASS |  | Wilder, completed bars |
| AVGO | T4w | words "20 or more / below 20" | below 20 | ADX 19.2 | PASS |  |  |
| AVGO | T5 | "counted at the last close ($X, date)" = last completed bar | $346.55, Nov 19 | $346.55, Nov 19 | PASS |  |  |
| AVGO | T6 | price vs 200-day average (S1 pattern sma values) | $346.55 vs $366.94 · -5.6% | $346.55 vs $366.94 · -5.6% | PASS |  |  |
| AVGO | T6w | word "Below" | Below | Below | PASS |  |  |
| AVGO | T7 | price vs 50-day average (S1 pattern sma values) | $346.55 vs $343.79 · +0.8% | $346.55 vs $343.79 · 0.8% | PASS |  |  |
| AVGO | T7w | word "Above" | Above | Above | PASS |  |  |
| AVGO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.0% over 30 td | -0.0% over 30 td | PASS |  |  |
| AVGO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AVGO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AVGO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.7% below $493.29 | 29.7% below $493.29 | PASS |  | closing high would be 479.91 |
| AVGO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.7% below | PASS |  |  |
| AVGO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $493.29 | $493.29416 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AVGO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.12%, close location 0.06, OBV falling |
| AVGO | V2 | day change of the last completed bar | down 2.1% | -2.12% | PASS |  |  |
| AVGO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0585) | PASS |  |  |
| AVGO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AVGO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.89× / 0.41× | 2.89× / 0.41× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 75713346) | 20 bars, last ('2026-11-19', 75713346) | PASS |  |  |
| AVGO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.89, OBV falling | condition true | PASS |  |  |
| AVGO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $13.13 | $13.13 | PASS |  |  |
| AVGO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $12.82 | $12.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO.TO | E3 | percent from the 21-day average | 2.4% above | 2.4% above | PASS |  |  |
| AVGO.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AVGO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.66 | $0.66 (sr=0.6642) | PASS |  | Wilder ATR14 |
| AVGO.TO | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| AVGO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $12.82, 2.4% | $12.82, 2.4% | PASS |  |  |
| AVGO.TO | L-now | ladder price row = compared price; name = the basis label | $13.13 "Last close" | $13.13 "last close" | PASS |  |  |
| AVGO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $14.02, -6.4% | $14.02, -6.4% | PASS |  |  |
| AVGO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $13.06, 0.5% | $13.06, 0.5% | PASS |  |  |
| AVGO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 52.5 | 52.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -0.4% vs +9.2% | -0.4% vs 9.2% | PASS |  |  |
| AVGO.TO | T3w | words "past year" vs the window used | 228 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.5 | 19.5 | PASS |  | Wilder, completed bars |
| AVGO.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.5 | PASS |  |  |
| AVGO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.94%, close location 0.06, OBV rising |
| AVGO.TO | V2 | day change of the last completed bar | down 1.9% | -1.94% | PASS |  |  |
| AVGO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0562) | PASS |  |  |
| AVGO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.88× / 0.38× | 1.88× / 0.38× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2226761) | 20 bars, last ('2026-11-19', 2226761) | PASS |  |  |
| BDT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $71.42 | $71.42 | PASS |  |  |
| BDT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.67 | $73.67 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BDT.TO | E3 | percent from the 21-day average | 3.1% below | 3.1% below | PASS |  |  |
| BDT.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BDT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.98 | $3.98 (sr=3.9797) | PASS |  | Wilder ATR14 |
| BDT.TO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| BDT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $73.67, -3.1% | $73.67, -3.1% | PASS |  |  |
| BDT.TO | L-note | "Last close $X · date" note = last completed bar | Last close $71.42 · Nov 19 | $71.42 · Nov 19 | PASS |  |  |
| BDT.TO | L-now | ladder price row = compared price; name = the basis label | $71.42 "After hours" | $71.42 "after hours" | PASS |  |  |
| BDT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.98, 21.1% | $58.98, 21.1% | PASS |  |  |
| BDT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $76.18, -6.2% | $76.18, -6.2% | PASS |  |  |
| BDT.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $71.42 / entry $71.42 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BDT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BDT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.5 | 45.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BDT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +180.2% vs +9.2% | 180.2% vs 9.2% | PASS |  |  |
| BDT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BDT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.1 | 13.1 | PASS |  | Wilder, completed bars |
| BDT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 13.1 | PASS |  |  |
| BDT.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $71.42, Nov 19 | $71.42, Nov 19 | PASS |  |  |
| BDT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $71.42 vs $58.98 · +21.1% | $71.42 vs $58.98 · 21.1% | PASS |  |  |
| BDT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| BDT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $71.42 vs $76.18 · -6.2% | $71.42 vs $76.18 · -6.2% | PASS |  |  |
| BDT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| BDT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +12.9% over 30 td | +12.9% over 30 td | PASS |  |  |
| BDT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| BDT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BDT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.4% below $86.42 | 17.4% below $86.42 | PASS |  | closing high would be 85.33 |
| BDT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.4% below | PASS |  |  |
| BDT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $86.42 | $86.42048390957993 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BDT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.23%, close location 0.17, OBV falling |
| BDT.TO | V2 | day change of the last completed bar | down 2.2% | -2.23% | PASS |  |  |
| BDT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1678) | PASS |  |  |
| BDT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BDT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.77× / 0.40× | 0.77× / 0.40× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BDT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 322037) | 20 bars, last ('2026-11-19', 322037) | PASS |  |  |
| BOTZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $29.00 | $29.00 | PASS |  |  |
| BOTZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $31.6 | $31.60 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BOTZ | E3 | percent from the 21-day average | 8.2% below | 8.2% below | PASS |  |  |
| BOTZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BOTZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.80 | $0.80 (sr=0.7976) | PASS |  | Wilder ATR14 |
| BOTZ | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| BOTZ | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.7 | +5.7 | PASS |  |  |
| BOTZ | L-ema21 | ladder row ema21: price and gap = price vs average | $31.6, -8.2% | $31.60, -8.2% | PASS |  |  |
| BOTZ | L-note | "Last close $X · date" note = last completed bar | Last close $29.00 · Nov 19 | $29.00 · Nov 19 | PASS |  |  |
| BOTZ | L-now | ladder price row = compared price; name = the basis label | $29 "After hours" | $29.00 "after hours" | PASS |  |  |
| BOTZ | L-sma200 | ladder row sma200: price and gap = price vs average | $36.13, -19.7% | $36.13, -19.7% | PASS |  |  |
| BOTZ | L-sma50 | ladder row sma50: price and gap = price vs average | $33.64, -13.8% | $33.64, -13.8% | PASS |  |  |
| BOTZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $29.00 / entry $29.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BOTZ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BOTZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.4 | 28.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BOTZ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -14.3% vs +9.2% | -14.3% vs 9.2% | PASS |  |  |
| BOTZ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BOTZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.6 | 35.5 | PASS |  | Wilder, completed bars |
| BOTZ | T4w | words "20 or more / below 20" | 20 or more | ADX 35.5 | PASS |  |  |
| BOTZ | T5 | "counted at the last close ($X, date)" = last completed bar | $29.00, Nov 19 | $29.00, Nov 19 | PASS |  |  |
| BOTZ | T6 | price vs 200-day average (S1 pattern sma values) | $29.00 vs $36.13 · -19.7% | $29.00 vs $36.13 · -19.7% | PASS |  |  |
| BOTZ | T6w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T7 | price vs 50-day average (S1 pattern sma values) | $29.00 vs $33.64 · -13.8% | $29.00 vs $33.64 · -13.8% | PASS |  |  |
| BOTZ | T7w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.0% over 30 td | -2.0% over 30 td | PASS |  |  |
| BOTZ | T8r | word "rising" | not rising | not rising | PASS |  |  |
| BOTZ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BOTZ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.5% below $41.71 | 30.5% below $41.71 | PASS |  | closing high would be 41.63 |
| BOTZ | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.5% below | PASS |  |  |
| BOTZ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $41.71 | $41.71 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BOTZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.39%, close location 0.02, OBV falling |
| BOTZ | V2 | day change of the last completed bar | down 2.4% | -2.39% | PASS |  |  |
| BOTZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0172) | PASS |  |  |
| BOTZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BOTZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.69× / 0.87× | 1.69× / 0.87× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BOTZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1239156) | 20 bars, last ('2026-11-19', 1239156) | PASS |  |  |
| BOTZ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.69, OBV falling | condition true | PASS |  |  |
| BRK-B | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $570.71 | $570.71 | PASS |  |  |
| BRK-B | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $567.13 | $567.13 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRK-B | E3 | percent from the 21-day average | 0.6% above | 0.6% above | PASS |  |  |
| BRK-B | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRK-B | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.59 | $9.59 (sr=9.5945) | PASS |  | Wilder ATR14 |
| BRK-B | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves above |
| BRK-B | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -6.8 | -6.8 | PASS |  |  |
| BRK-B | L-ema21 | ladder row ema21: price and gap = price vs average | $567.13, 0.6% | $567.13, 0.6% | PASS |  |  |
| BRK-B | L-note | "Last close $X · date" note = last completed bar | Last close $572.04 · Nov 19 | $572.04 · Nov 19 | PASS |  |  |
| BRK-B | L-now | ladder price row = compared price; name = the basis label | $570.71 "After hours" | $570.71 "after hours" | PASS |  |  |
| BRK-B | L-sma200 | ladder row sma200: price and gap = price vs average | $502.24, 13.6% | $502.24, 13.6% | PASS |  |  |
| BRK-B | L-sma50 | ladder row sma50: price and gap = price vs average | $535.67, 6.5% | $535.67, 6.5% | PASS |  |  |
| BRK-B | S5-price | S5: the same live price reads the same on the header and the Entry block | header $570.71 / entry $570.71 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRK-B | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRK-B | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 58.4 | 58.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRK-B | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.1% vs +9.2% | 14.1% vs 9.2% | PASS |  |  |
| BRK-B | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRK-B | T4 | ADX 14 (S1 /api/sr meta.adx) | 49.2 | 49.2 | PASS |  | Wilder, completed bars |
| BRK-B | T4w | words "20 or more / below 20" | 20 or more | ADX 49.2 | PASS |  |  |
| BRK-B | T5 | "counted at the last close ($X, date)" = last completed bar | $572.04, Nov 19 | $572.04, Nov 19 | PASS |  |  |
| BRK-B | T6 | price vs 200-day average (S1 pattern sma values) | $572.04 vs $502.24 · +13.9% | $572.04 vs $502.24 · 13.9% | PASS |  |  |
| BRK-B | T6w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T7 | price vs 50-day average (S1 pattern sma values) | $572.04 vs $535.67 · +6.8% | $572.04 vs $535.67 · 6.8% | PASS |  |  |
| BRK-B | T7w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.9% over 30 td | +1.9% over 30 td | PASS |  |  |
| BRK-B | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRK-B | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRK-B | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.2% below $596.92 | 4.2% below $596.92 | PASS |  | closing high would be 592.94 |
| BRK-B | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.2% below | PASS |  |  |
| BRK-B | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $596.92 | $596.9199829101562 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRK-B | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.45%, close location 0.86, OBV flat |
| BRK-B | V2 | day change of the last completed bar | down 0.5% | -0.45% | PASS |  |  |
| BRK-B | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.86 (raw 0.8552) | PASS |  |  |
| BRK-B | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| BRK-B | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.14× / 0.27× | 1.14× / 0.27× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRK-B | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 5577397) | 20 bars, last ('2026-11-19', 5577397) | PASS |  |  |
| BRKU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $28.55 | $28.55 | PASS |  |  |
| BRKU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.31 | $28.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRKU | E3 | percent from the 21-day average | 0.9% above | 0.9% above | PASS |  |  |
| BRKU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRKU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.91 | $0.91 (sr=0.9149) | PASS |  | Wilder ATR14 |
| BRKU | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| BRKU | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.5 | -5.5 | PASS |  |  |
| BRKU | L-ema21 | ladder row ema21: price and gap = price vs average | $28.31, 0.9% | $28.31, 0.9% | PASS |  |  |
| BRKU | L-note | "Last close $X · date" note = last completed bar | Last close $28.55 · Nov 19 | $28.55 · Nov 19 | PASS |  |  |
| BRKU | L-now | ladder price row = compared price; name = the basis label | $28.55 "After hours" | $28.55 "after hours" | PASS |  |  |
| BRKU | L-sma200 | ladder row sma200: price and gap = price vs average | $23.24, 22.8% | $23.24, 22.8% | PASS |  |  |
| BRKU | L-sma50 | ladder row sma50: price and gap = price vs average | $25.47, 12.1% | $25.47, 12.1% | PASS |  |  |
| BRKU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $28.55 / entry $28.55 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRKU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRKU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.0 | 56.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRKU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +13.0% vs +9.2% | 13.0% vs 9.2% | PASS |  |  |
| BRKU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRKU | T4 | ADX 14 (S1 /api/sr meta.adx) | 47.7 | 47.6 | PASS |  | Wilder, completed bars |
| BRKU | T4w | words "20 or more / below 20" | 20 or more | ADX 47.6 | PASS |  |  |
| BRKU | T5 | "counted at the last close ($X, date)" = last completed bar | $28.55, Nov 19 | $28.55, Nov 19 | PASS |  |  |
| BRKU | T6 | price vs 200-day average (S1 pattern sma values) | $28.55 vs $23.24 · +22.8% | $28.55 vs $23.24 · 22.8% | PASS |  |  |
| BRKU | T6w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T7 | price vs 50-day average (S1 pattern sma values) | $28.55 vs $25.47 · +12.1% | $28.55 vs $25.47 · 12.1% | PASS |  |  |
| BRKU | T7w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.2% over 30 td | PASS |  |  |
| BRKU | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRKU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRKU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.5% below $31.20 | 8.5% below $31.20 | PASS |  | closing high would be 30.81 |
| BRKU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.5% below | PASS |  |  |
| BRKU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.20 | $31.2 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRKU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.04%, close location 0.81, OBV falling |
| BRKU | V2 | day change of the last completed bar | down 1.0% | -1.04% | PASS |  |  |
| BRKU | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.81 (raw 0.8143) | PASS |  |  |
| BRKU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BRKU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.67× / 0.32× | 0.67× / 0.32× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRKU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 62712) | 20 bars, last ('2026-11-19', 62712) | PASS |  |  |
| CAMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $97.78 | $97.78 | PASS |  |  |
| CAMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $108.79 | $108.79 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAMT | E3 | percent from the 21-day average | 10.1% below | 10.1% below | PASS |  |  |
| CAMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CAMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.00 | $8.00 (sr=8.0011) | PASS |  | Wilder ATR14 |
| CAMT | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| CAMT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.7 | +5.7 | PASS |  |  |
| CAMT | L-ema21 | ladder row ema21: price and gap = price vs average | $108.79, -10.1% | $108.79, -10.1% | PASS |  |  |
| CAMT | L-note | "Last close $X · date" note = last completed bar | Last close $97.78 · Nov 19 | $97.78 · Nov 19 | PASS |  |  |
| CAMT | L-now | ladder price row = compared price; name = the basis label | $97.78 "After hours" | $97.78 "after hours" | PASS |  |  |
| CAMT | L-sma200 | ladder row sma200: price and gap = price vs average | $154.47, -36.7% | $154.47, -36.7% | PASS |  |  |
| CAMT | L-sma50 | ladder row sma50: price and gap = price vs average | $129.78, -24.7% | $129.78, -24.7% | PASS |  |  |
| CAMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $97.78 / entry $97.78 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.4 | 37.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.3% vs +9.2% | -2.3% vs 9.2% | PASS |  |  |
| CAMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.0 | 34.0 | PASS |  | Wilder, completed bars |
| CAMT | T4w | words "20 or more / below 20" | 20 or more | ADX 34.0 | PASS |  |  |
| CAMT | T5 | "counted at the last close ($X, date)" = last completed bar | $97.78, Nov 19 | $97.78, Nov 19 | PASS |  |  |
| CAMT | T6 | price vs 200-day average (S1 pattern sma values) | $97.78 vs $154.47 · -36.7% | $97.78 vs $154.47 · -36.7% | PASS |  |  |
| CAMT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T7 | price vs 50-day average (S1 pattern sma values) | $97.78 vs $129.78 · -24.7% | $97.78 vs $129.78 · -24.7% | PASS |  |  |
| CAMT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.4% over 30 td | -1.4% over 30 td | PASS |  |  |
| CAMT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CAMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.7% below $215.99 | 54.7% below $215.99 | PASS |  | closing high would be 207.46 |
| CAMT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.7% below | PASS |  |  |
| CAMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $215.99 | $215.99 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.65%, close location 0.30, OBV falling |
| CAMT | V2 | day change of the last completed bar | down 0.7% | -0.65% | PASS |  |  |
| CAMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.95× / 0.08× | 0.95× / 0.08× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 494358) | 20 bars, last ('2026-11-19', 494358) | PASS |  |  |
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
| CARS.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -22.4% vs +9.2% | -22.4% vs 9.2% | PASS |  |  |
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
| CAT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $537.37 | $537.37 | PASS |  |  |
| CAT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $617.74 | $617.74 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAT | E3 | percent from the 21-day average | 13.0% below | 13.0% below | PASS |  |  |
| CAT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CAT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $28.74 | $28.74 (sr=28.7397) | PASS |  | Wilder ATR14 |
| CAT | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| CAT | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| CAT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.4 | +6.4 | PASS |  |  |
| CAT | L-ema21 | ladder row ema21: price and gap = price vs average | $617.74, -13.0% | $617.74, -13.0% | PASS |  |  |
| CAT | L-note | "Last close $X · date" note = last completed bar | Last close $537.26 · Nov 19 | $537.26 · Nov 19 | PASS |  |  |
| CAT | L-now | ladder price row = compared price; name = the basis label | $537.37 "After hours" | $537.37 "after hours" | PASS |  |  |
| CAT | L-sma200 | ladder row sma200: price and gap = price vs average | $801.93, -33.0% | $801.93, -33.0% | PASS |  |  |
| CAT | L-sma50 | ladder row sma50: price and gap = price vs average | $719.22, -25.3% | $719.22, -25.3% | PASS |  |  |
| CAT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $537.37 / entry $537.37 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.1 | 27.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.0% vs +9.2% | -2.0% vs 9.2% | PASS |  |  |
| CAT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAT | T4 | ADX 14 (S1 /api/sr meta.adx) | 39.8 | 39.8 | PASS |  | Wilder, completed bars |
| CAT | T4w | words "20 or more / below 20" | 20 or more | ADX 39.8 | PASS |  |  |
| CAT | T5 | "counted at the last close ($X, date)" = last completed bar | $537.26, Nov 19 | $537.26, Nov 19 | PASS |  |  |
| CAT | T6 | price vs 200-day average (S1 pattern sma values) | $537.26 vs $801.93 · -33.0% | $537.26 vs $801.93 · -33.0% | PASS |  |  |
| CAT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAT | T7 | price vs 50-day average (S1 pattern sma values) | $537.26 vs $719.22 · -25.3% | $537.26 vs $719.22 · -25.3% | PASS |  |  |
| CAT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.7% over 30 td | +0.7% over 30 td | PASS |  |  |
| CAT | T8r | word "rising" | still rising | rising | PASS |  |  |
| CAT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.7% below $1,068.94 | 49.7% below $1068.94 | PASS |  | closing high would be 1060.42 |
| CAT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.7% below | PASS |  |  |
| CAT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,068.94 | $1068.93972 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.85%, close location 0.05, OBV falling |
| CAT | V2 | day change of the last completed bar | down 3.9% | -3.85% | PASS |  |  |
| CAT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0505) | PASS |  |  |
| CAT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.25× / 0.72× | 3.25× / 0.72× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 10623225) | 20 bars, last ('2026-11-19', 10623225) | PASS |  |  |
| CAT | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.25, OBV falling | condition true | PASS |  |  |
| CCO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $88.15 | $88.15 | PASS |  |  |
| CCO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $104.03 | $104.03 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CCO.TO | E3 | percent from the 21-day average | 15.3% below | 15.3% below | PASS |  |  |
| CCO.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CCO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.92 | $4.92 (sr=4.9224) | PASS |  | Wilder ATR14 |
| CCO.TO | E5 | distance in normal day-moves | 3.2 | 3.2 | PASS |  | gauge dot note uses the same number:  · 3.2 day-moves below |
| CCO.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.4 | +7.4 | PASS |  |  |
| CCO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $104.03, -15.3% | $104.03, -15.3% | PASS |  |  |
| CCO.TO | L-note | "Last close $X · date" note = last completed bar | Last close $89.40 · Nov 18 | $89.40 · Nov 18 | PASS |  |  |
| CCO.TO | L-now | ladder price row = compared price; name = the basis label | $88.15 "After hours" | $88.15 "after hours" | PASS |  |  |
| CCO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $140.51, -37.3% | $140.51, -37.3% | PASS |  |  |
| CCO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $116.73, -24.5% | $116.73, -24.5% | PASS |  |  |
| CCO.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $88.15 / entry $88.15 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CCO.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CCO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.3 | 29.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CCO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -23.1% vs +9.2% | -23.1% vs 9.2% | PASS |  |  |
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
| CCO.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.5× from 2026-11-18 | 1.54× from 2026-11-18 | PASS |  | window "50 bars" includes the bar itself |
| CCO.TO | V6 | Volume detail: last session date and RVOL | 2026-11-18 1.54× | 2026-11-18 1.54× | PASS |  |  |
| CCO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.54× / 0.54× | 1.54× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CCO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1938996) | 20 bars, last ('2026-11-18', 1938996) | PASS |  |  |
| CCO.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.54, OBV falling | condition true | PASS |  |  |
| CEG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $252.03 | $252.03 | PASS |  |  |
| CEG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $265.88 | $265.88 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CEG | E3 | percent from the 21-day average | 5.2% below | 5.2% below | PASS |  |  |
| CEG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CEG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $13.17 | $13.17 (sr=13.1699) | PASS |  | Wilder ATR14 |
| CEG | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| CEG | L-ema21 | ladder row ema21: price and gap = price vs average | $265.88, -5.2% | $265.88, -5.2% | PASS |  |  |
| CEG | L-note | "Last close $X · date" note = last completed bar | Last close $252.03 · Nov 19 | $252.03 · Nov 19 | PASS |  |  |
| CEG | L-now | ladder price row = compared price; name = the basis label | $252.03 "After hours" | $252.03 "after hours" | PASS |  |  |
| CEG | L-sma200 | ladder row sma200: price and gap = price vs average | $278.35, -9.5% | $278.35, -9.5% | PASS |  |  |
| CEG | L-sma50 | ladder row sma50: price and gap = price vs average | $267.16, -5.7% | $267.16, -5.7% | PASS |  |  |
| CEG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $252.03 / entry $252.03 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CEG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CEG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.9 | 42.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CEG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -29.5% vs +9.2% | -29.5% vs 9.2% | PASS |  |  |
| CEG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CEG | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.9 | 12.9 | PASS |  | Wilder, completed bars |
| CEG | T4w | words "20 or more / below 20" | below 20 | ADX 12.9 | PASS |  |  |
| CEG | T5 | "counted at the last close ($X, date)" = last completed bar | $252.03, Nov 19 | $252.03, Nov 19 | PASS |  |  |
| CEG | T6 | price vs 200-day average (S1 pattern sma values) | $252.03 vs $278.35 · -9.5% | $252.03 vs $278.35 · -9.5% | PASS |  |  |
| CEG | T6w | word "Below" | Below | Below | PASS |  |  |
| CEG | T7 | price vs 50-day average (S1 pattern sma values) | $252.03 vs $267.16 · -5.7% | $252.03 vs $267.16 · -5.7% | PASS |  |  |
| CEG | T7w | word "Below" | Below | Below | PASS |  |  |
| CEG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.8% over 30 td | -2.8% over 30 td | PASS |  |  |
| CEG | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CEG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CEG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 33.8% below $380.78 | 33.8% below $380.78 | PASS |  | closing high would be 378.60 |
| CEG | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 33.8% below | PASS |  |  |
| CEG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $380.78 | $380.78 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CEG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.08%, close location 0.04, OBV falling |
| CEG | V2 | day change of the last completed bar | down 4.1% | -4.08% | PASS |  |  |
| CEG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0357) | PASS |  |  |
| CEG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CEG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.95× / 0.78× | 0.95× / 0.78× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CEG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 3655171) | 20 bars, last ('2026-11-19', 3655171) | PASS |  |  |
| CGY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $81.56 | $81.56 | PASS |  |  |
| CGY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.87 | $84.87 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CGY.TO | E3 | percent from the 21-day average | 3.9% below | 3.9% below | PASS |  |  |
| CGY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CGY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.52 | $2.52 (sr=2.5223) | PASS |  | Wilder ATR14 |
| CGY.TO | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| CGY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $84.87, -3.9% | $84.87, -3.9% | PASS |  |  |
| CGY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $81.56 · Nov 19 | $81.56 · Nov 19 | PASS |  |  |
| CGY.TO | L-now | ladder price row = compared price; name = the basis label | $81.56 "After hours" | $81.56 "after hours" | PASS |  |  |
| CGY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $79, 3.2% | $79.00, 3.2% | PASS |  |  |
| CGY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $83.53, -2.4% | $83.53, -2.4% | PASS |  |  |
| CGY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $81.56 / entry $81.56 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CGY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CGY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.0 | 42.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CGY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +70.5% vs +9.2% | 70.5% vs 9.2% | PASS |  |  |
| CGY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CGY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.0 | 15.0 | PASS |  | Wilder, completed bars |
| CGY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.0 | PASS |  |  |
| CGY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $81.56, Nov 19 | $81.56, Nov 19 | PASS |  |  |
| CGY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $81.56 vs $79.00 · +3.2% | $81.56 vs $79.00 · 3.2% | PASS |  |  |
| CGY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CGY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $81.56 vs $83.53 · -2.4% | $81.56 vs $83.53 · -2.4% | PASS |  |  |
| CGY.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CGY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +5.0% over 30 td | PASS |  |  |
| CGY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CGY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CGY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.3% below $95.15 | 14.3% below $95.15 | PASS |  | closing high would be 91.80 |
| CGY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.3% below | PASS |  |  |
| CGY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $95.15 | $95.15474299571112 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CGY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.07%, close location 0.03, OBV falling |
| CGY.TO | V2 | day change of the last completed bar | down 3.1% | -3.07% | PASS |  |  |
| CGY.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0301) | PASS |  |  |
| CGY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CGY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.50× / 0.99× | 0.50× / 0.99× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CGY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 14961) | 20 bars, last ('2026-11-19', 14961) | PASS |  |  |
| CNQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $64.10 | $64.10 | PASS |  |  |
| CNQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $70.05 | $70.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNQ.TO | E3 | percent from the 21-day average | 8.5% below | 8.5% below | PASS |  |  |
| CNQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CNQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.06 | $2.06 (sr=2.0606) | PASS |  | Wilder ATR14 |
| CNQ.TO | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| CNQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $70.05, -8.5% | $70.05, -8.5% | PASS |  |  |
| CNQ.TO | L-now | ladder price row = compared price; name = the basis label | $64.1 "Last close" | $64.10 "last close" | PASS |  |  |
| CNQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.29, -0.3% | $64.29, -0.3% | PASS |  |  |
| CNQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $70.94, -9.6% | $70.94, -9.6% | PASS |  |  |
| CNQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.0 | 30.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.8% vs +9.2% | 39.8% vs 9.2% | PASS |  |  |
| CNQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.1 | 31.1 | PASS |  | Wilder, completed bars |
| CNQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.1 | PASS |  |  |
| CNQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $64.10 vs $64.29 · -0.3% | $64.10 vs $64.29 · -0.3% | PASS |  |  |
| CNQ.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CNQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $64.10 vs $70.94 · -9.6% | $64.10 vs $70.94 · -9.6% | PASS |  |  |
| CNQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CNQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.7% over 30 td | +6.7% over 30 td | PASS |  |  |
| CNQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 18.4% below $78.60 | 18.4% below $78.60 | PASS |  | closing high would be 78.42 |
| CNQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 18.4% below | PASS |  |  |
| CNQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $78.60 | $78.5999984741211 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.78%, close location 0.09, OBV falling |
| CNQ.TO | V2 | day change of the last completed bar | down 1.8% | -1.78% | PASS |  |  |
| CNQ.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0888) | PASS |  |  |
| CNQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CNQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.49× / 0.55× | 1.49× / 0.55× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 17856255) | 20 bars, last ('2026-11-19', 17856255) | PASS |  |  |
| CNR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $178.66 | $178.66 | PASS |  |  |
| CNR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $177.72 | $177.72 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNR.TO | E3 | percent from the 21-day average | 0.5% above | 0.5% above | PASS |  |  |
| CNR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CNR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.19 | $3.19 (sr=3.1918) | PASS |  | Wilder ATR14 |
| CNR.TO | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| CNR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $177.72, 0.5% | $177.72, 0.5% | PASS |  |  |
| CNR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $178.66 · Nov 19 | $178.66 · Nov 19 | PASS |  |  |
| CNR.TO | L-now | ladder price row = compared price; name = the basis label | $178.66 "After hours" | $178.66 "after hours" | PASS |  |  |
| CNR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $162.23, 10.1% | $162.23, 10.1% | PASS |  |  |
| CNR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $172.68, 3.5% | $172.68, 3.5% | PASS |  |  |
| CNR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $178.66 / entry $178.66 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CNR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.2 | 54.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.1% vs +9.2% | 39.1% vs 9.2% | PASS |  |  |
| CNR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.0 | 22.0 | PASS |  | Wilder, completed bars |
| CNR.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.0 | PASS |  |  |
| CNR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $178.66, Nov 19 | $178.66, Nov 19 | PASS |  |  |
| CNR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $178.66 vs $162.23 · +10.1% | $178.66 vs $162.23 · 10.1% | PASS |  |  |
| CNR.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $178.66 vs $172.68 · +3.5% | $178.66 vs $172.68 · 3.5% | PASS |  |  |
| CNR.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.0% over 30 td | +4.0% over 30 td | PASS |  |  |
| CNR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.0% below $184.26 | 3.0% below $184.26 | PASS |  | closing high would be 182.93 |
| CNR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.0% below | PASS |  |  |
| CNR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $184.26 | $184.25630798377267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -0.39%, close location 0.69, OBV flat |
| CNR.TO | V2 | day change of the last completed bar | down 0.4% | -0.39% | PASS |  |  |
| CNR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| CNR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.71× / 0.22× | 0.71× / 0.22× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 859851) | 20 bars, last ('2026-11-19', 859851) | PASS |  |  |
| COP | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $134.99 | $134.99 | PASS |  |  |
| COP | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $138.89 | $138.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COP | E3 | percent from the 21-day average | 2.8% below | 2.8% below | PASS |  |  |
| COP | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COP | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.91 | $3.91 (sr=3.912) | PASS |  | Wilder ATR14 |
| COP | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| COP | L-ema21 | ladder row ema21: price and gap = price vs average | $138.89, -2.8% | $138.89, -2.8% | PASS |  |  |
| COP | L-note | "Last close $X · date" note = last completed bar | Last close $134.99 · Nov 19 | $134.99 · Nov 19 | PASS |  |  |
| COP | L-now | ladder price row = compared price; name = the basis label | $134.99 "After hours" | $134.99 "after hours" | PASS |  |  |
| COP | L-sma200 | ladder row sma200: price and gap = price vs average | $122.36, 10.3% | $122.36, 10.3% | PASS |  |  |
| COP | L-sma50 | ladder row sma50: price and gap = price vs average | $136.59, -1.2% | $136.59, -1.2% | PASS |  |  |
| COP | S5-price | S5: the same live price reads the same on the header and the Entry block | header $134.99 / entry $134.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COP | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COP | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.5 | 43.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COP | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +57.9% vs +9.2% | 57.8% vs 9.2% | PASS |  |  |
| COP | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COP | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.6 | 22.6 | PASS |  | Wilder, completed bars |
| COP | T4w | words "20 or more / below 20" | 20 or more | ADX 22.6 | PASS |  |  |
| COP | T5 | "counted at the last close ($X, date)" = last completed bar | $134.99, Nov 19 | $134.99, Nov 19 | PASS |  |  |
| COP | T6 | price vs 200-day average (S1 pattern sma values) | $134.99 vs $122.36 · +10.3% | $134.99 vs $122.36 · 10.3% | PASS |  |  |
| COP | T6w | word "Above" | Above | Above | PASS |  |  |
| COP | T7 | price vs 50-day average (S1 pattern sma values) | $134.99 vs $136.59 · -1.2% | $134.99 vs $136.59 · -1.2% | PASS |  |  |
| COP | T7w | word "Below" | Below | Below | PASS |  |  |
| COP | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.0% over 30 td | +6.0% over 30 td | PASS |  |  |
| COP | T8r | word "rising" | still rising | rising | PASS |  |  |
| COP | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COP | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.9% below $153.27 | 11.9% below $153.27 | PASS |  | closing high would be 153.02 |
| COP | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.9% below | PASS |  |  |
| COP | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $153.27 | $153.2715592533114 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COP | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.44%, close location 0.58, OBV falling |
| COP | V2 | day change of the last completed bar | up 0.4% | +0.44% | PASS |  |  |
| COP | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COP | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.70× / 0.15× | 0.70× / 0.15× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COP | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4811961) | 20 bars, last ('2026-11-19', 4811961) | PASS |  |  |
| COPP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $41.83 | $41.83 | PASS |  |  |
| COPP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $50.41 | $50.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPP.TO | E3 | percent from the 21-day average | 17.0% below | 17.0% below | PASS |  |  |
| COPP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| COPP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.18 | $2.18 (sr=2.1825) | PASS |  | Wilder ATR14 |
| COPP.TO | E5 | distance in normal day-moves | 3.9 | 3.9 | PASS |  | gauge dot note uses the same number:  · 3.9 day-moves below |
| COPP.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| COPP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $50.41, -17.0% | $50.41, -17.0% | PASS |  |  |
| COPP.TO | L-now | ladder price row = compared price; name = the basis label | $41.83 "Last close" | $41.83 "last close" | PASS |  |  |
| COPP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.43, -28.4% | $58.43, -28.4% | PASS |  |  |
| COPP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $56.36, -25.8% | $56.36, -25.8% | PASS |  |  |
| COPP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 25.3 | 25.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.4% vs +9.2% | -5.4% vs 9.2% | PASS |  |  |
| COPP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.3 | 33.3 | PASS |  | Wilder, completed bars |
| COPP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 33.3 | PASS |  |  |
| COPP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $41.83 vs $58.43 · -28.4% | $41.83 vs $58.43 · -28.4% | PASS |  |  |
| COPP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $41.83 vs $56.36 · -25.8% | $41.83 vs $56.36 · -25.8% | PASS |  |  |
| COPP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.3% over 30 td | -1.3% over 30 td | PASS |  |  |
| COPP.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 40.7% below $70.54 | 40.7% below $70.54 | PASS |  | closing high would be 68.98 |
| COPP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 40.7% below | PASS |  |  |
| COPP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $70.54 | $70.54000091552734 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.90%, close location 0.01, OBV falling |
| COPP.TO | V2 | day change of the last completed bar | down 2.9% | -2.90% | PASS |  |  |
| COPP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0136) | PASS |  |  |
| COPP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.64× / 0.56× | 1.64× / 0.56× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 23766) | 20 bars, last ('2026-11-19', 23766) | PASS |  |  |
| COPP.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.64, OBV falling | condition true | PASS |  |  |
| COPX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $59.28 | $59.28 | PASS |  |  |
| COPX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $70.86 | $70.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPX | E3 | percent from the 21-day average | 16.3% below | 16.3% below | PASS |  |  |
| COPX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COPX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.91 | $2.91 (sr=2.9076) | PASS |  | Wilder ATR14 |
| COPX | E5 | distance in normal day-moves | 4.0 | 4.0 | PASS |  | gauge dot note uses the same number:  · 4.0 day-moves below |
| COPX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.9 | +3.9 | PASS |  |  |
| COPX | L-ema21 | ladder row ema21: price and gap = price vs average | $70.86, -16.3% | $70.86, -16.3% | PASS |  |  |
| COPX | L-note | "Last close $X · date" note = last completed bar | Last close $59.28 · Nov 19 | $59.28 · Nov 19 | PASS |  |  |
| COPX | L-now | ladder price row = compared price; name = the basis label | $59.28 "After hours" | $59.28 "after hours" | PASS |  |  |
| COPX | L-sma200 | ladder row sma200: price and gap = price vs average | $82.13, -27.8% | $82.13, -27.8% | PASS |  |  |
| COPX | L-sma50 | ladder row sma50: price and gap = price vs average | $78.93, -24.9% | $78.93, -24.9% | PASS |  |  |
| COPX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $59.28 / entry $59.28 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 24.8 | 24.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +1.7% vs +9.2% | 1.7% vs 9.2% | PASS |  |  |
| COPX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPX | T4w | words "20 or more / below 20" | 20 or more | ADX 28.7 | PASS |  |  |
| COPX | T5 | "counted at the last close ($X, date)" = last completed bar | $59.28, Nov 19 | $59.28, Nov 19 | PASS |  |  |
| COPX | T6 | price vs 200-day average (S1 pattern sma values) | $59.28 vs $82.13 · -27.8% | $59.28 vs $82.13 · -27.8% | PASS |  |  |
| COPX | T6w | word "Below" | Below | Below | PASS |  |  |
| COPX | T7 | price vs 50-day average (S1 pattern sma values) | $59.28 vs $78.93 · -24.9% | $59.28 vs $78.93 · -24.9% | PASS |  |  |
| COPX | T7w | word "Below" | Below | Below | PASS |  |  |
| COPX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.1% over 30 td | -1.1% over 30 td | PASS |  |  |
| COPX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 40.5% below $99.65 | 40.5% below $99.65 | PASS |  | closing high would be 96.45 |
| COPX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 40.5% below | PASS |  |  |
| COPX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $99.65 | $99.65136047369408 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.12%, close location 0.02, OBV falling |
| COPX | V2 | day change of the last completed bar | down 3.1% | -3.12% | PASS |  |  |
| COPX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0183) | PASS |  |  |
| COPX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.42× / 0.64× | 2.42× / 0.64× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 7173614) | 20 bars, last ('2026-11-19', 7173614) | PASS |  |  |
| COPX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.42, OBV falling | condition true | PASS |  |  |
| COPZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $7.06 | $7.06 | PASS |  |  |
| COPZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $10.43 | $10.43 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPZ | E3 | percent from the 21-day average | 32.3% below | 32.3% below | PASS |  |  |
| COPZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COPZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.81 | $0.81 (sr=0.8106) | PASS |  | Wilder ATR14 |
| COPZ | E5 | distance in normal day-moves | 4.2 | 4.2 | PASS |  | gauge dot note uses the same number:  · 4.2 day-moves below |
| COPZ | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| COPZ | L-ema21 | ladder row ema21: price and gap = price vs average | $10.43, -32.3% | $10.43, -32.3% | PASS |  |  |
| COPZ | L-note | "Last close $X · date" note = last completed bar | Last close $7.06 · Nov 19 | $7.06 · Nov 19 | PASS |  |  |
| COPZ | L-now | ladder price row = compared price; name = the basis label | $7.06 "After hours" | $7.06 "after hours" | PASS |  |  |
| COPZ | L-sma50 | ladder row sma50: price and gap = price vs average | $13.24, -46.7% | $13.24, -46.7% | PASS |  |  |
| COPZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $7.06 / entry $7.06 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 25.3 | 25.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.6 | 29.6 | PASS |  | Wilder, completed bars |
| COPZ | T4w | words "20 or more / below 20" | 20 or more | ADX 29.6 | PASS |  |  |
| COPZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.24%, close location 0.00, OBV falling |
| COPZ | V2 | day change of the last completed bar | down 6.2% | -6.24% | PASS |  |  |
| COPZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| COPZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.09× / 0.54× | 2.09× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 26552) | 20 bars, last ('2026-11-19', 26552) | PASS |  |  |
| COPZ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.09, OBV falling | condition true | PASS |  |  |
| COST | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,093.83 | $1,093.83 | PASS |  |  |
| COST | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1056.47 | $1056.47 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COST | E3 | percent from the 21-day average | 3.5% above | 3.5% above | PASS |  |  |
| COST | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COST | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $18.31 | $18.31 (sr=18.3134) | PASS |  | Wilder ATR14 |
| COST | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves above |
| COST | L-ema21 | ladder row ema21: price and gap = price vs average | $1056.47, 3.5% | $1056.47, 3.5% | PASS |  |  |
| COST | L-note | "Last close $X · date" note = last completed bar | Last close $1,093.83 · Nov 19 | $1,093.83 · Nov 19 | PASS |  |  |
| COST | L-now | ladder price row = compared price; name = the basis label | $1093.83 "After hours" | $1093.83 "after hours" | PASS |  |  |
| COST | L-sma200 | ladder row sma200: price and gap = price vs average | $978.43, 11.8% | $978.43, 11.8% | PASS |  |  |
| COST | L-sma50 | ladder row sma50: price and gap = price vs average | $982.78, 11.3% | $982.78, 11.3% | PASS |  |  |
| COST | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,093.83 / entry $1,093.83 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COST | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COST | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 67.8 | 67.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COST | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +22.8% vs +9.2% | 22.8% vs 9.2% | PASS |  |  |
| COST | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COST | T4 | ADX 14 (S1 /api/sr meta.adx) | 52.4 | 52.4 | PASS |  | Wilder, completed bars |
| COST | T4w | words "20 or more / below 20" | 20 or more | ADX 52.4 | PASS |  |  |
| COST | T5 | "counted at the last close ($X, date)" = last completed bar | $1,093.83, Nov 19 | $1093.83, Nov 19 | PASS |  |  |
| COST | T6 | price vs 200-day average (S1 pattern sma values) | $1,093.83 vs $978.43 · +11.8% | $1093.83 vs $978.43 · 11.8% | PASS |  |  |
| COST | T6w | word "Above" | Above | Above | PASS |  |  |
| COST | T7 | price vs 50-day average (S1 pattern sma values) | $1,093.83 vs $982.78 · +11.3% | $1093.83 vs $982.78 · 11.3% | PASS |  |  |
| COST | T7w | word "Above" | Above | Above | PASS |  |  |
| COST | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| COST | T8r | word "rising" | still rising | rising | PASS |  |  |
| COST | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COST | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.7% below $1,123.67 | 2.7% below $1123.67 | PASS |  | closing high would be 1113.74 |
| COST | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.7% below | PASS |  |  |
| COST | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,123.67 | $1123.6699 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COST | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change -0.25%, close location 0.92, OBV rising |
| COST | V2 | day change of the last completed bar | down 0.3% | -0.25% | PASS |  |  |
| COST | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.92 (raw 0.9175) | PASS |  |  |
| COST | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COST | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.90× / 0.15× | 0.90× / 0.15× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COST | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2130099) | 20 bars, last ('2026-11-19', 2130099) | PASS |  |  |
| COTG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $16.45 | $16.45 | PASS |  |  |
| COTG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.44 | $15.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COTG | E3 | percent from the 21-day average | 6.5% above | 6.5% above | PASS |  |  |
| COTG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COTG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.50 | $0.50 (sr=0.5035) | PASS |  | Wilder ATR14 |
| COTG | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves above |
| COTG | L-ema21 | ladder row ema21: price and gap = price vs average | $15.44, 6.5% | $15.44, 6.5% | PASS |  |  |
| COTG | L-note | "Last close $X · date" note = last completed bar | Last close $16.45 · Nov 19 | $16.45 · Nov 19 | PASS |  |  |
| COTG | L-now | ladder price row = compared price; name = the basis label | $16.45 "After hours" | $16.45 "after hours" | PASS |  |  |
| COTG | L-sma200 | ladder row sma200: price and gap = price vs average | $13.93, 18.1% | $13.93, 18.1% | PASS |  |  |
| COTG | L-sma50 | ladder row sma50: price and gap = price vs average | $13.49, 21.9% | $13.49, 21.9% | PASS |  |  |
| COTG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $16.45 / entry $16.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COTG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COTG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 66.2 | 66.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COTG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +31.1% vs +9.2% | 31.1% vs 9.2% | PASS |  |  |
| COTG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COTG | T4 | ADX 14 (S1 /api/sr meta.adx) | 51.0 | 51.0 | PASS |  | Wilder, completed bars |
| COTG | T4w | words "20 or more / below 20" | 20 or more | ADX 51.0 | PASS |  |  |
| COTG | T5 | "counted at the last close ($X, date)" = last completed bar | $16.45, Nov 19 | $16.45, Nov 19 | PASS |  |  |
| COTG | T6 | price vs 200-day average (S1 pattern sma values) | $16.45 vs $13.93 · +18.1% | $16.45 vs $13.93 · 18.1% | PASS |  |  |
| COTG | T6w | word "Above" | Above | Above | PASS |  |  |
| COTG | T7 | price vs 50-day average (S1 pattern sma values) | $16.45 vs $13.49 · +21.9% | $16.45 vs $13.49 · 21.9% | PASS |  |  |
| COTG | T7w | word "Above" | Above | Above | PASS |  |  |
| COTG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| COTG | T8r | word "rising" | still rising | rising | PASS |  |  |
| COTG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COTG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.6% below $17.80 | 7.6% below $17.80 | PASS |  | closing high would be 17.70 |
| COTG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.6% below | PASS |  |  |
| COTG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $17.80 | $17.80299949645996 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COTG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change -0.48%, close location 1.00, OBV rising |
| COTG | V2 | day change of the last completed bar | down 0.5% | -0.48% | PASS |  |  |
| COTG | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 1.00 (raw 1.0000) | PASS |  |  |
| COTG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COTG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.53× / 0.16× | 0.53× / 0.16× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COTG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 55250) | 20 bars, last ('2026-11-19', 55250) | PASS |  |  |
| CSU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3,180.00 | $3,180.00 | PASS |  |  |
| CSU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3347.07 | $3347.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CSU.TO | E3 | percent from the 21-day average | 5.0% below | 5.0% below | PASS |  |  |
| CSU.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CSU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $120.69 | $120.69 (sr=120.688) | PASS |  | Wilder ATR14 |
| CSU.TO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| CSU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $3347.07, -5.0% | $3347.07, -5.0% | PASS |  |  |
| CSU.TO | L-note | "Last close $X · date" note = last completed bar | Last close $3,180.00 · Nov 19 | $3,180.00 · Nov 19 | PASS |  |  |
| CSU.TO | L-now | ladder price row = compared price; name = the basis label | $3180 "After hours" | $3180.00 "after hours" | PASS |  |  |
| CSU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $2821.69, 12.7% | $2821.69, 12.7% | PASS |  |  |
| CSU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $3143.03, 1.2% | $3143.03, 1.2% | PASS |  |  |
| CSU.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3,180.00 / entry $3,180.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CSU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CSU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.1 | 40.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CSU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -0.5% vs +9.2% | -0.5% vs 9.2% | PASS |  |  |
| CSU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CSU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.1 | 30.1 | PASS |  | Wilder, completed bars |
| CSU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.1 | PASS |  |  |
| CSU.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $3,180.00, Nov 19 | $3180.00, Nov 19 | PASS |  |  |
| CSU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $3,180.00 vs $2,821.69 · +12.7% | $3180.00 vs $2821.69 · 12.7% | PASS |  |  |
| CSU.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CSU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $3,180.00 vs $3,143.03 · +1.2% | $3180.00 vs $3143.03 · 1.2% | PASS |  |  |
| CSU.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CSU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| CSU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CSU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CSU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.8% below $3,565.00 | 10.8% below $3565.00 | PASS |  | closing high would be 3526.52 |
| CSU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.8% below | PASS |  |  |
| CSU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $3,565.00 | $3565 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CSU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -4.31%, close location 0.05, OBV flat |
| CSU.TO | V2 | day change of the last completed bar | down 4.3% | -4.31% | PASS |  |  |
| CSU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0518) | PASS |  |  |
| CSU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| CSU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.03× / 1.14× | 1.03× / 1.14× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CSU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 63238) | 20 bars, last ('2026-11-19', 63238) | PASS |  |  |
| CVX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $206.50 | $206.50 | PASS |  |  |
| CVX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $216.33 | $216.33 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CVX | E3 | percent from the 21-day average | 4.5% below | 4.5% below | PASS |  |  |
| CVX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CVX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.06 | $5.06 (sr=5.0626) | PASS |  | Wilder ATR14 |
| CVX | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| CVX | L-ema21 | ladder row ema21: price and gap = price vs average | $216.33, -4.5% | $216.33, -4.5% | PASS |  |  |
| CVX | L-note | "Last close $X · date" note = last completed bar | Last close $206.50 · Nov 19 | $206.50 · Nov 19 | PASS |  |  |
| CVX | L-now | ladder price row = compared price; name = the basis label | $206.5 "After hours" | $206.50 "after hours" | PASS |  |  |
| CVX | L-sma200 | ladder row sma200: price and gap = price vs average | $196.45, 5.1% | $196.45, 5.1% | PASS |  |  |
| CVX | L-sma50 | ladder row sma50: price and gap = price vs average | $215.49, -4.2% | $215.49, -4.2% | PASS |  |  |
| CVX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $206.50 / entry $206.50 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CVX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CVX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.3 | 37.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CVX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +36.1% vs +9.2% | 36.1% vs 9.2% | PASS |  |  |
| CVX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CVX | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.2 | 26.2 | PASS |  | Wilder, completed bars |
| CVX | T4w | words "20 or more / below 20" | 20 or more | ADX 26.2 | PASS |  |  |
| CVX | T5 | "counted at the last close ($X, date)" = last completed bar | $206.50, Nov 19 | $206.50, Nov 19 | PASS |  |  |
| CVX | T6 | price vs 200-day average (S1 pattern sma values) | $206.50 vs $196.45 · +5.1% | $206.50 vs $196.45 · 5.1% | PASS |  |  |
| CVX | T6w | word "Above" | Above | Above | PASS |  |  |
| CVX | T7 | price vs 50-day average (S1 pattern sma values) | $206.50 vs $215.50 · -4.2% | $206.50 vs $215.49 · -4.2% | PASS |  |  |
| CVX | T7w | word "Below" | Below | Below | PASS |  |  |
| CVX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.6% over 30 td | +4.6% over 30 td | PASS |  |  |
| CVX | T8r | word "rising" | still rising | rising | PASS |  |  |
| CVX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CVX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.7% below $236.48 | 12.7% below $236.48 | PASS |  | closing high would be 235.52 |
| CVX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.7% below | PASS |  |  |
| CVX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $236.48 | $236.48 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CVX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.30%, close location 0.37, OBV falling |
| CVX | V2 | day change of the last completed bar | up 0.3% | +0.30% | PASS |  |  |
| CVX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CVX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.98× / 0.12× | 0.98× / 0.12× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CVX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 8582362) | 20 bars, last ('2026-11-19', 8582362) | PASS |  |  |
| DRAL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3.99 | $3.99 | PASS |  |  |
| DRAL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $5.68 | $5.68 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAL | E3 | percent from the 21-day average | 29.8% below | 29.8% below | PASS |  |  |
| DRAL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.77 | $0.77 (sr=0.7697) | PASS |  | Wilder ATR14 |
| DRAL | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| DRAL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| DRAL | L-ema21 | ladder row ema21: price and gap = price vs average | $5.68, -29.8% | $5.68, -29.8% | PASS |  |  |
| DRAL | L-note | "Last close $X · date" note = last completed bar | Last close $3.99 · Nov 19 | $3.99 · Nov 19 | PASS |  |  |
| DRAL | L-now | ladder price row = compared price; name = the basis label | $3.99 "After hours" | $3.99 "after hours" | PASS |  |  |
| DRAL | L-sma50 | ladder row sma50: price and gap = price vs average | $8.39, -52.5% | $8.39, -52.5% | PASS |  |  |
| DRAL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3.99 / entry $3.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.0 | 34.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.6 | PASS |  |  |
| DRAL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.86%, close location 0.00, OBV falling |
| DRAL | V2 | day change of the last completed bar | down 3.9% | -3.86% | PASS |  |  |
| DRAL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| DRAL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 4.65× / 0.20× | 4.65× / 0.20× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1219547) | 20 bars, last ('2026-11-19', 1219547) | PASS |  |  |
| DRAL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 4.65, OBV falling | condition true | PASS |  |  |
| DRAM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $38.43 | $38.43 | PASS |  |  |
| DRAM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $43.92 | $43.92 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAM | E3 | percent from the 21-day average | 12.5% below | 12.5% below | PASS |  |  |
| DRAM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.05 | $3.05 (sr=3.0528) | PASS |  | Wilder ATR14 |
| DRAM | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| DRAM | L-ema21 | ladder row ema21: price and gap = price vs average | $43.92, -12.5% | $43.92, -12.5% | PASS |  |  |
| DRAM | L-note | "Last close $X · date" note = last completed bar | Last close $38.43 · Nov 19 | $38.43 · Nov 19 | PASS |  |  |
| DRAM | L-now | ladder price row = compared price; name = the basis label | $38.43 "After hours" | $38.43 "after hours" | PASS |  |  |
| DRAM | L-sma50 | ladder row sma50: price and gap = price vs average | $51.61, -25.5% | $51.61, -25.5% | PASS |  |  |
| DRAM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $38.43 / entry $38.43 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.6 | 36.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAM | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.3 | 32.2 | PASS |  | Wilder, completed bars |
| DRAM | T4w | words "20 or more / below 20" | 20 or more | ADX 32.2 | PASS |  |  |
| DRAM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.84%, close location 0.01, OBV falling |
| DRAM | V2 | day change of the last completed bar | down 1.8% | -1.84% | PASS |  |  |
| DRAM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0094) | PASS |  |  |
| DRAM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.47× / 0.23× | 1.47× / 0.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 51553050) | 20 bars, last ('2026-11-19', 51553050) | PASS |  |  |
| DRIV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $26.26 | $26.26 | PASS |  |  |
| DRIV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.81 | $28.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRIV | E3 | percent from the 21-day average | 8.9% below | 8.9% below | PASS |  |  |
| DRIV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRIV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.78 | $0.78 (sr=0.7813) | PASS |  | Wilder ATR14 |
| DRIV | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| DRIV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.8 | +6.8 | PASS |  |  |
| DRIV | L-ema21 | ladder row ema21: price and gap = price vs average | $28.81, -8.9% | $28.81, -8.9% | PASS |  |  |
| DRIV | L-note | "Last close $X · date" note = last completed bar | Last close $26.26 · Nov 19 | $26.26 · Nov 19 | PASS |  |  |
| DRIV | L-now | ladder price row = compared price; name = the basis label | $26.26 "After hours" | $26.26 "after hours" | PASS |  |  |
| DRIV | L-sma200 | ladder row sma200: price and gap = price vs average | $34.16, -23.1% | $34.16, -23.1% | PASS |  |  |
| DRIV | L-sma50 | ladder row sma50: price and gap = price vs average | $31.15, -15.7% | $31.15, -15.7% | PASS |  |  |
| DRIV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $26.26 / entry $26.26 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRIV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DRIV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.4 | 28.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRIV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -7.5% vs +9.2% | -7.5% vs 9.2% | PASS |  |  |
| DRIV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DRIV | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.9 | 39.0 | PASS |  | Wilder, completed bars |
| DRIV | T4w | words "20 or more / below 20" | 20 or more | ADX 39.0 | PASS |  |  |
| DRIV | T5 | "counted at the last close ($X, date)" = last completed bar | $26.26, Nov 19 | $26.26, Nov 19 | PASS |  |  |
| DRIV | T6 | price vs 200-day average (S1 pattern sma values) | $26.26 vs $34.16 · -23.1% | $26.26 vs $34.16 · -23.1% | PASS |  |  |
| DRIV | T6w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T7 | price vs 50-day average (S1 pattern sma values) | $26.26 vs $31.15 · -15.7% | $26.26 vs $31.15 · -15.7% | PASS |  |  |
| DRIV | T7w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.9% over 30 td | -0.9% over 30 td | PASS |  |  |
| DRIV | T8r | word "rising" | not rising | not rising | PASS |  |  |
| DRIV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DRIV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 38.5% below $42.67 | 38.5% below $42.67 | PASS |  | closing high would be 42.45 |
| DRIV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 38.5% below | PASS |  |  |
| DRIV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $42.67 | $42.67459709729379 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DRIV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.09%, close location 0.00, OBV falling |
| DRIV | V2 | day change of the last completed bar | down 2.1% | -2.09% | PASS |  |  |
| DRIV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| DRIV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRIV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.75× / 0.70× | 0.75× / 0.70× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRIV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 29857) | 20 bars, last ('2026-11-19', 29857) | PASS |  |  |
| DUK | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $128.86 | $128.86 | PASS |  |  |
| DUK | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $127.16 | $127.16 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DUK | E3 | percent from the 21-day average | 1.3% above | 1.3% above | PASS |  |  |
| DUK | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DUK | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.16 | $2.16 (sr=2.1623) | PASS |  | Wilder ATR14 |
| DUK | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves above |
| DUK | L-ema21 | ladder row ema21: price and gap = price vs average | $127.16, 1.3% | $127.16, 1.3% | PASS |  |  |
| DUK | L-note | "Last close $X · date" note = last completed bar | Last close $128.86 · Nov 19 | $128.86 · Nov 19 | PASS |  |  |
| DUK | L-now | ladder price row = compared price; name = the basis label | $128.86 "After hours" | $128.86 "after hours" | PASS |  |  |
| DUK | L-sma200 | ladder row sma200: price and gap = price vs average | $124.99, 3.1% | $124.99, 3.1% | PASS |  |  |
| DUK | L-sma50 | ladder row sma50: price and gap = price vs average | $121.41, 6.1% | $121.41, 6.1% | PASS |  |  |
| DUK | S5-price | S5: the same live price reads the same on the header and the Entry block | header $128.86 / entry $128.86 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DUK | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DUK | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.7 | 59.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DUK | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +5.4% vs +9.2% | 5.4% vs 9.2% | PASS |  |  |
| DUK | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DUK | T4 | ADX 14 (S1 /api/sr meta.adx) | 43.9 | 43.9 | PASS |  | Wilder, completed bars |
| DUK | T4w | words "20 or more / below 20" | 20 or more | ADX 43.9 | PASS |  |  |
| DUK | T5 | "counted at the last close ($X, date)" = last completed bar | $128.86, Nov 19 | $128.86, Nov 19 | PASS |  |  |
| DUK | T6 | price vs 200-day average (S1 pattern sma values) | $128.86 vs $124.99 · +3.1% | $128.86 vs $124.99 · 3.1% | PASS |  |  |
| DUK | T6w | word "Above" | Above | Above | PASS |  |  |
| DUK | T7 | price vs 50-day average (S1 pattern sma values) | $128.86 vs $121.41 · +6.1% | $128.86 vs $121.41 · 6.1% | PASS |  |  |
| DUK | T7w | word "Above" | Above | Above | PASS |  |  |
| DUK | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.8% over 30 td | +0.8% over 30 td | PASS |  |  |
| DUK | T8r | word "rising" | still rising | rising | PASS |  |  |
| DUK | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DUK | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.2% below $134.49 | 4.2% below $134.49 | PASS |  | closing high would be 133.46 |
| DUK | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.2% below | PASS |  |  |
| DUK | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $134.49 | $134.49 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DUK | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change -0.92%, close location 0.87, OBV rising |
| DUK | V2 | day change of the last completed bar | down 0.9% | -0.92% | PASS |  |  |
| DUK | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.87 (raw 0.8708) | PASS |  |  |
| DUK | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| DUK | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.00× / 0.55× | 1.00× / 0.55× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DUK | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4486433) | 20 bars, last ('2026-11-19', 4486433) | PASS |  |  |
| ELIL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $36.57 | $36.57 | PASS |  |  |
| ELIL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $37.84 | $37.84 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ELIL | E3 | percent from the 21-day average | 3.4% below | 3.4% below | PASS |  |  |
| ELIL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ELIL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.21 | $2.21 (sr=2.2101) | PASS |  | Wilder ATR14 |
| ELIL | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| ELIL | L-ema21 | ladder row ema21: price and gap = price vs average | $37.84, -3.4% | $37.84, -3.4% | PASS |  |  |
| ELIL | L-note | "Last close $X · date" note = last completed bar | Last close $36.57 · Nov 19 | $36.57 · Nov 19 | PASS |  |  |
| ELIL | L-now | ladder price row = compared price; name = the basis label | $36.57 "After hours" | $36.57 "after hours" | PASS |  |  |
| ELIL | L-sma200 | ladder row sma200: price and gap = price vs average | $27.24, 34.3% | $27.24, 34.3% | PASS |  |  |
| ELIL | L-sma50 | ladder row sma50: price and gap = price vs average | $32.73, 11.7% | $32.73, 11.7% | PASS |  |  |
| ELIL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $36.57 / entry $36.57 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ELIL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ELIL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.6 | 48.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ELIL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +19.1% vs +9.2% | 19.1% vs 9.2% | PASS |  |  |
| ELIL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ELIL | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.0 | 31.0 | PASS |  | Wilder, completed bars |
| ELIL | T4w | words "20 or more / below 20" | 20 or more | ADX 31.0 | PASS |  |  |
| ELIL | T5 | "counted at the last close ($X, date)" = last completed bar | $36.57, Nov 19 | $36.57, Nov 19 | PASS |  |  |
| ELIL | T6 | price vs 200-day average (S1 pattern sma values) | $36.57 vs $27.24 · +34.3% | $36.57 vs $27.24 · 34.3% | PASS |  |  |
| ELIL | T6w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T7 | price vs 50-day average (S1 pattern sma values) | $36.57 vs $32.73 · +11.7% | $36.57 vs $32.73 · 11.7% | PASS |  |  |
| ELIL | T7w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +4.9% over 30 td | PASS |  |  |
| ELIL | T8r | word "rising" | still rising | rising | PASS |  |  |
| ELIL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ELIL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 16.0% below $43.56 | 16.0% below $43.55 | PASS |  | closing high would be 41.85 |
| ELIL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 16.0% below | PASS |  |  |
| ELIL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.56 | $43.555 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ELIL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.47%, close location 0.14, OBV falling |
| ELIL | V2 | day change of the last completed bar | down 4.5% | -4.47% | PASS |  |  |
| ELIL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1395) | PASS |  |  |
| ELIL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ELIL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.70× / 0.74× | 0.70× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ELIL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 43638) | 20 bars, last ('2026-11-19', 43638) | PASS |  |  |
| EQIX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,018.05 | $1,018.05 | PASS |  |  |
| EQIX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1024.76 | $1024.76 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| EQIX | E3 | percent from the 21-day average | 0.7% below | 0.7% below | PASS |  |  |
| EQIX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| EQIX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $32.99 | $32.99 (sr=32.9877) | PASS |  | Wilder ATR14 |
| EQIX | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| EQIX | L-ema21 | ladder row ema21: price and gap = price vs average | $1024.76, -0.7% | $1024.76, -0.7% | PASS |  |  |
| EQIX | L-note | "Last close $X · date" note = last completed bar | Last close $1,018.45 · Nov 19 | $1,018.45 · Nov 19 | PASS |  |  |
| EQIX | L-now | ladder price row = compared price; name = the basis label | $1018.05 "After hours" | $1018.05 "after hours" | PASS |  |  |
| EQIX | L-sma200 | ladder row sma200: price and gap = price vs average | $1016.34, 0.2% | $1016.34, 0.2% | PASS |  |  |
| EQIX | L-sma50 | ladder row sma50: price and gap = price vs average | $1013.93, 0.4% | $1013.92, 0.4% | PASS |  |  |
| EQIX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,018.05 / entry $1,018.05 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| EQIX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| EQIX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.1 | 49.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| EQIX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +35.8% vs +9.2% | 35.8% vs 9.2% | PASS |  |  |
| EQIX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| EQIX | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.3 | 17.3 | PASS |  | Wilder, completed bars |
| EQIX | T4w | words "20 or more / below 20" | below 20 | ADX 17.3 | PASS |  |  |
| EQIX | T5 | "counted at the last close ($X, date)" = last completed bar | $1,018.45, Nov 19 | $1018.45, Nov 19 | PASS |  |  |
| EQIX | T6 | price vs 200-day average (S1 pattern sma values) | $1,018.45 vs $1,016.34 · +0.2% | $1018.45 vs $1016.34 · 0.2% | PASS |  |  |
| EQIX | T6w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T7 | price vs 50-day average (S1 pattern sma values) | $1,018.45 vs $1,013.92 · +0.4% | $1018.45 vs $1013.92 · 0.4% | PASS |  |  |
| EQIX | T7w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| EQIX | T8r | word "rising" | still rising | rising | PASS |  |  |
| EQIX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| EQIX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.5% below $1,112.65 | 8.5% below $1112.65 | PASS |  | closing high would be 1104.67 |
| EQIX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.5% below | PASS |  |  |
| EQIX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,112.65 | $1112.652 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| EQIX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.74%, close location 0.06, OBV falling |
| EQIX | V2 | day change of the last completed bar | down 1.7% | -1.74% | PASS |  |  |
| EQIX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0577) | PASS |  |  |
| EQIX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| EQIX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.93× / 0.54× | 1.93× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| EQIX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1159637) | 20 bars, last ('2026-11-19', 1159637) | PASS |  |  |
| EQIX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.93, OBV falling | condition true | PASS |  |  |
| ETN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $330.57 | $330.57 | PASS |  |  |
| ETN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $360.16 | $360.16 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ETN | E3 | percent from the 21-day average | 8.2% below | 8.2% below | PASS |  |  |
| ETN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ETN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.49 | $17.49 (sr=17.4889) | PASS |  | Wilder ATR14 |
| ETN | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| ETN | L-ema21 | ladder row ema21: price and gap = price vs average | $360.16, -8.2% | $360.16, -8.2% | PASS |  |  |
| ETN | L-note | "Last close $X · date" note = last completed bar | Last close $330.57 · Nov 19 | $330.57 · Nov 19 | PASS |  |  |
| ETN | L-now | ladder price row = compared price; name = the basis label | $330.57 "After hours" | $330.57 "after hours" | PASS |  |  |
| ETN | L-sma200 | ladder row sma200: price and gap = price vs average | $397.3, -16.8% | $397.30, -16.8% | PASS |  |  |
| ETN | L-sma50 | ladder row sma50: price and gap = price vs average | $395.04, -16.3% | $395.04, -16.3% | PASS |  |  |
| ETN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $330.57 / entry $330.57 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ETN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ETN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.1 | 36.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ETN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.4% vs +9.2% | -4.4% vs 9.2% | PASS |  |  |
| ETN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ETN | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.4 | 27.4 | PASS |  | Wilder, completed bars |
| ETN | T4w | words "20 or more / below 20" | 20 or more | ADX 27.4 | PASS |  |  |
| ETN | T5 | "counted at the last close ($X, date)" = last completed bar | $330.57, Nov 19 | $330.57, Nov 19 | PASS |  |  |
| ETN | T6 | price vs 200-day average (S1 pattern sma values) | $330.57 vs $397.30 · -16.8% | $330.57 vs $397.30 · -16.8% | PASS |  |  |
| ETN | T6w | word "Below" | Below | Below | PASS |  |  |
| ETN | T7 | price vs 50-day average (S1 pattern sma values) | $330.57 vs $395.04 · -16.3% | $330.57 vs $395.04 · -16.3% | PASS |  |  |
| ETN | T7w | word "Below" | Below | Below | PASS |  |  |
| ETN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| ETN | T8r | word "rising" | still rising | rising | PASS |  |  |
| ETN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ETN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.8% below $478.00 | 30.8% below $478.00 | PASS |  | closing high would be 459.96 |
| ETN | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.8% below | PASS |  |  |
| ETN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $478.00 | $478 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ETN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.30%, close location 0.04, OBV falling |
| ETN | V2 | day change of the last completed bar | down 2.3% | -2.30% | PASS |  |  |
| ETN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0354) | PASS |  |  |
| ETN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ETN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.23× / 0.43× | 1.23× / 0.43× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ETN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 3301873) | 20 bars, last ('2026-11-19', 3301873) | PASS |  |  |
| FCX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $49.12 | $49.12 | PASS |  |  |
| FCX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $60.07 | $60.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FCX | E3 | percent from the 21-day average | 18.2% below | 18.2% below | PASS |  |  |
| FCX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| FCX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.02 | $3.02 (sr=3.0159) | PASS |  | Wilder ATR14 |
| FCX | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  · 3.6 day-moves below |
| FCX | L-ema21 | ladder row ema21: price and gap = price vs average | $60.07, -18.2% | $60.07, -18.2% | PASS |  |  |
| FCX | L-note | "Last close $X · date" note = last completed bar | Last close $49.12 · Nov 19 | $49.12 · Nov 19 | PASS |  |  |
| FCX | L-now | ladder price row = compared price; name = the basis label | $49.12 "After hours" | $49.12 "after hours" | PASS |  |  |
| FCX | L-sma200 | ladder row sma200: price and gap = price vs average | $65.01, -24.4% | $65.01, -24.4% | PASS |  |  |
| FCX | L-sma50 | ladder row sma50: price and gap = price vs average | $66.79, -26.5% | $66.79, -26.5% | PASS |  |  |
| FCX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $49.12 / entry $49.12 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| FCX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FCX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.8 | 23.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FCX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +19.1% vs +9.2% | 19.1% vs 9.2% | PASS |  |  |
| FCX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FCX | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.5 | 30.5 | PASS |  | Wilder, completed bars |
| FCX | T4w | words "20 or more / below 20" | 20 or more | ADX 30.5 | PASS |  |  |
| FCX | T5 | "counted at the last close ($X, date)" = last completed bar | $49.12, Nov 19 | $49.12, Nov 19 | PASS |  |  |
| FCX | T6 | price vs 200-day average (S1 pattern sma values) | $49.12 vs $65.01 · -24.4% | $49.12 vs $65.01 · -24.4% | PASS |  |  |
| FCX | T6w | word "Below" | Below | Below | PASS |  |  |
| FCX | T7 | price vs 50-day average (S1 pattern sma values) | $49.12 vs $66.79 · -26.5% | $49.12 vs $66.79 · -26.5% | PASS |  |  |
| FCX | T7w | word "Below" | Below | Below | PASS |  |  |
| FCX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.4% over 30 td | +1.4% over 30 td | PASS |  |  |
| FCX | T8r | word "rising" | still rising | rising | PASS |  |  |
| FCX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FCX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 38.8% below $80.24 | 38.8% below $80.24 | PASS |  | closing high would be 79.91 |
| FCX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 38.8% below | PASS |  |  |
| FCX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.24 | $80.24 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FCX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.53%, close location 0.05, OBV falling |
| FCX | V2 | day change of the last completed bar | down 4.5% | -4.53% | PASS |  |  |
| FCX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0548) | PASS |  |  |
| FCX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FCX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.18× / 0.74× | 2.18× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FCX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 26737212) | 20 bars, last ('2026-11-19', 26737212) | PASS |  |  |
| FCX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.18, OBV falling | condition true | PASS |  |  |
| GDX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $72.00 | $72.00 | PASS |  |  |
| GDX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $81.82 | $81.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDX | E3 | percent from the 21-day average | 12.0% below | 12.0% below | PASS |  |  |
| GDX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GDX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.57 | $3.57 (sr=3.5688) | PASS |  | Wilder ATR14 |
| GDX | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| GDX | L-ema21 | ladder row ema21: price and gap = price vs average | $81.82, -12.0% | $81.82, -12.0% | PASS |  |  |
| GDX | L-note | "Last close $X · date" note = last completed bar | Last close $72.00 · Nov 19 | $72.00 · Nov 19 | PASS |  |  |
| GDX | L-now | ladder price row = compared price; name = the basis label | $72 "After hours" | $72.00 "after hours" | PASS |  |  |
| GDX | L-sma200 | ladder row sma200: price and gap = price vs average | $89.18, -19.3% | $89.18, -19.3% | PASS |  |  |
| GDX | L-sma50 | ladder row sma50: price and gap = price vs average | $86.51, -16.8% | $86.51, -16.8% | PASS |  |  |
| GDX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $72.00 / entry $72.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GDX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.1 | 33.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.1% vs +9.2% | -5.1% vs 9.2% | PASS |  |  |
| GDX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDX | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.9 | 19.9 | PASS |  | Wilder, completed bars |
| GDX | T4w | words "20 or more / below 20" | below 20 | ADX 19.9 | PASS |  |  |
| GDX | T5 | "counted at the last close ($X, date)" = last completed bar | $72.00, Nov 19 | $72.00, Nov 19 | PASS |  |  |
| GDX | T6 | price vs 200-day average (S1 pattern sma values) | $72.00 vs $89.18 · -19.3% | $72.00 vs $89.18 · -19.3% | PASS |  |  |
| GDX | T6w | word "Below" | Below | Below | PASS |  |  |
| GDX | T7 | price vs 50-day average (S1 pattern sma values) | $72.00 vs $86.51 · -16.8% | $72.00 vs $86.51 · -16.8% | PASS |  |  |
| GDX | T7w | word "Below" | Below | Below | PASS |  |  |
| GDX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.1% over 30 td | -2.1% over 30 td | PASS |  |  |
| GDX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 38.6% below $117.18 | 38.6% below $117.18 | PASS |  | closing high would be 115.84 |
| GDX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 38.6% below | PASS |  |  |
| GDX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $117.18 | $117.18000030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.77%, close location 0.03, OBV falling |
| GDX | V2 | day change of the last completed bar | down 3.8% | -3.77% | PASS |  |  |
| GDX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0294) | PASS |  |  |
| GDX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.31× / 0.76× | 1.31× / 0.76× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 28913954) | 20 bars, last ('2026-11-19', 28913954) | PASS |  |  |
| GDXU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $20.35 | $20.35 | PASS |  |  |
| GDXU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $26.63 | $26.63 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDXU.TO | E3 | percent from the 21-day average | 23.6% below | 23.6% below | PASS |  |  |
| GDXU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GDXU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.38 | $2.38 (sr=2.3835) | PASS |  | Wilder ATR14 |
| GDXU.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| GDXU.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| GDXU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $26.63, -23.6% | $26.63, -23.6% | PASS |  |  |
| GDXU.TO | L-now | ladder price row = compared price; name = the basis label | $20.35 "Last close" | $20.35 "last close" | PASS |  |  |
| GDXU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $35.66, -42.9% | $35.66, -42.9% | PASS |  |  |
| GDXU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $30.66, -33.6% | $30.66, -33.6% | PASS |  |  |
| GDXU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDXU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.4 | 33.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDXU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -34.1% vs +9.2% | -34.1% vs 9.2% | PASS |  |  |
| GDXU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDXU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.8 | 20.8 | PASS |  | Wilder, completed bars |
| GDXU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.8 | PASS |  |  |
| GDXU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $20.35 vs $35.66 · -42.9% | $20.35 vs $35.66 · -42.9% | PASS |  |  |
| GDXU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $20.35 vs $30.66 · -33.6% | $20.35 vs $30.66 · -33.6% | PASS |  |  |
| GDXU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -7.0% over 30 td | -7.0% over 30 td | PASS |  |  |
| GDXU.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDXU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDXU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 68.7% below $65.00 | 68.7% below $65.00 | PASS |  | closing high would be 63.22 |
| GDXU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 68.7% below | PASS |  |  |
| GDXU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $65.00 | $65 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDXU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.78%, close location 0.02, OBV falling |
| GDXU.TO | V2 | day change of the last completed bar | down 6.8% | -6.78% | PASS |  |  |
| GDXU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0244) | PASS |  |  |
| GDXU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDXU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.69× / 0.58× | 1.69× / 0.58× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDXU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 419648) | 20 bars, last ('2026-11-19', 419648) | PASS |  |  |
| GDXU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.69, OBV falling | condition true | PASS |  |  |
| GE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $318.88 | $318.88 | PASS |  |  |
| GE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $321.56 | $321.56 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GE | E3 | percent from the 21-day average | 0.8% below | 0.8% below | PASS |  |  |
| GE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.17 | $10.17 (sr=10.1722) | PASS |  | Wilder ATR14 |
| GE | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| GE | L-ema21 | ladder row ema21: price and gap = price vs average | $321.56, -0.8% | $321.56, -0.8% | PASS |  |  |
| GE | L-note | "Last close $X · date" note = last completed bar | Last close $318.88 · Nov 19 | $318.88 · Nov 19 | PASS |  |  |
| GE | L-now | ladder price row = compared price; name = the basis label | $318.88 "After hours" | $318.88 "after hours" | PASS |  |  |
| GE | L-sma200 | ladder row sma200: price and gap = price vs average | $323.55, -1.4% | $323.55, -1.4% | PASS |  |  |
| GE | L-sma50 | ladder row sma50: price and gap = price vs average | $314.17, 1.5% | $314.17, 1.5% | PASS |  |  |
| GE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $318.88 / entry $318.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.1 | 49.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.6% vs +9.2% | 6.6% vs 9.2% | PASS |  |  |
| GE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GE | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.3 | 19.3 | PASS |  | Wilder, completed bars |
| GE | T4w | words "20 or more / below 20" | below 20 | ADX 19.3 | PASS |  |  |
| GE | T5 | "counted at the last close ($X, date)" = last completed bar | $318.88, Nov 19 | $318.88, Nov 19 | PASS |  |  |
| GE | T6 | price vs 200-day average (S1 pattern sma values) | $318.88 vs $323.55 · -1.4% | $318.88 vs $323.55 · -1.4% | PASS |  |  |
| GE | T6w | word "Below" | Below | Below | PASS |  |  |
| GE | T7 | price vs 50-day average (S1 pattern sma values) | $318.88 vs $314.17 · +1.5% | $318.88 vs $314.17 · 1.5% | PASS |  |  |
| GE | T7w | word "Above" | Above | Above | PASS |  |  |
| GE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| GE | T8r | word "rising" | still rising | rising | PASS |  |  |
| GE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.9% below $388.25 | 17.9% below $388.25 | PASS |  | closing high would be 380.64 |
| GE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.9% below | PASS |  |  |
| GE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $388.25 | $388.2496041459131 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.81%, close location 0.12, OBV rising |
| GE | V2 | day change of the last completed bar | down 2.8% | -2.81% | PASS |  |  |
| GE | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1223) | PASS |  |  |
| GE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.88× | 0.99× / 0.88× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4804813) | 20 bars, last ('2026-11-19', 4804813) | PASS |  |  |
| GEV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $756.28 | $756.28 | PASS |  |  |
| GEV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $825.02 | $825.02 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV | E3 | percent from the 21-day average | 8.3% below | 8.3% below | PASS |  |  |
| GEV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GEV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $53.56 | $53.56 (sr=53.5552) | PASS |  | Wilder ATR14 |
| GEV | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| GEV | L-ema21 | ladder row ema21: price and gap = price vs average | $825.02, -8.3% | $825.02, -8.3% | PASS |  |  |
| GEV | L-note | "Last close $X · date" note = last completed bar | Last close $756.28 · Nov 19 | $756.28 · Nov 19 | PASS |  |  |
| GEV | L-now | ladder price row = compared price; name = the basis label | $756.28 "After hours" | $756.28 "after hours" | PASS |  |  |
| GEV | L-sma200 | ladder row sma200: price and gap = price vs average | $951.31, -20.5% | $951.31, -20.5% | PASS |  |  |
| GEV | L-sma50 | ladder row sma50: price and gap = price vs average | $898.51, -15.8% | $898.51, -15.8% | PASS |  |  |
| GEV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $756.28 / entry $756.28 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GEV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GEV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.5 | 37.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +27.3% vs +9.2% | 27.3% vs 9.2% | PASS |  |  |
| GEV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.6 | 25.6 | PASS |  | Wilder, completed bars |
| GEV | T4w | words "20 or more / below 20" | 20 or more | ADX 25.6 | PASS |  |  |
| GEV | T5 | "counted at the last close ($X, date)" = last completed bar | $756.28, Nov 19 | $756.28, Nov 19 | PASS |  |  |
| GEV | T6 | price vs 200-day average (S1 pattern sma values) | $756.28 vs $951.31 · -20.5% | $756.28 vs $951.31 · -20.5% | PASS |  |  |
| GEV | T6w | word "Below" | Below | Below | PASS |  |  |
| GEV | T7 | price vs 50-day average (S1 pattern sma values) | $756.28 vs $898.51 · -15.8% | $756.28 vs $898.51 · -15.8% | PASS |  |  |
| GEV | T7w | word "Below" | Below | Below | PASS |  |  |
| GEV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.0% over 30 td | +3.0% over 30 td | PASS |  |  |
| GEV | T8r | word "rising" | still rising | rising | PASS |  |  |
| GEV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GEV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.7% below $1,195.24 | 36.7% below $1195.24 | PASS |  | closing high would be 1174.17 |
| GEV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.7% below | PASS |  |  |
| GEV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,195.24 | $1195.2406896758491 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GEV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.06%, close location 0.04, OBV falling |
| GEV | V2 | day change of the last completed bar | down 2.1% | -2.06% | PASS |  |  |
| GEV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0381) | PASS |  |  |
| GEV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.29× | 0.99× / 0.29× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 3169698) | 20 bars, last ('2026-11-19', 3169698) | PASS |  |  |
| GEV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $50.60 | $50.60 | PASS |  |  |
| GEV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $55.18 | $55.18 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV.TO | E3 | percent from the 21-day average | 8.3% below | 8.3% below | PASS |  |  |
| GEV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GEV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.47 | $3.47 (sr=3.4717) | PASS |  | Wilder ATR14 |
| GEV.TO | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| GEV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $55.18, -8.3% | $55.18, -8.3% | PASS |  |  |
| GEV.TO | L-now | ladder price row = compared price; name = the basis label | $50.6 "Last close" | $50.60 "last close" | PASS |  |  |
| GEV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.08, -21.0% | $64.08, -21.0% | PASS |  |  |
| GEV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $60.04, -15.7% | $60.04, -15.7% | PASS |  |  |
| GEV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.4 | 37.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +12.4% vs +9.2% | 12.4% vs 9.2% | PASS |  |  |
| GEV.TO | T3w | words "past year" vs the window used | 228 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.4 | 25.3 | PASS |  | Wilder, completed bars |
| GEV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.3 | PASS |  |  |
| GEV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.05%, close location 0.05, OBV falling |
| GEV.TO | V2 | day change of the last completed bar | down 2.0% | -2.05% | PASS |  |  |
| GEV.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0475) | PASS |  |  |
| GEV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.45× / 0.30× | 1.45× / 0.30× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 112061) | 20 bars, last ('2026-11-19', 112061) | PASS |  |  |
| GGLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $59.74 | $59.74 | PASS |  |  |
| GGLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $71.86 | $71.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GGLL | E3 | percent from the 21-day average | 16.9% below | 16.9% below | PASS |  |  |
| GGLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GGLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.30 | $5.30 (sr=5.2961) | PASS |  | Wilder ATR14 |
| GGLL | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| GGLL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.0 | +3.0 | PASS |  |  |
| GGLL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.6 | +5.6 | PASS |  |  |
| GGLL | L-ema21 | ladder row ema21: price and gap = price vs average | $71.86, -16.9% | $71.86, -16.9% | PASS |  |  |
| GGLL | L-note | "Last close $X · date" note = last completed bar | Last close $59.74 · Nov 19 | $59.74 · Nov 19 | PASS |  |  |
| GGLL | L-now | ladder price row = compared price; name = the basis label | $59.74 "After hours" | $59.74 "after hours" | PASS |  |  |
| GGLL | L-sma200 | ladder row sma200: price and gap = price vs average | $101.57, -41.2% | $101.57, -41.2% | PASS |  |  |
| GGLL | L-sma50 | ladder row sma50: price and gap = price vs average | $87.82, -32.0% | $87.82, -32.0% | PASS |  |  |
| GGLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $59.74 / entry $59.74 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GGLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GGLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.7 | 29.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GGLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -29.8% vs +9.2% | -29.8% vs 9.2% | PASS |  |  |
| GGLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GGLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.4 | 26.4 | PASS |  | Wilder, completed bars |
| GGLL | T4w | words "20 or more / below 20" | 20 or more | ADX 26.4 | PASS |  |  |
| GGLL | T5 | "counted at the last close ($X, date)" = last completed bar | $59.74, Nov 19 | $59.74, Nov 19 | PASS |  |  |
| GGLL | T6 | price vs 200-day average (S1 pattern sma values) | $59.74 vs $101.57 · -41.2% | $59.74 vs $101.57 · -41.2% | PASS |  |  |
| GGLL | T6w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T7 | price vs 50-day average (S1 pattern sma values) | $59.74 vs $87.82 · -32.0% | $59.74 vs $87.82 · -32.0% | PASS |  |  |
| GGLL | T7w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.4% over 30 td | -3.4% over 30 td | PASS |  |  |
| GGLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GGLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GGLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 60.5% below $151.33 | 60.5% below $151.33 | PASS |  | closing high would be 147.32 |
| GGLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 60.5% below | PASS |  |  |
| GGLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $151.33 | $151.33258699596215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GGLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.89%, close location 0.01, OBV falling |
| GGLL | V2 | day change of the last completed bar | down 6.9% | -6.89% | PASS |  |  |
| GGLL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0096) | PASS |  |  |
| GGLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GGLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.22× / 0.78× | 1.22× / 0.78× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GGLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2350123) | 20 bars, last ('2026-11-19', 2350123) | PASS |  |  |
| GIB-A.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $112.41 | $112.41 | PASS |  |  |
| GIB-A.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.49 | $113.49 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GIB-A.TO | E3 | percent from the 21-day average | 1.0% below | 1.0% below | PASS |  |  |
| GIB-A.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GIB-A.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.67 | $2.67 (sr=2.6744) | PASS |  | Wilder ATR14 |
| GIB-A.TO | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| GIB-A.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.1 | -5.1 | PASS |  |  |
| GIB-A.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.49, -1.0% | $113.49, -1.0% | PASS |  |  |
| GIB-A.TO | L-note | "Last close $X · date" note = last completed bar | Last close $112.41 · Nov 19 | $112.41 · Nov 19 | PASS |  |  |
| GIB-A.TO | L-now | ladder price row = compared price; name = the basis label | $112.41 "After hours" | $112.41 "after hours" | PASS |  |  |
| GIB-A.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $99.82, 12.6% | $99.82, 12.6% | PASS |  |  |
| GIB-A.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $106.44, 5.6% | $106.44, 5.6% | PASS |  |  |
| GIB-A.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $112.41 / entry $112.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GIB-A.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GIB-A.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.0 | 50.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GIB-A.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -7.0% vs +9.2% | -7.0% vs 9.2% | PASS |  |  |
| GIB-A.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GIB-A.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.3 | 38.3 | PASS |  | Wilder, completed bars |
| GIB-A.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 38.3 | PASS |  |  |
| GIB-A.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $112.41, Nov 19 | $112.41, Nov 19 | PASS |  |  |
| GIB-A.TO | T6 | price vs 200-day average (S1 pattern sma values) | $112.41 vs $99.82 · +12.6% | $112.41 vs $99.82 · 12.6% | PASS |  |  |
| GIB-A.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T7 | price vs 50-day average (S1 pattern sma values) | $112.41 vs $106.44 · +5.6% | $112.41 vs $106.44 · 5.6% | PASS |  |  |
| GIB-A.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.8% over 30 td | -1.8% over 30 td | PASS |  |  |
| GIB-A.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GIB-A.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GIB-A.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.4% below $131.27 | 14.4% below $131.27 | PASS |  | closing high would be 130.81 |
| GIB-A.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.4% below | PASS |  |  |
| GIB-A.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.27 | $131.26875042581284 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GIB-A.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.43%, close location 0.15, OBV rising |
| GIB-A.TO | V2 | day change of the last completed bar | down 2.4% | -2.43% | PASS |  |  |
| GIB-A.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1513) | PASS |  |  |
| GIB-A.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GIB-A.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.61× / 1.02× | 0.61× / 1.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GIB-A.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 380224) | 20 bars, last ('2026-11-19', 380224) | PASS |  |  |
| GOOGL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $272.66 | $272.66 | PASS |  |  |
| GOOGL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $295.99 | $295.99 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GOOGL | E3 | percent from the 21-day average | 7.9% below | 7.9% below | PASS |  |  |
| GOOGL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GOOGL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.73 | $10.73 (sr=10.729) | PASS |  | Wilder ATR14 |
| GOOGL | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| GOOGL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| GOOGL | L-ema21 | ladder row ema21: price and gap = price vs average | $295.99, -7.9% | $295.99, -7.9% | PASS |  |  |
| GOOGL | L-note | "Last close $X · date" note = last completed bar | Last close $272.66 · Nov 19 | $272.66 · Nov 19 | PASS |  |  |
| GOOGL | L-now | ladder price row = compared price; name = the basis label | $272.66 "After hours" | $272.66 "after hours" | PASS |  |  |
| GOOGL | L-sma200 | ladder row sma200: price and gap = price vs average | $337.04, -19.1% | $337.04, -19.1% | PASS |  |  |
| GOOGL | L-sma50 | ladder row sma50: price and gap = price vs average | $323.76, -15.8% | $323.76, -15.8% | PASS |  |  |
| GOOGL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $272.66 / entry $272.66 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GOOGL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GOOGL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.6 | 30.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GOOGL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -6.6% vs +9.2% | -6.6% vs 9.2% | PASS |  |  |
| GOOGL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GOOGL | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.3 | 24.3 | PASS |  | Wilder, completed bars |
| GOOGL | T4w | words "20 or more / below 20" | 20 or more | ADX 24.3 | PASS |  |  |
| GOOGL | T5 | "counted at the last close ($X, date)" = last completed bar | $272.66, Nov 19 | $272.66, Nov 19 | PASS |  |  |
| GOOGL | T6 | price vs 200-day average (S1 pattern sma values) | $272.66 vs $337.04 · -19.1% | $272.66 vs $337.04 · -19.1% | PASS |  |  |
| GOOGL | T6w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T7 | price vs 50-day average (S1 pattern sma values) | $272.66 vs $323.76 · -15.8% | $272.66 vs $323.76 · -15.8% | PASS |  |  |
| GOOGL | T7w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.7% over 30 td | -0.7% over 30 td | PASS |  |  |
| GOOGL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GOOGL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GOOGL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 33.2% below $408.10 | 33.2% below $408.10 | PASS |  | closing high would be 402.12 |
| GOOGL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 33.2% below | PASS |  |  |
| GOOGL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $408.10 | $408.10376741205215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GOOGL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.46%, close location 0.01, OBV falling |
| GOOGL | V2 | day change of the last completed bar | down 3.5% | -3.46% | PASS |  |  |
| GOOGL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0130) | PASS |  |  |
| GOOGL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GOOGL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.48× / 0.88× | 1.48× / 0.88× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GOOGL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 48101304) | 20 bars, last ('2026-11-19', 48101304) | PASS |  |  |
| GRID | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $152.42 | $152.42 | PASS |  |  |
| GRID | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $161.3 | $161.30 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GRID | E3 | percent from the 21-day average | 5.5% below | 5.5% below | PASS |  |  |
| GRID | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GRID | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.18 | $4.18 (sr=4.1824) | PASS |  | Wilder ATR14 |
| GRID | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| GRID | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.0 | +4.0 | PASS |  |  |
| GRID | L-ema21 | ladder row ema21: price and gap = price vs average | $161.3, -5.5% | $161.30, -5.5% | PASS |  |  |
| GRID | L-note | "Last close $X · date" note = last completed bar | Last close $152.42 · Nov 19 | $152.42 · Nov 19 | PASS |  |  |
| GRID | L-now | ladder price row = compared price; name = the basis label | $152.42 "After hours" | $152.42 "after hours" | PASS |  |  |
| GRID | L-sma200 | ladder row sma200: price and gap = price vs average | $177.83, -14.3% | $177.83, -14.3% | PASS |  |  |
| GRID | L-sma50 | ladder row sma50: price and gap = price vs average | $170.39, -10.5% | $170.39, -10.5% | PASS |  |  |
| GRID | S5-price | S5: the same live price reads the same on the header and the Entry block | header $152.42 / entry $152.42 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GRID | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GRID | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.6 | 34.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GRID | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.9% vs +9.2% | 2.9% vs 9.2% | PASS |  |  |
| GRID | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GRID | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.8 | 30.8 | PASS |  | Wilder, completed bars |
| GRID | T4w | words "20 or more / below 20" | 20 or more | ADX 30.8 | PASS |  |  |
| GRID | T5 | "counted at the last close ($X, date)" = last completed bar | $152.42, Nov 19 | $152.42, Nov 19 | PASS |  |  |
| GRID | T6 | price vs 200-day average (S1 pattern sma values) | $152.42 vs $177.83 · -14.3% | $152.42 vs $177.83 · -14.3% | PASS |  |  |
| GRID | T6w | word "Below" | Below | Below | PASS |  |  |
| GRID | T7 | price vs 50-day average (S1 pattern sma values) | $152.42 vs $170.39 · -10.5% | $152.42 vs $170.39 · -10.5% | PASS |  |  |
| GRID | T7w | word "Below" | Below | Below | PASS |  |  |
| GRID | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.6% over 30 td | +0.6% over 30 td | PASS |  |  |
| GRID | T8r | word "rising" | still rising | rising | PASS |  |  |
| GRID | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GRID | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.3% below $198.79 | 23.3% below $198.79 | PASS |  | closing high would be 198.61 |
| GRID | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.3% below | PASS |  |  |
| GRID | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $198.79 | $198.7949156186822 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GRID | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.78%, close location 0.03, OBV falling |
| GRID | V2 | day change of the last completed bar | down 1.8% | -1.78% | PASS |  |  |
| GRID | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0323) | PASS |  |  |
| GRID | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GRID | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.89× / 0.65× | 0.89× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GRID | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 547888) | 20 bars, last ('2026-11-19', 547888) | PASS |  |  |
| HD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $336.68 | $336.68 | PASS |  |  |
| HD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $336.07 | $336.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HD | E3 | percent from the 21-day average | 0.2% above | 0.2% above | PASS |  |  |
| HD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| HD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.92 | $8.92 (sr=8.917) | PASS |  | Wilder ATR14 |
| HD | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| HD | L-ema21 | ladder row ema21: price and gap = price vs average | $336.07, 0.2% | $336.07, 0.2% | PASS |  |  |
| HD | L-note | "Last close $X · date" note = last completed bar | Last close $336.68 · Nov 19 | $336.68 · Nov 19 | PASS |  |  |
| HD | L-now | ladder price row = compared price; name = the basis label | $336.68 "After hours" | $336.68 "after hours" | PASS |  |  |
| HD | L-sma200 | ladder row sma200: price and gap = price vs average | $328.77, 2.4% | $328.77, 2.4% | PASS |  |  |
| HD | L-sma50 | ladder row sma50: price and gap = price vs average | $314.35, 7.1% | $314.35, 7.1% | PASS |  |  |
| HD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $336.68 / entry $336.68 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| HD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.3 | 53.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.5% vs +9.2% | 3.5% vs 9.2% | PASS |  |  |
| HD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HD | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.4 | 38.4 | PASS |  | Wilder, completed bars |
| HD | T4w | words "20 or more / below 20" | 20 or more | ADX 38.4 | PASS |  |  |
| HD | T5 | "counted at the last close ($X, date)" = last completed bar | $336.68, Nov 19 | $336.68, Nov 19 | PASS |  |  |
| HD | T6 | price vs 200-day average (S1 pattern sma values) | $336.68 vs $328.77 · +2.4% | $336.68 vs $328.77 · 2.4% | PASS |  |  |
| HD | T6w | word "Above" | Above | Above | PASS |  |  |
| HD | T7 | price vs 50-day average (S1 pattern sma values) | $336.68 vs $314.35 · +7.1% | $336.68 vs $314.35 · 7.1% | PASS |  |  |
| HD | T7w | word "Above" | Above | Above | PASS |  |  |
| HD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.4% over 30 td | -1.4% over 30 td | PASS |  |  |
| HD | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.5% below $389.18 | 13.5% below $389.18 | PASS |  | closing high would be 382.74 |
| HD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.5% below | PASS |  |  |
| HD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $389.18 | $389.18067797780816 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.28%, close location 0.56, OBV falling |
| HD | V2 | day change of the last completed bar | down 0.3% | -0.28% | PASS |  |  |
| HD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.92× / 0.11× | 0.92× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4658535) | 20 bars, last ('2026-11-19', 4658535) | PASS |  |  |
| HURA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $35.85 | $35.85 | PASS |  |  |
| HURA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $39.77 | $39.77 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HURA.TO | E3 | percent from the 21-day average | 9.9% below | 9.9% below | PASS |  |  |
| HURA.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HURA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.33 | $1.33 (sr=1.3259) | PASS |  | Wilder ATR14 |
| HURA.TO | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| HURA.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +9.8 | +9.8 | PASS |  |  |
| HURA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $39.77, -9.9% | $39.77, -9.9% | PASS |  |  |
| HURA.TO | L-now | ladder price row = compared price; name = the basis label | $35.85 "Last close" | $35.85 "last close" | PASS |  |  |
| HURA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $52.73, -32.0% | $52.73, -32.0% | PASS |  |  |
| HURA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.6, -17.8% | $43.60, -17.8% | PASS |  |  |
| HURA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HURA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.5 | 31.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HURA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -32.5% vs +9.2% | -32.5% vs 9.2% | PASS |  |  |
| HURA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HURA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.3 | 31.3 | PASS |  | Wilder, completed bars |
| HURA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.3 | PASS |  |  |
| HURA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $35.85 vs $52.73 · -32.0% | $35.85 vs $52.73 · -32.0% | PASS |  |  |
| HURA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $35.85 vs $43.60 · -17.8% | $35.85 vs $43.60 · -17.8% | PASS |  |  |
| HURA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.6% over 30 td | -5.6% over 30 td | PASS |  |  |
| HURA.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HURA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HURA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.5% below $73.95 | 51.5% below $73.95 | PASS |  | closing high would be 73.19 |
| HURA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.5% below | PASS |  |  |
| HURA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $73.95 | $73.94999694824219 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HURA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.21%, close location 0.12, OBV falling |
| HURA.TO | V2 | day change of the last completed bar | down 2.2% | -2.21% | PASS |  |  |
| HURA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1176) | PASS |  |  |
| HURA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HURA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.81× / 0.60× | 0.81× / 0.60× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HURA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 9711) | 20 bars, last ('2026-11-19', 9711) | PASS |  |  |
| HXQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $109.61 | $109.61 | PASS |  |  |
| HXQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $114.45 | $114.45 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HXQ.TO | E3 | percent from the 21-day average | 4.2% below | 4.2% below | PASS |  |  |
| HXQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HXQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.75 | $2.75 (sr=2.748) | PASS |  | Wilder ATR14 |
| HXQ.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| HXQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $114.45, -4.2% | $114.45, -4.2% | PASS |  |  |
| HXQ.TO | L-now | ladder price row = compared price; name = the basis label | $109.61 "Last close" | $109.61 "last close" | PASS |  |  |
| HXQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $112.34, -2.4% | $112.34, -2.4% | PASS |  |  |
| HXQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $118.94, -7.8% | $118.94, -7.8% | PASS |  |  |
| HXQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HXQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.9 | 37.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HXQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.1% vs +9.2% | 10.1% vs 9.2% | PASS |  |  |
| HXQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HXQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.4 | 30.4 | PASS |  | Wilder, completed bars |
| HXQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.4 | PASS |  |  |
| HXQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $109.61 vs $112.34 · -2.4% | $109.61 vs $112.34 · -2.4% | PASS |  |  |
| HXQ.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $109.61 vs $118.94 · -7.8% | $109.61 vs $118.94 · -7.8% | PASS |  |  |
| HXQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| HXQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| HXQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HXQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.6% below $128.37 | 14.6% below $128.37 | PASS |  | closing high would be 127.79 |
| HXQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.6% below | PASS |  |  |
| HXQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $128.37 | $128.3699951171875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HXQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.97%, close location 0.05, OBV falling |
| HXQ.TO | V2 | day change of the last completed bar | down 2.0% | -1.97% | PASS |  |  |
| HXQ.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0544) | PASS |  |  |
| HXQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HXQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.48× / 0.79× | 1.48× / 0.78× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HXQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 49834) | 20 bars, last ('2026-11-19', 49834) | PASS |  |  |
| JNJ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $267.14 | $267.14 | PASS |  |  |
| JNJ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $273.73 | $273.73 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JNJ | E3 | percent from the 21-day average | 2.4% below | 2.4% below | PASS |  |  |
| JNJ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JNJ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.81 | $6.81 (sr=6.8066) | PASS |  | Wilder ATR14 |
| JNJ | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| JNJ | L-ema21 | ladder row ema21: price and gap = price vs average | $273.73, -2.4% | $273.73, -2.4% | PASS |  |  |
| JNJ | L-note | "Last close $X · date" note = last completed bar | Last close $267.14 · Nov 19 | $267.14 · Nov 19 | PASS |  |  |
| JNJ | L-now | ladder price row = compared price; name = the basis label | $267.14 "After hours" | $267.14 "after hours" | PASS |  |  |
| JNJ | L-sma200 | ladder row sma200: price and gap = price vs average | $249.26, 7.2% | $249.26, 7.2% | PASS |  |  |
| JNJ | L-sma50 | ladder row sma50: price and gap = price vs average | $267.33, -0.1% | $267.33, -0.1% | PASS |  |  |
| JNJ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $267.14 / entry $267.14 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JNJ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JNJ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.6 | 44.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JNJ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +34.9% vs +9.2% | 34.9% vs 9.2% | PASS |  |  |
| JNJ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JNJ | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.4 | 23.4 | PASS |  | Wilder, completed bars |
| JNJ | T4w | words "20 or more / below 20" | 20 or more | ADX 23.4 | PASS |  |  |
| JNJ | T5 | "counted at the last close ($X, date)" = last completed bar | $267.14, Nov 19 | $267.14, Nov 19 | PASS |  |  |
| JNJ | T6 | price vs 200-day average (S1 pattern sma values) | $267.14 vs $249.26 · +7.2% | $267.14 vs $249.26 · 7.2% | PASS |  |  |
| JNJ | T6w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T7 | price vs 50-day average (S1 pattern sma values) | $267.14 vs $267.33 · -0.1% | $267.14 vs $267.33 · -0.1% | PASS |  |  |
| JNJ | T7w | word "Below" | Below | Below | PASS |  |  |
| JNJ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.5% over 30 td | +3.5% over 30 td | PASS |  |  |
| JNJ | T8r | word "rising" | still rising | rising | PASS |  |  |
| JNJ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JNJ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.0% below $290.25 | 8.0% below $290.25 | PASS |  | closing high would be 285.75 |
| JNJ | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.0% below | PASS |  |  |
| JNJ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $290.25 | $290.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JNJ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.04%, close location 0.42, OBV falling |
| JNJ | V2 | day change of the last completed bar | down 2.0% | -2.04% | PASS |  |  |
| JNJ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JNJ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.32× / 0.80× | 1.32× / 0.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JNJ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 9825584) | 20 bars, last ('2026-11-19', 9825584) | PASS |  |  |
| JPM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $320.22 | $320.22 | PASS |  |  |
| JPM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $336.1 | $336.10 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JPM | E3 | percent from the 21-day average | 4.7% below | 4.7% below | PASS |  |  |
| JPM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JPM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.63 | $7.63 (sr=7.628) | PASS |  | Wilder ATR14 |
| JPM | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| JPM | L-ema21 | ladder row ema21: price and gap = price vs average | $336.1, -4.7% | $336.10, -4.7% | PASS |  |  |
| JPM | L-note | "Last close $X · date" note = last completed bar | Last close $320.22 · Nov 19 | $320.22 · Nov 19 | PASS |  |  |
| JPM | L-now | ladder price row = compared price; name = the basis label | $320.22 "After hours" | $320.22 "after hours" | PASS |  |  |
| JPM | L-sma200 | ladder row sma200: price and gap = price vs average | $322.86, -0.8% | $322.86, -0.8% | PASS |  |  |
| JPM | L-sma50 | ladder row sma50: price and gap = price vs average | $337.69, -5.2% | $337.69, -5.2% | PASS |  |  |
| JPM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $320.22 / entry $320.22 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JPM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JPM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.9 | 35.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JPM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +7.6% vs +9.2% | 7.6% vs 9.2% | PASS |  |  |
| JPM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JPM | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.2 | 17.2 | PASS |  | Wilder, completed bars |
| JPM | T4w | words "20 or more / below 20" | below 20 | ADX 17.2 | PASS |  |  |
| JPM | T5 | "counted at the last close ($X, date)" = last completed bar | $320.22, Nov 19 | $320.22, Nov 19 | PASS |  |  |
| JPM | T6 | price vs 200-day average (S1 pattern sma values) | $320.22 vs $322.86 · -0.8% | $320.22 vs $322.86 · -0.8% | PASS |  |  |
| JPM | T6w | word "Below" | Below | Below | PASS |  |  |
| JPM | T7 | price vs 50-day average (S1 pattern sma values) | $320.22 vs $337.69 · -5.2% | $320.22 vs $337.69 · -5.2% | PASS |  |  |
| JPM | T7w | word "Below" | Below | Below | PASS |  |  |
| JPM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.2% over 30 td | +1.2% over 30 td | PASS |  |  |
| JPM | T8r | word "rising" | still rising | rising | PASS |  |  |
| JPM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JPM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.2% below $364.68 | 12.2% below $364.68 | PASS |  | closing high would be 363.37 |
| JPM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.2% below | PASS |  |  |
| JPM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $364.68 | $364.68062001340013 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JPM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.20%, close location 0.26, OBV falling |
| JPM | V2 | day change of the last completed bar | down 1.2% | -1.20% | PASS |  |  |
| JPM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JPM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.90× / 0.50× | 0.90× / 0.50× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JPM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 6909850) | 20 bars, last ('2026-11-19', 6909850) | PASS |  |  |
| KEYS | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $281.42 | $281.42 | PASS |  |  |
| KEYS | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $301.93 | $301.93 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| KEYS | E3 | percent from the 21-day average | 6.8% below | 6.8% below | PASS |  |  |
| KEYS | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| KEYS | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $15.58 | $15.58 (sr=15.5758) | PASS |  | Wilder ATR14 |
| KEYS | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| KEYS | L-ema21 | ladder row ema21: price and gap = price vs average | $301.93, -6.8% | $301.93, -6.8% | PASS |  |  |
| KEYS | L-note | "Last close $X · date" note = last completed bar | Last close $281.42 · Nov 19 | $281.42 · Nov 19 | PASS |  |  |
| KEYS | L-now | ladder price row = compared price; name = the basis label | $281.42 "After hours" | $281.42 "after hours" | PASS |  |  |
| KEYS | L-sma200 | ladder row sma200: price and gap = price vs average | $321.72, -12.5% | $321.72, -12.5% | PASS |  |  |
| KEYS | L-sma50 | ladder row sma50: price and gap = price vs average | $331.43, -15.1% | $331.43, -15.1% | PASS |  |  |
| KEYS | S5-price | S5: the same live price reads the same on the header and the Entry block | header $281.42 / entry $281.42 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| KEYS | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| KEYS | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.3 | 38.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| KEYS | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +61.2% vs +9.2% | 61.2% vs 9.2% | PASS |  |  |
| KEYS | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| KEYS | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.6 | 33.6 | PASS |  | Wilder, completed bars |
| KEYS | T4w | words "20 or more / below 20" | 20 or more | ADX 33.6 | PASS |  |  |
| KEYS | T5 | "counted at the last close ($X, date)" = last completed bar | $281.42, Nov 19 | $281.42, Nov 19 | PASS |  |  |
| KEYS | T6 | price vs 200-day average (S1 pattern sma values) | $281.42 vs $321.72 · -12.5% | $281.42 vs $321.72 · -12.5% | PASS |  |  |
| KEYS | T6w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T7 | price vs 50-day average (S1 pattern sma values) | $281.42 vs $331.43 · -15.1% | $281.42 vs $331.43 · -15.1% | PASS |  |  |
| KEYS | T7w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.1% over 30 td | +5.1% over 30 td | PASS |  |  |
| KEYS | T8r | word "rising" | still rising | rising | PASS |  |  |
| KEYS | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| KEYS | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.8% below $389.93 | 27.8% below $389.93 | PASS |  | closing high would be 388.03 |
| KEYS | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.8% below | PASS |  |  |
| KEYS | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $389.93 | $389.93 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| KEYS | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.70%, close location 0.02, OBV falling |
| KEYS | V2 | day change of the last completed bar | down 1.7% | -1.70% | PASS |  |  |
| KEYS | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0196) | PASS |  |  |
| KEYS | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| KEYS | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.80× / 0.31× | 1.80× / 0.31× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| KEYS | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2437293) | 20 bars, last ('2026-11-19', 2437293) | PASS |  |  |
| KEYS | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.80, OBV falling | condition true | PASS |  |  |
| LIN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $510.21 | $510.21 | PASS |  |  |
| LIN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $513.22 | $513.22 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LIN | E3 | percent from the 21-day average | 0.6% below | 0.6% below | PASS |  |  |
| LIN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| LIN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.72 | $8.72 (sr=8.7168) | PASS |  | Wilder ATR14 |
| LIN | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| LIN | L-ema21 | ladder row ema21: price and gap = price vs average | $513.22, -0.6% | $513.22, -0.6% | PASS |  |  |
| LIN | L-note | "Last close $X · date" note = last completed bar | Last close $510.21 · Nov 19 | $510.21 · Nov 19 | PASS |  |  |
| LIN | L-now | ladder price row = compared price; name = the basis label | $510.21 "After hours" | $510.21 "after hours" | PASS |  |  |
| LIN | L-sma200 | ladder row sma200: price and gap = price vs average | $497.71, 2.5% | $497.71, 2.5% | PASS |  |  |
| LIN | L-sma50 | ladder row sma50: price and gap = price vs average | $493.94, 3.3% | $493.94, 3.3% | PASS |  |  |
| LIN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $510.21 / entry $510.21 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LIN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LIN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.8 | 49.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LIN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +23.5% vs +9.2% | 23.5% vs 9.2% | PASS |  |  |
| LIN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LIN | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.6 | 28.6 | PASS |  | Wilder, completed bars |
| LIN | T4w | words "20 or more / below 20" | 20 or more | ADX 28.6 | PASS |  |  |
| LIN | T5 | "counted at the last close ($X, date)" = last completed bar | $510.21, Nov 19 | $510.21, Nov 19 | PASS |  |  |
| LIN | T6 | price vs 200-day average (S1 pattern sma values) | $510.21 vs $497.71 · +2.5% | $510.21 vs $497.71 · 2.5% | PASS |  |  |
| LIN | T6w | word "Above" | Above | Above | PASS |  |  |
| LIN | T7 | price vs 50-day average (S1 pattern sma values) | $510.21 vs $493.94 · +3.3% | $510.21 vs $493.94 · 3.3% | PASS |  |  |
| LIN | T7w | word "Above" | Above | Above | PASS |  |  |
| LIN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| LIN | T8r | word "rising" | still rising | rising | PASS |  |  |
| LIN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LIN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.9% below $548.20 | 6.9% below $548.20 | PASS |  | closing high would be 546.64 |
| LIN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.9% below | PASS |  |  |
| LIN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $548.20 | $548.2 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LIN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.38%, close location 0.13, OBV falling |
| LIN | V2 | day change of the last completed bar | down 0.4% | -0.38% | PASS |  |  |
| LIN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1335) | PASS |  |  |
| LIN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LIN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.19× / 0.22× | 1.19× / 0.22× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LIN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2472822) | 20 bars, last ('2026-11-19', 2472822) | PASS |  |  |
| LLY | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,351.12 | $1,351.12 | PASS |  |  |
| LLY | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1367.81 | $1367.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LLY | E3 | percent from the 21-day average | 1.2% below | 1.2% below | PASS |  |  |
| LLY | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| LLY | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $43.36 | $43.36 (sr=43.3603) | PASS |  | Wilder ATR14 |
| LLY | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| LLY | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.8 | -5.8 | PASS |  |  |
| LLY | L-ema21 | ladder row ema21: price and gap = price vs average | $1367.81, -1.2% | $1367.81, -1.2% | PASS |  |  |
| LLY | L-note | "Last close $X · date" note = last completed bar | Last close $1,351.12 · Nov 19 | $1,351.12 · Nov 19 | PASS |  |  |
| LLY | L-now | ladder price row = compared price; name = the basis label | $1351.12 "After hours" | $1351.12 "after hours" | PASS |  |  |
| LLY | L-sma200 | ladder row sma200: price and gap = price vs average | $1116.24, 21.0% | $1116.24, 21.0% | PASS |  |  |
| LLY | L-sma50 | ladder row sma50: price and gap = price vs average | $1262.29, 7.0% | $1262.29, 7.0% | PASS |  |  |
| LLY | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,351.12 / entry $1,351.12 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LLY | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LLY | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.2 | 50.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LLY | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.7% vs +9.2% | 28.7% vs 9.2% | PASS |  |  |
| LLY | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LLY | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.8 | 34.8 | PASS |  | Wilder, completed bars |
| LLY | T4w | words "20 or more / below 20" | 20 or more | ADX 34.8 | PASS |  |  |
| LLY | T5 | "counted at the last close ($X, date)" = last completed bar | $1,351.12, Nov 19 | $1351.12, Nov 19 | PASS |  |  |
| LLY | T6 | price vs 200-day average (S1 pattern sma values) | $1,351.12 vs $1,116.24 · +21.0% | $1351.12 vs $1116.24 · 21.0% | PASS |  |  |
| LLY | T6w | word "Above" | Above | Above | PASS |  |  |
| LLY | T7 | price vs 50-day average (S1 pattern sma values) | $1,351.12 vs $1,262.29 · +7.0% | $1351.12 vs $1262.29 · 7.0% | PASS |  |  |
| LLY | T7w | word "Above" | Above | Above | PASS |  |  |
| LLY | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.7% over 30 td | +3.7% over 30 td | PASS |  |  |
| LLY | T8r | word "rising" | still rising | rising | PASS |  |  |
| LLY | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LLY | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.4% below $1,475.25 | 8.4% below $1475.25 | PASS |  | closing high would be 1443.50 |
| LLY | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.4% below | PASS |  |  |
| LLY | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,475.25 | $1475.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LLY | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.29%, close location 0.24, OBV falling |
| LLY | V2 | day change of the last completed bar | down 2.3% | -2.29% | PASS |  |  |
| LLY | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.24 (raw 0.2383) | PASS |  |  |
| LLY | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LLY | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.22× / 0.71× | 1.22× / 0.71× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LLY | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 3197830) | 20 bars, last ('2026-11-19', 3197830) | PASS |  |  |
| MDA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $38.44 | $38.44 | PASS |  |  |
| MDA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.27 | $40.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MDA.TO | E3 | percent from the 21-day average | 4.5% below | 4.5% below | PASS |  |  |
| MDA.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MDA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.21 | $2.21 (sr=2.2069) | PASS |  | Wilder ATR14 |
| MDA.TO | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| MDA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.27, -4.5% | $40.27, -4.5% | PASS |  |  |
| MDA.TO | L-note | "Last close $X · date" note = last completed bar | Last close $38.44 · Nov 19 | $38.44 · Nov 19 | PASS |  |  |
| MDA.TO | L-now | ladder price row = compared price; name = the basis label | $38.44 "After hours" | $38.44 "after hours" | PASS |  |  |
| MDA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $44.7, -14.0% | $44.70, -14.0% | PASS |  |  |
| MDA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.86, -5.9% | $40.86, -5.9% | PASS |  |  |
| MDA.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $38.44 / entry $38.44 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MDA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MDA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.1 | 44.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MDA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +68.4% vs +9.2% | 68.4% vs 9.2% | PASS |  |  |
| MDA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MDA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.3 | 25.3 | PASS |  | Wilder, completed bars |
| MDA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.3 | PASS |  |  |
| MDA.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $38.44, Nov 19 | $38.44, Nov 19 | PASS |  |  |
| MDA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $38.44 vs $44.70 · -14.0% | $38.44 vs $44.70 · -14.0% | PASS |  |  |
| MDA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $38.44 vs $40.86 · -5.9% | $38.44 vs $40.86 · -5.9% | PASS |  |  |
| MDA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.6% over 30 td | +2.6% over 30 td | PASS |  |  |
| MDA.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MDA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MDA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 43.4% below $67.90 | 43.4% below $67.90 | PASS |  | closing high would be 67.13 |
| MDA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 43.4% below | PASS |  |  |
| MDA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $67.90 | $67.9000015258789 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MDA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -3.85%, close location 0.00, OBV flat |
| MDA.TO | V2 | day change of the last completed bar | down 3.9% | -3.85% | PASS |  |  |
| MDA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0043) | PASS |  |  |
| MDA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| MDA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.62× / 0.67× | 0.62× / 0.67× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MDA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 988338) | 20 bars, last ('2026-11-19', 988338) | PASS |  |  |
| META | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $596.22 | $596.22 | PASS |  |  |
| META | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $634.22 | $634.22 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| META | E3 | percent from the 21-day average | 6.0% below | 6.0% below | PASS |  |  |
| META | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| META | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $22.17 | $22.17 (sr=22.1742) | PASS |  | Wilder ATR14 |
| META | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| META | L-ema21 | ladder row ema21: price and gap = price vs average | $634.22, -6.0% | $634.22, -6.0% | PASS |  |  |
| META | L-note | "Last close $X · date" note = last completed bar | Last close $596.22 · Nov 19 | $596.22 · Nov 19 | PASS |  |  |
| META | L-now | ladder price row = compared price; name = the basis label | $596.22 "After hours" | $596.22 "after hours" | PASS |  |  |
| META | L-sma200 | ladder row sma200: price and gap = price vs average | $629.14, -5.2% | $629.14, -5.2% | PASS |  |  |
| META | L-sma50 | ladder row sma50: price and gap = price vs average | $678.4, -12.1% | $678.40, -12.1% | PASS |  |  |
| META | S5-price | S5: the same live price reads the same on the header and the Entry block | header $596.22 / entry $596.22 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| META | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| META | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.7 | 36.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| META | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +1.0% vs +9.2% | 1.0% vs 9.2% | PASS |  |  |
| META | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| META | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.6 | 23.6 | PASS |  | Wilder, completed bars |
| META | T4w | words "20 or more / below 20" | 20 or more | ADX 23.6 | PASS |  |  |
| META | T5 | "counted at the last close ($X, date)" = last completed bar | $596.22, Nov 19 | $596.22, Nov 19 | PASS |  |  |
| META | T6 | price vs 200-day average (S1 pattern sma values) | $596.22 vs $629.14 · -5.2% | $596.22 vs $629.14 · -5.2% | PASS |  |  |
| META | T6w | word "Below" | Below | Below | PASS |  |  |
| META | T7 | price vs 50-day average (S1 pattern sma values) | $596.22 vs $678.40 · -12.1% | $596.22 vs $678.40 · -12.1% | PASS |  |  |
| META | T7w | word "Below" | Below | Below | PASS |  |  |
| META | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.1% over 30 td | -0.1% over 30 td | PASS |  |  |
| META | T8r | word "rising" | not rising | not rising | PASS |  |  |
| META | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| META | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.5% below $779.82 | 23.5% below $779.82 | PASS |  | closing high would be 777.59 |
| META | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.5% below | PASS |  |  |
| META | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $779.82 | $779.8192 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| META | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.27%, close location 0.01, OBV falling |
| META | V2 | day change of the last completed bar | down 3.3% | -3.27% | PASS |  |  |
| META | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0128) | PASS |  |  |
| META | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| META | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.71× / 0.88× | 0.71× / 0.88× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| META | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 15277898) | 20 bars, last ('2026-11-19', 15277898) | PASS |  |  |
| METU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $20.01 | $20.01 | PASS |  |  |
| METU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $22.94 | $22.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| METU | E3 | percent from the 21-day average | 12.8% below | 12.8% below | PASS |  |  |
| METU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| METU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.62 | $1.62 (sr=1.6224) | PASS |  | Wilder ATR14 |
| METU | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| METU | L-ema21 | ladder row ema21: price and gap = price vs average | $22.94, -12.8% | $22.94, -12.8% | PASS |  |  |
| METU | L-note | "Last close $X · date" note = last completed bar | Last close $20.01 · Nov 19 | $20.01 · Nov 19 | PASS |  |  |
| METU | L-now | ladder price row = compared price; name = the basis label | $20.01 "After hours" | $20.01 "after hours" | PASS |  |  |
| METU | L-sma200 | ladder row sma200: price and gap = price vs average | $25.34, -21.0% | $25.34, -21.0% | PASS |  |  |
| METU | L-sma50 | ladder row sma50: price and gap = price vs average | $26.77, -25.3% | $26.77, -25.3% | PASS |  |  |
| METU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $20.01 / entry $20.01 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| METU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| METU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.9 | 35.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| METU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -24.3% vs +9.2% | -24.3% vs 9.2% | PASS |  |  |
| METU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| METU | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.6 | 24.6 | PASS |  | Wilder, completed bars |
| METU | T4w | words "20 or more / below 20" | 20 or more | ADX 24.6 | PASS |  |  |
| METU | T5 | "counted at the last close ($X, date)" = last completed bar | $20.01, Nov 19 | $20.01, Nov 19 | PASS |  |  |
| METU | T6 | price vs 200-day average (S1 pattern sma values) | $20.01 vs $25.34 · -21.0% | $20.01 vs $25.34 · -21.0% | PASS |  |  |
| METU | T6w | word "Below" | Below | Below | PASS |  |  |
| METU | T7 | price vs 50-day average (S1 pattern sma values) | $20.01 vs $26.77 · -25.3% | $20.01 vs $26.77 · -25.3% | PASS |  |  |
| METU | T7w | word "Below" | Below | Below | PASS |  |  |
| METU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.1% over 30 td | -4.1% over 30 td | PASS |  |  |
| METU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| METU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| METU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.6% below $39.74 | 49.6% below $39.74 | PASS |  | closing high would be 39.22 |
| METU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.6% below | PASS |  |  |
| METU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $39.74 | $39.74 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| METU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.32%, close location 0.02, OBV falling |
| METU | V2 | day change of the last completed bar | down 6.3% | -6.32% | PASS |  |  |
| METU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0169) | PASS |  |  |
| METU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| METU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.43× / 0.78× | 0.43× / 0.78× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| METU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2029799) | 20 bars, last ('2026-11-19', 2029799) | PASS |  |  |
| MRVL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $138.47 | $138.47 | PASS |  |  |
| MRVL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $174.97 | $174.97 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MRVL | E3 | percent from the 21-day average | 20.9% below | 20.9% below | PASS |  |  |
| MRVL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MRVL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $15.92 | $15.92 (sr=15.9155) | PASS |  | Wilder ATR14 |
| MRVL | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| MRVL | L-ema21 | ladder row ema21: price and gap = price vs average | $174.97, -20.9% | $174.97, -20.9% | PASS |  |  |
| MRVL | L-note | "Last close $X · date" note = last completed bar | Last close $138.47 · Nov 19 | $138.47 · Nov 19 | PASS |  |  |
| MRVL | L-now | ladder price row = compared price; name = the basis label | $138.47 "After hours" | $138.47 "after hours" | PASS |  |  |
| MRVL | L-sma200 | ladder row sma200: price and gap = price vs average | $188.35, -26.5% | $188.35, -26.5% | PASS |  |  |
| MRVL | L-sma50 | ladder row sma50: price and gap = price vs average | $222.55, -37.8% | $222.55, -37.8% | PASS |  |  |
| MRVL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $138.47 / entry $138.47 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MRVL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MRVL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.6 | 31.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MRVL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +70.3% vs +9.2% | 70.3% vs 9.2% | PASS |  |  |
| MRVL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MRVL | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.7 | 32.7 | PASS |  | Wilder, completed bars |
| MRVL | T4w | words "20 or more / below 20" | 20 or more | ADX 32.7 | PASS |  |  |
| MRVL | T5 | "counted at the last close ($X, date)" = last completed bar | $138.47, Nov 19 | $138.47, Nov 19 | PASS |  |  |
| MRVL | T6 | price vs 200-day average (S1 pattern sma values) | $138.47 vs $188.35 · -26.5% | $138.47 vs $188.35 · -26.5% | PASS |  |  |
| MRVL | T6w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T7 | price vs 50-day average (S1 pattern sma values) | $138.47 vs $222.55 · -37.8% | $138.47 vs $222.55 · -37.8% | PASS |  |  |
| MRVL | T7w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +10.3% over 30 td | +10.3% over 30 td | PASS |  |  |
| MRVL | T8r | word "rising" | still rising | rising | PASS |  |  |
| MRVL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MRVL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 58.0% below $329.88 | 58.0% below $329.88 | PASS |  | closing high would be 316.43 |
| MRVL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 58.0% below | PASS |  |  |
| MRVL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $329.88 | $329.88 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MRVL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.86%, close location 0.01, OBV falling |
| MRVL | V2 | day change of the last completed bar | down 4.9% | -4.86% | PASS |  |  |
| MRVL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0074) | PASS |  |  |
| MRVL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MRVL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.22× / 0.42× | 1.22× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MRVL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 29880239) | 20 bars, last ('2026-11-19', 29880239) | PASS |  |  |
| MSFT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $498.30 | $498.30 | PASS |  |  |
| MSFT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $521.42 | $521.42 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFT | E3 | percent from the 21-day average | 4.4% below | 4.4% below | PASS |  |  |
| MSFT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MSFT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $15.92 | $15.92 (sr=15.9173) | PASS |  | Wilder ATR14 |
| MSFT | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| MSFT | L-ema21 | ladder row ema21: price and gap = price vs average | $521.42, -4.4% | $521.42, -4.4% | PASS |  |  |
| MSFT | L-note | "Last close $X · date" note = last completed bar | Last close $498.30 · Nov 19 | $498.30 · Nov 19 | PASS |  |  |
| MSFT | L-now | ladder price row = compared price; name = the basis label | $498.3 "After hours" | $498.30 "after hours" | PASS |  |  |
| MSFT | L-sma200 | ladder row sma200: price and gap = price vs average | $442.3, 12.7% | $442.30, 12.7% | PASS |  |  |
| MSFT | L-sma50 | ladder row sma50: price and gap = price vs average | $520.06, -4.2% | $520.06, -4.2% | PASS |  |  |
| MSFT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $498.30 / entry $498.30 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.2 | 39.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.1% vs +9.2% | 3.1% vs 9.2% | PASS |  |  |
| MSFT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFT | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.9 | 17.9 | PASS |  | Wilder, completed bars |
| MSFT | T4w | words "20 or more / below 20" | below 20 | ADX 17.9 | PASS |  |  |
| MSFT | T5 | "counted at the last close ($X, date)" = last completed bar | $498.30, Nov 19 | $498.30, Nov 19 | PASS |  |  |
| MSFT | T6 | price vs 200-day average (S1 pattern sma values) | $498.30 vs $442.30 · +12.7% | $498.30 vs $442.30 · 12.7% | PASS |  |  |
| MSFT | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFT | T7 | price vs 50-day average (S1 pattern sma values) | $498.30 vs $520.06 · -4.2% | $498.30 vs $520.06 · -4.2% | PASS |  |  |
| MSFT | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| MSFT | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.9% below $559.15 | 10.9% below $559.15 | PASS |  | closing high would be 555.80 |
| MSFT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.9% below | PASS |  |  |
| MSFT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $559.15 | $559.1500244140625 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.97%, close location 0.00, OBV falling |
| MSFT | V2 | day change of the last completed bar | down 2.0% | -1.97% | PASS |  |  |
| MSFT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0049) | PASS |  |  |
| MSFT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.18× / 0.62× | 1.18× / 0.62× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 28435392) | 20 bars, last ('2026-11-19', 28435392) | PASS |  |  |
| MSFU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $36.29 | $36.29 | PASS |  |  |
| MSFU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $39.97 | $39.97 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFU | E3 | percent from the 21-day average | 9.2% below | 9.2% below | PASS |  |  |
| MSFU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MSFU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.41 | $2.41 (sr=2.4138) | PASS |  | Wilder ATR14 |
| MSFU | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| MSFU | L-ema21 | ladder row ema21: price and gap = price vs average | $39.97, -9.2% | $39.97, -9.2% | PASS |  |  |
| MSFU | L-note | "Last close $X · date" note = last completed bar | Last close $36.29 · Nov 19 | $36.29 · Nov 19 | PASS |  |  |
| MSFU | L-now | ladder price row = compared price; name = the basis label | $36.29 "After hours" | $36.29 "after hours" | PASS |  |  |
| MSFU | L-sma200 | ladder row sma200: price and gap = price vs average | $31.13, 16.6% | $31.13, 16.6% | PASS |  |  |
| MSFU | L-sma50 | ladder row sma50: price and gap = price vs average | $40.16, -9.6% | $40.16, -9.6% | PASS |  |  |
| MSFU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $36.29 / entry $36.29 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.7 | 38.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -13.2% vs +9.2% | -13.2% vs 9.2% | PASS |  |  |
| MSFU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFU | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.1 | 18.1 | PASS |  | Wilder, completed bars |
| MSFU | T4w | words "20 or more / below 20" | below 20 | ADX 18.1 | PASS |  |  |
| MSFU | T5 | "counted at the last close ($X, date)" = last completed bar | $36.29, Nov 19 | $36.29, Nov 19 | PASS |  |  |
| MSFU | T6 | price vs 200-day average (S1 pattern sma values) | $36.29 vs $31.13 · +16.6% | $36.29 vs $31.13 · 16.6% | PASS |  |  |
| MSFU | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFU | T7 | price vs 50-day average (S1 pattern sma values) | $36.29 vs $40.16 · -9.6% | $36.29 vs $40.16 · -9.6% | PASS |  |  |
| MSFU | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| MSFU | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 20.9% below $45.88 | 20.9% below $45.88 | PASS |  | closing high would be 45.40 |
| MSFU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 20.9% below | PASS |  |  |
| MSFU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $45.88 | $45.880001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.51%, close location 0.01, OBV falling |
| MSFU | V2 | day change of the last completed bar | down 3.5% | -3.51% | PASS |  |  |
| MSFU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0072) | PASS |  |  |
| MSFU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.68× / 0.53× | 0.68× / 0.53× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1649880) | 20 bars, last ('2026-11-19', 1649880) | PASS |  |  |
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
| MTRX.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.3% vs +9.2% | -5.3% vs 9.2% | PASS |  |  |
| MTRX.TO | T3w | words "past year" vs the window used | 210 / 251 bars back | 250-253 bars | PASS |  |  |
| MTRX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.9 | 28.9 | PASS |  | Wilder, completed bars |
| MTRX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.9 | PASS |  |  |
| MTRX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.22%, close location 0.03, OBV falling |
| MTRX.TO | V2 | day change of the last completed bar | down 2.2% | -2.22% | PASS |  |  |
| MTRX.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0254) | PASS |  |  |
| MTRX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MTRX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.65× | 1.02× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MTRX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 9740) | 20 bars, last ('2026-11-19', 9740) | PASS |  |  |
| MU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.13 | $30.13 | PASS |  |  |
| MU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $34.71 | $34.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MU.TO | E3 | percent from the 21-day average | 13.2% below | 13.2% below | PASS |  |  |
| MU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| MU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.52 | $2.52 (sr=2.5224) | PASS |  | Wilder ATR14 |
| MU.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| MU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $34.71, -13.2% | $34.71, -13.2% | PASS |  |  |
| MU.TO | L-now | ladder price row = compared price; name = the basis label | $30.13 "Last close" | $30.13 "last close" | PASS |  |  |
| MU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.92, -11.2% | $33.92, -11.2% | PASS |  |  |
| MU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.25, -25.1% | $40.25, -25.1% | PASS |  |  |
| MU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.7 | 35.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +197.7% vs +9.2% | 197.7% vs 9.2% | PASS |  |  |
| MU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.1 | 35.1 | PASS |  | Wilder, completed bars |
| MU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 35.1 | PASS |  |  |
| MU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $30.13 vs $33.92 · -11.2% | $30.13 vs $33.92 · -11.2% | PASS |  |  |
| MU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $30.13 vs $40.25 · -25.1% | $30.13 vs $40.25 · -25.1% | PASS |  |  |
| MU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +10.4% over 30 td | +10.4% over 30 td | PASS |  |  |
| MU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 45.5% below $55.28 | 45.5% below $55.28 | PASS |  | closing high would be 53.52 |
| MU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 45.5% below | PASS |  |  |
| MU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $55.28 | $55.282308204978015 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.05%, close location 0.01, OBV falling |
| MU.TO | V2 | day change of the last completed bar | down 2.0% | -2.05% | PASS |  |  |
| MU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0132) | PASS |  |  |
| MU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.60× / 0.24× | 1.60× / 0.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 3019004) | 20 bars, last ('2026-11-19', 3019004) | PASS |  |  |
| MU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.60, OBV falling | condition true | PASS |  |  |
| NEE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $83.79 | $83.79 | PASS |  |  |
| NEE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.11 | $84.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEE | E3 | percent from the 21-day average | 0.4% below | 0.4% below | PASS |  |  |
| NEE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.62 | $1.62 (sr=1.6153) | PASS |  | Wilder ATR14 |
| NEE | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| NEE | L-ema21 | ladder row ema21: price and gap = price vs average | $84.11, -0.4% | $84.11, -0.4% | PASS |  |  |
| NEE | L-note | "Last close $X · date" note = last completed bar | Last close $83.79 · Nov 19 | $83.79 · Nov 19 | PASS |  |  |
| NEE | L-now | ladder price row = compared price; name = the basis label | $83.79 "After hours" | $83.79 "after hours" | PASS |  |  |
| NEE | L-sma200 | ladder row sma200: price and gap = price vs average | $87.29, -4.0% | $87.29, -4.0% | PASS |  |  |
| NEE | L-sma50 | ladder row sma50: price and gap = price vs average | $80.93, 3.5% | $80.93, 3.5% | PASS |  |  |
| NEE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $83.79 / entry $83.79 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.7 | 50.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -0.6% vs +9.2% | -0.6% vs 9.2% | PASS |  |  |
| NEE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEE | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.4 | 30.5 | PASS |  | Wilder, completed bars |
| NEE | T4w | words "20 or more / below 20" | 20 or more | ADX 30.5 | PASS |  |  |
| NEE | T5 | "counted at the last close ($X, date)" = last completed bar | $83.79, Nov 19 | $83.79, Nov 19 | PASS |  |  |
| NEE | T6 | price vs 200-day average (S1 pattern sma values) | $83.79 vs $87.29 · -4.0% | $83.79 vs $87.29 · -4.0% | PASS |  |  |
| NEE | T6w | word "Below" | Below | Below | PASS |  |  |
| NEE | T7 | price vs 50-day average (S1 pattern sma values) | $83.79 vs $80.93 · +3.5% | $83.79 vs $80.93 · 3.5% | PASS |  |  |
| NEE | T7w | word "Above" | Above | Above | PASS |  |  |
| NEE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.0% over 30 td | -0.1% over 30 td | PASS |  |  |
| NEE | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NEE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 15.1% below $98.75 | 15.1% below $98.75 | PASS |  | closing high would be 97.88 |
| NEE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 15.1% below | PASS |  |  |
| NEE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $98.75 | $98.75 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.17%, close location 0.58, OBV falling |
| NEE | V2 | day change of the last completed bar | down 1.2% | -1.17% | PASS |  |  |
| NEE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NEE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.76× / 0.61× | 0.76× / 0.61× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 9576224) | 20 bars, last ('2026-11-19', 9576224) | PASS |  |  |
| NEM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $100.05 | $100.05 | PASS |  |  |
| NEM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $112.72 | $112.72 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEM | E3 | percent from the 21-day average | 11.2% below | 11.2% below | PASS |  |  |
| NEM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.84 | $4.84 (sr=4.8367) | PASS |  | Wilder ATR14 |
| NEM | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| NEM | L-ema21 | ladder row ema21: price and gap = price vs average | $112.72, -11.2% | $112.72, -11.2% | PASS |  |  |
| NEM | L-note | "Last close $X · date" note = last completed bar | Last close $100.05 · Nov 19 | $100.05 · Nov 19 | PASS |  |  |
| NEM | L-now | ladder price row = compared price; name = the basis label | $100.05 "After hours" | $100.05 "after hours" | PASS |  |  |
| NEM | L-sma200 | ladder row sma200: price and gap = price vs average | $111.98, -10.7% | $111.98, -10.7% | PASS |  |  |
| NEM | L-sma50 | ladder row sma50: price and gap = price vs average | $116.36, -14.0% | $116.36, -14.0% | PASS |  |  |
| NEM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $100.05 / entry $100.05 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.6 | 33.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.3% vs +9.2% | 14.3% vs 9.2% | PASS |  |  |
| NEM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEM | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.0 | 18.0 | PASS |  | Wilder, completed bars |
| NEM | T4w | words "20 or more / below 20" | below 20 | ADX 18.0 | PASS |  |  |
| NEM | T5 | "counted at the last close ($X, date)" = last completed bar | $100.05, Nov 19 | $100.05, Nov 19 | PASS |  |  |
| NEM | T6 | price vs 200-day average (S1 pattern sma values) | $100.05 vs $111.98 · -10.7% | $100.05 vs $111.98 · -10.7% | PASS |  |  |
| NEM | T6w | word "Below" | Below | Below | PASS |  |  |
| NEM | T7 | price vs 50-day average (S1 pattern sma values) | $100.05 vs $116.36 · -14.0% | $100.05 vs $116.36 · -14.0% | PASS |  |  |
| NEM | T7w | word "Below" | Below | Below | PASS |  |  |
| NEM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.2% over 30 td | +0.1% over 30 td | PASS |  |  |
| NEM | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.0% below $135.29 | 26.0% below $135.29 | PASS |  | closing high would be 135.14 |
| NEM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.0% below | PASS |  |  |
| NEM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $135.29 | $135.29 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.29%, close location 0.04, OBV falling |
| NEM | V2 | day change of the last completed bar | down 4.3% | -4.29% | PASS |  |  |
| NEM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0385) | PASS |  |  |
| NEM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NEM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.48× / 0.89× | 1.48× / 0.89× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 9702626) | 20 bars, last ('2026-11-19', 9702626) | PASS |  |  |
| NFLX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $58.46 | $58.46 | PASS |  |  |
| NFLX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $63.24 | $63.24 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFLX | E3 | percent from the 21-day average | 7.6% below | 7.6% below | PASS |  |  |
| NFLX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NFLX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.91 | $1.91 (sr=1.9123) | PASS |  | Wilder ATR14 |
| NFLX | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| NFLX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.8 | +8.8 | PASS |  |  |
| NFLX | L-ema21 | ladder row ema21: price and gap = price vs average | $63.24, -7.6% | $63.24, -7.6% | PASS |  |  |
| NFLX | L-note | "Last close $X · date" note = last completed bar | Last close $58.46 · Nov 19 | $58.46 · Nov 19 | PASS |  |  |
| NFLX | L-now | ladder price row = compared price; name = the basis label | $58.46 "After hours" | $58.46 "after hours" | PASS |  |  |
| NFLX | L-sma200 | ladder row sma200: price and gap = price vs average | $80.06, -27.0% | $80.06, -27.0% | PASS |  |  |
| NFLX | L-sma50 | ladder row sma50: price and gap = price vs average | $67.82, -13.8% | $67.82, -13.8% | PASS |  |  |
| NFLX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $58.46 / entry $58.46 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFLX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFLX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.7 | 30.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFLX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -46.9% vs +9.2% | -46.9% vs 9.2% | PASS |  |  |
| NFLX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFLX | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.6 | 25.6 | PASS |  | Wilder, completed bars |
| NFLX | T4w | words "20 or more / below 20" | 20 or more | ADX 25.6 | PASS |  |  |
| NFLX | T5 | "counted at the last close ($X, date)" = last completed bar | $58.46, Nov 19 | $58.46, Nov 19 | PASS |  |  |
| NFLX | T6 | price vs 200-day average (S1 pattern sma values) | $58.46 vs $80.06 · -27.0% | $58.46 vs $80.06 · -27.0% | PASS |  |  |
| NFLX | T6w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T7 | price vs 50-day average (S1 pattern sma values) | $58.46 vs $67.82 · -13.8% | $58.46 vs $67.82 · -13.8% | PASS |  |  |
| NFLX | T7w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.2% over 30 td | -4.2% over 30 td | PASS |  |  |
| NFLX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFLX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFLX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 48.4% below $113.34 | 48.4% below $113.34 | PASS |  | closing high would be 110.00 |
| NFLX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 48.4% below | PASS |  |  |
| NFLX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $113.34 | $113.33999633789062 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFLX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.27%, close location 0.12, OBV falling |
| NFLX | V2 | day change of the last completed bar | down 2.3% | -2.27% | PASS |  |  |
| NFLX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1195) | PASS |  |  |
| NFLX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFLX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.93× / 0.69× | 0.93× / 0.70× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFLX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 37424853) | 20 bars, last ('2026-11-19', 37424853) | PASS |  |  |
| NFXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.45 | $9.45 | PASS |  |  |
| NFXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.2 | $11.20 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFXL | E3 | percent from the 21-day average | 15.7% below | 15.7% below | PASS |  |  |
| NFXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NFXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.69 | $0.69 (sr=0.6884) | PASS |  | Wilder ATR14 |
| NFXL | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| NFXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.9 | +12.9 | PASS |  |  |
| NFXL | L-ema21 | ladder row ema21: price and gap = price vs average | $11.2, -15.7% | $11.20, -15.7% | PASS |  |  |
| NFXL | L-note | "Last close $X · date" note = last completed bar | Last close $9.45 · Nov 19 | $9.45 · Nov 19 | PASS |  |  |
| NFXL | L-now | ladder price row = compared price; name = the basis label | $9.45 "After hours" | $9.45 "after hours" | PASS |  |  |
| NFXL | L-sma200 | ladder row sma200: price and gap = price vs average | $20.07, -52.9% | $20.07, -52.9% | PASS |  |  |
| NFXL | L-sma50 | ladder row sma50: price and gap = price vs average | $13.1, -27.9% | $13.10, -27.9% | PASS |  |  |
| NFXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.45 / entry $9.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.3 | 30.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -77.7% vs +9.2% | -77.7% vs 9.2% | PASS |  |  |
| NFXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.3 | 27.3 | PASS |  | Wilder, completed bars |
| NFXL | T4w | words "20 or more / below 20" | 20 or more | ADX 27.3 | PASS |  |  |
| NFXL | T5 | "counted at the last close ($X, date)" = last completed bar | $9.45, Nov 19 | $9.45, Nov 19 | PASS |  |  |
| NFXL | T6 | price vs 200-day average (S1 pattern sma values) | $9.45 vs $20.07 · -52.9% | $9.45 vs $20.07 · -52.9% | PASS |  |  |
| NFXL | T6w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T7 | price vs 50-day average (S1 pattern sma values) | $9.45 vs $13.10 · -27.9% | $9.45 vs $13.10 · -27.9% | PASS |  |  |
| NFXL | T7w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -9.9% over 30 td | -9.9% over 30 td | PASS |  |  |
| NFXL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 79.0% below $45.02 | 79.0% below $45.02 | PASS |  | closing high would be 42.41 |
| NFXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 79.0% below | PASS |  |  |
| NFXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $45.02 | $45.02122582583708 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.35%, close location 0.12, OBV falling |
| NFXL | V2 | day change of the last completed bar | down 4.3% | -4.35% | PASS |  |  |
| NFXL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1200) | PASS |  |  |
| NFXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.60× | 0.88× / 0.60× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1477109) | 20 bars, last ('2026-11-19', 1477109) | PASS |  |  |
| NTR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $94.00 | $94.00 | PASS |  |  |
| NTR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $98.84 | $98.84 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NTR.TO | E3 | percent from the 21-day average | 4.9% below | 4.9% below | PASS |  |  |
| NTR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NTR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.87 | $2.87 (sr=2.8701) | PASS |  | Wilder ATR14 |
| NTR.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| NTR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $98.84, -4.9% | $98.84, -4.9% | PASS |  |  |
| NTR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $94.00 · Nov 19 | $94.00 · Nov 19 | PASS |  |  |
| NTR.TO | L-now | ladder price row = compared price; name = the basis label | $94 "After hours" | $94.00 "after hours" | PASS |  |  |
| NTR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $97.78, -3.9% | $97.78, -3.9% | PASS |  |  |
| NTR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $100.66, -6.6% | $100.66, -6.6% | PASS |  |  |
| NTR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $94.00 / entry $94.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NTR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NTR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.2 | 35.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NTR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +23.4% vs +9.2% | 23.4% vs 9.2% | PASS |  |  |
| NTR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NTR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.3 | 21.3 | PASS |  | Wilder, completed bars |
| NTR.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 21.3 | PASS |  |  |
| NTR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $94.00, Nov 19 | $94.00, Nov 19 | PASS |  |  |
| NTR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $94.00 vs $97.78 · -3.9% | $94.00 vs $97.78 · -3.9% | PASS |  |  |
| NTR.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| NTR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $94.00 vs $100.66 · -6.6% | $94.00 vs $100.66 · -6.6% | PASS |  |  |
| NTR.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| NTR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.7% over 30 td | +1.7% over 30 td | PASS |  |  |
| NTR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| NTR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NTR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.7% below $114.19 | 17.7% below $114.19 | PASS |  | closing high would be 111.71 |
| NTR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.7% below | PASS |  |  |
| NTR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $114.19 | $114.18839715257722 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NTR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.55%, close location 0.32, OBV rising |
| NTR.TO | V2 | day change of the last completed bar | down 0.6% | -0.55% | PASS |  |  |
| NTR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| NTR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.45× / 0.18× | 0.45× / 0.18× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NTR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 850679) | 20 bars, last ('2026-11-19', 850679) | PASS |  |  |
| NVDA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $145.98 | $145.98 | PASS |  |  |
| NVDA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $180.71 | $180.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDA | E3 | percent from the 21-day average | 19.2% below | 19.2% below | PASS |  |  |
| NVDA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NVDA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.88 | $9.88 (sr=9.8765) | PASS |  | Wilder ATR14 |
| NVDA | E5 | distance in normal day-moves | 3.5 | 3.5 | PASS |  | gauge dot note uses the same number:  · 3.5 day-moves below |
| NVDA | L-ema21 | ladder row ema21: price and gap = price vs average | $180.71, -19.2% | $180.71, -19.2% | PASS |  |  |
| NVDA | L-note | "Last close $X · date" note = last completed bar | Last close $145.98 · Nov 19 | $145.98 · Nov 19 | PASS |  |  |
| NVDA | L-now | ladder price row = compared price; name = the basis label | $145.98 "After hours" | $145.98 "after hours" | PASS |  |  |
| NVDA | L-sma200 | ladder row sma200: price and gap = price vs average | $203.32, -28.2% | $203.32, -28.2% | PASS |  |  |
| NVDA | L-sma50 | ladder row sma50: price and gap = price vs average | $208.86, -30.1% | $208.86, -30.1% | PASS |  |  |
| NVDA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $145.98 / entry $145.98 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 19.6 | 19.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -21.6% vs +9.2% | -21.5% vs 9.2% | PASS |  |  |
| NVDA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDA | T4 | ADX 14 (S1 /api/sr meta.adx) | 48.6 | 48.6 | PASS |  | Wilder, completed bars |
| NVDA | T4w | words "20 or more / below 20" | 20 or more | ADX 48.6 | PASS |  |  |
| NVDA | T5 | "counted at the last close ($X, date)" = last completed bar | $145.98, Nov 19 | $145.98, Nov 19 | PASS |  |  |
| NVDA | T6 | price vs 200-day average (S1 pattern sma values) | $145.98 vs $203.32 · -28.2% | $145.98 vs $203.32 · -28.2% | PASS |  |  |
| NVDA | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T7 | price vs 50-day average (S1 pattern sma values) | $145.98 vs $208.86 · -30.1% | $145.98 vs $208.86 · -30.1% | PASS |  |  |
| NVDA | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.9% over 30 td | +0.9% over 30 td | PASS |  |  |
| NVDA | T8r | word "rising" | still rising | rising | PASS |  |  |
| NVDA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 40.0% below $243.37 | 40.0% below $243.37 | PASS |  | closing high would be 239.24 |
| NVDA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 40.0% below | PASS |  |  |
| NVDA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $243.37 | $243.3699951171875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.30%, close location 0.02, OBV falling |
| NVDA | V2 | day change of the last completed bar | down 3.3% | -3.30% | PASS |  |  |
| NVDA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0217) | PASS |  |  |
| NVDA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.86× / 0.49× | 1.86× / 0.49× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 311799752) | 20 bars, last ('2026-11-19', 311799752) | PASS |  |  |
| NVDA | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.86, OBV falling | condition true | PASS |  |  |
| NVDL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $14.25 | $14.25 | PASS |  |  |
| NVDL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $22.87 | $22.87 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDL | E3 | percent from the 21-day average | 37.7% below | 37.7% below | PASS |  |  |
| NVDL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NVDL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.47 | $2.47 (sr=2.4655) | PASS |  | Wilder ATR14 |
| NVDL | E5 | distance in normal day-moves | 3.5 | 3.5 | PASS |  | gauge dot note uses the same number:  · 3.5 day-moves below |
| NVDL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.2 | +3.2 | PASS |  |  |
| NVDL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.4 | +3.4 | PASS |  |  |
| NVDL | L-ema21 | ladder row ema21: price and gap = price vs average | $22.87, -37.7% | $22.87, -37.7% | PASS |  |  |
| NVDL | L-note | "Last close $X · date" note = last completed bar | Last close $14.25 · Nov 19 | $14.25 · Nov 19 | PASS |  |  |
| NVDL | L-now | ladder price row = compared price; name = the basis label | $14.25 "After hours" | $14.25 "after hours" | PASS |  |  |
| NVDL | L-sma200 | ladder row sma200: price and gap = price vs average | $31.19, -54.3% | $31.19, -54.3% | PASS |  |  |
| NVDL | L-sma50 | ladder row sma50: price and gap = price vs average | $30.85, -53.8% | $30.85, -53.8% | PASS |  |  |
| NVDL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $14.25 / entry $14.25 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 20.3 | 20.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -52.7% vs +9.2% | -52.7% vs 9.2% | PASS |  |  |
| NVDL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDL | T4 | ADX 14 (S1 /api/sr meta.adx) | 48.9 | 48.9 | PASS |  | Wilder, completed bars |
| NVDL | T4w | words "20 or more / below 20" | 20 or more | ADX 48.9 | PASS |  |  |
| NVDL | T5 | "counted at the last close ($X, date)" = last completed bar | $14.25, Nov 19 | $14.25, Nov 19 | PASS |  |  |
| NVDL | T6 | price vs 200-day average (S1 pattern sma values) | $14.25 vs $31.19 · -54.3% | $14.25 vs $31.19 · -54.3% | PASS |  |  |
| NVDL | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T7 | price vs 50-day average (S1 pattern sma values) | $14.25 vs $30.85 · -53.8% | $14.25 vs $30.85 · -53.8% | PASS |  |  |
| NVDL | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.9% over 30 td | -0.9% over 30 td | PASS |  |  |
| NVDL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NVDL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 67.1% below $43.27 | 67.1% below $43.27 | PASS |  | closing high would be 43.02 |
| NVDL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 67.1% below | PASS |  |  |
| NVDL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.27 | $43.27333450317383 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.50%, close location 0.02, OBV falling |
| NVDL | V2 | day change of the last completed bar | down 6.5% | -6.50% | PASS |  |  |
| NVDL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0240) | PASS |  |  |
| NVDL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.56× / 0.38× | 2.56× / 0.38× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 49920872) | 20 bars, last ('2026-11-19', 49920872) | PASS |  |  |
| NVDL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.56, OBV falling | condition true | PASS |  |  |
| ONTO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $195.93 | $195.93 | PASS |  |  |
| ONTO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $207.06 | $207.06 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ONTO | E3 | percent from the 21-day average | 5.4% below | 5.4% below | PASS |  |  |
| ONTO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ONTO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.90 | $16.90 (sr=16.9022) | PASS |  | Wilder ATR14 |
| ONTO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| ONTO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| ONTO | L-ema21 | ladder row ema21: price and gap = price vs average | $207.06, -5.4% | $207.06, -5.4% | PASS |  |  |
| ONTO | L-note | "Last close $X · date" note = last completed bar | Last close $195.93 · Nov 19 | $195.93 · Nov 19 | PASS |  |  |
| ONTO | L-now | ladder price row = compared price; name = the basis label | $195.93 "After hours" | $195.93 "after hours" | PASS |  |  |
| ONTO | L-sma200 | ladder row sma200: price and gap = price vs average | $260, -24.6% | $260.00, -24.6% | PASS |  |  |
| ONTO | L-sma50 | ladder row sma50: price and gap = price vs average | $241.99, -19.0% | $241.99, -19.0% | PASS |  |  |
| ONTO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $195.93 / entry $195.93 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ONTO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ONTO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.2 | 43.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ONTO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.6% vs +9.2% | 49.6% vs 9.2% | PASS |  |  |
| ONTO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ONTO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.6 | 25.6 | PASS |  | Wilder, completed bars |
| ONTO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.6 | PASS |  |  |
| ONTO | T5 | "counted at the last close ($X, date)" = last completed bar | $195.93, Nov 19 | $195.93, Nov 19 | PASS |  |  |
| ONTO | T6 | price vs 200-day average (S1 pattern sma values) | $195.93 vs $260.00 · -24.6% | $195.93 vs $260.00 · -24.6% | PASS |  |  |
| ONTO | T6w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T7 | price vs 50-day average (S1 pattern sma values) | $195.93 vs $241.99 · -19.0% | $195.93 vs $241.99 · -19.0% | PASS |  |  |
| ONTO | T7w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| ONTO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ONTO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ONTO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.3% below $386.46 | 49.3% below $386.46 | PASS |  | closing high would be 378.45 |
| ONTO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.3% below | PASS |  |  |
| ONTO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $386.46 | $386.4599914550781 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ONTO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.53%, close location 0.03, OBV rising |
| ONTO | V2 | day change of the last completed bar | down 2.5% | -2.53% | PASS |  |  |
| ONTO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0276) | PASS |  |  |
| ONTO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ONTO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.89× / 0.29× | 0.89× / 0.29× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ONTO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 934845) | 20 bars, last ('2026-11-19', 934845) | PASS |  |  |
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
| ORCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $110.57 | $110.57 | PASS |  |  |
| ORCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $123.11 | $123.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORCL | E3 | percent from the 21-day average | 10.2% below | 10.2% below | PASS |  |  |
| ORCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ORCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.75 | $7.75 (sr=7.7528) | PASS |  | Wilder ATR14 |
| ORCL | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| ORCL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| ORCL | L-ema21 | ladder row ema21: price and gap = price vs average | $123.11, -10.2% | $123.11, -10.2% | PASS |  |  |
| ORCL | L-note | "Last close $X · date" note = last completed bar | Last close $110.57 · Nov 19 | $110.57 · Nov 19 | PASS |  |  |
| ORCL | L-now | ladder price row = compared price; name = the basis label | $110.57 "After hours" | $110.57 "after hours" | PASS |  |  |
| ORCL | L-sma200 | ladder row sma200: price and gap = price vs average | $152.36, -27.4% | $152.36, -27.4% | PASS |  |  |
| ORCL | L-sma50 | ladder row sma50: price and gap = price vs average | $132.91, -16.8% | $132.91, -16.8% | PASS |  |  |
| ORCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $110.57 / entry $110.57 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ORCL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ORCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.2 | 37.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORCL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -50.3% vs +9.2% | -50.3% vs 9.2% | PASS |  |  |
| ORCL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ORCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.1 | 14.1 | PASS |  | Wilder, completed bars |
| ORCL | T4w | words "20 or more / below 20" | below 20 | ADX 14.1 | PASS |  |  |
| ORCL | T5 | "counted at the last close ($X, date)" = last completed bar | $110.57, Nov 19 | $110.57, Nov 19 | PASS |  |  |
| ORCL | T6 | price vs 200-day average (S1 pattern sma values) | $110.57 vs $152.36 · -27.4% | $110.57 vs $152.36 · -27.4% | PASS |  |  |
| ORCL | T6w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T7 | price vs 50-day average (S1 pattern sma values) | $110.57 vs $132.91 · -16.8% | $110.57 vs $132.91 · -16.8% | PASS |  |  |
| ORCL | T7w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.2% over 30 td | -5.2% over 30 td | PASS |  |  |
| ORCL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| ORCL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ORCL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 55.5% below $248.46 | 55.5% below $248.46 | PASS |  | closing high would be 246.38 |
| ORCL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 55.5% below | PASS |  |  |
| ORCL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $248.46 | $248.4634626242363 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ORCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.92%, close location 0.04, OBV falling |
| ORCL | V2 | day change of the last completed bar | down 2.9% | -2.92% | PASS |  |  |
| ORCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0400) | PASS |  |  |
| ORCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.75× / 0.42× | 0.75× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 26755372) | 20 bars, last ('2026-11-19', 26755372) | PASS |  |  |
| PG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $167.85 | $167.85 | PASS |  |  |
| PG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $165.31 | $165.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PG | E3 | percent from the 21-day average | 1.5% above | 1.5% above | PASS |  |  |
| PG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| PG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.16 | $3.16 (sr=3.158) | PASS |  | Wilder ATR14 |
| PG | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves above |
| PG | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.4 | -5.4 | PASS |  |  |
| PG | L-ema21 | ladder row ema21: price and gap = price vs average | $165.31, 1.5% | $165.31, 1.5% | PASS |  |  |
| PG | L-note | "Last close $X · date" note = last completed bar | Last close $167.85 · Nov 19 | $167.85 · Nov 19 | PASS |  |  |
| PG | L-now | ladder price row = compared price; name = the basis label | $167.85 "After hours" | $167.85 "after hours" | PASS |  |  |
| PG | L-sma200 | ladder row sma200: price and gap = price vs average | $148.39, 13.1% | $148.39, 13.1% | PASS |  |  |
| PG | L-sma50 | ladder row sma50: price and gap = price vs average | $155.77, 7.8% | $155.77, 7.8% | PASS |  |  |
| PG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $167.85 / entry $167.85 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.1 | 59.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +17.5% vs +9.2% | 17.5% vs 9.2% | PASS |  |  |
| PG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PG | T4 | ADX 14 (S1 /api/sr meta.adx) | 41.0 | 41.1 | PASS |  | Wilder, completed bars |
| PG | T4w | words "20 or more / below 20" | 20 or more | ADX 41.1 | PASS |  |  |
| PG | T5 | "counted at the last close ($X, date)" = last completed bar | $167.85, Nov 19 | $167.85, Nov 19 | PASS |  |  |
| PG | T6 | price vs 200-day average (S1 pattern sma values) | $167.85 vs $148.39 · +13.1% | $167.85 vs $148.39 · 13.1% | PASS |  |  |
| PG | T6w | word "Above" | Above | Above | PASS |  |  |
| PG | T7 | price vs 50-day average (S1 pattern sma values) | $167.85 vs $155.77 · +7.8% | $167.85 vs $155.77 · 7.8% | PASS |  |  |
| PG | T7w | word "Above" | Above | Above | PASS |  |  |
| PG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| PG | T8r | word "rising" | still rising | rising | PASS |  |  |
| PG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.3% below $173.59 | 3.3% below $173.59 | PASS |  | closing high would be 173.02 |
| PG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.3% below | PASS |  |  |
| PG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $173.59 | $173.58999633789062 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -1.43%, close location 0.43, OBV flat |
| PG | V2 | day change of the last completed bar | down 1.4% | -1.43% | PASS |  |  |
| PG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| PG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.87× / 0.76× | 0.87× / 0.76× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 8195114) | 20 bars, last ('2026-11-19', 8195114) | PASS |  |  |
| PLD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $123.36 | $123.36 | PASS |  |  |
| PLD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $127.77 | $127.77 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PLD | E3 | percent from the 21-day average | 3.5% below | 3.5% below | PASS |  |  |
| PLD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| PLD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.43 | $2.43 (sr=2.4319) | PASS |  | Wilder ATR14 |
| PLD | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| PLD | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| PLD | L-ema21 | ladder row ema21: price and gap = price vs average | $127.77, -3.5% | $127.77, -3.5% | PASS |  |  |
| PLD | L-note | "Last close $X · date" note = last completed bar | Last close $123.36 · Nov 19 | $123.36 · Nov 19 | PASS |  |  |
| PLD | L-now | ladder price row = compared price; name = the basis label | $123.36 "After hours" | $123.36 "after hours" | PASS |  |  |
| PLD | L-sma200 | ladder row sma200: price and gap = price vs average | $136.28, -9.5% | $136.28, -9.5% | PASS |  |  |
| PLD | L-sma50 | ladder row sma50: price and gap = price vs average | $129.71, -4.9% | $129.71, -4.9% | PASS |  |  |
| PLD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $123.36 / entry $123.36 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PLD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PLD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.8 | 35.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PLD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.0% vs +9.2% | 4.0% vs 9.2% | PASS |  |  |
| PLD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PLD | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.6 | 16.6 | PASS |  | Wilder, completed bars |
| PLD | T4w | words "20 or more / below 20" | below 20 | ADX 16.6 | PASS |  |  |
| PLD | T5 | "counted at the last close ($X, date)" = last completed bar | $123.36, Nov 19 | $123.36, Nov 19 | PASS |  |  |
| PLD | T6 | price vs 200-day average (S1 pattern sma values) | $123.36 vs $136.28 · -9.5% | $123.36 vs $136.28 · -9.5% | PASS |  |  |
| PLD | T6w | word "Below" | Below | Below | PASS |  |  |
| PLD | T7 | price vs 50-day average (S1 pattern sma values) | $123.36 vs $129.71 · -4.9% | $123.36 vs $129.71 · -4.9% | PASS |  |  |
| PLD | T7w | word "Below" | Below | Below | PASS |  |  |
| PLD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.2% over 30 td | +0.2% over 30 td | PASS |  |  |
| PLD | T8r | word "rising" | still rising | rising | PASS |  |  |
| PLD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PLD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 18.9% below $152.14 | 18.9% below $152.14 | PASS |  | closing high would be 148.88 |
| PLD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 18.9% below | PASS |  |  |
| PLD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $152.14 | $152.14207825389113 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PLD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.49%, close location 0.30, OBV falling |
| PLD | V2 | day change of the last completed bar | down 1.5% | -1.49% | PASS |  |  |
| PLD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PLD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.95× / 0.76× | 0.95× / 0.75× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PLD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 3673876) | 20 bars, last ('2026-11-19', 3673876) | PASS |  |  |
| PNG.V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $2.88 | $2.88 | PASS |  |  |
| PNG.V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3.53 | $3.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PNG.V | E3 | percent from the 21-day average | 18.4% below | 18.4% below | PASS |  |  |
| PNG.V | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| PNG.V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.22 | $0.22 (sr=0.2236) | PASS |  | Wilder ATR14 |
| PNG.V | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| PNG.V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +13.5 | +13.5 | PASS |  |  |
| PNG.V | L-ema21 | ladder row ema21: price and gap = price vs average | $3.53, -18.4% | $3.53, -18.4% | PASS |  |  |
| PNG.V | L-now | ladder price row = compared price; name = the basis label | $2.88 "Last close" | $2.88 "last close" | PASS |  |  |
| PNG.V | L-sma200 | ladder row sma200: price and gap = price vs average | $6.55, -56.0% | $6.55, -56.0% | PASS |  |  |
| PNG.V | L-sma50 | ladder row sma50: price and gap = price vs average | $4.08, -29.5% | $4.08, -29.5% | PASS |  |  |
| PNG.V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PNG.V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.7 | 23.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PNG.V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -45.6% vs +9.2% | -45.6% vs 9.2% | PASS |  |  |
| PNG.V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PNG.V | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.1 | 40.0 | PASS |  | Wilder, completed bars |
| PNG.V | T4w | words "20 or more / below 20" | 20 or more | ADX 40.0 | PASS |  |  |
| PNG.V | T6 | price vs 200-day average (S1 pattern sma values) | $2.88 vs $6.55 · -56.0% | $2.88 vs $6.55 · -56.0% | PASS |  |  |
| PNG.V | T6w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T7 | price vs 50-day average (S1 pattern sma values) | $2.88 vs $4.08 · -29.4% | $2.88 vs $4.08 · -29.5% | PASS |  |  |
| PNG.V | T7w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -8.0% over 30 td | -8.0% over 30 td | PASS |  |  |
| PNG.V | T8r | word "rising" | not rising | not rising | PASS |  |  |
| PNG.V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PNG.V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 73.1% below $10.72 | 73.1% below $10.72 | PASS |  | closing high would be 10.23 |
| PNG.V | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 73.1% below | PASS |  |  |
| PNG.V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $10.72 | $10.720000267028809 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PNG.V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.68%, close location 0.00, OBV falling |
| PNG.V | V2 | day change of the last completed bar | down 3.7% | -3.68% | PASS |  |  |
| PNG.V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| PNG.V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PNG.V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.34× / 0.47× | 1.34× / 0.47× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PNG.V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1625027) | 20 bars, last ('2026-11-19', 1625027) | PASS |  |  |
| QCOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $162.01 | $162.01 | PASS |  |  |
| QCOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $170.41 | $170.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QCOM | E3 | percent from the 21-day average | 4.9% below | 4.9% below | PASS |  |  |
| QCOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QCOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.03 | $9.03 (sr=9.0295) | PASS |  | Wilder ATR14 |
| QCOM | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves below |
| QCOM | L-ema21 | ladder row ema21: price and gap = price vs average | $170.41, -4.9% | $170.41, -4.9% | PASS |  |  |
| QCOM | L-note | "Last close $X · date" note = last completed bar | Last close $162.01 · Nov 19 | $162.01 · Nov 19 | PASS |  |  |
| QCOM | L-now | ladder price row = compared price; name = the basis label | $162.01 "After hours" | $162.01 "after hours" | PASS |  |  |
| QCOM | L-sma200 | ladder row sma200: price and gap = price vs average | $170.48, -5.0% | $170.48, -5.0% | PASS |  |  |
| QCOM | L-sma50 | ladder row sma50: price and gap = price vs average | $177.95, -9.0% | $177.95, -9.0% | PASS |  |  |
| QCOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $162.01 / entry $162.01 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QCOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QCOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.1 | 42.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QCOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.5% vs +9.2% | -2.5% vs 9.2% | PASS |  |  |
| QCOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QCOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 10.8 | 10.8 | PASS |  | Wilder, completed bars |
| QCOM | T4w | words "20 or more / below 20" | below 20 | ADX 10.8 | PASS |  |  |
| QCOM | T5 | "counted at the last close ($X, date)" = last completed bar | $162.01, Nov 19 | $162.01, Nov 19 | PASS |  |  |
| QCOM | T6 | price vs 200-day average (S1 pattern sma values) | $162.01 vs $170.48 · -5.0% | $162.01 vs $170.48 · -5.0% | PASS |  |  |
| QCOM | T6w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T7 | price vs 50-day average (S1 pattern sma values) | $162.01 vs $177.95 · -9.0% | $162.01 vs $177.95 · -9.0% | PASS |  |  |
| QCOM | T7w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.7% over 30 td | +0.7% over 30 td | PASS |  |  |
| QCOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QCOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QCOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 37.7% below $259.92 | 37.7% below $259.92 | PASS |  | closing high would be 251.02 |
| QCOM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 37.7% below | PASS |  |  |
| QCOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $259.92 | $259.92 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QCOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 1.38%, close location 0.16, OBV rising |
| QCOM | V2 | day change of the last completed bar | up 1.4% | +1.38% | PASS |  |  |
| QCOM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1561) | PASS |  |  |
| QCOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| QCOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.25× | 1.02× / 0.25× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QCOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 13403943) | 20 bars, last ('2026-11-19', 13403943) | PASS |  |  |
| QPUX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $2.86 | $2.86 | PASS |  |  |
| QPUX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $5.38 | $5.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QPUX | E3 | percent from the 21-day average | 46.8% below | 46.8% below | PASS |  |  |
| QPUX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QPUX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.84 | $0.84 (sr=0.8362) | PASS |  | Wilder ATR14 |
| QPUX | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| QPUX | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.9 | +3.9 | PASS |  |  |
| QPUX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +17.6 | +17.6 | PASS |  |  |
| QPUX | L-ema21 | ladder row ema21: price and gap = price vs average | $5.38, -46.8% | $5.38, -46.8% | PASS |  |  |
| QPUX | L-note | "Last close $X · date" note = last completed bar | Last close $2.86 · Nov 19 | $2.86 · Nov 19 | PASS |  |  |
| QPUX | L-now | ladder price row = compared price; name = the basis label | $2.86 "After hours" | $2.86 "after hours" | PASS |  |  |
| QPUX | L-sma200 | ladder row sma200: price and gap = price vs average | $20.08, -85.8% | $20.08, -85.8% | PASS |  |  |
| QPUX | L-sma50 | ladder row sma50: price and gap = price vs average | $8.68, -67.0% | $8.68, -67.0% | PASS |  |  |
| QPUX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $2.86 / entry $2.86 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QPUX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QPUX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.5 | 27.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QPUX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -95.3% vs +9.2% | -95.3% vs 9.2% | PASS |  |  |
| QPUX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QPUX | T4 | ADX 14 (S1 /api/sr meta.adx) | 39.4 | 39.4 | PASS |  | Wilder, completed bars |
| QPUX | T4w | words "20 or more / below 20" | 20 or more | ADX 39.4 | PASS |  |  |
| QPUX | T5 | "counted at the last close ($X, date)" = last completed bar | $2.86, Nov 19 | $2.86, Nov 19 | PASS |  |  |
| QPUX | T6 | price vs 200-day average (S1 pattern sma values) | $2.86 vs $20.08 · -85.8% | $2.86 vs $20.08 · -85.8% | PASS |  |  |
| QPUX | T6w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T7 | price vs 50-day average (S1 pattern sma values) | $2.86 vs $8.68 · -67.1% | $2.86 vs $8.68 · -67.0% | PASS |  |  |
| QPUX | T7w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -25.8% over 30 td | -25.8% over 30 td | PASS |  |  |
| QPUX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| QPUX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QPUX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 96.4% below $80.28 | 96.4% below $80.28 | PASS |  | closing high would be 79.57 |
| QPUX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 96.4% below | PASS |  |  |
| QPUX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.28 | $80.27999877929688 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QPUX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.34%, close location 0.00, OBV falling |
| QPUX | V2 | day change of the last completed bar | down 10.3% | -10.34% | PASS |  |  |
| QPUX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| QPUX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QPUX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.32× / 0.35× | 1.32× / 0.35× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QPUX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 408677) | 20 bars, last ('2026-11-19', 408677) | PASS |  |  |
| QTUM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $119.71 | $119.71 | PASS |  |  |
| QTUM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $130.73 | $130.73 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QTUM | E3 | percent from the 21-day average | 8.4% below | 8.4% below | PASS |  |  |
| QTUM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QTUM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.78 | $4.78 (sr=4.7846) | PASS |  | Wilder ATR14 |
| QTUM | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| QTUM | L-ema21 | ladder row ema21: price and gap = price vs average | $130.73, -8.4% | $130.73, -8.4% | PASS |  |  |
| QTUM | L-note | "Last close $X · date" note = last completed bar | Last close $119.71 · Nov 19 | $119.71 · Nov 19 | PASS |  |  |
| QTUM | L-now | ladder price row = compared price; name = the basis label | $119.71 "After hours" | $119.71 "after hours" | PASS |  |  |
| QTUM | L-sma200 | ladder row sma200: price and gap = price vs average | $138.03, -13.3% | $138.03, -13.3% | PASS |  |  |
| QTUM | L-sma50 | ladder row sma50: price and gap = price vs average | $141.19, -15.2% | $141.19, -15.2% | PASS |  |  |
| QTUM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $119.71 / entry $119.71 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QTUM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QTUM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.9 | 33.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QTUM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.7% vs +9.2% | 15.7% vs 9.2% | PASS |  |  |
| QTUM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QTUM | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.1 | 34.1 | PASS |  | Wilder, completed bars |
| QTUM | T4w | words "20 or more / below 20" | 20 or more | ADX 34.1 | PASS |  |  |
| QTUM | T5 | "counted at the last close ($X, date)" = last completed bar | $119.71, Nov 19 | $119.71, Nov 19 | PASS |  |  |
| QTUM | T6 | price vs 200-day average (S1 pattern sma values) | $119.71 vs $138.03 · -13.3% | $119.71 vs $138.03 · -13.3% | PASS |  |  |
| QTUM | T6w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T7 | price vs 50-day average (S1 pattern sma values) | $119.71 vs $141.19 · -15.2% | $119.71 vs $141.19 · -15.2% | PASS |  |  |
| QTUM | T7w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.2% over 30 td | PASS |  |  |
| QTUM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QTUM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QTUM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.3% below $169.21 | 29.3% below $169.21 | PASS |  | closing high would be 167.97 |
| QTUM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.3% below | PASS |  |  |
| QTUM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $169.21 | $169.2079473044215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QTUM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.64%, close location 0.03, OBV falling |
| QTUM | V2 | day change of the last completed bar | down 2.6% | -2.64% | PASS |  |  |
| QTUM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0251) | PASS |  |  |
| QTUM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QTUM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.94× / 0.66× | 0.94× / 0.66× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QTUM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 321205) | 20 bars, last ('2026-11-19', 321205) | PASS |  |  |
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
| RBOT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -13.4% vs +9.2% | -13.5% vs 9.2% | PASS |  |  |
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
| RBOT.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.4× from 2026-11-18 | 0.41× from 2026-11-18 | PASS |  | window "50 bars" includes the bar itself |
| RBOT.TO | V6 | Volume detail: last session date and RVOL | 2026-11-18 0.41× | 2026-11-18 0.41× | PASS |  |  |
| RBOT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1285) | 20 bars, last ('2026-11-18', 1285) | PASS |  |  |
| RTX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $193.44 | $193.44 | PASS |  |  |
| RTX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $196.05 | $196.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RTX | E3 | percent from the 21-day average | 1.3% below | 1.3% below | PASS |  |  |
| RTX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RTX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.23 | $5.23 (sr=5.2345) | PASS |  | Wilder ATR14 |
| RTX | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| RTX | L-ema21 | ladder row ema21: price and gap = price vs average | $196.05, -1.3% | $196.05, -1.3% | PASS |  |  |
| RTX | L-note | "Last close $X · date" note = last completed bar | Last close $193.44 · Nov 19 | $193.44 · Nov 19 | PASS |  |  |
| RTX | L-now | ladder price row = compared price; name = the basis label | $193.44 "After hours" | $193.44 "after hours" | PASS |  |  |
| RTX | L-sma200 | ladder row sma200: price and gap = price vs average | $195.2, -0.9% | $195.20, -0.9% | PASS |  |  |
| RTX | L-sma50 | ladder row sma50: price and gap = price vs average | $192.57, 0.5% | $192.57, 0.5% | PASS |  |  |
| RTX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $193.44 / entry $193.44 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RTX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RTX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.9 | 46.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RTX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +11.3% vs +9.2% | 11.3% vs 9.2% | PASS |  |  |
| RTX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RTX | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.2 | 16.2 | PASS |  | Wilder, completed bars |
| RTX | T4w | words "20 or more / below 20" | below 20 | ADX 16.2 | PASS |  |  |
| RTX | T5 | "counted at the last close ($X, date)" = last completed bar | $193.44, Nov 19 | $193.44, Nov 19 | PASS |  |  |
| RTX | T6 | price vs 200-day average (S1 pattern sma values) | $193.44 vs $195.20 · -0.9% | $193.44 vs $195.20 · -0.9% | PASS |  |  |
| RTX | T6w | word "Below" | Below | Below | PASS |  |  |
| RTX | T7 | price vs 50-day average (S1 pattern sma values) | $193.44 vs $192.57 · +0.5% | $193.44 vs $192.57 · 0.5% | PASS |  |  |
| RTX | T7w | word "Above" | Above | Above | PASS |  |  |
| RTX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| RTX | T8r | word "rising" | still rising | rising | PASS |  |  |
| RTX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RTX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.7% below $226.88 | 14.7% below $226.88 | PASS |  | closing high would be 225.49 |
| RTX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.7% below | PASS |  |  |
| RTX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $226.88 | $226.884 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RTX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.03%, close location 0.11, OBV flat |
| RTX | V2 | day change of the last completed bar | down 2.0% | -2.03% | PASS |  |  |
| RTX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1059) | PASS |  |  |
| RTX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| RTX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.90× / 0.75× | 0.90× / 0.75× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RTX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4417880) | 20 bars, last ('2026-11-19', 4417880) | PASS |  |  |
| RY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $269.45 | $269.45 | PASS |  |  |
| RY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $282.56 | $282.56 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RY.TO | E3 | percent from the 21-day average | 4.6% below | 4.6% below | PASS |  |  |
| RY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.09 | $5.09 (sr=5.0919) | PASS |  | Wilder ATR14 |
| RY.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| RY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $282.56, -4.6% | $282.56, -4.6% | PASS |  |  |
| RY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $269.45 · Nov 19 | $269.45 · Nov 19 | PASS |  |  |
| RY.TO | L-now | ladder price row = compared price; name = the basis label | $269.45 "After hours" | $269.45 "after hours" | PASS |  |  |
| RY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $263.74, 2.2% | $263.74, 2.2% | PASS |  |  |
| RY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $281.51, -4.3% | $281.51, -4.3% | PASS |  |  |
| RY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $269.45 / entry $269.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.3 | 33.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +32.6% vs +9.2% | 32.6% vs 9.2% | PASS |  |  |
| RY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.9 | 16.9 | PASS |  | Wilder, completed bars |
| RY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 16.9 | PASS |  |  |
| RY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $269.45, Nov 19 | $269.45, Nov 19 | PASS |  |  |
| RY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $269.45 vs $263.74 · +2.2% | $269.45 vs $263.74 · 2.2% | PASS |  |  |
| RY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| RY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $269.45 vs $281.51 · -4.3% | $269.45 vs $281.51 · -4.3% | PASS |  |  |
| RY.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| RY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| RY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| RY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.0% below $302.65 | 11.0% below $302.65 | PASS |  | closing high would be 302.02 |
| RY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.0% below | PASS |  |  |
| RY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.65 | $302.64985314246684 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.03%, close location 0.37, OBV falling |
| RY.TO | V2 | day change of the last completed bar | down 1.0% | -1.03% | PASS |  |  |
| RY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.84× / 0.55× | 0.84× / 0.55× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2820111) | 20 bars, last ('2026-11-19', 2820111) | PASS |  |  |
| SETM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $20.64 | $20.64 | PASS |  |  |
| SETM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.21 | $24.21 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SETM | E3 | percent from the 21-day average | 14.7% below | 14.7% below | PASS |  |  |
| SETM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SETM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.99 | $0.99 (sr=0.9871) | PASS |  | Wilder ATR14 |
| SETM | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  · 3.6 day-moves below |
| SETM | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.2 | +8.2 | PASS |  |  |
| SETM | L-ema21 | ladder row ema21: price and gap = price vs average | $24.21, -14.7% | $24.21, -14.7% | PASS |  |  |
| SETM | L-note | "Last close $X · date" note = last completed bar | Last close $20.64 · Nov 19 | $20.64 · Nov 19 | PASS |  |  |
| SETM | L-now | ladder price row = compared price; name = the basis label | $20.64 "After hours" | $20.64 "after hours" | PASS |  |  |
| SETM | L-sma200 | ladder row sma200: price and gap = price vs average | $32.26, -36.0% | $32.26, -36.0% | PASS |  |  |
| SETM | L-sma50 | ladder row sma50: price and gap = price vs average | $27.12, -23.9% | $27.12, -23.9% | PASS |  |  |
| SETM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $20.64 / entry $20.64 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SETM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SETM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.9 | 26.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SETM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -21.9% vs +9.2% | -21.8% vs 9.2% | PASS |  |  |
| SETM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SETM | T4 | ADX 14 (S1 /api/sr meta.adx) | 36.5 | 36.5 | PASS |  | Wilder, completed bars |
| SETM | T4w | words "20 or more / below 20" | 20 or more | ADX 36.5 | PASS |  |  |
| SETM | T5 | "counted at the last close ($X, date)" = last completed bar | $20.64, Nov 19 | $20.64, Nov 19 | PASS |  |  |
| SETM | T6 | price vs 200-day average (S1 pattern sma values) | $20.64 vs $32.26 · -36.0% | $20.64 vs $32.26 · -36.0% | PASS |  |  |
| SETM | T6w | word "Below" | Below | Below | PASS |  |  |
| SETM | T7 | price vs 50-day average (S1 pattern sma values) | $20.64 vs $27.12 · -23.9% | $20.64 vs $27.12 · -23.9% | PASS |  |  |
| SETM | T7w | word "Below" | Below | Below | PASS |  |  |
| SETM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.0% over 30 td | -4.0% over 30 td | PASS |  |  |
| SETM | T8r | word "rising" | not rising | not rising | PASS |  |  |
| SETM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SETM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.1% below $40.55 | 49.1% below $40.55 | PASS |  | closing high would be 39.73 |
| SETM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.1% below | PASS |  |  |
| SETM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $40.55 | $40.54999923706055 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SETM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.10%, close location 0.04, OBV falling |
| SETM | V2 | day change of the last completed bar | down 3.1% | -3.10% | PASS |  |  |
| SETM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0444) | PASS |  |  |
| SETM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SETM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.26× / 0.65× | 1.26× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SETM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 225671) | 20 bars, last ('2026-11-19', 225671) | PASS |  |  |
| SGRD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.69 | $17.69 | PASS |  |  |
| SGRD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.49 | $18.49 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SGRD.TO | E3 | percent from the 21-day average | 4.3% below | 4.3% below | PASS |  |  |
| SGRD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SGRD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.38 | $0.38 (sr=0.3772) | PASS |  | Wilder ATR14 |
| SGRD.TO | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| SGRD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $18.49, -4.3% | $18.49, -4.3% | PASS |  |  |
| SGRD.TO | L-now | ladder price row = compared price; name = the basis label | $17.69 "Last close" | $17.69 "last close" | PASS |  |  |
| SGRD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $19.43, -9.0% | $19.43, -9.0% | PASS |  |  |
| SGRD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.0 | 38.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SGRD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.8 | 27.8 | PASS |  | Wilder, completed bars |
| SGRD.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.8 | PASS |  |  |
| SGRD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.50%, close location 0.00, OBV falling |
| SGRD.TO | V2 | day change of the last completed bar | down 1.5% | -1.50% | PASS |  |  |
| SGRD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| SGRD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SGRD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.55× / 0.70× | 0.55× / 0.71× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SGRD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 4992) | 20 bars, last ('2026-11-19', 4992) | PASS |  |  |
| SMH | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $447.48 | $447.48 | PASS |  |  |
| SMH | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $498.58 | $498.58 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SMH | E3 | percent from the 21-day average | 10.2% below | 10.2% below | PASS |  |  |
| SMH | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SMH | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $24.24 | $24.24 (sr=24.2418) | PASS |  | Wilder ATR14 |
| SMH | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| SMH | L-ema21 | ladder row ema21: price and gap = price vs average | $498.58, -10.2% | $498.58, -10.2% | PASS |  |  |
| SMH | L-note | "Last close $X · date" note = last completed bar | Last close $447.48 · Nov 19 | $447.48 · Nov 19 | PASS |  |  |
| SMH | L-now | ladder price row = compared price; name = the basis label | $447.48 "After hours" | $447.48 "after hours" | PASS |  |  |
| SMH | L-sma200 | ladder row sma200: price and gap = price vs average | $525.08, -14.8% | $525.08, -14.8% | PASS |  |  |
| SMH | L-sma50 | ladder row sma50: price and gap = price vs average | $550.88, -18.8% | $550.88, -18.8% | PASS |  |  |
| SMH | S5-price | S5: the same live price reads the same on the header and the Entry block | header $447.48 / entry $447.48 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SMH | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SMH | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.0 | 33.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SMH | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +32.2% vs +9.2% | 32.2% vs 9.2% | PASS |  |  |
| SMH | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SMH | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.3 | 35.3 | PASS |  | Wilder, completed bars |
| SMH | T4w | words "20 or more / below 20" | 20 or more | ADX 35.3 | PASS |  |  |
| SMH | T5 | "counted at the last close ($X, date)" = last completed bar | $447.48, Nov 19 | $447.48, Nov 19 | PASS |  |  |
| SMH | T6 | price vs 200-day average (S1 pattern sma values) | $447.48 vs $525.08 · -14.8% | $447.48 vs $525.08 · -14.8% | PASS |  |  |
| SMH | T6w | word "Below" | Below | Below | PASS |  |  |
| SMH | T7 | price vs 50-day average (S1 pattern sma values) | $447.48 vs $550.88 · -18.8% | $447.48 vs $550.88 · -18.8% | PASS |  |  |
| SMH | T7w | word "Below" | Below | Below | PASS |  |  |
| SMH | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.0% over 30 td | +4.0% over 30 td | PASS |  |  |
| SMH | T8r | word "rising" | still rising | rising | PASS |  |  |
| SMH | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SMH | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 33.4% below $671.83 | 33.4% below $671.83 | PASS |  | closing high would be 668.91 |
| SMH | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 33.4% below | PASS |  |  |
| SMH | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $671.83 | $671.8300170898438 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SMH | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.62%, close location 0.01, OBV falling |
| SMH | V2 | day change of the last completed bar | down 2.6% | -2.62% | PASS |  |  |
| SMH | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0085) | PASS |  |  |
| SMH | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SMH | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.10× / 0.48× | 1.10× / 0.48× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SMH | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 10271740) | 20 bars, last ('2026-11-19', 10271740) | PASS |  |  |
| SNDK.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $18.35 | $18.35 | PASS |  |  |
| SNDK.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.45 | $24.45 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SNDK.TO | E3 | percent from the 21-day average | 24.9% below | 24.9% below | PASS |  |  |
| SNDK.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SNDK.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.38 | $2.38 (sr=2.3834) | PASS |  | Wilder ATR14 |
| SNDK.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| SNDK.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| SNDK.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $24.45, -24.9% | $24.45, -24.9% | PASS |  |  |
| SNDK.TO | L-now | ladder price row = compared price; name = the basis label | $18.35 "Last close" | $18.35 "last close" | PASS |  |  |
| SNDK.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $33.22, -44.8% | $33.22, -44.8% | PASS |  |  |
| SNDK.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.3 | 29.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SNDK.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.4 | 40.4 | PASS |  | Wilder, completed bars |
| SNDK.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 40.4 | PASS |  |  |
| SNDK.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.08%, close location 0.05, OBV falling |
| SNDK.TO | V2 | day change of the last completed bar | down 2.1% | -2.08% | PASS |  |  |
| SNDK.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0548) | PASS |  |  |
| SNDK.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SNDK.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.69× / 0.16× | 1.69× / 0.16× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SNDK.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 2172018) | 20 bars, last ('2026-11-19', 2172018) | PASS |  |  |
| SNDK.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.69, OBV falling | condition true | PASS |  |  |
| SO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $93.29 | $93.29 | PASS |  |  |
| SO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $92.21 | $92.21 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SO | E3 | percent from the 21-day average | 1.2% above | 1.2% above | PASS |  |  |
| SO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.79 | $1.79 (sr=1.7908) | PASS |  | Wilder ATR14 |
| SO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| SO | L-ema21 | ladder row ema21: price and gap = price vs average | $92.21, 1.2% | $92.21, 1.2% | PASS |  |  |
| SO | L-note | "Last close $X · date" note = last completed bar | Last close $93.29 · Nov 19 | $93.29 · Nov 19 | PASS |  |  |
| SO | L-now | ladder price row = compared price; name = the basis label | $93.29 "After hours" | $93.29 "after hours" | PASS |  |  |
| SO | L-sma200 | ladder row sma200: price and gap = price vs average | $91.23, 2.3% | $91.23, 2.3% | PASS |  |  |
| SO | L-sma50 | ladder row sma50: price and gap = price vs average | $88.48, 5.4% | $88.48, 5.4% | PASS |  |  |
| SO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $93.29 / entry $93.29 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.7 | 56.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +8.2% vs +9.2% | 8.2% vs 9.2% | PASS |  |  |
| SO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.7 | 26.7 | PASS |  | Wilder, completed bars |
| SO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.7 | PASS |  |  |
| SO | T5 | "counted at the last close ($X, date)" = last completed bar | $93.29, Nov 19 | $93.29, Nov 19 | PASS |  |  |
| SO | T6 | price vs 200-day average (S1 pattern sma values) | $93.29 vs $91.23 · +2.3% | $93.29 vs $91.23 · 2.3% | PASS |  |  |
| SO | T6w | word "Above" | Above | Above | PASS |  |  |
| SO | T7 | price vs 50-day average (S1 pattern sma values) | $93.29 vs $88.48 · +5.4% | $93.29 vs $88.48 · 5.4% | PASS |  |  |
| SO | T7w | word "Above" | Above | Above | PASS |  |  |
| SO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.1% over 30 td | +1.1% over 30 td | PASS |  |  |
| SO | T8r | word "rising" | still rising | rising | PASS |  |  |
| SO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.5% below $97.65 | 4.5% below $97.65 | PASS |  | closing high would be 96.70 |
| SO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.5% below | PASS |  |  |
| SO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $97.65 | $97.64764917949712 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -1.19%, close location 0.48, OBV rising |
| SO | V2 | day change of the last completed bar | down 1.2% | -1.19% | PASS |  |  |
| SO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| SO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.80× / 0.62× | 0.80× / 0.62× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 5852847) | 20 bars, last ('2026-11-19', 5852847) | PASS |  |  |
| SOXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $45.30 | $45.30 | PASS |  |  |
| SOXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $68.7 | $68.70 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL | E3 | percent from the 21-day average | 34.1% below | 34.1% below | PASS |  |  |
| SOXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $11.72 | $11.72 (sr=11.7218) | PASS |  | Wilder ATR14 |
| SOXL | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| SOXL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| SOXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.7 | +4.7 | PASS |  |  |
| SOXL | L-ema21 | ladder row ema21: price and gap = price vs average | $68.7, -34.1% | $68.70, -34.1% | PASS |  |  |
| SOXL | L-note | "Last close $X · date" note = last completed bar | Last close $45.30 · Nov 19 | $45.30 · Nov 19 | PASS |  |  |
| SOXL | L-now | ladder price row = compared price; name = the basis label | $45.3 "After hours" | $45.30 "after hours" | PASS |  |  |
| SOXL | L-sma200 | ladder row sma200: price and gap = price vs average | $123.76, -63.4% | $123.76, -63.4% | PASS |  |  |
| SOXL | L-sma50 | ladder row sma50: price and gap = price vs average | $104.59, -56.7% | $104.59, -56.7% | PASS |  |  |
| SOXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $45.30 / entry $45.30 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.1 | 33.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +26.0% vs +9.2% | 26.0% vs 9.2% | PASS |  |  |
| SOXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.7 | 34.7 | PASS |  | Wilder, completed bars |
| SOXL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.7 | PASS |  |  |
| SOXL | T5 | "counted at the last close ($X, date)" = last completed bar | $45.30, Nov 19 | $45.30, Nov 19 | PASS |  |  |
| SOXL | T6 | price vs 200-day average (S1 pattern sma values) | $45.30 vs $123.76 · -63.4% | $45.30 vs $123.76 · -63.4% | PASS |  |  |
| SOXL | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T7 | price vs 50-day average (S1 pattern sma values) | $45.30 vs $104.59 · -56.7% | $45.30 vs $104.59 · -56.7% | PASS |  |  |
| SOXL | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.3% over 30 td | +3.3% over 30 td | PASS |  |  |
| SOXL | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 85.0% below $301.80 | 85.0% below $301.80 | PASS |  | closing high would be 300.57 |
| SOXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 85.0% below | PASS |  |  |
| SOXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $301.80 | $301.8021115035658 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.04%, close location 0.03, OBV falling |
| SOXL | V2 | day change of the last completed bar | down 8.0% | -8.04% | PASS |  |  |
| SOXL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0315) | PASS |  |  |
| SOXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.43× / 0.31× | 2.43× / 0.31× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 311359019) | 20 bars, last ('2026-11-19', 311359019) | PASS |  |  |
| SOXL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.43, OBV falling | condition true | PASS |  |  |
| SOXL.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.42 | $11.42 | PASS |  |  |
| SOXL.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $17.24 | $17.24 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL.NE | E3 | percent from the 21-day average | 33.7% below | 33.7% below | PASS |  |  |
| SOXL.NE | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SOXL.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.85 | $1.85 (sr=1.8485) | PASS |  | Wilder ATR14 |
| SOXL.NE | E5 | distance in normal day-moves | 3.1 | 3.1 | PASS |  | gauge dot note uses the same number:  · 3.1 day-moves below |
| SOXL.NE | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.7 | +4.7 | PASS |  |  |
| SOXL.NE | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.4 | +7.4 | PASS |  |  |
| SOXL.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $17.24, -33.7% | $17.24, -33.7% | PASS |  |  |
| SOXL.NE | L-now | ladder price row = compared price; name = the basis label | $11.42 "Last close" | $11.42 "last close" | PASS |  |  |
| SOXL.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.83, -63.0% | $30.83, -63.0% | PASS |  |  |
| SOXL.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $25.98, -56.0% | $25.98, -56.0% | PASS |  |  |
| SOXL.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.4 | 33.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.5% vs +9.2% | 29.5% vs 9.2% | PASS |  |  |
| SOXL.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.7 | 26.7 | PASS |  | Wilder, completed bars |
| SOXL.NE | T4w | words "20 or more / below 20" | 20 or more | ADX 26.7 | PASS |  |  |
| SOXL.NE | T6 | price vs 200-day average (S1 pattern sma values) | $11.42 vs $30.83 · -63.0% | $11.42 vs $30.83 · -63.0% | PASS |  |  |
| SOXL.NE | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T7 | price vs 50-day average (S1 pattern sma values) | $11.42 vs $25.98 · -56.0% | $11.42 vs $25.98 · -56.0% | PASS |  |  |
| SOXL.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| SOXL.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 84.6% below $74.21 | 84.6% below $74.21 | PASS |  | closing high would be 74.21 |
| SOXL.NE | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 84.6% below | PASS |  |  |
| SOXL.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $74.21 | $74.21369934082031 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL.NE | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 49 of 50 days empty | 49 of 50 days empty | PASS |  |  |
| SOXX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $137.95 | $137.95 | PASS |  |  |
| SOXX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $152.02 | $152.02 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXX | E3 | percent from the 21-day average | 9.3% below | 9.3% below | PASS |  |  |
| SOXX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.37 | $8.37 (sr=8.3726) | PASS |  | Wilder ATR14 |
| SOXX | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| SOXX | L-ema21 | ladder row ema21: price and gap = price vs average | $152.02, -9.3% | $152.02, -9.3% | PASS |  |  |
| SOXX | L-note | "Last close $X · date" note = last completed bar | Last close $137.95 · Nov 19 | $137.95 · Nov 19 | PASS |  |  |
| SOXX | L-now | ladder price row = compared price; name = the basis label | $137.95 "After hours" | $137.95 "after hours" | PASS |  |  |
| SOXX | L-sma200 | ladder row sma200: price and gap = price vs average | $160.79, -14.2% | $160.79, -14.2% | PASS |  |  |
| SOXX | L-sma50 | ladder row sma50: price and gap = price vs average | $169.16, -18.4% | $169.16, -18.4% | PASS |  |  |
| SOXX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $137.95 / entry $137.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.0 | 36.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +47.4% vs +9.2% | 47.4% vs 9.2% | PASS |  |  |
| SOXX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXX | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.6 | 31.6 | PASS |  | Wilder, completed bars |
| SOXX | T4w | words "20 or more / below 20" | 20 or more | ADX 31.6 | PASS |  |  |
| SOXX | T5 | "counted at the last close ($X, date)" = last completed bar | $137.95, Nov 19 | $137.95, Nov 19 | PASS |  |  |
| SOXX | T6 | price vs 200-day average (S1 pattern sma values) | $137.95 vs $160.79 · -14.2% | $137.95 vs $160.79 · -14.2% | PASS |  |  |
| SOXX | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T7 | price vs 50-day average (S1 pattern sma values) | $137.95 vs $169.16 · -18.4% | $137.95 vs $169.16 · -18.4% | PASS |  |  |
| SOXX | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.8% over 30 td | +4.8% over 30 td | PASS |  |  |
| SOXX | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.9% below $218.51 | 36.9% below $218.51 | PASS |  | closing high would be 218.19 |
| SOXX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.9% below | PASS |  |  |
| SOXX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $218.51 | $218.50713476135667 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.75%, close location 0.03, OBV falling |
| SOXX | V2 | day change of the last completed bar | down 2.8% | -2.75% | PASS |  |  |
| SOXX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0283) | PASS |  |  |
| SOXX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.33× / 0.45× | 1.33× / 0.45× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 40752666) | 20 bars, last ('2026-11-19', 40752666) | PASS |  |  |
| SPCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $8.91 | $8.91 | PASS |  |  |
| SPCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $12.46 | $12.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SPCL | E3 | percent from the 21-day average | 28.5% below | 28.5% below | PASS |  |  |
| SPCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SPCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.67 | $1.67 (sr=1.6723) | PASS |  | Wilder ATR14 |
| SPCL | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| SPCL | L-ema21 | ladder row ema21: price and gap = price vs average | $12.46, -28.5% | $12.46, -28.5% | PASS |  |  |
| SPCL | L-note | "Last close $X · date" note = last completed bar | Last close $8.91 · Nov 19 | $8.91 · Nov 19 | PASS |  |  |
| SPCL | L-now | ladder price row = compared price; name = the basis label | $8.91 "After hours" | $8.91 "after hours" | PASS |  |  |
| SPCL | L-sma50 | ladder row sma50: price and gap = price vs average | $16.89, -47.2% | $16.89, -47.2% | PASS |  |  |
| SPCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $8.91 / entry $8.91 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SPCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.1 | 34.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SPCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.7 | 32.7 | PASS |  | Wilder, completed bars |
| SPCL | T4w | words "20 or more / below 20" | 20 or more | ADX 32.7 | PASS |  |  |
| SPCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.61%, close location 0.05, OBV falling |
| SPCL | V2 | day change of the last completed bar | down 5.6% | -5.61% | PASS |  |  |
| SPCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0543) | PASS |  |  |
| SPCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SPCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.18× / 0.30× | 1.18× / 0.30× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SPCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 44680) | 20 bars, last ('2026-11-19', 44680) | PASS |  |  |
| TSLA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $374.41 | $374.41 | PASS |  |  |
| TSLA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $381.71 | $381.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLA | E3 | percent from the 21-day average | 1.9% below | 1.9% below | PASS |  |  |
| TSLA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.15 | $16.15 (sr=16.145) | PASS |  | Wilder ATR14 |
| TSLA | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| TSLA | L-ema21 | ladder row ema21: price and gap = price vs average | $381.71, -1.9% | $381.71, -1.9% | PASS |  |  |
| TSLA | L-note | "Last close $X · date" note = last completed bar | Last close $374.41 · Nov 19 | $374.41 · Nov 19 | PASS |  |  |
| TSLA | L-now | ladder price row = compared price; name = the basis label | $374.41 "After hours" | $374.41 "after hours" | PASS |  |  |
| TSLA | L-sma200 | ladder row sma200: price and gap = price vs average | $381.92, -2.0% | $381.92, -2.0% | PASS |  |  |
| TSLA | L-sma50 | ladder row sma50: price and gap = price vs average | $376.03, -0.4% | $376.03, -0.4% | PASS |  |  |
| TSLA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $374.41 / entry $374.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.2 | 47.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -7.3% vs +9.2% | -7.3% vs 9.2% | PASS |  |  |
| TSLA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLA | T4 | ADX 14 (S1 /api/sr meta.adx) | 10.9 | 10.9 | PASS |  | Wilder, completed bars |
| TSLA | T4w | words "20 or more / below 20" | below 20 | ADX 10.9 | PASS |  |  |
| TSLA | T5 | "counted at the last close ($X, date)" = last completed bar | $374.41, Nov 19 | $374.41, Nov 19 | PASS |  |  |
| TSLA | T6 | price vs 200-day average (S1 pattern sma values) | $374.41 vs $381.92 · -2.0% | $374.41 vs $381.92 · -2.0% | PASS |  |  |
| TSLA | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLA | T7 | price vs 50-day average (S1 pattern sma values) | $374.41 vs $376.03 · -0.4% | $374.41 vs $376.03 · -0.4% | PASS |  |  |
| TSLA | T7w | word "Below" | Below | Below | PASS |  |  |
| TSLA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.4% over 30 td | -2.4% over 30 td | PASS |  |  |
| TSLA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 24.9% below $498.83 | 24.9% below $498.83 | PASS |  | closing high would be 489.88 |
| TSLA | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 24.9% below | PASS |  |  |
| TSLA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $498.83 | $498.83 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.43%, close location 0.16, OBV flat |
| TSLA | V2 | day change of the last completed bar | down 2.4% | -2.43% | PASS |  |  |
| TSLA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1580) | PASS |  |  |
| TSLA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| TSLA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.73× / 0.56× | 0.73× / 0.56× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 26361008) | 20 bars, last ('2026-11-19', 26361008) | PASS |  |  |
| TSLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.53 | $9.53 | PASS |  |  |
| TSLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $10.06 | $10.06 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLL | E3 | percent from the 21-day average | 5.2% below | 5.2% below | PASS |  |  |
| TSLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.85 | $0.85 (sr=0.8496) | PASS |  | Wilder ATR14 |
| TSLL | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| TSLL | L-ema21 | ladder row ema21: price and gap = price vs average | $10.06, -5.2% | $10.06, -5.2% | PASS |  |  |
| TSLL | L-note | "Last close $X · date" note = last completed bar | Last close $9.53 · Nov 19 | $9.53 · Nov 19 | PASS |  |  |
| TSLL | L-now | ladder price row = compared price; name = the basis label | $9.53 "After hours" | $9.53 "after hours" | PASS |  |  |
| TSLL | L-sma200 | ladder row sma200: price and gap = price vs average | $11.67, -18.4% | $11.67, -18.4% | PASS |  |  |
| TSLL | L-sma50 | ladder row sma50: price and gap = price vs average | $9.97, -4.4% | $9.97, -4.4% | PASS |  |  |
| TSLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.53 / entry $9.53 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.6 | 45.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -38.9% vs +9.2% | -38.9% vs 9.2% | PASS |  |  |
| TSLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 10.8 | 10.8 | PASS |  | Wilder, completed bars |
| TSLL | T4w | words "20 or more / below 20" | below 20 | ADX 10.8 | PASS |  |  |
| TSLL | T5 | "counted at the last close ($X, date)" = last completed bar | $9.53, Nov 19 | $9.53, Nov 19 | PASS |  |  |
| TSLL | T6 | price vs 200-day average (S1 pattern sma values) | $9.53 vs $11.67 · -18.3% | $9.53 vs $11.67 · -18.4% | PASS |  |  |
| TSLL | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T7 | price vs 50-day average (S1 pattern sma values) | $9.53 vs $9.97 · -4.4% | $9.53 vs $9.97 · -4.4% | PASS |  |  |
| TSLL | T7w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -9.2% over 30 td | -9.2% over 30 td | PASS |  |  |
| TSLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 58.7% below $23.10 | 58.7% below $23.10 | PASS |  | closing high would be 22.41 |
| TSLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 58.7% below | PASS |  |  |
| TSLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $23.10 | $23.09813194913166 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -4.70%, close location 0.16, OBV rising |
| TSLL | V2 | day change of the last completed bar | down 4.7% | -4.70% | PASS |  |  |
| TSLL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1610) | PASS |  |  |
| TSLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| TSLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.70× / 0.53× | 0.70× / 0.53× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 37618242) | 20 bars, last ('2026-11-19', 37618242) | PASS |  |  |
| TSM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $352.09 | $352.09 | PASS |  |  |
| TSM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $393.82 | $393.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSM | E3 | percent from the 21-day average | 10.6% below | 10.6% below | PASS |  |  |
| TSM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.94 | $17.94 (sr=17.9377) | PASS |  | Wilder ATR14 |
| TSM | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| TSM | L-ema21 | ladder row ema21: price and gap = price vs average | $393.82, -10.6% | $393.82, -10.6% | PASS |  |  |
| TSM | L-note | "Last close $X · date" note = last completed bar | Last close $352.09 · Nov 19 | $352.09 · Nov 19 | PASS |  |  |
| TSM | L-now | ladder price row = compared price; name = the basis label | $352.09 "After hours" | $352.09 "after hours" | PASS |  |  |
| TSM | L-sma200 | ladder row sma200: price and gap = price vs average | $402.29, -12.5% | $402.29, -12.5% | PASS |  |  |
| TSM | L-sma50 | ladder row sma50: price and gap = price vs average | $424.37, -17.0% | $424.37, -17.0% | PASS |  |  |
| TSM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $352.09 / entry $352.09 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.5 | 34.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +26.0% vs +9.2% | 26.0% vs 9.2% | PASS |  |  |
| TSM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSM | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.6 | 32.6 | PASS |  | Wilder, completed bars |
| TSM | T4w | words "20 or more / below 20" | 20 or more | ADX 32.6 | PASS |  |  |
| TSM | T5 | "counted at the last close ($X, date)" = last completed bar | $352.09, Nov 19 | $352.09, Nov 19 | PASS |  |  |
| TSM | T6 | price vs 200-day average (S1 pattern sma values) | $352.09 vs $402.29 · -12.5% | $352.09 vs $402.29 · -12.5% | PASS |  |  |
| TSM | T6w | word "Below" | Below | Below | PASS |  |  |
| TSM | T7 | price vs 50-day average (S1 pattern sma values) | $352.09 vs $424.37 · -17.0% | $352.09 vs $424.37 · -17.0% | PASS |  |  |
| TSM | T7w | word "Below" | Below | Below | PASS |  |  |
| TSM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.3% over 30 td | +3.3% over 30 td | PASS |  |  |
| TSM | T8r | word "rising" | still rising | rising | PASS |  |  |
| TSM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.8% below $487.47 | 27.8% below $487.47 | PASS |  | closing high would be 485.80 |
| TSM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.8% below | PASS |  |  |
| TSM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $487.47 | $487.4700012207031 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.90%, close location 0.04, OBV falling |
| TSM | V2 | day change of the last completed bar | down 2.9% | -2.90% | PASS |  |  |
| TSM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0402) | PASS |  |  |
| TSM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.37× / 0.57× | 1.37× / 0.57× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 17715746) | 20 bars, last ('2026-11-19', 17715746) | PASS |  |  |
| UBOT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $14.34 | $14.34 | PASS |  |  |
| UBOT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $17.23 | $17.23 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UBOT | E3 | percent from the 21-day average | 16.8% below | 16.8% below | PASS |  |  |
| UBOT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| UBOT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.82 | $0.82 (sr=0.8177) | PASS |  | Wilder ATR14 |
| UBOT | E5 | distance in normal day-moves | 3.5 | 3.5 | PASS |  | gauge dot note uses the same number:  · 3.5 day-moves below |
| UBOT | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.0 | +3.0 | PASS |  |  |
| UBOT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.0 | +8.0 | PASS |  |  |
| UBOT | L-ema21 | ladder row ema21: price and gap = price vs average | $17.23, -16.8% | $17.23, -16.8% | PASS |  |  |
| UBOT | L-note | "Last close $X · date" note = last completed bar | Last close $14.34 · Nov 19 | $14.34 · Nov 19 | PASS |  |  |
| UBOT | L-now | ladder price row = compared price; name = the basis label | $14.34 "After hours" | $14.34 "after hours" | PASS |  |  |
| UBOT | L-sma200 | ladder row sma200: price and gap = price vs average | $23.75, -39.6% | $23.75, -39.6% | PASS |  |  |
| UBOT | L-sma50 | ladder row sma50: price and gap = price vs average | $19.71, -27.3% | $19.71, -27.3% | PASS |  |  |
| UBOT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $14.34 / entry $14.34 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UBOT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UBOT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.4 | 28.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UBOT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -35.4% vs +9.2% | -35.4% vs 9.2% | PASS |  |  |
| UBOT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UBOT | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.1 | 40.2 | PASS |  | Wilder, completed bars |
| UBOT | T4w | words "20 or more / below 20" | 20 or more | ADX 40.2 | PASS |  |  |
| UBOT | T5 | "counted at the last close ($X, date)" = last completed bar | $14.34, Nov 19 | $14.34, Nov 19 | PASS |  |  |
| UBOT | T6 | price vs 200-day average (S1 pattern sma values) | $14.34 vs $23.75 · -39.6% | $14.34 vs $23.75 · -39.6% | PASS |  |  |
| UBOT | T6w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T7 | price vs 50-day average (S1 pattern sma values) | $14.34 vs $19.71 · -27.2% | $14.34 vs $19.71 · -27.3% | PASS |  |  |
| UBOT | T7w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.2% over 30 td | -5.2% over 30 td | PASS |  |  |
| UBOT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UBOT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UBOT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 55.1% below $31.91 | 55.1% below $31.91 | PASS |  | closing high would be 31.87 |
| UBOT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 55.1% below | PASS |  |  |
| UBOT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.91 | $31.9057618947555 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UBOT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.84%, close location 0.01, OBV falling |
| UBOT | V2 | day change of the last completed bar | down 4.8% | -4.84% | PASS |  |  |
| UBOT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0091) | PASS |  |  |
| UBOT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UBOT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.04× / 0.85× | 1.04× / 0.85× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UBOT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 16782) | 20 bars, last ('2026-11-19', 16782) | PASS |  |  |
| UFO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $37.97 | $37.97 | PASS |  |  |
| UFO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.17 | $40.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UFO | E3 | percent from the 21-day average | 5.5% below | 5.5% below | PASS |  |  |
| UFO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| UFO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.38 | $1.38 (sr=1.3804) | PASS |  | Wilder ATR14 |
| UFO | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| UFO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.9 | +4.9 | PASS |  |  |
| UFO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.17, -5.5% | $40.17, -5.5% | PASS |  |  |
| UFO | L-note | "Last close $X · date" note = last completed bar | Last close $37.97 · Nov 19 | $37.97 · Nov 19 | PASS |  |  |
| UFO | L-now | ladder price row = compared price; name = the basis label | $37.97 "After hours" | $37.97 "after hours" | PASS |  |  |
| UFO | L-sma200 | ladder row sma200: price and gap = price vs average | $46.94, -19.1% | $46.94, -19.1% | PASS |  |  |
| UFO | L-sma50 | ladder row sma50: price and gap = price vs average | $41.39, -8.3% | $41.39, -8.3% | PASS |  |  |
| UFO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $37.97 / entry $37.97 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UFO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UFO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.4 | 38.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UFO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +16.6% vs +9.2% | 16.7% vs 9.2% | PASS |  |  |
| UFO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UFO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.5 | 25.5 | PASS |  | Wilder, completed bars |
| UFO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.5 | PASS |  |  |
| UFO | T5 | "counted at the last close ($X, date)" = last completed bar | $37.97, Nov 19 | $37.97, Nov 19 | PASS |  |  |
| UFO | T6 | price vs 200-day average (S1 pattern sma values) | $37.97 vs $46.94 · -19.1% | $37.97 vs $46.94 · -19.1% | PASS |  |  |
| UFO | T6w | word "Below" | Below | Below | PASS |  |  |
| UFO | T7 | price vs 50-day average (S1 pattern sma values) | $37.97 vs $41.39 · -8.3% | $37.97 vs $41.39 · -8.3% | PASS |  |  |
| UFO | T7w | word "Below" | Below | Below | PASS |  |  |
| UFO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.1% over 30 td | -1.1% over 30 td | PASS |  |  |
| UFO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UFO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UFO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 44.3% below $68.12 | 44.3% below $68.12 | PASS |  | closing high would be 67.71 |
| UFO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 44.3% below | PASS |  |  |
| UFO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $68.12 | $68.11999548611959 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UFO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.87%, close location 0.04, OBV falling |
| UFO | V2 | day change of the last completed bar | down 2.9% | -2.87% | PASS |  |  |
| UFO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0437) | PASS |  |  |
| UFO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UFO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.49× / 0.79× | 0.49× / 0.79× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UFO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 123706) | 20 bars, last ('2026-11-19', 123706) | PASS |  |  |
| URA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $28.67 | $28.67 | PASS |  |  |
| URA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.76 | $32.76 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URA | E3 | percent from the 21-day average | 12.5% below | 12.5% below | PASS |  |  |
| URA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| URA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.40 | $1.40 (sr=1.3971) | PASS |  | Wilder ATR14 |
| URA | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| URA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +9.1 | +9.1 | PASS |  |  |
| URA | L-ema21 | ladder row ema21: price and gap = price vs average | $32.76, -12.5% | $32.76, -12.5% | PASS |  |  |
| URA | L-note | "Last close $X · date" note = last completed bar | Last close $28.66 · Nov 19 | $28.66 · Nov 19 | PASS |  |  |
| URA | L-now | ladder price row = compared price; name = the basis label | $28.67 "After hours" | $28.67 "after hours" | PASS |  |  |
| URA | L-sma200 | ladder row sma200: price and gap = price vs average | $45.43, -36.9% | $45.43, -36.9% | PASS |  |  |
| URA | L-sma50 | ladder row sma50: price and gap = price vs average | $36.82, -22.1% | $36.82, -22.1% | PASS |  |  |
| URA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $28.67 / entry $28.67 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.8 | 28.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -33.6% vs +9.2% | -33.6% vs 9.2% | PASS |  |  |
| URA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URA | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.1 | 35.1 | PASS |  | Wilder, completed bars |
| URA | T4w | words "20 or more / below 20" | 20 or more | ADX 35.1 | PASS |  |  |
| URA | T5 | "counted at the last close ($X, date)" = last completed bar | $28.66, Nov 19 | $28.66, Nov 19 | PASS |  |  |
| URA | T6 | price vs 200-day average (S1 pattern sma values) | $28.66 vs $45.43 · -36.9% | $28.66 vs $45.43 · -36.9% | PASS |  |  |
| URA | T6w | word "Below" | Below | Below | PASS |  |  |
| URA | T7 | price vs 50-day average (S1 pattern sma values) | $28.66 vs $36.82 · -22.2% | $28.66 vs $36.82 · -22.2% | PASS |  |  |
| URA | T7w | word "Below" | Below | Below | PASS |  |  |
| URA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.4% over 30 td | -5.4% over 30 td | PASS |  |  |
| URA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.0% below $62.28 | 54.0% below $62.28 | PASS |  | closing high would be 61.81 |
| URA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.0% below | PASS |  |  |
| URA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.28 | $62.28 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.58%, close location 0.05, OBV falling |
| URA | V2 | day change of the last completed bar | down 2.6% | -2.58% | PASS |  |  |
| URA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0492) | PASS |  |  |
| URA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.37× / 0.53× | 1.37× / 0.53× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| URA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 5629544) | 20 bars, last ('2026-11-19', 5629544) | PASS |  |  |
| URAA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $10.37 | $10.37 | PASS |  |  |
| URAA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.56 | $13.56 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URAA | E3 | percent from the 21-day average | 23.5% below | 23.5% below | PASS |  |  |
| URAA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| URAA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.12 | $1.12 (sr=1.1204) | PASS |  | Wilder ATR14 |
| URAA | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| URAA | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.0 | +3.0 | PASS |  |  |
| URAA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +13.8 | +13.8 | PASS |  |  |
| URAA | L-ema21 | ladder row ema21: price and gap = price vs average | $13.56, -23.5% | $13.56, -23.5% | PASS |  |  |
| URAA | L-note | "Last close $X · date" note = last completed bar | Last close $10.37 · Nov 19 | $10.37 · Nov 19 | PASS |  |  |
| URAA | L-now | ladder price row = compared price; name = the basis label | $10.37 "After hours" | $10.37 "after hours" | PASS |  |  |
| URAA | L-sma200 | ladder row sma200: price and gap = price vs average | $29.07, -64.3% | $29.07, -64.3% | PASS |  |  |
| URAA | L-sma50 | ladder row sma50: price and gap = price vs average | $16.97, -38.9% | $16.97, -38.9% | PASS |  |  |
| URAA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $10.37 / entry $10.37 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URAA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URAA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.9 | 29.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URAA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -67.9% vs +9.2% | -67.9% vs 9.2% | PASS |  |  |
| URAA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URAA | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.5 | 32.6 | PASS |  | Wilder, completed bars |
| URAA | T4w | words "20 or more / below 20" | 20 or more | ADX 32.6 | PASS |  |  |
| URAA | T5 | "counted at the last close ($X, date)" = last completed bar | $10.37, Nov 19 | $10.37, Nov 19 | PASS |  |  |
| URAA | T6 | price vs 200-day average (S1 pattern sma values) | $10.37 vs $29.07 · -64.3% | $10.37 vs $29.07 · -64.3% | PASS |  |  |
| URAA | T6w | word "Below" | Below | Below | PASS |  |  |
| URAA | T7 | price vs 50-day average (S1 pattern sma values) | $10.37 vs $16.97 · -38.9% | $10.37 vs $16.97 · -38.9% | PASS |  |  |
| URAA | T7w | word "Below" | Below | Below | PASS |  |  |
| URAA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -12.9% over 30 td | -12.9% over 30 td | PASS |  |  |
| URAA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URAA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URAA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 83.3% below $62.21 | 83.3% below $62.21 | PASS |  | closing high would be 61.16 |
| URAA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 83.3% below | PASS |  |  |
| URAA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.21 | $62.21386524011286 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URAA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.38%, close location 0.03, OBV falling |
| URAA | V2 | day change of the last completed bar | down 5.4% | -5.38% | PASS |  |  |
| URAA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0256) | PASS |  |  |
| URAA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URAA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 0.50× | 1.11× / 0.50× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| URAA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 81222) | 20 bars, last ('2026-11-19', 81222) | PASS |  |  |
| V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $402.25 | $402.25 | PASS |  |  |
| V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $413.84 | $413.84 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| V | E3 | percent from the 21-day average | 2.8% below | 2.8% below | PASS |  |  |
| V | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.05 | $9.05 (sr=9.0485) | PASS |  | Wilder ATR14 |
| V | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -7.2 | -7.2 | PASS |  |  |
| V | L-ema21 | ladder row ema21: price and gap = price vs average | $413.84, -2.8% | $413.84, -2.8% | PASS |  |  |
| V | L-note | "Last close $X · date" note = last completed bar | Last close $402.25 · Nov 19 | $402.25 · Nov 19 | PASS |  |  |
| V | L-now | ladder price row = compared price; name = the basis label | $402.25 "After hours" | $402.25 "after hours" | PASS |  |  |
| V | L-sma200 | ladder row sma200: price and gap = price vs average | $348.79, 15.3% | $348.79, 15.3% | PASS |  |  |
| V | L-sma50 | ladder row sma50: price and gap = price vs average | $394.01, 2.1% | $394.01, 2.1% | PASS |  |  |
| V | S5-price | S5: the same live price reads the same on the header and the Entry block | header $402.25 / entry $402.25 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.8 | 43.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +24.1% vs +9.2% | 24.1% vs 9.2% | PASS |  |  |
| V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| V | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.9 | 33.9 | PASS |  | Wilder, completed bars |
| V | T4w | words "20 or more / below 20" | 20 or more | ADX 33.9 | PASS |  |  |
| V | T5 | "counted at the last close ($X, date)" = last completed bar | $402.25, Nov 19 | $402.25, Nov 19 | PASS |  |  |
| V | T6 | price vs 200-day average (S1 pattern sma values) | $402.25 vs $348.79 · +15.3% | $402.25 vs $348.79 · 15.3% | PASS |  |  |
| V | T6w | word "Above" | Above | Above | PASS |  |  |
| V | T7 | price vs 50-day average (S1 pattern sma values) | $402.25 vs $394.01 · +2.1% | $402.25 vs $394.01 · 2.1% | PASS |  |  |
| V | T7w | word "Above" | Above | Above | PASS |  |  |
| V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| V | T8r | word "rising" | still rising | rising | PASS |  |  |
| V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 9.0% below $442.23 | 9.0% below $442.23 | PASS |  | closing high would be 436.57 |
| V | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 9.0% below | PASS |  |  |
| V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $442.23 | $442.2254 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.12%, close location 0.12, OBV falling |
| V | V2 | day change of the last completed bar | down 3.1% | -3.12% | PASS |  |  |
| V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1182) | PASS |  |  |
| V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.24× / 1.39× | 1.24× / 1.39× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 8274590) | 20 bars, last ('2026-11-19', 8274590) | PASS |  |  |
| VFV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $182.95 | $182.95 | PASS |  |  |
| VFV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $188.89 | $188.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VFV.TO | E3 | percent from the 21-day average | 3.1% below | 3.1% below | PASS |  |  |
| VFV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| VFV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.00 | $3.00 (sr=3.004) | PASS |  | Wilder ATR14 |
| VFV.TO | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| VFV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $188.89, -3.1% | $188.89, -3.1% | PASS |  |  |
| VFV.TO | L-now | ladder price row = compared price; name = the basis label | $182.95 "Last close" | $182.95 "last close" | PASS |  |  |
| VFV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $180.86, 1.2% | $180.86, 1.2% | PASS |  |  |
| VFV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $191.13, -4.3% | $191.13, -4.3% | PASS |  |  |
| VFV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VFV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.7 | 36.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VFV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +11.3% vs +9.2% | 11.3% vs 9.2% | PASS |  |  |
| VFV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VFV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.6 | 20.6 | PASS |  | Wilder, completed bars |
| VFV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.6 | PASS |  |  |
| VFV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $182.95 vs $180.86 · +1.2% | $182.95 vs $180.86 · 1.2% | PASS |  |  |
| VFV.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| VFV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $182.95 vs $191.13 · -4.3% | $182.95 vs $191.13 · -4.3% | PASS |  |  |
| VFV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| VFV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.9% over 30 td | +1.9% over 30 td | PASS |  |  |
| VFV.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| VFV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VFV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.5% below $197.83 | 7.5% below $197.83 | PASS |  | closing high would be 197.56 |
| VFV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.5% below | PASS |  |  |
| VFV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $197.83 | $197.8300018310547 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VFV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.75%, close location 0.06, OBV falling |
| VFV.TO | V2 | day change of the last completed bar | down 1.8% | -1.75% | PASS |  |  |
| VFV.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0642) | PASS |  |  |
| VFV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| VFV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.87× / 1.07× | 1.87× / 1.06× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VFV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 603237) | 20 bars, last ('2026-11-19', 603237) | PASS |  |  |
| VFV.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.87, OBV falling | condition true | PASS |  |  |
| VRT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $184.99 | $184.99 | PASS |  |  |
| VRT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $204.72 | $204.72 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VRT | E3 | percent from the 21-day average | 9.6% below | 9.6% below | PASS |  |  |
| VRT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| VRT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.42 | $16.42 (sr=16.418) | PASS |  | Wilder ATR14 |
| VRT | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| VRT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| VRT | L-ema21 | ladder row ema21: price and gap = price vs average | $204.72, -9.6% | $204.72, -9.6% | PASS |  |  |
| VRT | L-note | "Last close $X · date" note = last completed bar | Last close $184.99 · Nov 19 | $184.99 · Nov 19 | PASS |  |  |
| VRT | L-now | ladder price row = compared price; name = the basis label | $184.99 "After hours" | $184.99 "after hours" | PASS |  |  |
| VRT | L-sma200 | ladder row sma200: price and gap = price vs average | $271.54, -31.9% | $271.54, -31.9% | PASS |  |  |
| VRT | L-sma50 | ladder row sma50: price and gap = price vs average | $224.83, -17.7% | $224.83, -17.7% | PASS |  |  |
| VRT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $184.99 / entry $184.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| VRT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VRT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.4 | 40.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VRT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +8.5% vs +9.2% | 8.5% vs 9.2% | PASS |  |  |
| VRT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VRT | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.7 | 21.7 | PASS |  | Wilder, completed bars |
| VRT | T4w | words "20 or more / below 20" | 20 or more | ADX 21.7 | PASS |  |  |
| VRT | T5 | "counted at the last close ($X, date)" = last completed bar | $184.99, Nov 19 | $184.99, Nov 19 | PASS |  |  |
| VRT | T6 | price vs 200-day average (S1 pattern sma values) | $184.99 vs $271.54 · -31.9% | $184.99 vs $271.54 · -31.9% | PASS |  |  |
| VRT | T6w | word "Below" | Below | Below | PASS |  |  |
| VRT | T7 | price vs 50-day average (S1 pattern sma values) | $184.99 vs $224.83 · -17.7% | $184.99 vs $224.83 · -17.7% | PASS |  |  |
| VRT | T7w | word "Below" | Below | Below | PASS |  |  |
| VRT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.9% over 30 td | +1.9% over 30 td | PASS |  |  |
| VRT | T8r | word "rising" | still rising | rising | PASS |  |  |
| VRT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VRT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.3% below $379.76 | 51.3% below $379.76 | PASS |  | closing high would be 376.06 |
| VRT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.3% below | PASS |  |  |
| VRT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $379.76 | $379.76284762424655 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VRT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.88%, close location 0.07, OBV falling |
| VRT | V2 | day change of the last completed bar | down 4.9% | -4.88% | PASS |  |  |
| VRT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0670) | PASS |  |  |
| VRT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| VRT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.09× / 0.55× | 1.09× / 0.55× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VRT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 7246438) | 20 bars, last ('2026-11-19', 7246438) | PASS |  |  |
| WDC.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.98 | $17.98 | PASS |  |  |
| WDC.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $19.37 | $19.37 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WDC.TO | E3 | percent from the 21-day average | 7.2% below | 7.2% below | PASS |  |  |
| WDC.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| WDC.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.49 | $1.49 (sr=1.4852) | PASS |  | Wilder ATR14 |
| WDC.TO | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves below |
| WDC.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $19.37, -7.2% | $19.37, -7.2% | PASS |  |  |
| WDC.TO | L-now | ladder price row = compared price; name = the basis label | $17.98 "Last close" | $17.98 "last close" | PASS |  |  |
| WDC.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $22.98, -21.8% | $22.98, -21.8% | PASS |  |  |
| WDC.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.7 | 40.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WDC.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.2 | 33.2 | PASS |  | Wilder, completed bars |
| WDC.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 33.2 | PASS |  |  |
| WDC.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change 3.10%, close location 0.22, OBV falling |
| WDC.TO | V2 | day change of the last completed bar | up 3.1% | +3.10% | PASS |  |  |
| WDC.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2153) | PASS |  |  |
| WDC.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| WDC.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.20× / 0.38× | 1.20× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WDC.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 197669) | 20 bars, last ('2026-11-19', 197669) | PASS |  |  |
| WELL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $243.19 | $243.19 | PASS |  |  |
| WELL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $241.93 | $241.93 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WELL | E3 | percent from the 21-day average | 0.5% above | 0.5% above | PASS |  |  |
| WELL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| WELL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.26 | $5.26 (sr=5.2614) | PASS |  | Wilder ATR14 |
| WELL | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| WELL | L-ema21 | ladder row ema21: price and gap = price vs average | $241.93, 0.5% | $241.93, 0.5% | PASS |  |  |
| WELL | L-note | "Last close $X · date" note = last completed bar | Last close $243.19 · Nov 19 | $243.19 · Nov 19 | PASS |  |  |
| WELL | L-now | ladder price row = compared price; name = the basis label | $243.19 "After hours" | $243.19 "after hours" | PASS |  |  |
| WELL | L-sma200 | ladder row sma200: price and gap = price vs average | $222.6, 9.2% | $222.60, 9.2% | PASS |  |  |
| WELL | L-sma50 | ladder row sma50: price and gap = price vs average | $235.25, 3.4% | $235.25, 3.4% | PASS |  |  |
| WELL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $243.19 / entry $243.19 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WELL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WELL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.1 | 54.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WELL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +23.5% vs +9.2% | 23.5% vs 9.2% | PASS |  |  |
| WELL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WELL | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.1 | 11.1 | PASS |  | Wilder, completed bars |
| WELL | T4w | words "20 or more / below 20" | below 20 | ADX 11.1 | PASS |  |  |
| WELL | T5 | "counted at the last close ($X, date)" = last completed bar | $243.19, Nov 19 | $243.19, Nov 19 | PASS |  |  |
| WELL | T6 | price vs 200-day average (S1 pattern sma values) | $243.19 vs $222.60 · +9.2% | $243.19 vs $222.60 · 9.2% | PASS |  |  |
| WELL | T6w | word "Above" | Above | Above | PASS |  |  |
| WELL | T7 | price vs 50-day average (S1 pattern sma values) | $243.19 vs $235.25 · +3.4% | $243.19 vs $235.25 · 3.4% | PASS |  |  |
| WELL | T7w | word "Above" | Above | Above | PASS |  |  |
| WELL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| WELL | T8r | word "rising" | still rising | rising | PASS |  |  |
| WELL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WELL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.7% below $255.20 | 4.7% below $255.20 | PASS |  | closing high would be 252.07 |
| WELL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.7% below | PASS |  |  |
| WELL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $255.20 | $255.2 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WELL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.64%, close location 0.04, OBV rising |
| WELL | V2 | day change of the last completed bar | down 1.6% | -1.64% | PASS |  |  |
| WELL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0379) | PASS |  |  |
| WELL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WELL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.18× / 0.76× | 1.18× / 0.76× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WELL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 3383635) | 20 bars, last ('2026-11-19', 3383635) | PASS |  |  |
| WMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $126.04 | $126.04 | PASS |  |  |
| WMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $124.15 | $124.15 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WMT | E3 | percent from the 21-day average | 1.5% above | 1.5% above | PASS |  |  |
| WMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| WMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.77 | $2.77 (sr=2.7737) | PASS |  | Wilder ATR14 |
| WMT | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves above |
| WMT | L-ema21 | ladder row ema21: price and gap = price vs average | $124.15, 1.5% | $124.15, 1.5% | PASS |  |  |
| WMT | L-note | "Last close $X · date" note = last completed bar | Last close $126.04 · Nov 19 | $126.04 · Nov 19 | PASS |  |  |
| WMT | L-now | ladder price row = compared price; name = the basis label | $126.04 "After hours" | $126.04 "after hours" | PASS |  |  |
| WMT | L-sma200 | ladder row sma200: price and gap = price vs average | $118.99, 5.9% | $118.99, 5.9% | PASS |  |  |
| WMT | L-sma50 | ladder row sma50: price and gap = price vs average | $116.23, 8.4% | $116.23, 8.4% | PASS |  |  |
| WMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $126.04 / entry $126.04 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.8 | 59.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.3% vs +9.2% | 25.3% vs 9.2% | PASS |  |  |
| WMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 43.7 | 43.6 | PASS |  | Wilder, completed bars |
| WMT | T4w | words "20 or more / below 20" | 20 or more | ADX 43.6 | PASS |  |  |
| WMT | T5 | "counted at the last close ($X, date)" = last completed bar | $126.04, Nov 19 | $126.04, Nov 19 | PASS |  |  |
| WMT | T6 | price vs 200-day average (S1 pattern sma values) | $126.04 vs $118.99 · +5.9% | $126.04 vs $118.99 · 5.9% | PASS |  |  |
| WMT | T6w | word "Above" | Above | Above | PASS |  |  |
| WMT | T7 | price vs 50-day average (S1 pattern sma values) | $126.04 vs $116.23 · +8.4% | $126.04 vs $116.23 · 8.4% | PASS |  |  |
| WMT | T7w | word "Above" | Above | Above | PASS |  |  |
| WMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.7% over 30 td | +0.7% over 30 td | PASS |  |  |
| WMT | T8r | word "rising" | still rising | rising | PASS |  |  |
| WMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.7% below $135.16 | 6.7% below $135.16 | PASS |  | closing high would be 134.20 |
| WMT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.7% below | PASS |  |  |
| WMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $135.16 | $135.155 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.04%, close location 0.75, OBV falling |
| WMT | V2 | day change of the last completed bar | down 1.0% | -1.04% | PASS |  |  |
| WMT | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.75 (raw 0.7527) | PASS |  |  |
| WMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| WMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.46× / 0.47× | 1.46× / 0.47× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 32257811) | 20 bars, last ('2026-11-19', 32257811) | PASS |  |  |
| XCHP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $103.19 | $103.19 | PASS |  |  |
| XCHP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $112.31 | $112.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XCHP.TO | E3 | percent from the 21-day average | 8.1% below | 8.1% below | PASS |  |  |
| XCHP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XCHP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.17 | $6.17 (sr=6.1667) | PASS |  | Wilder ATR14 |
| XCHP.TO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| XCHP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $112.31, -8.1% | $112.31, -8.1% | PASS |  |  |
| XCHP.TO | L-now | ladder price row = compared price; name = the basis label | $103.19 "Last close" | $103.19 "last close" | PASS |  |  |
| XCHP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $116.79, -11.6% | $116.79, -11.6% | PASS |  |  |
| XCHP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $124.27, -17.0% | $124.27, -17.0% | PASS |  |  |
| XCHP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XCHP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.0 | 38.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XCHP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.7% vs +9.2% | 49.7% vs 9.2% | PASS |  |  |
| XCHP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XCHP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.0 | 32.0 | PASS |  | Wilder, completed bars |
| XCHP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.0 | PASS |  |  |
| XCHP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $103.19 vs $116.79 · -11.6% | $103.19 vs $116.79 · -11.6% | PASS |  |  |
| XCHP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $103.19 vs $124.27 · -17.0% | $103.19 vs $124.27 · -17.0% | PASS |  |  |
| XCHP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.1% over 30 td | +5.1% over 30 td | PASS |  |  |
| XCHP.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XCHP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XCHP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.0% below $161.26 | 36.0% below $161.26 | PASS |  | closing high would be 160.97 |
| XCHP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.0% below | PASS |  |  |
| XCHP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $161.26 | $161.25523669513825 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XCHP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.50%, close location 0.02, OBV falling |
| XCHP.TO | V2 | day change of the last completed bar | down 2.5% | -2.50% | PASS |  |  |
| XCHP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0250) | PASS |  |  |
| XCHP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XCHP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.33× / 0.42× | 1.33× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XCHP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 70123) | 20 bars, last ('2026-11-19', 70123) | PASS |  |  |
| XDRV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.55 | $39.55 | PASS |  |  |
| XDRV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.96 | $40.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XDRV.TO | E3 | percent from the 21-day average | 3.4% below | 3.4% below | PASS |  |  |
| XDRV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XDRV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.80 | $0.80 (sr=0.7991) | PASS |  | Wilder ATR14 |
| XDRV.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| XDRV.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.3 | +8.3 | PASS |  |  |
| XDRV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.96, -3.4% | $40.96, -3.4% | PASS |  |  |
| XDRV.TO | L-now | ladder price row = compared price; name = the basis label | $39.55 "Last close" | $39.55 "last close" | PASS |  |  |
| XDRV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $47.59, -16.9% | $47.59, -16.9% | PASS |  |  |
| XDRV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.27, -8.6% | $43.27, -8.6% | PASS |  |  |
| XDRV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XDRV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.0 | 41.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XDRV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.4% vs +9.2% | -1.4% vs 9.2% | PASS |  |  |
| XDRV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XDRV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.3 | 22.3 | PASS |  | Wilder, completed bars |
| XDRV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.3 | PASS |  |  |
| XDRV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $39.55 vs $47.59 · -16.9% | $39.55 vs $47.59 · -16.9% | PASS |  |  |
| XDRV.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $39.55 vs $43.27 · -8.6% | $39.55 vs $43.27 · -8.6% | PASS |  |  |
| XDRV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.8% over 30 td | -0.8% over 30 td | PASS |  |  |
| XDRV.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XDRV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XDRV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.5% below $61.36 | 35.5% below $61.36 | PASS |  | closing high would be 61.36 |
| XDRV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.5% below | PASS |  |  |
| XDRV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $61.36 | $61.35662078857422 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XDRV.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 42 of 50 days empty | 42 of 50 days empty | PASS |  |  |
| XEQT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $43.28 | $43.28 | PASS |  |  |
| XEQT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $44.88 | $44.88 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XEQT.TO | E3 | percent from the 21-day average | 3.6% below | 3.6% below | PASS |  |  |
| XEQT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XEQT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.60 | $0.60 (sr=0.603) | PASS |  | Wilder ATR14 |
| XEQT.TO | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| XEQT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $44.88, -3.6% | $44.88, -3.6% | PASS |  |  |
| XEQT.TO | L-now | ladder price row = compared price; name = the basis label | $43.28 "Last close" | $43.28 "last close" | PASS |  |  |
| XEQT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $43.6, -0.7% | $43.60, -0.7% | PASS |  |  |
| XEQT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $45.32, -4.5% | $45.32, -4.5% | PASS |  |  |
| XEQT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XEQT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.4 | 34.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XEQT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +12.6% vs +9.2% | 12.6% vs 9.2% | PASS |  |  |
| XEQT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XEQT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.7 | 17.7 | PASS |  | Wilder, completed bars |
| XEQT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 17.7 | PASS |  |  |
| XEQT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $43.28 vs $43.60 · -0.7% | $43.28 vs $43.60 · -0.7% | PASS |  |  |
| XEQT.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XEQT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $43.28 vs $45.32 · -4.5% | $43.28 vs $45.32 · -4.5% | PASS |  |  |
| XEQT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XEQT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.7% over 30 td | +1.7% over 30 td | PASS |  |  |
| XEQT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XEQT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XEQT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.7% below $46.38 | 6.7% below $46.38 | PASS |  | closing high would be 46.27 |
| XEQT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.7% below | PASS |  |  |
| XEQT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.38 | $46.380001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XEQT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.66%, close location 0.07, OBV falling |
| XEQT.TO | V2 | day change of the last completed bar | down 1.7% | -1.66% | PASS |  |  |
| XEQT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0654) | PASS |  |  |
| XEQT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XEQT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.12× / 1.19× | 2.12× / 1.19× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XEQT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 1981270) | 20 bars, last ('2026-11-19', 1981270) | PASS |  |  |
| XEQT.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.12, OBV falling | condition true | PASS |  |  |
| XETM.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $56.19 | $56.19 | PASS |  |  |
| XETM.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $66.37 | $66.37 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XETM.TO | E3 | percent from the 21-day average | 15.3% below | 15.3% below | PASS |  |  |
| XETM.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XETM.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.50 | $2.50 (sr=2.4984) | PASS |  | Wilder ATR14 |
| XETM.TO | E5 | distance in normal day-moves | 4.1 | 4.1 | PASS |  | gauge dot note uses the same number:  · 4.1 day-moves below |
| XETM.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.0 | +3.0 | PASS |  |  |
| XETM.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.3 | +5.3 | PASS |  |  |
| XETM.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $66.37, -15.3% | $66.37, -15.3% | PASS |  |  |
| XETM.TO | L-now | ladder price row = compared price; name = the basis label | $56.19 "Last close" | $56.19 "last close" | PASS |  |  |
| XETM.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $79.59, -29.4% | $79.59, -29.4% | PASS |  |  |
| XETM.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $73.96, -24.0% | $73.96, -24.0% | PASS |  |  |
| XETM.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.1 | 27.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XETM.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -33.3% vs +9.2% | -33.3% vs 9.2% | PASS |  |  |
| XETM.TO | T3w | words "past year" vs the window used | 210 / 251 bars back | 250-253 bars | PASS |  |  |
| XETM.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.8 | 24.8 | PASS |  | Wilder, completed bars |
| XETM.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 24.8 | PASS |  |  |
| XETM.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.72%, close location 0.00, OBV falling |
| XETM.TO | V2 | day change of the last completed bar | down 2.7% | -2.72% | PASS |  |  |
| XETM.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| XETM.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XETM.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.05× / 0.61× | 3.05× / 0.61× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XETM.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 10042) | 20 bars, last ('2026-11-19', 10042) | PASS |  |  |
| XETM.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.05, OBV falling | condition true | PASS |  |  |
| XGD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $46.79 | $46.79 | PASS |  |  |
| XGD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $52.15 | $52.15 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XGD.TO | E3 | percent from the 21-day average | 10.3% below | 10.3% below | PASS |  |  |
| XGD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XGD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.14 | $2.14 (sr=2.1419) | PASS |  | Wilder ATR14 |
| XGD.TO | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| XGD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $52.15, -10.3% | $52.15, -10.3% | PASS |  |  |
| XGD.TO | L-now | ladder price row = compared price; name = the basis label | $46.79 "Last close" | $46.79 "last close" | PASS |  |  |
| XGD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $55.04, -15.0% | $55.04, -15.0% | PASS |  |  |
| XGD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $54.71, -14.5% | $54.71, -14.5% | PASS |  |  |
| XGD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XGD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.3 | 35.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XGD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.8% vs +9.2% | 0.8% vs 9.2% | PASS |  |  |
| XGD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XGD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.9 | 18.9 | PASS |  | Wilder, completed bars |
| XGD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.9 | PASS |  |  |
| XGD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $46.79 vs $55.04 · -15.0% | $46.79 vs $55.04 · -15.0% | PASS |  |  |
| XGD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $46.79 vs $54.71 · -14.5% | $46.79 vs $54.71 · -14.5% | PASS |  |  |
| XGD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.2% over 30 td | -1.2% over 30 td | PASS |  |  |
| XGD.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XGD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XGD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 32.7% below $69.54 | 32.7% below $69.54 | PASS |  | closing high would be 68.70 |
| XGD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 32.7% below | PASS |  |  |
| XGD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $69.54 | $69.54086233267267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XGD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.41%, close location 0.05, OBV falling |
| XGD.TO | V2 | day change of the last completed bar | down 3.4% | -3.41% | PASS |  |  |
| XGD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0495) | PASS |  |  |
| XGD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XGD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.78× / 0.74× | 0.78× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XGD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 363658) | 20 bars, last ('2026-11-19', 363658) | PASS |  |  |
| XOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $158.93 | $158.93 | PASS |  |  |
| XOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $169.05 | $169.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XOM | E3 | percent from the 21-day average | 6.0% below | 6.0% below | PASS |  |  |
| XOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| XOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.33 | $4.33 (sr=4.3295) | PASS |  | Wilder ATR14 |
| XOM | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| XOM | L-ema21 | ladder row ema21: price and gap = price vs average | $169.05, -6.0% | $169.05, -6.0% | PASS |  |  |
| XOM | L-note | "Last close $X · date" note = last completed bar | Last close $158.93 · Nov 19 | $158.93 · Nov 19 | PASS |  |  |
| XOM | L-now | ladder price row = compared price; name = the basis label | $158.93 "After hours" | $158.93 "after hours" | PASS |  |  |
| XOM | L-sma200 | ladder row sma200: price and gap = price vs average | $156.76, 1.4% | $156.76, 1.4% | PASS |  |  |
| XOM | L-sma50 | ladder row sma50: price and gap = price vs average | $169.46, -6.2% | $169.46, -6.2% | PASS |  |  |
| XOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $158.93 / entry $158.93 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| XOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.2 | 34.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +35.4% vs +9.2% | 35.4% vs 9.2% | PASS |  |  |
| XOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.1 | 28.1 | PASS |  | Wilder, completed bars |
| XOM | T4w | words "20 or more / below 20" | 20 or more | ADX 28.1 | PASS |  |  |
| XOM | T5 | "counted at the last close ($X, date)" = last completed bar | $158.93, Nov 19 | $158.93, Nov 19 | PASS |  |  |
| XOM | T6 | price vs 200-day average (S1 pattern sma values) | $158.93 vs $156.76 · +1.4% | $158.93 vs $156.76 · 1.4% | PASS |  |  |
| XOM | T6w | word "Above" | Above | Above | PASS |  |  |
| XOM | T7 | price vs 50-day average (S1 pattern sma values) | $158.93 vs $169.46 · -6.2% | $158.93 vs $169.46 · -6.2% | PASS |  |  |
| XOM | T7w | word "Below" | Below | Below | PASS |  |  |
| XOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.5% over 30 td | +4.5% over 30 td | PASS |  |  |
| XOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| XOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 15.7% below $188.50 | 15.7% below $188.50 | PASS |  | closing high would be 187.25 |
| XOM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 15.7% below | PASS |  |  |
| XOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $188.50 | $188.5 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.03%, close location 0.10, OBV falling |
| XOM | V2 | day change of the last completed bar | down 1.0% | -1.03% | PASS |  |  |
| XOM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.0951) | PASS |  |  |
| XOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.91× / 0.38× | 0.91× / 0.38× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 12263492) | 20 bars, last ('2026-11-19', 12263492) | PASS |  |  |
