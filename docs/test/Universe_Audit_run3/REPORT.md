# Statement Audit report

Run: 2026-11-17T18:47 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM · ET at first dump: 11/17/2026, 5:33:40 PM

Verdicts: PASS 3797 · WRONG 1 (CRITICAL) · MISLEADING 8 (HIGH) · UNVERIFIED 342 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| TSLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 2 up, 0 down, 1 flat | WRONG | CRITICAL | change 0.10%, close location 0.64, OBV rising |
| ANET.TO | T3w | words "past year" vs the window used | 226 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| ASTL.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.5 | 27.7 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AVGC | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.5 | 21.3 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AVGO.TO | T3w | words "past year" vs the window used | 226 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| DRAL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.0 | 34.3 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| GEV.TO | T3w | words "past year" vs the window used | 226 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| MTRX.TO | T3w | words "past year" vs the window used | 208 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| XETM.TO | T3w | words "past year" vs the window used | 208 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| AAPL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.83× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.44× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AAPU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.80× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ABBV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.82× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AIPO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.11× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ALAB | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.27× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.03× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.89× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.45× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 227 252. 0.7× 0.72× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| ANET.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.03× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASML.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.33× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASTL.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.34× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ATD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | U1 | numbers on the card no statement above claimed (exhaustive scan) | 99 252. 0.4× 0.41× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AVGC | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.02× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AVGO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 227 252. 0.9× 0.87× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AVGO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.3× 2.30× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BDT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.2× 2.21× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BOTZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.06× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRK-B | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.2× 2.18× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRKU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.64× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.97× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.41× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CCO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.79× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CEG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.37× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CGY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.72× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.12× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COP | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.84× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.0× 2.03× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 190 252. 2.8× 2.77× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| COPZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | U1 | numbers on the card no statement above claimed (exhaustive scan) | $1,104.75 3.0 1.3× 1.25× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| COST | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | U1 | numbers on the card no statement above claimed (exhaustive scan) | $16.87 3.2 0.3× 0.27× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| COTG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CSU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.96× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CVX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 102 252. 1.7× 1.68× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 159 252. 1.2× 1.22× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.73× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DRIV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.54× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DUK | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ELIL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.02× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| EQIX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.30× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ETN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.26× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| FCX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.5× 3.54× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| FINN.NE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.01× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.50× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDXU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.77× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.59× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GEV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 227 252. 1.5× 1.52× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| GEV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.55× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GGLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.05× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GIB-A.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.97× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GOOGL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.00× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GRID | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.41× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.66× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HURA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.11× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HXQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.10× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JNJ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.07× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JPM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.40× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| KEYS | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.12× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| LIN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.96× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| LLY | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.39× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MDA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.58× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| META | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.2× 0.24× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| METU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.08× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MRVL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.15× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MSFT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.14× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MSFU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 209 252. 0.7× 0.67× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| MTRX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.17× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.86× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.08× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NFLX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.70× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NFXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.41× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NTR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.4× 2.35× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NVDA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.3× 3.32× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NVDL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.05× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ONTO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 140 252. 0.2× 0.19× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| ORBX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.69× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ORCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.90× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.89× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PLD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.42× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PNG.V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.82× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QCOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.56× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QPUX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.00× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QTUM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 4.7× 4.74× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RBOT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.14× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RTX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.13× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.93× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SETM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 146 252. 0.1× 0.15× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SGRD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.28× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SMH | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 13 252. 1.7× 1.73× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SNDK.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.25× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.0× 1.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.26× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 156 252. 0.4× 0.40× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SPCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.61× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.64× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.93× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.39× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UBOT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.50× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UFO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.43× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| URA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.01× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| URAA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.87× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.63× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| VFV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.84× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| VRT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 13 252. 0.8× 0.80× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| WDC.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.16× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WELL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.90× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.91× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XCHP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.46× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XEQT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 209 252. 1.2× 1.19× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| XETM.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.77× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XGD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.77× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $349.45 | $349.45 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $347.14 | $347.14 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 0.7% above | 0.7% above | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.87 | $7.87 (sr=7.8729) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.8 | -5.8 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $347.14, 0.7% | $347.14, 0.7% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $349.45 "After hours" | $349.45 "after hours" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $301.66, 15.8% | $301.66, 15.8% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $340.17, 2.7% | $340.17, 2.7% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $349.45 / entry $349.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| AAPL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.83× / 0.11× | 0.83× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 36248936) | 20 bars, last ('2026-11-17', 36248936) | PASS |  |  |
| AAPU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $48.27 | $48.27 | PASS |  |  |
| AAPU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $47.52 | $47.52 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPU | E3 | percent from the 21-day average | 1.6% above | 1.6% above | PASS |  |  |
| AAPU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AAPU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.04 | $2.04 (sr=2.0423) | PASS |  | Wilder ATR14 |
| AAPU | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves above |
| AAPU | L-ema21 | ladder row ema21: price and gap = price vs average | $47.52, 1.6% | $47.52, 1.6% | PASS |  |  |
| AAPU | L-note | "Last close $X · date" note = last completed bar | Last close $48.49 · Nov 17 | $48.49 · Nov 17 | PASS |  |  |
| AAPU | L-now | ladder price row = compared price; name = the basis label | $48.27 "After hours" | $48.27 "after hours" | PASS |  |  |
| AAPU | L-sma200 | ladder row sma200: price and gap = price vs average | $38.12, 26.6% | $38.12, 26.6% | PASS |  |  |
| AAPU | L-sma50 | ladder row sma50: price and gap = price vs average | $45.99, 5.0% | $45.99, 5.0% | PASS |  |  |
| AAPU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $48.27 / entry $48.27 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.8 | 54.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.5% vs +11.2% | 49.5% vs 11.2% | PASS |  |  |
| AAPU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPU | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.9 | 17.9 | PASS |  | Wilder, completed bars |
| AAPU | T4w | words "20 or more / below 20" | below 20 | ADX 17.9 | PASS |  |  |
| AAPU | T5 | "counted at the last close ($X, date)" = last completed bar | $48.49, Nov 17 | $48.49, Nov 17 | PASS |  |  |
| AAPU | T6 | price vs 200-day average (S1 pattern sma values) | $48.49 vs $38.12 · +27.2% | $48.49 vs $38.12 · 27.2% | PASS |  |  |
| AAPU | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T7 | price vs 50-day average (S1 pattern sma values) | $48.49 vs $45.99 · +5.4% | $48.49 vs $45.99 · 5.4% | PASS |  |  |
| AAPU | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.8% over 30 td | +6.8% over 30 td | PASS |  |  |
| AAPU | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.0% below $51.04 | 5.0% below $51.04 | PASS |  | closing high would be 49.81 |
| AAPU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.0% below | PASS |  |  |
| AAPU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $51.04 | $51.040000915527344 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.57%, close location 0.36, OBV falling |
| AAPU | V2 | day change of the last completed bar | down 0.6% | -0.57% | PASS |  |  |
| AAPU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.44× / 0.14× | 0.44× / 0.14× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 424092) | 20 bars, last ('2026-11-17', 424092) | PASS |  |  |
| ABBV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $292.82 | $292.82 | PASS |  |  |
| ABBV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $289.16 | $289.16 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ABBV | E3 | percent from the 21-day average | 1.3% above | 1.3% above | PASS |  |  |
| ABBV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ABBV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.66 | $6.66 (sr=6.6623) | PASS |  | Wilder ATR14 |
| ABBV | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| ABBV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -7.5 | -7.5 | PASS |  |  |
| ABBV | L-ema21 | ladder row ema21: price and gap = price vs average | $289.16, 1.3% | $289.16, 1.3% | PASS |  |  |
| ABBV | L-note | "Last close $X · date" note = last completed bar | Last close $292.82 · Nov 17 | $292.82 · Nov 17 | PASS |  |  |
| ABBV | L-now | ladder price row = compared price; name = the basis label | $292.82 "After hours" | $292.82 "after hours" | PASS |  |  |
| ABBV | L-sma200 | ladder row sma200: price and gap = price vs average | $238.92, 22.6% | $238.92, 22.6% | PASS |  |  |
| ABBV | L-sma50 | ladder row sma50: price and gap = price vs average | $276.3, 6.0% | $276.30, 6.0% | PASS |  |  |
| ABBV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $292.82 / entry $292.82 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ABBV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ABBV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.1 | 59.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ABBV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.9% vs +11.2% | 28.9% vs 11.2% | PASS |  |  |
| ABBV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ABBV | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.7 | 30.7 | PASS |  | Wilder, completed bars |
| ABBV | T4w | words "20 or more / below 20" | 20 or more | ADX 30.7 | PASS |  |  |
| ABBV | T5 | "counted at the last close ($X, date)" = last completed bar | $292.82, Nov 17 | $292.82, Nov 17 | PASS |  |  |
| ABBV | T6 | price vs 200-day average (S1 pattern sma values) | $292.82 vs $238.92 · +22.6% | $292.82 vs $238.92 · 22.6% | PASS |  |  |
| ABBV | T6w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T7 | price vs 50-day average (S1 pattern sma values) | $292.82 vs $276.30 · +6.0% | $292.82 vs $276.30 · 6.0% | PASS |  |  |
| ABBV | T7w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.5% over 30 td | +4.5% over 30 td | PASS |  |  |
| ABBV | T8r | word "rising" | still rising | rising | PASS |  |  |
| ABBV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ABBV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.3% below $302.93 | 3.3% below $302.93 | PASS |  | closing high would be 295.03 |
| ABBV | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.3% below | PASS |  |  |
| ABBV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.93 | $302.92999267578125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ABBV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -0.59%, close location 0.59, OBV flat |
| ABBV | V2 | day change of the last completed bar | down 0.6% | -0.59% | PASS |  |  |
| ABBV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| ABBV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.80× / 0.26× | 0.80× / 0.26× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ABBV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3925606) | 20 bars, last ('2026-11-17', 3925606) | PASS |  |  |
| AIPO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $22.63 | $22.63 | PASS |  |  |
| AIPO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.34 | $24.34 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AIPO | E3 | percent from the 21-day average | 7.0% below | 7.0% below | PASS |  |  |
| AIPO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AIPO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.13 | $1.13 (sr=1.1313) | PASS |  | Wilder ATR14 |
| AIPO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| AIPO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| AIPO | L-ema21 | ladder row ema21: price and gap = price vs average | $24.34, -7.0% | $24.34, -7.0% | PASS |  |  |
| AIPO | L-now | ladder price row = compared price; name = the basis label | $22.63 "Last close" | $22.63 "last close" | PASS |  |  |
| AIPO | L-sma200 | ladder row sma200: price and gap = price vs average | $28.5, -20.6% | $28.50, -20.6% | PASS |  |  |
| AIPO | L-sma50 | ladder row sma50: price and gap = price vs average | $26.56, -14.8% | $26.56, -14.8% | PASS |  |  |
| AIPO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AIPO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.5 | 38.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AIPO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.0% vs +11.2% | 2.0% vs 11.2% | PASS |  |  |
| AIPO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AIPO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.8 | 31.8 | PASS |  | Wilder, completed bars |
| AIPO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.8 | PASS |  |  |
| AIPO | T6 | price vs 200-day average (S1 pattern sma values) | $22.63 vs $28.50 · -20.6% | $22.63 vs $28.50 · -20.6% | PASS |  |  |
| AIPO | T6w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T7 | price vs 50-day average (S1 pattern sma values) | $22.63 vs $26.56 · -14.8% | $22.63 vs $26.56 · -14.8% | PASS |  |  |
| AIPO | T7w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.9% over 30 td | +0.9% over 30 td | PASS |  |  |
| AIPO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AIPO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AIPO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.0% below $34.79 | 35.0% below $34.79 | PASS |  | closing high would be 34.77 |
| AIPO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.0% below | PASS |  |  |
| AIPO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $34.79 | $34.790000915527344 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AIPO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.26%, close location 0.50, OBV falling |
| AIPO | V2 | day change of the last completed bar | down 0.3% | -0.26% | PASS |  |  |
| AIPO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AIPO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.82× / 0.05× | 0.82× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AIPO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1311327) | 20 bars, last ('2026-11-17', 1311327) | PASS |  |  |
| ALAB | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $222.00 | $222.00 | PASS |  |  |
| ALAB | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $241.0 | $241.00 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ALAB | E3 | percent from the 21-day average | 7.9% below | 7.9% below | PASS |  |  |
| ALAB | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ALAB | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $23.67 | $23.67 (sr=23.6682) | PASS |  | Wilder ATR14 |
| ALAB | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| ALAB | L-ema21 | ladder row ema21: price and gap = price vs average | $241, -7.9% | $241.00, -7.9% | PASS |  |  |
| ALAB | L-note | "Last close $X · date" note = last completed bar | Last close $211.60 · Nov 17 | $211.60 · Nov 17 | PASS |  |  |
| ALAB | L-now | ladder price row = compared price; name = the basis label | $222 "After hours" | $222.00 "after hours" | PASS |  |  |
| ALAB | L-sma200 | ladder row sma200: price and gap = price vs average | $258.02, -14.0% | $258.02, -14.0% | PASS |  |  |
| ALAB | L-sma50 | ladder row sma50: price and gap = price vs average | $290.56, -23.6% | $290.56, -23.6% | PASS |  |  |
| ALAB | S5-price | S5: the same live price reads the same on the header and the Entry block | header $222.00 / entry $222.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ALAB | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ALAB | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.0 | 38.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ALAB | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.7% vs +11.2% | 49.7% vs 11.2% | PASS |  |  |
| ALAB | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ALAB | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.2 | 29.2 | PASS |  | Wilder, completed bars |
| ALAB | T4w | words "20 or more / below 20" | 20 or more | ADX 29.2 | PASS |  |  |
| ALAB | T5 | "counted at the last close ($X, date)" = last completed bar | $211.60, Nov 17 | $211.60, Nov 17 | PASS |  |  |
| ALAB | T6 | price vs 200-day average (S1 pattern sma values) | $211.60 vs $258.02 · -18.0% | $211.60 vs $258.02 · -18.0% | PASS |  |  |
| ALAB | T6w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T7 | price vs 50-day average (S1 pattern sma values) | $211.60 vs $290.56 · -27.2% | $211.60 vs $290.56 · -27.2% | PASS |  |  |
| ALAB | T7w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.0% over 30 td | +6.0% over 30 td | PASS |  |  |
| ALAB | T8r | word "rising" | still rising | rising | PASS |  |  |
| ALAB | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ALAB | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 57.6% below $499.48 | 57.6% below $499.48 | PASS |  | closing high would be 483.02 |
| ALAB | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 57.6% below | PASS |  |  |
| ALAB | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $499.48 | $499.47601318359375 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ALAB | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 4.58%, close location 0.98, OBV falling |
| ALAB | V2 | day change of the last completed bar | up 4.6% | +4.58% | PASS |  |  |
| ALAB | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.98 (raw 0.9798) | PASS |  |  |
| ALAB | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ALAB | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 0.41× | 1.11× / 0.41× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ALAB | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 5040994) | 20 bars, last ('2026-11-17', 5040994) | PASS |  |  |
| AMD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $525.65 | $525.65 | PASS |  |  |
| AMD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $523.46 | $523.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD | E3 | percent from the 21-day average | 0.4% above | 0.4% above | PASS |  |  |
| AMD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $40.57 | $40.57 (sr=40.5705) | PASS |  | Wilder ATR14 |
| AMD | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| AMD | L-ema21 | ladder row ema21: price and gap = price vs average | $523.46, 0.4% | $523.46, 0.4% | PASS |  |  |
| AMD | L-note | "Last close $X · date" note = last completed bar | Last close $503.41 · Nov 17 | $503.41 · Nov 17 | PASS |  |  |
| AMD | L-now | ladder price row = compared price; name = the basis label | $525.65 "After hours" | $525.65 "after hours" | PASS |  |  |
| AMD | L-sma200 | ladder row sma200: price and gap = price vs average | $425.74, 23.5% | $425.74, 23.5% | PASS |  |  |
| AMD | L-sma50 | ladder row sma50: price and gap = price vs average | $555.04, -5.3% | $555.04, -5.3% | PASS |  |  |
| AMD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $525.65 / entry $525.65 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| AMD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.27× / 0.02× | 1.27× / 0.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 34975206) | 20 bars, last ('2026-11-17', 34975206) | PASS |  |  |
| AMD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.95 | $12.95 | PASS |  |  |
| AMD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.47 | $13.47 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD.TO | E3 | percent from the 21-day average | 3.9% below | 3.9% below | PASS |  |  |
| AMD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AMD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.03 | $1.03 (sr=1.0253) | PASS |  | Wilder ATR14 |
| AMD.TO | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| AMD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $13.47, -3.9% | $13.47, -3.9% | PASS |  |  |
| AMD.TO | L-now | ladder price row = compared price; name = the basis label | $12.95 "Last close" | $12.95 "last close" | PASS |  |  |
| AMD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $11, 17.8% | $11.00, 17.8% | PASS |  |  |
| AMD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $14.26, -9.2% | $14.26, -9.2% | PASS |  |  |
| AMD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.5 | 46.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +104.3% vs +11.2% | 104.3% vs 11.2% | PASS |  |  |
| AMD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.9 | 18.9 | PASS |  | Wilder, completed bars |
| AMD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.9 | PASS |  |  |
| AMD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $12.95 vs $11.00 · +17.7% | $12.95 vs $11.00 · 17.8% | PASS |  |  |
| AMD.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| AMD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $12.95 vs $14.26 · -9.2% | $12.95 vs $14.26 · -9.2% | PASS |  |  |
| AMD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +12.2% over 30 td | +12.2% over 30 td | PASS |  |  |
| AMD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.7% below $16.97 | 23.7% below $16.97 | PASS |  | closing high would be 16.73 |
| AMD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.7% below | PASS |  |  |
| AMD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $16.97 | $16.968570709228516 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.15%, close location 0.72, OBV rising |
| AMD.TO | V2 | day change of the last completed bar | down 0.1% | -0.15% | PASS |  |  |
| AMD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AMD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.03× / 0.02× | 1.03× / 0.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2346685) | 20 bars, last ('2026-11-17', 2346685) | PASS |  |  |
| AMZN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $258.05 | $258.05 | PASS |  |  |
| AMZN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $258.94 | $258.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZN | E3 | percent from the 21-day average | 0.3% below | 0.3% below | PASS |  |  |
| AMZN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.91 | $8.91 (sr=8.9141) | PASS |  | Wilder ATR14 |
| AMZN | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves below |
| AMZN | L-ema21 | ladder row ema21: price and gap = price vs average | $258.94, -0.3% | $258.94, -0.3% | PASS |  |  |
| AMZN | L-note | "Last close $X · date" note = last completed bar | Last close $257.89 · Nov 17 | $257.89 · Nov 17 | PASS |  |  |
| AMZN | L-now | ladder price row = compared price; name = the basis label | $258.05 "After hours" | $258.05 "after hours" | PASS |  |  |
| AMZN | L-sma200 | ladder row sma200: price and gap = price vs average | $244.76, 5.4% | $244.76, 5.4% | PASS |  |  |
| AMZN | L-sma50 | ladder row sma50: price and gap = price vs average | $254.81, 1.3% | $254.81, 1.3% | PASS |  |  |
| AMZN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $258.05 / entry $258.05 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.8 | 49.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.7% vs +11.2% | 10.7% vs 11.2% | PASS |  |  |
| AMZN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZN | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.8 | 11.8 | PASS |  | Wilder, completed bars |
| AMZN | T4w | words "20 or more / below 20" | below 20 | ADX 11.8 | PASS |  |  |
| AMZN | T5 | "counted at the last close ($X, date)" = last completed bar | $257.89, Nov 17 | $257.89, Nov 17 | PASS |  |  |
| AMZN | T6 | price vs 200-day average (S1 pattern sma values) | $257.89 vs $244.76 · +5.4% | $257.89 vs $244.76 · 5.4% | PASS |  |  |
| AMZN | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T7 | price vs 50-day average (S1 pattern sma values) | $257.89 vs $254.81 · +1.2% | $257.89 vs $254.81 · 1.2% | PASS |  |  |
| AMZN | T7w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| AMZN | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMZN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.2% below $287.20 | 10.2% below $287.20 | PASS |  | closing high would be 284.02 |
| AMZN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.2% below | PASS |  |  |
| AMZN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $287.20 | $287.20001220703125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change 0.05%, close location 0.66, OBV falling |
| AMZN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.89× / 0.01× | 0.89× / 0.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 37098176) | 20 bars, last ('2026-11-17', 37098176) | PASS |  |  |
| AMZU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $36.00 | $36.00 | PASS |  |  |
| AMZU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $35.94 | $35.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZU | E3 | percent from the 21-day average | 0.2% above | 0.2% above | PASS |  |  |
| AMZU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.45 | $2.44 (sr=2.4458) | PASS |  | Wilder ATR14 |
| AMZU | E5 | distance in normal day-moves | 0.0 | 0.0 | PASS |  | gauge dot note uses the same number:  · 0.0 day-moves above |
| AMZU | L-ema21 | ladder row ema21: price and gap = price vs average | $35.94, 0.2% | $35.94, 0.2% | PASS |  |  |
| AMZU | L-note | "Last close $X · date" note = last completed bar | Last close $35.25 · Nov 17 | $35.25 · Nov 17 | PASS |  |  |
| AMZU | L-now | ladder price row = compared price; name = the basis label | $36 "After hours" | $36.00 "after hours" | PASS |  |  |
| AMZU | L-sma200 | ladder row sma200: price and gap = price vs average | $34.92, 3.1% | $34.92, 3.1% | PASS |  |  |
| AMZU | L-sma50 | ladder row sma50: price and gap = price vs average | $35.26, 2.1% | $35.26, 2.1% | PASS |  |  |
| AMZU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $36.00 / entry $36.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.1 | 48.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.1% vs +11.2% | -1.1% vs 11.2% | PASS |  |  |
| AMZU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZU | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.9 | 11.9 | PASS |  | Wilder, completed bars |
| AMZU | T4w | words "20 or more / below 20" | below 20 | ADX 11.9 | PASS |  |  |
| AMZU | T5 | "counted at the last close ($X, date)" = last completed bar | $35.25, Nov 17 | $35.25, Nov 17 | PASS |  |  |
| AMZU | T6 | price vs 200-day average (S1 pattern sma values) | $35.25 vs $34.92 · +0.9% | $35.25 vs $34.92 · 0.9% | PASS |  |  |
| AMZU | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZU | T7 | price vs 50-day average (S1 pattern sma values) | $35.25 vs $35.26 · -0.0% | $35.25 vs $35.26 · -0.0% | PASS |  |  |
| AMZU | T7w | word "Below" | Below | Below | PASS |  |  |
| AMZU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.1% over 30 td | -0.1% over 30 td | PASS |  |  |
| AMZU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AMZU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 24.4% below $46.64 | 24.4% below $46.64 | PASS |  | closing high would be 45.45 |
| AMZU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 24.4% below | PASS |  |  |
| AMZU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.64 | $46.64482080439608 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -0.06%, close location 0.62, OBV falling |
| AMZU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.45× / 0.01× | 0.45× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 869728) | 20 bars, last ('2026-11-17', 869728) | PASS |  |  |
| ANET.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $33.32 | $33.32 | PASS |  |  |
| ANET.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.29 | $33.29 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ANET.TO | E3 | percent from the 21-day average | 0.1% above | 0.1% above | PASS |  |  |
| ANET.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ANET.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.99 | $1.99 (sr=1.9896) | PASS |  | Wilder ATR14 |
| ANET.TO | E5 | distance in normal day-moves | 0.0 | 0.0 | PASS |  | gauge dot note uses the same number:  · 0.0 day-moves above |
| ANET.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $33.29, 0.1% | $33.29, 0.1% | PASS |  |  |
| ANET.TO | L-now | ladder price row = compared price; name = the basis label | $33.32 "Last close" | $33.32 "last close" | PASS |  |  |
| ANET.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $30.13, 10.6% | $30.13, 10.6% | PASS |  |  |
| ANET.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $34.42, -3.2% | $34.42, -3.2% | PASS |  |  |
| ANET.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.8 | 49.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ANET.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.8% vs +11.2% | 39.8% vs 11.2% | PASS |  |  |
| ANET.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.2 | 18.2 | PASS |  | Wilder, completed bars |
| ANET.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.2 | PASS |  |  |
| ANET.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.27%, close location 0.41, OBV rising |
| ANET.TO | V2 | day change of the last completed bar | down 0.3% | -0.27% | PASS |  |  |
| ANET.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ANET.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.72× / 0.05× | 0.72× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ANET.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 33639) | 20 bars, last ('2026-11-17', 33639) | PASS |  |  |
| ASML.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $40.80 | $40.80 | PASS |  |  |
| ASML.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $44.56 | $44.56 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASML.TO | E3 | percent from the 21-day average | 8.4% below | 8.4% below | PASS |  |  |
| ASML.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ASML.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.97 | $1.97 (sr=1.9727) | PASS |  | Wilder ATR14 |
| ASML.TO | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| ASML.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $44.56, -8.4% | $44.56, -8.4% | PASS |  |  |
| ASML.TO | L-now | ladder price row = compared price; name = the basis label | $40.8 "Last close" | $40.80 "last close" | PASS |  |  |
| ASML.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $45.07, -9.5% | $45.07, -9.5% | PASS |  |  |
| ASML.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $47.35, -13.8% | $47.35, -13.8% | PASS |  |  |
| ASML.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASML.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.3 | 37.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASML.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.4% vs +11.2% | 43.4% vs 11.2% | PASS |  |  |
| ASML.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASML.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.0 | 26.0 | PASS |  | Wilder, completed bars |
| ASML.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.0 | PASS |  |  |
| ASML.TO | T6 | price vs 200-day average (S1 pattern sma values) | $40.80 vs $45.07 · -9.5% | $40.80 vs $45.07 · -9.5% | PASS |  |  |
| ASML.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T7 | price vs 50-day average (S1 pattern sma values) | $40.80 vs $47.35 · -13.8% | $40.80 vs $47.35 · -13.8% | PASS |  |  |
| ASML.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.2% over 30 td | +4.2% over 30 td | PASS |  |  |
| ASML.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASML.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASML.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 28.1% below $56.75 | 28.1% below $56.75 | PASS |  | closing high would be 56.67 |
| ASML.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 28.1% below | PASS |  |  |
| ASML.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $56.75 | $56.745395859548175 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASML.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.97%, close location 0.28, OBV falling |
| ASML.TO | V2 | day change of the last completed bar | down 2.0% | -1.97% | PASS |  |  |
| ASML.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASML.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.03× / 0.41× | 1.03× / 0.41× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASML.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 46038) | 20 bars, last ('2026-11-17', 46038) | PASS |  |  |
| ASTL.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $7.25 | $7.25 | PASS |  |  |
| ASTL.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $7.27 | $7.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASTL.TO | E3 | percent from the 21-day average | 0.2% below | 0.2% below | PASS |  |  |
| ASTL.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ASTL.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.43 | $0.43 (sr=0.4265) | PASS |  | Wilder ATR14 |
| ASTL.TO | E5 | distance in normal day-moves | 0.0 | 0.0 | PASS |  | gauge dot note uses the same number:  · 0.0 day-moves below |
| ASTL.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $7.27, -0.2% | $7.27, -0.2% | PASS |  |  |
| ASTL.TO | L-note | "Last close $X · date" note = last completed bar | Last close $7.25 · Nov 17 | $7.25 · Nov 17 | PASS |  |  |
| ASTL.TO | L-now | ladder price row = compared price; name = the basis label | $7.25 "After hours" | $7.25 "after hours" | PASS |  |  |
| ASTL.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $6.26, 15.8% | $6.26, 15.8% | PASS |  |  |
| ASTL.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $6.5, 11.5% | $6.50, 11.5% | PASS |  |  |
| ASTL.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $7.25 / entry $7.25 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ASTL.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASTL.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 52.2 | 52.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASTL.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +47.7% vs +11.2% | 47.7% vs 11.2% | PASS |  |  |
| ASTL.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASTL.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.7 | PASS |  |  |
| ASTL.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $7.25, Nov 17 | $7.25, Nov 17 | PASS |  |  |
| ASTL.TO | T6 | price vs 200-day average (S1 pattern sma values) | $7.25 vs $6.26 · +15.8% | $7.25 vs $6.26 · 15.8% | PASS |  |  |
| ASTL.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| ASTL.TO | T7 | price vs 50-day average (S1 pattern sma values) | $7.25 vs $6.50 · +11.5% | $7.25 vs $6.50 · 11.5% | PASS |  |  |
| ASTL.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| ASTL.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.2% over 30 td | PASS |  |  |
| ASTL.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASTL.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASTL.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.8% below $8.31 | 12.8% below $8.31 | PASS |  | closing high would be 8.22 |
| ASTL.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.8% below | PASS |  |  |
| ASTL.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $8.31 | $8.3100004196167 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASTL.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.48%, close location 0.04, OBV falling |
| ASTL.TO | V2 | day change of the last completed bar | down 5.5% | -5.48% | PASS |  |  |
| ASTL.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0377) | PASS |  |  |
| ASTL.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASTL.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.33× / 0.93× | 1.33× / 0.93× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASTL.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 794491) | 20 bars, last ('2026-11-17', 794491) | PASS |  |  |
| ATD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $83.65 | $83.65 | PASS |  |  |
| ATD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $82.48 | $82.48 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ATD.TO | E3 | percent from the 21-day average | 1.4% above | 1.4% above | PASS |  |  |
| ATD.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ATD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.67 | $1.67 (sr=1.6748) | PASS |  | Wilder ATR14 |
| ATD.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves above |
| ATD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $82.48, 1.4% | $82.48, 1.4% | PASS |  |  |
| ATD.TO | L-note | "Last close $X · date" note = last completed bar | Last close $83.65 · Nov 17 | $83.65 · Nov 17 | PASS |  |  |
| ATD.TO | L-now | ladder price row = compared price; name = the basis label | $83.65 "After hours" | $83.65 "after hours" | PASS |  |  |
| ATD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $82.38, 1.5% | $82.38, 1.5% | PASS |  |  |
| ATD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $80.75, 3.6% | $80.75, 3.6% | PASS |  |  |
| ATD.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $83.65 / entry $83.65 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ATD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ATD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.4 | 56.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ATD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.7% vs +11.2% | 20.7% vs 11.2% | PASS |  |  |
| ATD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ATD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.2 | 16.2 | PASS |  | Wilder, completed bars |
| ATD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 16.2 | PASS |  |  |
| ATD.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $83.65, Nov 17 | $83.65, Nov 17 | PASS |  |  |
| ATD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $83.65 vs $82.38 · +1.5% | $83.65 vs $82.38 · 1.5% | PASS |  |  |
| ATD.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| ATD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $83.65 vs $80.75 · +3.6% | $83.65 vs $80.75 · 3.6% | PASS |  |  |
| ATD.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| ATD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| ATD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ATD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ATD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.6% below $94.68 | 11.6% below $94.68 | PASS |  | closing high would be 93.29 |
| ATD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.6% below | PASS |  |  |
| ATD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $94.68 | $94.67525459795411 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ATD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.30%, close location 0.40, OBV rising |
| ATD.TO | V2 | day change of the last completed bar | down 0.3% | -0.30% | PASS |  |  |
| ATD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ATD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.34× / 0.15× | 1.34× / 0.15× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ATD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1761389) | 20 bars, last ('2026-11-17', 1761389) | PASS |  |  |
| AVGC | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $18.20 | $18.20 | PASS |  |  |
| AVGC | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.25 | $18.25 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGC | E3 | percent from the 21-day average | 0.3% below | 0.3% below | PASS |  |  |
| AVGC | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AVGC | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.66 | $1.66 (sr=1.6599) | PASS |  | Wilder ATR14 |
| AVGC | E5 | distance in normal day-moves | 0.0 | 0.0 | PASS |  | gauge dot note uses the same number:  · 0.0 day-moves below |
| AVGC | L-ema21 | ladder row ema21: price and gap = price vs average | $18.25, -0.3% | $18.25, -0.3% | PASS |  |  |
| AVGC | L-now | ladder price row = compared price; name = the basis label | $18.2 "Last close" | $18.20 "last close" | PASS |  |  |
| AVGC | L-sma50 | ladder row sma50: price and gap = price vs average | $19.7, -7.6% | $19.70, -7.6% | PASS |  |  |
| AVGC | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.0 | 49.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGC | T4w | words "20 or more / below 20" | 20 or more | ADX 21.3 | PASS |  |  |
| AVGC | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 4.12%, close location 1.00, OBV falling |
| AVGC | V2 | day change of the last completed bar | up 4.1% | +4.12% | PASS |  |  |
| AVGC | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 1.00 (raw 1.0000) | PASS |  |  |
| AVGC | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AVGC | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.41× / 0.45× | 0.41× / 0.45× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGC | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1249) | 20 bars, last ('2026-11-17', 1249) | PASS |  |  |
| AVGO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $347.00 | $347.00 | PASS |  |  |
| AVGO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $335.83 | $335.83 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO | E3 | percent from the 21-day average | 3.3% above | 3.3% above | PASS |  |  |
| AVGO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AVGO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.48 | $17.48 (sr=17.4829) | PASS |  | Wilder ATR14 |
| AVGO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| AVGO | L-ema21 | ladder row ema21: price and gap = price vs average | $335.83, 3.3% | $335.83, 3.3% | PASS |  |  |
| AVGO | L-note | "Last close $X · date" note = last completed bar | Last close $341.60 · Nov 17 | $341.60 · Nov 17 | PASS |  |  |
| AVGO | L-now | ladder price row = compared price; name = the basis label | $347 "After hours" | $347.00 "after hours" | PASS |  |  |
| AVGO | L-sma200 | ladder row sma200: price and gap = price vs average | $366.56, -5.3% | $366.56, -5.3% | PASS |  |  |
| AVGO | L-sma50 | ladder row sma50: price and gap = price vs average | $344.25, 0.8% | $344.25, 0.8% | PASS |  |  |
| AVGO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $347.00 / entry $347.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AVGO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AVGO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.4 | 51.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.4% vs +11.2% | 0.4% vs 11.2% | PASS |  |  |
| AVGO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.7 | 20.7 | PASS |  | Wilder, completed bars |
| AVGO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.7 | PASS |  |  |
| AVGO | T5 | "counted at the last close ($X, date)" = last completed bar | $341.60, Nov 17 | $341.60, Nov 17 | PASS |  |  |
| AVGO | T6 | price vs 200-day average (S1 pattern sma values) | $341.60 vs $366.56 · -6.8% | $341.60 vs $366.56 · -6.8% | PASS |  |  |
| AVGO | T6w | word "Below" | Below | Below | PASS |  |  |
| AVGO | T7 | price vs 50-day average (S1 pattern sma values) | $341.60 vs $344.25 · -0.8% | $341.60 vs $344.25 · -0.8% | PASS |  |  |
| AVGO | T7w | word "Below" | Below | Below | PASS |  |  |
| AVGO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.0% over 30 td | -0.0% over 30 td | PASS |  |  |
| AVGO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AVGO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AVGO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.8% below $493.32 | 30.8% below $493.32 | PASS |  | closing high would be 479.94 |
| AVGO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.8% below | PASS |  |  |
| AVGO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $493.32 | $493.3195088404053 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AVGO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 2.46%, close location 0.99, OBV rising |
| AVGO | V2 | day change of the last completed bar | up 2.5% | +2.46% | PASS |  |  |
| AVGO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.99 (raw 0.9879) | PASS |  |  |
| AVGO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.48× | 1.02× / 0.48× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 25732265) | 20 bars, last ('2026-11-17', 25732265) | PASS |  |  |
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
| AVGO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.8% vs +11.2% | -1.8% vs 11.2% | PASS |  |  |
| AVGO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.0 | 21.0 | PASS |  | Wilder, completed bars |
| AVGO.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 21.0 | PASS |  |  |
| AVGO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 2.37%, close location 1.00, OBV rising |
| AVGO.TO | V2 | day change of the last completed bar | up 2.4% | +2.37% | PASS |  |  |
| AVGO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 1.00 (raw 1.0000) | PASS |  |  |
| AVGO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.87× / 0.47× | 0.87× / 0.47× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 993758) | 20 bars, last ('2026-11-17', 993758) | PASS |  |  |
| BDT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $71.13 | $71.13 | PASS |  |  |
| BDT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.98 | $73.98 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BDT.TO | E3 | percent from the 21-day average | 3.9% below | 3.9% below | PASS |  |  |
| BDT.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BDT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.10 | $4.10 (sr=4.1013) | PASS |  | Wilder ATR14 |
| BDT.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| BDT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $73.98, -3.9% | $73.98, -3.9% | PASS |  |  |
| BDT.TO | L-note | "Last close $X · date" note = last completed bar | Last close $71.13 · Nov 17 | $71.13 · Nov 17 | PASS |  |  |
| BDT.TO | L-now | ladder price row = compared price; name = the basis label | $71.13 "After hours" | $71.13 "after hours" | PASS |  |  |
| BDT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.56, 21.5% | $58.56, 21.5% | PASS |  |  |
| BDT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $76.15, -6.6% | $76.15, -6.6% | PASS |  |  |
| BDT.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $71.13 / entry $71.13 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BDT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BDT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.6 | 44.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BDT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +190.8% vs +11.2% | 190.8% vs 11.2% | PASS |  |  |
| BDT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BDT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.1 | 15.1 | PASS |  | Wilder, completed bars |
| BDT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.1 | PASS |  |  |
| BDT.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $71.13, Nov 17 | $71.13, Nov 17 | PASS |  |  |
| BDT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $71.13 vs $58.56 · +21.5% | $71.13 vs $58.56 · 21.5% | PASS |  |  |
| BDT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| BDT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $71.13 vs $76.15 · -6.6% | $71.13 vs $76.15 · -6.6% | PASS |  |  |
| BDT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| BDT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +13.2% over 30 td | +13.2% over 30 td | PASS |  |  |
| BDT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| BDT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BDT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.7% below $86.42 | 17.7% below $86.42 | PASS |  | closing high would be 85.33 |
| BDT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.7% below | PASS |  |  |
| BDT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $86.42 | $86.42048390957993 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BDT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -5.39%, close location 0.69, OBV falling |
| BDT.TO | V2 | day change of the last completed bar | down 5.4% | -5.39% | PASS |  |  |
| BDT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BDT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.30× / 0.93× | 2.30× / 0.93× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BDT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 947723) | 20 bars, last ('2026-11-17', 947723) | PASS |  |  |
| BDT.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.30, OBV falling | condition true | PASS |  |  |
| BOTZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.00 | $30.00 | PASS |  |  |
| BOTZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.07 | $32.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BOTZ | E3 | percent from the 21-day average | 6.5% below | 6.5% below | PASS |  |  |
| BOTZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BOTZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.79 | $0.79 (sr=0.7941) | PASS |  | Wilder ATR14 |
| BOTZ | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| BOTZ | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.2 | +5.2 | PASS |  |  |
| BOTZ | L-ema21 | ladder row ema21: price and gap = price vs average | $32.07, -6.5% | $32.07, -6.5% | PASS |  |  |
| BOTZ | L-note | "Last close $X · date" note = last completed bar | Last close $29.71 · Nov 17 | $29.71 · Nov 17 | PASS |  |  |
| BOTZ | L-now | ladder price row = compared price; name = the basis label | $30 "After hours" | $30.00 "after hours" | PASS |  |  |
| BOTZ | L-sma200 | ladder row sma200: price and gap = price vs average | $36.2, -17.1% | $36.20, -17.1% | PASS |  |  |
| BOTZ | L-sma50 | ladder row sma50: price and gap = price vs average | $33.86, -11.4% | $33.86, -11.4% | PASS |  |  |
| BOTZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $30.00 / entry $30.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BOTZ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BOTZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.4 | 31.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BOTZ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -13.0% vs +11.2% | -13.0% vs 11.2% | PASS |  |  |
| BOTZ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BOTZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.6 | 33.5 | PASS |  | Wilder, completed bars |
| BOTZ | T4w | words "20 or more / below 20" | 20 or more | ADX 33.5 | PASS |  |  |
| BOTZ | T5 | "counted at the last close ($X, date)" = last completed bar | $29.71, Nov 17 | $29.71, Nov 17 | PASS |  |  |
| BOTZ | T6 | price vs 200-day average (S1 pattern sma values) | $29.71 vs $36.20 · -17.9% | $29.71 vs $36.20 · -17.9% | PASS |  |  |
| BOTZ | T6w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T7 | price vs 50-day average (S1 pattern sma values) | $29.71 vs $33.86 · -12.3% | $29.71 vs $33.86 · -12.3% | PASS |  |  |
| BOTZ | T7w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.8% over 30 td | -1.8% over 30 td | PASS |  |  |
| BOTZ | T8r | word "rising" | not rising | not rising | PASS |  |  |
| BOTZ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BOTZ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 28.7% below $41.69 | 28.7% below $41.69 | PASS |  | closing high would be 41.61 |
| BOTZ | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 28.7% below | PASS |  |  |
| BOTZ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $41.69 | $41.689149923077814 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BOTZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.36%, close location 0.57, OBV falling |
| BOTZ | V2 | day change of the last completed bar | down 1.4% | -1.36% | PASS |  |  |
| BOTZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BOTZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.21× / 0.51× | 2.21× / 0.51× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BOTZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1592041) | 20 bars, last ('2026-11-17', 1592041) | PASS |  |  |
| BOTZ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.21, OBV falling | condition true | PASS |  |  |
| BRK-B | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $585.12 | $585.12 | PASS |  |  |
| BRK-B | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $565.84 | $565.84 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRK-B | E3 | percent from the 21-day average | 3.4% above | 3.4% above | PASS |  |  |
| BRK-B | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRK-B | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.33 | $9.33 (sr=9.3286) | PASS |  | Wilder ATR14 |
| BRK-B | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves above |
| BRK-B | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -6.9 | -6.9 | PASS |  |  |
| BRK-B | L-ema21 | ladder row ema21: price and gap = price vs average | $565.84, 3.4% | $565.84, 3.4% | PASS |  |  |
| BRK-B | L-note | "Last close $X · date" note = last completed bar | Last close $586.76 · Nov 17 | $586.76 · Nov 17 | PASS |  |  |
| BRK-B | L-now | ladder price row = compared price; name = the basis label | $585.12 "After hours" | $585.12 "after hours" | PASS |  |  |
| BRK-B | L-sma200 | ladder row sma200: price and gap = price vs average | $501.49, 16.7% | $501.49, 16.7% | PASS |  |  |
| BRK-B | L-sma50 | ladder row sma50: price and gap = price vs average | $533.01, 9.8% | $533.01, 9.8% | PASS |  |  |
| BRK-B | S5-price | S5: the same live price reads the same on the header and the Entry block | header $585.12 / entry $585.12 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRK-B | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRK-B | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 73.1 | 73.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRK-B | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +16.6% vs +11.2% | 16.6% vs 11.2% | PASS |  |  |
| BRK-B | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRK-B | T4 | ADX 14 (S1 /api/sr meta.adx) | 54.2 | 54.2 | PASS |  | Wilder, completed bars |
| BRK-B | T4w | words "20 or more / below 20" | 20 or more | ADX 54.2 | PASS |  |  |
| BRK-B | T5 | "counted at the last close ($X, date)" = last completed bar | $586.76, Nov 17 | $586.76, Nov 17 | PASS |  |  |
| BRK-B | T6 | price vs 200-day average (S1 pattern sma values) | $586.76 vs $501.49 · +17.0% | $586.76 vs $501.49 · 17.0% | PASS |  |  |
| BRK-B | T6w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T7 | price vs 50-day average (S1 pattern sma values) | $586.76 vs $533.01 · +10.1% | $586.76 vs $533.01 · 10.1% | PASS |  |  |
| BRK-B | T7w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| BRK-B | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRK-B | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRK-B | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.7% below $596.92 | 1.7% below $596.92 | PASS |  | closing high would be 592.94 |
| BRK-B | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.7% below | PASS |  |  |
| BRK-B | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $596.92 | $596.9199829101562 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRK-B | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.03%, close location 0.12, OBV rising |
| BRK-B | V2 | day change of the last completed bar | down 1.0% | -1.03% | PASS |  |  |
| BRK-B | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1206) | PASS |  |  |
| BRK-B | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| BRK-B | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.06× / 0.65× | 1.06× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRK-B | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 5073791) | 20 bars, last ('2026-11-17', 5073791) | PASS |  |  |
| BRKU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.00 | $30.00 | PASS |  |  |
| BRKU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.22 | $28.22 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRKU | E3 | percent from the 21-day average | 6.3% above | 6.3% above | PASS |  |  |
| BRKU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRKU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.88 | $0.87 (sr=0.875) | PASS |  | Wilder ATR14 |
| BRKU | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves above |
| BRKU | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.9 | -5.9 | PASS |  |  |
| BRKU | L-ema21 | ladder row ema21: price and gap = price vs average | $28.22, 6.3% | $28.22, 6.3% | PASS |  |  |
| BRKU | L-note | "Last close $X · date" note = last completed bar | Last close $30.19 · Nov 17 | $30.19 · Nov 17 | PASS |  |  |
| BRKU | L-now | ladder price row = compared price; name = the basis label | $30 "After hours" | $30.00 "after hours" | PASS |  |  |
| BRKU | L-sma200 | ladder row sma200: price and gap = price vs average | $23.03, 30.3% | $23.03, 30.3% | PASS |  |  |
| BRKU | L-sma50 | ladder row sma50: price and gap = price vs average | $25.23, 18.9% | $25.23, 18.9% | PASS |  |  |
| BRKU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $30.00 / entry $30.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRKU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRKU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 72.5 | 72.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRKU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +21.4% vs +11.2% | 21.4% vs 11.2% | PASS |  |  |
| BRKU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRKU | T4 | ADX 14 (S1 /api/sr meta.adx) | 53.2 | 53.2 | PASS |  | Wilder, completed bars |
| BRKU | T4w | words "20 or more / below 20" | 20 or more | ADX 53.2 | PASS |  |  |
| BRKU | T5 | "counted at the last close ($X, date)" = last completed bar | $30.19, Nov 17 | $30.19, Nov 17 | PASS |  |  |
| BRKU | T6 | price vs 200-day average (S1 pattern sma values) | $30.19 vs $23.03 · +31.1% | $30.19 vs $23.03 · 31.1% | PASS |  |  |
| BRKU | T6w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T7 | price vs 50-day average (S1 pattern sma values) | $30.19 vs $25.23 · +19.7% | $30.19 vs $25.23 · 19.7% | PASS |  |  |
| BRKU | T7w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.2% over 30 td | PASS |  |  |
| BRKU | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRKU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRKU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.2% below $31.20 | 3.2% below $31.20 | PASS |  | closing high would be 30.81 |
| BRKU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.2% below | PASS |  |  |
| BRKU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.20 | $31.200000762939453 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRKU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.01%, close location 0.25, OBV rising |
| BRKU | V2 | day change of the last completed bar | down 2.0% | -2.01% | PASS |  |  |
| BRKU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.25 (raw 0.2456) | PASS |  |  |
| BRKU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| BRKU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.18× / 0.69× | 2.18× / 0.69× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRKU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 200276) | 20 bars, last ('2026-11-17', 200276) | PASS |  |  |
| CAMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $94.96 | $94.96 | PASS |  |  |
| CAMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $111.04 | $111.04 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAMT | E3 | percent from the 21-day average | 14.5% below | 14.5% below | PASS |  |  |
| CAMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CAMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.13 | $8.13 (sr=8.1264) | PASS |  | Wilder ATR14 |
| CAMT | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| CAMT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.4 | +5.4 | PASS |  |  |
| CAMT | L-ema21 | ladder row ema21: price and gap = price vs average | $111.04, -14.5% | $111.04, -14.5% | PASS |  |  |
| CAMT | L-note | "Last close $X · date" note = last completed bar | Last close $94.96 · Nov 17 | $94.96 · Nov 17 | PASS |  |  |
| CAMT | L-now | ladder price row = compared price; name = the basis label | $94.96 "After hours" | $94.96 "after hours" | PASS |  |  |
| CAMT | L-sma200 | ladder row sma200: price and gap = price vs average | $154.86, -38.7% | $154.86, -38.7% | PASS |  |  |
| CAMT | L-sma50 | ladder row sma50: price and gap = price vs average | $131.72, -27.9% | $131.72, -27.9% | PASS |  |  |
| CAMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $94.96 / entry $94.96 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.5 | 34.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.0% vs +11.2% | -1.0% vs 11.2% | PASS |  |  |
| CAMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.4 | 34.4 | PASS |  | Wilder, completed bars |
| CAMT | T4w | words "20 or more / below 20" | 20 or more | ADX 34.4 | PASS |  |  |
| CAMT | T5 | "counted at the last close ($X, date)" = last completed bar | $94.96, Nov 17 | $94.96, Nov 17 | PASS |  |  |
| CAMT | T6 | price vs 200-day average (S1 pattern sma values) | $94.96 vs $154.86 · -38.7% | $94.96 vs $154.86 · -38.7% | PASS |  |  |
| CAMT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T7 | price vs 50-day average (S1 pattern sma values) | $94.96 vs $131.72 · -27.9% | $94.96 vs $131.72 · -27.9% | PASS |  |  |
| CAMT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.9% over 30 td | -0.9% over 30 td | PASS |  |  |
| CAMT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CAMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 56.0% below $215.99 | 56.0% below $215.99 | PASS |  | closing high would be 207.46 |
| CAMT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 56.0% below | PASS |  |  |
| CAMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $215.99 | $215.99001 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 1.83%, close location 0.84, OBV falling |
| CAMT | V2 | day change of the last completed bar | up 1.8% | +1.83% | PASS |  |  |
| CAMT | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.84 (raw 0.8374) | PASS |  |  |
| CAMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.64× / 0.21× | 0.64× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 327729) | 20 bars, last ('2026-11-17', 327729) | PASS |  |  |
| CARS.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $19.88 | $19.88 | PASS |  |  |
| CARS.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $21.81 | $21.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CARS.TO | E3 | percent from the 21-day average | 8.9% below | 8.9% below | PASS |  |  |
| CARS.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CARS.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.51 | $0.51 (sr=0.5064) | PASS |  | Wilder ATR14 |
| CARS.TO | E5 | distance in normal day-moves | 3.8 | 3.8 | PASS |  | gauge dot note uses the same number:  · 3.8 day-moves below |
| CARS.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.9 | +3.9 | PASS |  |  |
| CARS.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.2 | +12.2 | PASS |  |  |
| CARS.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $21.81, -8.9% | $21.81, -8.9% | PASS |  |  |
| CARS.TO | L-now | ladder price row = compared price; name = the basis label | $19.88 "Last close" | $19.88 "last close" | PASS |  |  |
| CARS.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $27.97, -28.9% | $27.97, -28.9% | PASS |  |  |
| CARS.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $23.8, -16.5% | $23.80, -16.5% | PASS |  |  |
| CARS.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CARS.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.0 | 31.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CARS.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -23.1% vs +11.2% | -23.2% vs 11.2% | PASS |  |  |
| CARS.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CARS.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.4 | 28.5 | PASS |  | Wilder, completed bars |
| CARS.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.5 | PASS |  |  |
| CARS.TO | T6 | price vs 200-day average (S1 pattern sma values) | $19.88 vs $27.97 · -28.9% | $19.88 vs $27.97 · -28.9% | PASS |  |  |
| CARS.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T7 | price vs 50-day average (S1 pattern sma values) | $19.88 vs $23.80 · -16.5% | $19.88 vs $23.80 · -16.5% | PASS |  |  |
| CARS.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.4% over 30 td | -2.4% over 30 td | PASS |  |  |
| CARS.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CARS.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CARS.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 47.9% below $38.16 | 47.9% below $38.16 | PASS |  | closing high would be 38.16 |
| CARS.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 47.9% below | PASS |  |  |
| CARS.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.16 | $38.15896987915039 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CARS.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 11 of 50 days empty | 11 of 50 days empty | PASS |  |  |
| CAT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $570.79 | $570.79 | PASS |  |  |
| CAT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $632.49 | $632.49 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAT | E3 | percent from the 21-day average | 9.8% below | 9.8% below | PASS |  |  |
| CAT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CAT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $28.45 | $28.45 (sr=28.448) | PASS |  | Wilder ATR14 |
| CAT | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| CAT | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.4 | +3.4 | PASS |  |  |
| CAT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.0 | +6.0 | PASS |  |  |
| CAT | L-ema21 | ladder row ema21: price and gap = price vs average | $632.49, -9.8% | $632.49, -9.8% | PASS |  |  |
| CAT | L-note | "Last close $X · date" note = last completed bar | Last close $570.79 · Nov 17 | $570.79 · Nov 17 | PASS |  |  |
| CAT | L-now | ladder price row = compared price; name = the basis label | $570.79 "After hours" | $570.79 "after hours" | PASS |  |  |
| CAT | L-sma200 | ladder row sma200: price and gap = price vs average | $803.37, -29.0% | $803.37, -29.0% | PASS |  |  |
| CAT | L-sma50 | ladder row sma50: price and gap = price vs average | $729.63, -21.8% | $729.63, -21.8% | PASS |  |  |
| CAT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $570.79 / entry $570.79 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.5 | 31.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.3% vs +11.2% | 4.3% vs 11.2% | PASS |  |  |
| CAT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAT | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.9 | 38.9 | PASS |  | Wilder, completed bars |
| CAT | T4w | words "20 or more / below 20" | 20 or more | ADX 38.9 | PASS |  |  |
| CAT | T5 | "counted at the last close ($X, date)" = last completed bar | $570.79, Nov 17 | $570.79, Nov 17 | PASS |  |  |
| CAT | T6 | price vs 200-day average (S1 pattern sma values) | $570.79 vs $803.37 · -29.0% | $570.79 vs $803.37 · -29.0% | PASS |  |  |
| CAT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAT | T7 | price vs 50-day average (S1 pattern sma values) | $570.79 vs $729.63 · -21.8% | $570.79 vs $729.63 · -21.8% | PASS |  |  |
| CAT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.1% over 30 td | +1.1% over 30 td | PASS |  |  |
| CAT | T8r | word "rising" | still rising | rising | PASS |  |  |
| CAT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 46.6% below $1,068.93 | 46.6% below $1068.93 | PASS |  | closing high would be 1060.41 |
| CAT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 46.6% below | PASS |  |  |
| CAT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,068.93 | $1068.930064424787 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change 0.05%, close location 0.43, OBV falling |
| CAT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 0.01× | 0.97× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2958138) | 20 bars, last ('2026-11-17', 2958138) | PASS |  |  |
| CCO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $92.16 | $92.16 | PASS |  |  |
| CCO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $105.49 | $105.49 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CCO.TO | E3 | percent from the 21-day average | 12.6% below | 12.6% below | PASS |  |  |
| CCO.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CCO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.00 | $5.00 (sr=5.0045) | PASS |  | Wilder ATR14 |
| CCO.TO | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| CCO.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.1 | +7.1 | PASS |  |  |
| CCO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $105.49, -12.6% | $105.49, -12.6% | PASS |  |  |
| CCO.TO | L-note | "Last close $X · date" note = last completed bar | Last close $92.16 · Nov 17 | $92.16 · Nov 17 | PASS |  |  |
| CCO.TO | L-now | ladder price row = compared price; name = the basis label | $92.16 "After hours" | $92.16 "after hours" | PASS |  |  |
| CCO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $140.89, -34.6% | $140.89, -34.6% | PASS |  |  |
| CCO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $117.76, -21.7% | $117.76, -21.7% | PASS |  |  |
| CCO.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $92.16 / entry $92.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CCO.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CCO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.2 | 31.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CCO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -20.8% vs +11.2% | -20.8% vs 11.2% | PASS |  |  |
| CCO.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CCO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.3 | 29.3 | PASS |  | Wilder, completed bars |
| CCO.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 29.3 | PASS |  |  |
| CCO.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $92.16, Nov 17 | $92.16, Nov 17 | PASS |  |  |
| CCO.TO | T6 | price vs 200-day average (S1 pattern sma values) | $92.16 vs $140.89 · -34.6% | $92.16 vs $140.89 · -34.6% | PASS |  |  |
| CCO.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T7 | price vs 50-day average (S1 pattern sma values) | $92.16 vs $117.76 · -21.7% | $92.16 vs $117.76 · -21.7% | PASS |  |  |
| CCO.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.9% over 30 td | -3.9% over 30 td | PASS |  |  |
| CCO.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CCO.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CCO.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.6% below $182.72 | 49.6% below $182.72 | PASS |  | closing high would be 181.66 |
| CCO.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.6% below | PASS |  |  |
| CCO.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $182.72 | $182.72000122070312 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CCO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.37%, close location 0.11, OBV falling |
| CCO.TO | V2 | day change of the last completed bar | down 2.4% | -2.37% | PASS |  |  |
| CCO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1124) | PASS |  |  |
| CCO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CCO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.41× / 0.44× | 1.41× / 0.44× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CCO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1741636) | 20 bars, last ('2026-11-17', 1741636) | PASS |  |  |
| CEG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $268.89 | $268.89 | PASS |  |  |
| CEG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $267.38 | $267.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CEG | E3 | percent from the 21-day average | 0.6% above | 0.6% above | PASS |  |  |
| CEG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CEG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $12.99 | $12.99 (sr=12.989) | PASS |  | Wilder ATR14 |
| CEG | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| CEG | L-ema21 | ladder row ema21: price and gap = price vs average | $267.38, 0.6% | $267.38, 0.6% | PASS |  |  |
| CEG | L-note | "Last close $X · date" note = last completed bar | Last close $268.07 · Nov 17 | $268.07 · Nov 17 | PASS |  |  |
| CEG | L-now | ladder price row = compared price; name = the basis label | $268.89 "After hours" | $268.89 "after hours" | PASS |  |  |
| CEG | L-sma200 | ladder row sma200: price and gap = price vs average | $277.45, -3.1% | $277.45, -3.1% | PASS |  |  |
| CEG | L-sma50 | ladder row sma50: price and gap = price vs average | $268.07, 0.3% | $268.07, 0.3% | PASS |  |  |
| CEG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $268.89 / entry $268.89 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CEG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CEG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.4 | 50.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CEG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -20.4% vs +11.2% | -20.4% vs 11.2% | PASS |  |  |
| CEG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CEG | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.1 | 14.1 | PASS |  | Wilder, completed bars |
| CEG | T4w | words "20 or more / below 20" | below 20 | ADX 14.1 | PASS |  |  |
| CEG | T5 | "counted at the last close ($X, date)" = last completed bar | $268.07, Nov 17 | $268.07, Nov 17 | PASS |  |  |
| CEG | T6 | price vs 200-day average (S1 pattern sma values) | $268.07 vs $277.46 · -3.4% | $268.07 vs $277.45 · -3.4% | PASS |  |  |
| CEG | T6w | word "Below" | Below | Below | PASS |  |  |
| CEG | T7 | price vs 50-day average (S1 pattern sma values) | $268.07 vs $268.07 · +0.0% | $268.07 vs $268.07 · -0.0% | PASS |  |  |
| CEG | T7w | word "Below" | Below | Below | PASS |  |  |
| CEG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.0% over 30 td | -3.0% over 30 td | PASS |  |  |
| CEG | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CEG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CEG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.2% below $378.52 | 29.2% below $378.52 | PASS |  | closing high would be 376.35 |
| CEG | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.2% below | PASS |  |  |
| CEG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $378.52 | $378.52004956998206 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CEG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.51%, close location 0.06, OBV falling |
| CEG | V2 | day change of the last completed bar | down 3.5% | -3.51% | PASS |  |  |
| CEG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0576) | PASS |  |  |
| CEG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CEG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.79× / 0.72× | 0.79× / 0.72× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CEG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2992421) | 20 bars, last ('2026-11-17', 2992421) | PASS |  |  |
| CGY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $84.30 | $84.30 | PASS |  |  |
| CGY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $85.3 | $85.30 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CGY.TO | E3 | percent from the 21-day average | 1.2% below | 1.2% below | PASS |  |  |
| CGY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CGY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.58 | $2.58 (sr=2.5803) | PASS |  | Wilder ATR14 |
| CGY.TO | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| CGY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $85.3, -1.2% | $85.30, -1.2% | PASS |  |  |
| CGY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $84.30 · Nov 17 | $84.30 · Nov 17 | PASS |  |  |
| CGY.TO | L-now | ladder price row = compared price; name = the basis label | $84.3 "After hours" | $84.30 "after hours" | PASS |  |  |
| CGY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $78.83, 6.9% | $78.83, 6.9% | PASS |  |  |
| CGY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $83.39, 1.1% | $83.39, 1.1% | PASS |  |  |
| CGY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $84.30 / entry $84.30 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CGY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CGY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.5 | 48.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CGY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +65.3% vs +11.2% | 65.3% vs 11.2% | PASS |  |  |
| CGY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CGY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.9 | 15.9 | PASS |  | Wilder, completed bars |
| CGY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.9 | PASS |  |  |
| CGY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $84.30, Nov 17 | $84.30, Nov 17 | PASS |  |  |
| CGY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $84.30 vs $78.83 · +6.9% | $84.30 vs $78.83 · 6.9% | PASS |  |  |
| CGY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CGY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $84.30 vs $83.39 · +1.1% | $84.30 vs $83.39 · 1.1% | PASS |  |  |
| CGY.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CGY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.1% over 30 td | +5.1% over 30 td | PASS |  |  |
| CGY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CGY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CGY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.4% below $95.15 | 11.4% below $95.15 | PASS |  | closing high would be 91.80 |
| CGY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.4% below | PASS |  |  |
| CGY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $95.15 | $95.15474299571112 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CGY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.07%, close location 0.46, OBV falling |
| CGY.TO | V2 | day change of the last completed bar | down 2.1% | -2.07% | PASS |  |  |
| CGY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CGY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.37× / 0.68× | 0.37× / 0.68× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CGY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 11265) | 20 bars, last ('2026-11-17', 11265) | PASS |  |  |
| CNQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $68.29 | $68.29 | PASS |  |  |
| CNQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $71.18 | $71.18 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNQ.TO | E3 | percent from the 21-day average | 4.1% below | 4.1% below | PASS |  |  |
| CNQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CNQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.93 | $1.93 (sr=1.9336) | PASS |  | Wilder ATR14 |
| CNQ.TO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| CNQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $71.18, -4.1% | $71.18, -4.1% | PASS |  |  |
| CNQ.TO | L-now | ladder price row = compared price; name = the basis label | $68.29 "Last close" | $68.29 "last close" | PASS |  |  |
| CNQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.14, 6.5% | $64.14, 6.5% | PASS |  |  |
| CNQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $71.15, -4.0% | $71.15, -4.0% | PASS |  |  |
| CNQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.2 | 39.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +51.9% vs +11.2% | 51.9% vs 11.2% | PASS |  |  |
| CNQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.8 | 28.8 | PASS |  | Wilder, completed bars |
| CNQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.8 | PASS |  |  |
| CNQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $68.29 vs $64.14 · +6.5% | $68.29 vs $64.14 · 6.5% | PASS |  |  |
| CNQ.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $68.29 vs $71.15 · -4.0% | $68.29 vs $71.15 · -4.0% | PASS |  |  |
| CNQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CNQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.9% over 30 td | +6.9% over 30 td | PASS |  |  |
| CNQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.1% below $78.60 | 13.1% below $78.60 | PASS |  | closing high would be 78.42 |
| CNQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.1% below | PASS |  |  |
| CNQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $78.60 | $78.5999984741211 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.97%, close location 0.10, OBV falling |
| CNQ.TO | V2 | day change of the last completed bar | down 1.0% | -0.97% | PASS |  |  |
| CNQ.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1029) | PASS |  |  |
| CNQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CNQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.72× / 0.34× | 1.72× / 0.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 21721735) | 20 bars, last ('2026-11-17', 21721735) | PASS |  |  |
| CNQ.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.72, OBV falling | condition true | PASS |  |  |
| CNR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $180.54 | $180.54 | PASS |  |  |
| CNR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $177.45 | $177.45 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNR.TO | E3 | percent from the 21-day average | 1.7% above | 1.7% above | PASS |  |  |
| CNR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CNR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.33 | $3.33 (sr=3.3338) | PASS |  | Wilder ATR14 |
| CNR.TO | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves above |
| CNR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $177.45, 1.7% | $177.45, 1.7% | PASS |  |  |
| CNR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $180.54 · Nov 17 | $180.54 · Nov 17 | PASS |  |  |
| CNR.TO | L-now | ladder price row = compared price; name = the basis label | $180.54 "After hours" | $180.54 "after hours" | PASS |  |  |
| CNR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $161.73, 11.6% | $161.73, 11.6% | PASS |  |  |
| CNR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $172.28, 4.8% | $172.28, 4.8% | PASS |  |  |
| CNR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $180.54 / entry $180.54 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CNR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 58.7 | 58.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +37.9% vs +11.2% | 37.9% vs 11.2% | PASS |  |  |
| CNR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.9 | 23.9 | PASS |  | Wilder, completed bars |
| CNR.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 23.9 | PASS |  |  |
| CNR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $180.54, Nov 17 | $180.54, Nov 17 | PASS |  |  |
| CNR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $180.54 vs $161.73 · +11.6% | $180.54 vs $161.73 · 11.6% | PASS |  |  |
| CNR.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $180.54 vs $172.28 · +4.8% | $180.54 vs $172.28 · 4.8% | PASS |  |  |
| CNR.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.9% over 30 td | +3.9% over 30 td | PASS |  |  |
| CNR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.0% below $184.26 | 2.0% below $184.26 | PASS |  | closing high would be 182.93 |
| CNR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.0% below | PASS |  |  |
| CNR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $184.26 | $184.25630798377267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -1.22%, close location 0.33, OBV rising |
| CNR.TO | V2 | day change of the last completed bar | down 1.2% | -1.22% | PASS |  |  |
| CNR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| CNR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.66× | 0.88× / 0.66× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1085648) | 20 bars, last ('2026-11-17', 1085648) | PASS |  |  |
| COP | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $139.00 | $139.00 | PASS |  |  |
| COP | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $139.77 | $139.77 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COP | E3 | percent from the 21-day average | 0.6% below | 0.6% below | PASS |  |  |
| COP | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COP | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.87 | $3.88 (sr=3.8743) | PASS |  | Wilder ATR14 |
| COP | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| COP | L-ema21 | ladder row ema21: price and gap = price vs average | $139.77, -0.6% | $139.77, -0.6% | PASS |  |  |
| COP | L-note | "Last close $X · date" note = last completed bar | Last close $139.48 · Nov 17 | $139.48 · Nov 17 | PASS |  |  |
| COP | L-now | ladder price row = compared price; name = the basis label | $139 "After hours" | $139.00 "after hours" | PASS |  |  |
| COP | L-sma200 | ladder row sma200: price and gap = price vs average | $122.04, 13.9% | $122.04, 13.9% | PASS |  |  |
| COP | L-sma50 | ladder row sma50: price and gap = price vs average | $136.64, 1.7% | $136.64, 1.7% | PASS |  |  |
| COP | S5-price | S5: the same live price reads the same on the header and the Entry block | header $139.00 / entry $139.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COP | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COP | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.2 | 50.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COP | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +61.7% vs +11.2% | 61.7% vs 11.2% | PASS |  |  |
| COP | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COP | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.6 | 23.6 | PASS |  | Wilder, completed bars |
| COP | T4w | words "20 or more / below 20" | 20 or more | ADX 23.6 | PASS |  |  |
| COP | T5 | "counted at the last close ($X, date)" = last completed bar | $139.48, Nov 17 | $139.48, Nov 17 | PASS |  |  |
| COP | T6 | price vs 200-day average (S1 pattern sma values) | $139.48 vs $122.04 · +14.3% | $139.48 vs $122.04 · 14.3% | PASS |  |  |
| COP | T6w | word "Above" | Above | Above | PASS |  |  |
| COP | T7 | price vs 50-day average (S1 pattern sma values) | $139.48 vs $136.64 · +2.1% | $139.48 vs $136.64 · 2.1% | PASS |  |  |
| COP | T7w | word "Above" | Above | Above | PASS |  |  |
| COP | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.1% over 30 td | +6.2% over 30 td | PASS |  |  |
| COP | T8r | word "rising" | still rising | rising | PASS |  |  |
| COP | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COP | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 9.0% below $153.27 | 9.0% below $153.27 | PASS |  | closing high would be 153.02 |
| COP | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 9.0% below | PASS |  |  |
| COP | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $153.27 | $153.2715592533114 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COP | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.74%, close location 0.06, OBV falling |
| COP | V2 | day change of the last completed bar | down 0.7% | -0.74% | PASS |  |  |
| COP | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0600) | PASS |  |  |
| COP | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COP | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.12× / 0.27× | 1.12× / 0.27× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COP | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 7652629) | 20 bars, last ('2026-11-17', 7652629) | PASS |  |  |
| COPP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $46.42 | $46.42 | PASS |  |  |
| COPP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $52.08 | $52.08 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPP.TO | E3 | percent from the 21-day average | 10.9% below | 10.9% below | PASS |  |  |
| COPP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| COPP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.05 | $2.05 (sr=2.0505) | PASS |  | Wilder ATR14 |
| COPP.TO | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| COPP.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.2 | +3.2 | PASS |  |  |
| COPP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $52.08, -10.9% | $52.08, -10.9% | PASS |  |  |
| COPP.TO | L-now | ladder price row = compared price; name = the basis label | $46.42 "Last close" | $46.42 "last close" | PASS |  |  |
| COPP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.63, -20.8% | $58.63, -20.8% | PASS |  |  |
| COPP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $57.32, -19.0% | $57.32, -19.0% | PASS |  |  |
| COPP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.8 | 31.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.0% vs +11.2% | 6.1% vs 11.2% | PASS |  |  |
| COPP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.9 | 29.9 | PASS |  | Wilder, completed bars |
| COPP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 29.9 | PASS |  |  |
| COPP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $46.42 vs $58.63 · -20.8% | $46.42 vs $58.63 · -20.8% | PASS |  |  |
| COPP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $46.42 vs $57.32 · -19.0% | $46.42 vs $57.32 · -19.0% | PASS |  |  |
| COPP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.7% over 30 td | -0.7% over 30 td | PASS |  |  |
| COPP.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.2% below $70.54 | 34.2% below $70.54 | PASS |  | closing high would be 68.98 |
| COPP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.2% below | PASS |  |  |
| COPP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $70.54 | $70.54000091552734 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.13%, close location 0.19, OBV falling |
| COPP.TO | V2 | day change of the last completed bar | down 0.1% | -0.13% | PASS |  |  |
| COPP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.19 (raw 0.1921) | PASS |  |  |
| COPP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.84× / 0.03× | 0.84× / 0.03× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 12238) | 20 bars, last ('2026-11-17', 12238) | PASS |  |  |
| COPX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $65.31 | $65.31 | PASS |  |  |
| COPX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.1 | $73.10 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPX | E3 | percent from the 21-day average | 10.7% below | 10.7% below | PASS |  |  |
| COPX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COPX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.76 | $2.76 (sr=2.7598) | PASS |  | Wilder ATR14 |
| COPX | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| COPX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.4 | +3.4 | PASS |  |  |
| COPX | L-ema21 | ladder row ema21: price and gap = price vs average | $73.1, -10.7% | $73.10, -10.7% | PASS |  |  |
| COPX | L-note | "Last close $X · date" note = last completed bar | Last close $65.31 · Nov 17 | $65.31 · Nov 17 | PASS |  |  |
| COPX | L-now | ladder price row = compared price; name = the basis label | $65.31 "After hours" | $65.31 "after hours" | PASS |  |  |
| COPX | L-sma200 | ladder row sma200: price and gap = price vs average | $82.41, -20.8% | $82.41, -20.8% | PASS |  |  |
| COPX | L-sma50 | ladder row sma50: price and gap = price vs average | $80.2, -18.6% | $80.20, -18.6% | PASS |  |  |
| COPX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $65.31 / entry $65.31 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.1 | 31.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +11.8% vs +11.2% | 11.9% vs 11.2% | PASS |  |  |
| COPX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPX | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.2 | 25.1 | PASS |  | Wilder, completed bars |
| COPX | T4w | words "20 or more / below 20" | 20 or more | ADX 25.1 | PASS |  |  |
| COPX | T5 | "counted at the last close ($X, date)" = last completed bar | $65.31, Nov 17 | $65.31, Nov 17 | PASS |  |  |
| COPX | T6 | price vs 200-day average (S1 pattern sma values) | $65.31 vs $82.41 · -20.7% | $65.31 vs $82.41 · -20.8% | PASS |  |  |
| COPX | T6w | word "Below" | Below | Below | PASS |  |  |
| COPX | T7 | price vs 50-day average (S1 pattern sma values) | $65.31 vs $80.20 · -18.6% | $65.31 vs $80.20 · -18.6% | PASS |  |  |
| COPX | T7w | word "Below" | Below | Below | PASS |  |  |
| COPX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.5% over 30 td | -0.5% over 30 td | PASS |  |  |
| COPX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.5% below $99.65 | 34.5% below $99.65 | PASS |  | closing high would be 96.45 |
| COPX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.5% below | PASS |  |  |
| COPX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $99.65 | $99.65136047369408 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.31%, close location 0.20, OBV falling |
| COPX | V2 | day change of the last completed bar | down 0.3% | -0.31% | PASS |  |  |
| COPX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.20 (raw 0.2030) | PASS |  |  |
| COPX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.03× / 0.07× | 2.03× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 5636662) | 20 bars, last ('2026-11-17', 5636662) | PASS |  |  |
| COPX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.03, OBV falling | condition true | PASS |  |  |
| COPZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $8.59 | $8.59 | PASS |  |  |
| COPZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.09 | $11.09 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPZ | E3 | percent from the 21-day average | 22.5% below | 22.5% below | PASS |  |  |
| COPZ | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| COPZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.80 | $0.80 (sr=0.7979) | PASS |  | Wilder ATR14 |
| COPZ | E5 | distance in normal day-moves | 3.1 | 3.1 | PASS |  | gauge dot note uses the same number:  · 3.1 day-moves below |
| COPZ | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.2 | +3.3 | PASS |  |  |
| COPZ | L-ema21 | ladder row ema21: price and gap = price vs average | $11.09, -22.5% | $11.09, -22.5% | PASS |  |  |
| COPZ | L-now | ladder price row = compared price; name = the basis label | $8.59 "Last close" | $8.59 "last close" | PASS |  |  |
| COPZ | L-sma50 | ladder row sma50: price and gap = price vs average | $13.68, -37.2% | $13.68, -37.2% | PASS |  |  |
| COPZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.4 | 30.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.5 | 26.5 | PASS |  | Wilder, completed bars |
| COPZ | T4w | words "20 or more / below 20" | 20 or more | ADX 26.5 | PASS |  |  |
| COPZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.04%, close location 0.14, OBV falling |
| COPZ | V2 | day change of the last completed bar | down 1.0% | -1.04% | PASS |  |  |
| COPZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1400) | PASS |  |  |
| COPZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.77× / 0.11× | 2.77× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 35620) | 20 bars, last ('2026-11-17', 35620) | PASS |  |  |
| COPZ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.77, OBV falling | condition true | PASS |  |  |
| COST | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,104.75 | $1,104.75 | PASS |  |  |
| COST | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1047.92 | $1047.92 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COST | E3 | percent from the 21-day average | 5.4% above | 5.4% above | PASS |  |  |
| COST | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COST | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $18.79 | $18.79 (sr=18.7878) | PASS |  | Wilder ATR14 |
| COST | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  ▸ · 3.0 day-moves above |
| COST | L-ema21 | ladder row ema21: price and gap = price vs average | $1047.92, 5.4% | $1047.92, 5.4% | PASS |  |  |
| COST | L-note | "Last close $X · date" note = last completed bar | Last close $1,110.08 · Nov 17 | $1,110.08 · Nov 17 | PASS |  |  |
| COST | L-now | ladder price row = compared price; name = the basis label | $1104.75 "After hours" | $1104.75 "after hours" | PASS |  |  |
| COST | L-sma200 | ladder row sma200: price and gap = price vs average | $974.56, 13.4% | $974.56, 13.4% | PASS |  |  |
| COST | L-sma50 | ladder row sma50: price and gap = price vs average | $974.05, 13.4% | $974.04, 13.4% | PASS |  |  |
| COST | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,104.75 / entry $1,104.75 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COST | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COST | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 75.4 | 75.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COST | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +22.4% vs +11.2% | 22.4% vs 11.2% | PASS |  |  |
| COST | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COST | T4 | ADX 14 (S1 /api/sr meta.adx) | 53.5 | 53.5 | PASS |  | Wilder, completed bars |
| COST | T4w | words "20 or more / below 20" | 20 or more | ADX 53.5 | PASS |  |  |
| COST | T5 | "counted at the last close ($X, date)" = last completed bar | $1,110.08, Nov 17 | $1110.08, Nov 17 | PASS |  |  |
| COST | T6 | price vs 200-day average (S1 pattern sma values) | $1,110.08 vs $974.56 · +13.9% | $1110.08 vs $974.56 · 13.9% | PASS |  |  |
| COST | T6w | word "Above" | Above | Above | PASS |  |  |
| COST | T7 | price vs 50-day average (S1 pattern sma values) | $1,110.08 vs $974.04 · +14.0% | $1110.08 vs $974.04 · 14.0% | PASS |  |  |
| COST | T7w | word "Above" | Above | Above | PASS |  |  |
| COST | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.7% over 30 td | +1.7% over 30 td | PASS |  |  |
| COST | T8r | word "rising" | still rising | rising | PASS |  |  |
| COST | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COST | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.2% below $1,123.67 | 1.2% below $1123.67 | PASS |  | closing high would be 1113.74 |
| COST | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.2% below | PASS |  |  |
| COST | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,123.67 | $1123.669921875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COST | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.33%, close location 0.09, OBV rising |
| COST | V2 | day change of the last completed bar | down 0.3% | -0.33% | PASS |  |  |
| COST | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0928) | PASS |  |  |
| COST | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COST | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.25× / 0.19× | 1.25× / 0.19× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COST | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2942897) | 20 bars, last ('2026-11-17', 2942897) | PASS |  |  |
| COTG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $16.87 | $16.87 | PASS |  |  |
| COTG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.22 | $15.22 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COTG | E3 | percent from the 21-day average | 10.8% above | 10.8% above | PASS |  |  |
| COTG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COTG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.51 | $0.51 (sr=0.5142) | PASS |  | Wilder ATR14 |
| COTG | E5 | distance in normal day-moves | 3.2 | 3.2 | PASS |  | gauge dot note uses the same number:  ▸ · 3.2 day-moves above |
| COTG | L-ema21 | ladder row ema21: price and gap = price vs average | $15.22, 10.8% | $15.22, 10.8% | PASS |  |  |
| COTG | L-note | "Last close $X · date" note = last completed bar | Last close $16.93 · Nov 17 | $16.93 · Nov 17 | PASS |  |  |
| COTG | L-now | ladder price row = compared price; name = the basis label | $16.87 "After hours" | $16.87 "after hours" | PASS |  |  |
| COTG | L-sma200 | ladder row sma200: price and gap = price vs average | $13.92, 21.2% | $13.92, 21.2% | PASS |  |  |
| COTG | L-sma50 | ladder row sma50: price and gap = price vs average | $13.29, 26.9% | $13.29, 26.9% | PASS |  |  |
| COTG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $16.87 / entry $16.87 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COTG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COTG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 73.6 | 73.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COTG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.6% vs +11.2% | 28.5% vs 11.2% | PASS |  |  |
| COTG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COTG | T4 | ADX 14 (S1 /api/sr meta.adx) | 52.2 | 52.1 | PASS |  | Wilder, completed bars |
| COTG | T4w | words "20 or more / below 20" | 20 or more | ADX 52.1 | PASS |  |  |
| COTG | T5 | "counted at the last close ($X, date)" = last completed bar | $16.93, Nov 17 | $16.93, Nov 17 | PASS |  |  |
| COTG | T6 | price vs 200-day average (S1 pattern sma values) | $16.93 vs $13.92 · +21.6% | $16.93 vs $13.92 · 21.7% | PASS |  |  |
| COTG | T6w | word "Above" | Above | Above | PASS |  |  |
| COTG | T7 | price vs 50-day average (S1 pattern sma values) | $16.93 vs $13.29 · +27.4% | $16.93 vs $13.29 · 27.4% | PASS |  |  |
| COTG | T7w | word "Above" | Above | Above | PASS |  |  |
| COTG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| COTG | T8r | word "rising" | still rising | rising | PASS |  |  |
| COTG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COTG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.9% below $17.80 | 4.9% below $17.80 | PASS |  | closing high would be 17.70 |
| COTG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.9% below | PASS |  |  |
| COTG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $17.80 | $17.80299949645996 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COTG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.70%, close location 0.00, OBV rising |
| COTG | V2 | day change of the last completed bar | down 0.7% | -0.70% | PASS |  |  |
| COTG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| COTG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COTG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.27× / 0.22× | 0.27× / 0.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COTG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 28896) | 20 bars, last ('2026-11-17', 28896) | PASS |  |  |
| CSU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3,316.93 | $3,316.93 | PASS |  |  |
| CSU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3367.84 | $3367.84 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CSU.TO | E3 | percent from the 21-day average | 1.5% below | 1.5% below | PASS |  |  |
| CSU.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CSU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $121.33 | $121.33 (sr=121.3349) | PASS |  | Wilder ATR14 |
| CSU.TO | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| CSU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $3367.84, -1.5% | $3367.84, -1.5% | PASS |  |  |
| CSU.TO | L-note | "Last close $X · date" note = last completed bar | Last close $3,316.93 · Nov 17 | $3,316.93 · Nov 17 | PASS |  |  |
| CSU.TO | L-now | ladder price row = compared price; name = the basis label | $3316.93 "After hours" | $3316.93 "after hours" | PASS |  |  |
| CSU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $2812.85, 17.9% | $2812.85, 17.9% | PASS |  |  |
| CSU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $3126.03, 6.1% | $3126.03, 6.1% | PASS |  |  |
| CSU.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3,316.93 / entry $3,316.93 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CSU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CSU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.9 | 48.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CSU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.4% vs +11.2% | 2.4% vs 11.2% | PASS |  |  |
| CSU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CSU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.3 | 32.3 | PASS |  | Wilder, completed bars |
| CSU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.3 | PASS |  |  |
| CSU.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $3,316.93, Nov 17 | $3316.93, Nov 17 | PASS |  |  |
| CSU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $3,316.93 vs $2,812.85 · +17.9% | $3316.93 vs $2812.85 · 17.9% | PASS |  |  |
| CSU.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CSU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $3,316.93 vs $3,126.03 · +6.1% | $3316.93 vs $3126.03 · 6.1% | PASS |  |  |
| CSU.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CSU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.4% over 30 td | +1.4% over 30 td | PASS |  |  |
| CSU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CSU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CSU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.0% below $3,565.00 | 7.0% below $3565.00 | PASS |  | closing high would be 3526.52 |
| CSU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.0% below | PASS |  |  |
| CSU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $3,565.00 | $3565 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CSU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -3.48%, close location 0.20, OBV rising |
| CSU.TO | V2 | day change of the last completed bar | down 3.5% | -3.48% | PASS |  |  |
| CSU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.20 (raw 0.1990) | PASS |  |  |
| CSU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| CSU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.95× | 0.99× / 0.95× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CSU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 60779) | 20 bars, last ('2026-11-17', 60779) | PASS |  |  |
| CVX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $216.13 | $216.13 | PASS |  |  |
| CVX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $218.45 | $218.45 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CVX | E3 | percent from the 21-day average | 1.1% below | 1.1% below | PASS |  |  |
| CVX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CVX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.86 | $4.86 (sr=4.8615) | PASS |  | Wilder ATR14 |
| CVX | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| CVX | L-ema21 | ladder row ema21: price and gap = price vs average | $218.45, -1.1% | $218.45, -1.1% | PASS |  |  |
| CVX | L-note | "Last close $X · date" note = last completed bar | Last close $216.13 · Nov 17 | $216.13 · Nov 17 | PASS |  |  |
| CVX | L-now | ladder price row = compared price; name = the basis label | $216.13 "After hours" | $216.13 "after hours" | PASS |  |  |
| CVX | L-sma200 | ladder row sma200: price and gap = price vs average | $194.4, 11.2% | $194.40, 11.2% | PASS |  |  |
| CVX | L-sma50 | ladder row sma50: price and gap = price vs average | $215.78, 0.2% | $215.78, 0.2% | PASS |  |  |
| CVX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $216.13 / entry $216.13 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CVX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CVX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.1 | 47.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CVX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +45.1% vs +11.2% | 45.1% vs 11.2% | PASS |  |  |
| CVX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CVX | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.2 | 25.2 | PASS |  | Wilder, completed bars |
| CVX | T4w | words "20 or more / below 20" | 20 or more | ADX 25.2 | PASS |  |  |
| CVX | T5 | "counted at the last close ($X, date)" = last completed bar | $216.13, Nov 17 | $216.13, Nov 17 | PASS |  |  |
| CVX | T6 | price vs 200-day average (S1 pattern sma values) | $216.13 vs $194.40 · +11.2% | $216.13 vs $194.40 · 11.2% | PASS |  |  |
| CVX | T6w | word "Above" | Above | Above | PASS |  |  |
| CVX | T7 | price vs 50-day average (S1 pattern sma values) | $216.13 vs $215.78 · +0.2% | $216.13 vs $215.78 · 0.2% | PASS |  |  |
| CVX | T7w | word "Above" | Above | Above | PASS |  |  |
| CVX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.2% over 30 td | +5.2% over 30 td | PASS |  |  |
| CVX | T8r | word "rising" | still rising | rising | PASS |  |  |
| CVX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CVX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.6% below $236.48 | 8.6% below $236.48 | PASS |  | closing high would be 235.52 |
| CVX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.6% below | PASS |  |  |
| CVX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $236.48 | $236.47999572753906 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CVX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.47%, close location 0.20, OBV falling |
| CVX | V2 | day change of the last completed bar | down 0.5% | -0.47% | PASS |  |  |
| CVX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.20 (raw 0.2019) | PASS |  |  |
| CVX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CVX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.96× / 0.21× | 0.96× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CVX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 8401634) | 20 bars, last ('2026-11-17', 8401634) | PASS |  |  |
| DRAL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $4.39 | $4.39 | PASS |  |  |
| DRAL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $6.02 | $6.02 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAL | E3 | percent from the 21-day average | 27.1% below | 27.1% below | PASS |  |  |
| DRAL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.81 | $0.81 (sr=0.8105) | PASS |  | Wilder ATR14 |
| DRAL | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| DRAL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.3 | +3.3 | PASS |  |  |
| DRAL | L-ema21 | ladder row ema21: price and gap = price vs average | $6.02, -27.1% | $6.02, -27.1% | PASS |  |  |
| DRAL | L-note | "Last close $X · date" note = last completed bar | Last close $4.11 · Nov 17 | $4.11 · Nov 17 | PASS |  |  |
| DRAL | L-now | ladder price row = compared price; name = the basis label | $4.39 "After hours" | $4.39 "after hours" | PASS |  |  |
| DRAL | L-sma50 | ladder row sma50: price and gap = price vs average | $8.7, -49.5% | $8.70, -49.5% | PASS |  |  |
| DRAL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $4.39 / entry $4.39 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.5 | 34.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.3 | PASS |  |  |
| DRAL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.14%, close location 0.88, OBV falling |
| DRAL | V2 | day change of the last completed bar | down 2.1% | -2.14% | PASS |  |  |
| DRAL | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.88 (raw 0.8837) | PASS |  |  |
| DRAL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.68× / 0.11× | 1.68× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 383574) | 20 bars, last ('2026-11-17', 383574) | PASS |  |  |
| DRAL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.68, OBV falling | condition true | PASS |  |  |
| DRAM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $40.81 | $40.81 | PASS |  |  |
| DRAM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $45.0 | $45.00 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAM | E3 | percent from the 21-day average | 9.3% below | 9.3% below | PASS |  |  |
| DRAM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.16 | $3.16 (sr=3.1551) | PASS |  | Wilder ATR14 |
| DRAM | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| DRAM | L-ema21 | ladder row ema21: price and gap = price vs average | $45, -9.3% | $45.00, -9.3% | PASS |  |  |
| DRAM | L-note | "Last close $X · date" note = last completed bar | Last close $38.93 · Nov 17 | $38.93 · Nov 17 | PASS |  |  |
| DRAM | L-now | ladder price row = compared price; name = the basis label | $40.81 "After hours" | $40.81 "after hours" | PASS |  |  |
| DRAM | L-sma50 | ladder row sma50: price and gap = price vs average | $52.46, -22.2% | $52.46, -22.2% | PASS |  |  |
| DRAM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $40.81 / entry $40.81 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.1 | 37.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAM | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.2 | 32.2 | PASS |  | Wilder, completed bars |
| DRAM | T4w | words "20 or more / below 20" | 20 or more | ADX 32.2 | PASS |  |  |
| DRAM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.87%, close location 0.77, OBV falling |
| DRAM | V2 | day change of the last completed bar | down 0.9% | -0.87% | PASS |  |  |
| DRAM | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.77 (raw 0.7737) | PASS |  |  |
| DRAM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.22× / 0.11× | 1.22× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 42130960) | 20 bars, last ('2026-11-17', 42130960) | PASS |  |  |
| DRIV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $26.75 | $26.75 | PASS |  |  |
| DRIV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $29.29 | $29.29 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRIV | E3 | percent from the 21-day average | 8.7% below | 8.7% below | PASS |  |  |
| DRIV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRIV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.79 | $0.79 (sr=0.7887) | PASS |  | Wilder ATR14 |
| DRIV | E5 | distance in normal day-moves | 3.2 | 3.2 | PASS |  | gauge dot note uses the same number:  · 3.2 day-moves below |
| DRIV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.2 | +6.2 | PASS |  |  |
| DRIV | L-ema21 | ladder row ema21: price and gap = price vs average | $29.29, -8.7% | $29.29, -8.7% | PASS |  |  |
| DRIV | L-note | "Last close $X · date" note = last completed bar | Last close $27.00 · Nov 17 | $27.00 · Nov 17 | PASS |  |  |
| DRIV | L-now | ladder price row = compared price; name = the basis label | $26.75 "After hours" | $26.75 "after hours" | PASS |  |  |
| DRIV | L-sma200 | ladder row sma200: price and gap = price vs average | $34.22, -21.8% | $34.22, -21.8% | PASS |  |  |
| DRIV | L-sma50 | ladder row sma50: price and gap = price vs average | $31.46, -15.0% | $31.45, -15.0% | PASS |  |  |
| DRIV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $26.75 / entry $26.75 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRIV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DRIV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.5 | 31.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRIV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.6% vs +11.2% | -5.6% vs 11.2% | PASS |  |  |
| DRIV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DRIV | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.5 | 37.6 | PASS |  | Wilder, completed bars |
| DRIV | T4w | words "20 or more / below 20" | 20 or more | ADX 37.6 | PASS |  |  |
| DRIV | T5 | "counted at the last close ($X, date)" = last completed bar | $27.00, Nov 17 | $27.00, Nov 17 | PASS |  |  |
| DRIV | T6 | price vs 200-day average (S1 pattern sma values) | $27.00 vs $34.22 · -21.1% | $27.00 vs $34.22 · -21.1% | PASS |  |  |
| DRIV | T6w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T7 | price vs 50-day average (S1 pattern sma values) | $27.00 vs $31.46 · -14.2% | $27.00 vs $31.45 · -14.2% | PASS |  |  |
| DRIV | T7w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.6% over 30 td | -0.7% over 30 td | PASS |  |  |
| DRIV | T8r | word "rising" | not rising | not rising | PASS |  |  |
| DRIV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DRIV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.7% below $42.67 | 36.7% below $42.67 | PASS |  | closing high would be 42.45 |
| DRIV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.7% below | PASS |  |  |
| DRIV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $42.67 | $42.67459709729379 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DRIV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.28%, close location 0.36, OBV falling |
| DRIV | V2 | day change of the last completed bar | down 1.3% | -1.28% | PASS |  |  |
| DRIV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRIV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.73× / 0.45× | 0.73× / 0.44× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRIV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 29332) | 20 bars, last ('2026-11-17', 29332) | PASS |  |  |
| DUK | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $129.80 | $129.80 | PASS |  |  |
| DUK | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $125.89 | $125.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DUK | E3 | percent from the 21-day average | 3.1% above | 3.1% above | PASS |  |  |
| DUK | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DUK | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.15 | $2.15 (sr=2.1475) | PASS |  | Wilder ATR14 |
| DUK | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves above |
| DUK | L-ema21 | ladder row ema21: price and gap = price vs average | $125.89, 3.1% | $125.89, 3.1% | PASS |  |  |
| DUK | L-note | "Last close $X · date" note = last completed bar | Last close $129.84 · Nov 17 | $129.84 · Nov 17 | PASS |  |  |
| DUK | L-now | ladder price row = compared price; name = the basis label | $129.8 "After hours" | $129.80 "after hours" | PASS |  |  |
| DUK | L-sma200 | ladder row sma200: price and gap = price vs average | $122.74, 5.8% | $122.74, 5.8% | PASS |  |  |
| DUK | L-sma50 | ladder row sma50: price and gap = price vs average | $120.08, 8.1% | $120.08, 8.1% | PASS |  |  |
| DUK | S5-price | S5: the same live price reads the same on the header and the Entry block | header $129.80 / entry $129.80 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| DUK | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.54× / 0.34× | 1.54× / 0.35× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DUK | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 6743545) | 20 bars, last ('2026-11-17', 6743545) | PASS |  |  |
| ELIL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.13 | $39.13 | PASS |  |  |
| ELIL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $37.94 | $37.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ELIL | E3 | percent from the 21-day average | 3.1% above | 3.1% above | PASS |  |  |
| ELIL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ELIL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.23 | $2.23 (sr=2.2284) | PASS |  | Wilder ATR14 |
| ELIL | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| ELIL | L-ema21 | ladder row ema21: price and gap = price vs average | $37.94, 3.1% | $37.94, 3.1% | PASS |  |  |
| ELIL | L-note | "Last close $X · date" note = last completed bar | Last close $40.25 · Nov 17 | $40.25 · Nov 17 | PASS |  |  |
| ELIL | L-now | ladder price row = compared price; name = the basis label | $39.13 "After hours" | $39.13 "after hours" | PASS |  |  |
| ELIL | L-sma200 | ladder row sma200: price and gap = price vs average | $27, 44.9% | $27.00, 44.9% | PASS |  |  |
| ELIL | L-sma50 | ladder row sma50: price and gap = price vs average | $32.27, 21.3% | $32.27, 21.3% | PASS |  |  |
| ELIL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $39.13 / entry $39.13 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ELIL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ELIL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 62.2 | 62.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ELIL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +56.3% vs +11.2% | 56.3% vs 11.2% | PASS |  |  |
| ELIL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ELIL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.1 | 34.0 | PASS |  | Wilder, completed bars |
| ELIL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.0 | PASS |  |  |
| ELIL | T5 | "counted at the last close ($X, date)" = last completed bar | $40.25, Nov 17 | $40.25, Nov 17 | PASS |  |  |
| ELIL | T6 | price vs 200-day average (S1 pattern sma values) | $40.25 vs $27.00 · +49.1% | $40.25 vs $27.00 · 49.0% | PASS |  |  |
| ELIL | T6w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T7 | price vs 50-day average (S1 pattern sma values) | $40.25 vs $32.27 · +24.7% | $40.25 vs $32.27 · 24.7% | PASS |  |  |
| ELIL | T7w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.7% over 30 td | +4.8% over 30 td | PASS |  |  |
| ELIL | T8r | word "rising" | still rising | rising | PASS |  |  |
| ELIL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ELIL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.6% below $43.56 | 7.6% below $43.56 | PASS |  | closing high would be 41.85 |
| ELIL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.6% below | PASS |  |  |
| ELIL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.56 | $43.55500030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ELIL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -2.12%, close location 0.51, OBV flat |
| ELIL | V2 | day change of the last completed bar | down 2.1% | -2.12% | PASS |  |  |
| ELIL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| ELIL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.38× | 0.88× / 0.38× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ELIL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 55100) | 20 bars, last ('2026-11-17', 55100) | PASS |  |  |
| EQIX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,034.83 | $1,034.83 | PASS |  |  |
| EQIX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1029.51 | $1029.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| EQIX | E3 | percent from the 21-day average | 0.5% above | 0.5% above | PASS |  |  |
| EQIX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| EQIX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $34.07 | $34.07 (sr=34.068) | PASS |  | Wilder ATR14 |
| EQIX | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| EQIX | L-ema21 | ladder row ema21: price and gap = price vs average | $1029.51, 0.5% | $1029.51, 0.5% | PASS |  |  |
| EQIX | L-note | "Last close $X · date" note = last completed bar | Last close $1,034.83 · Nov 17 | $1,034.83 · Nov 17 | PASS |  |  |
| EQIX | L-now | ladder price row = compared price; name = the basis label | $1034.83 "After hours" | $1034.83 "after hours" | PASS |  |  |
| EQIX | L-sma200 | ladder row sma200: price and gap = price vs average | $1019.22, 1.5% | $1019.22, 1.5% | PASS |  |  |
| EQIX | L-sma50 | ladder row sma50: price and gap = price vs average | $1019.14, 1.5% | $1019.14, 1.5% | PASS |  |  |
| EQIX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,034.83 / entry $1,034.83 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| EQIX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| EQIX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.7 | 51.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| EQIX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +36.0% vs +11.2% | 36.1% vs 11.2% | PASS |  |  |
| EQIX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| EQIX | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.4 | 18.4 | PASS |  | Wilder, completed bars |
| EQIX | T4w | words "20 or more / below 20" | below 20 | ADX 18.4 | PASS |  |  |
| EQIX | T5 | "counted at the last close ($X, date)" = last completed bar | $1,034.83, Nov 17 | $1034.83, Nov 17 | PASS |  |  |
| EQIX | T6 | price vs 200-day average (S1 pattern sma values) | $1,034.83 vs $1,019.22 · +1.5% | $1034.83 vs $1019.22 · 1.5% | PASS |  |  |
| EQIX | T6w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T7 | price vs 50-day average (S1 pattern sma values) | $1,034.83 vs $1,019.14 · +1.5% | $1034.83 vs $1019.14 · 1.5% | PASS |  |  |
| EQIX | T7w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.7% over 30 td | +3.7% over 30 td | PASS |  |  |
| EQIX | T8r | word "rising" | still rising | rising | PASS |  |  |
| EQIX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| EQIX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.5% below $1,118.65 | 7.5% below $1118.65 | PASS |  | closing high would be 1110.63 |
| EQIX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.5% below | PASS |  |  |
| EQIX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,118.65 | $1118.6549839367933 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| EQIX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.79%, close location 0.36, OBV rising |
| EQIX | V2 | day change of the last completed bar | down 0.8% | -0.79% | PASS |  |  |
| EQIX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| EQIX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.24× | 1.02× / 0.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| EQIX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 594593) | 20 bars, last ('2026-11-17', 594593) | PASS |  |  |
| ETN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $340.00 | $340.00 | PASS |  |  |
| ETN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $364.94 | $364.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ETN | E3 | percent from the 21-day average | 6.8% below | 6.8% below | PASS |  |  |
| ETN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ETN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $18.05 | $18.05 (sr=18.0454) | PASS |  | Wilder ATR14 |
| ETN | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| ETN | L-ema21 | ladder row ema21: price and gap = price vs average | $364.94, -6.8% | $364.94, -6.8% | PASS |  |  |
| ETN | L-note | "Last close $X · date" note = last completed bar | Last close $337.11 · Nov 17 | $337.11 · Nov 17 | PASS |  |  |
| ETN | L-now | ladder price row = compared price; name = the basis label | $340 "After hours" | $340.00 "after hours" | PASS |  |  |
| ETN | L-sma200 | ladder row sma200: price and gap = price vs average | $395.33, -14.0% | $395.33, -14.0% | PASS |  |  |
| ETN | L-sma50 | ladder row sma50: price and gap = price vs average | $397.06, -14.4% | $397.06, -14.4% | PASS |  |  |
| ETN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $340.00 / entry $340.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| ETN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.30× / 0.01× | 1.30× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ETN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3435048) | 20 bars, last ('2026-11-17', 3435048) | PASS |  |  |
| FCX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $56.01 | $56.01 | PASS |  |  |
| FCX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $62.12 | $62.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FCX | E3 | percent from the 21-day average | 9.8% below | 9.8% below | PASS |  |  |
| FCX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| FCX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.82 | $2.82 (sr=2.8226) | PASS |  | Wilder ATR14 |
| FCX | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| FCX | L-ema21 | ladder row ema21: price and gap = price vs average | $62.12, -9.8% | $62.12, -9.8% | PASS |  |  |
| FCX | L-note | "Last close $X · date" note = last completed bar | Last close $55.30 · Nov 17 | $55.30 · Nov 17 | PASS |  |  |
| FCX | L-now | ladder price row = compared price; name = the basis label | $56.01 "After hours" | $56.01 "after hours" | PASS |  |  |
| FCX | L-sma200 | ladder row sma200: price and gap = price vs average | $64.91, -13.7% | $64.91, -13.7% | PASS |  |  |
| FCX | L-sma50 | ladder row sma50: price and gap = price vs average | $67.65, -17.2% | $67.65, -17.2% | PASS |  |  |
| FCX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $56.01 / entry $56.01 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| FCX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.26× / 0.04× | 1.26× / 0.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FCX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 14934793) | 20 bars, last ('2026-11-17', 14934793) | PASS |  |  |
| FINN.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $31.76 | $31.76 | PASS |  |  |
| FINN.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.68 | $32.68 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FINN.NE | E3 | percent from the 21-day average | 2.8% below | 2.8% below | PASS |  |  |
| FINN.NE | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| FINN.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.69 | $0.69 (sr=0.6884) | PASS |  | Wilder ATR14 |
| FINN.NE | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| FINN.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $32.68, -2.8% | $32.68, -2.8% | PASS |  |  |
| FINN.NE | L-now | ladder price row = compared price; name = the basis label | $31.76 "Last close" | $31.76 "last close" | PASS |  |  |
| FINN.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.08, 5.6% | $30.08, 5.6% | PASS |  |  |
| FINN.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $33.26, -4.5% | $33.26, -4.5% | PASS |  |  |
| FINN.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FINN.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.2 | 40.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FINN.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.7% vs +11.2% | 39.7% vs 11.2% | PASS |  |  |
| FINN.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FINN.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.6 | 13.6 | PASS |  | Wilder, completed bars |
| FINN.NE | T4w | words "20 or more / below 20" | below 20 | ADX 13.6 | PASS |  |  |
| FINN.NE | T6 | price vs 200-day average (S1 pattern sma values) | $31.76 vs $30.08 · +5.6% | $31.76 vs $30.08 · 5.6% | PASS |  |  |
| FINN.NE | T6w | word "Above" | Above | Above | PASS |  |  |
| FINN.NE | T7 | price vs 50-day average (S1 pattern sma values) | $31.76 vs $33.26 · -4.5% | $31.76 vs $33.26 · -4.5% | PASS |  |  |
| FINN.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| FINN.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.7% over 30 td | +4.7% over 30 td | PASS |  |  |
| FINN.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| FINN.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FINN.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.4% below $35.83 | 11.4% below $35.83 | PASS |  | closing high would be 35.43 |
| FINN.NE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.4% below | PASS |  |  |
| FINN.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $35.83 | $35.83000183105469 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FINN.NE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.06%, close location 0.31, OBV falling |
| FINN.NE | V2 | day change of the last completed bar | down 1.1% | -1.06% | PASS |  |  |
| FINN.NE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FINN.NE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.54× / 0.49× | 3.54× / 0.49× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FINN.NE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1115637) | 20 bars, last ('2026-11-17', 1115637) | PASS |  |  |
| FINN.NE | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.54, OBV falling | condition true | PASS |  |  |
| GDX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $80.45 | $80.45 | PASS |  |  |
| GDX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $83.6 | $83.60 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDX | E3 | percent from the 21-day average | 3.8% below | 3.8% below | PASS |  |  |
| GDX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GDX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.40 | $3.40 (sr=3.4036) | PASS |  | Wilder ATR14 |
| GDX | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves below |
| GDX | L-ema21 | ladder row ema21: price and gap = price vs average | $83.6, -3.8% | $83.60, -3.8% | PASS |  |  |
| GDX | L-note | "Last close $X · date" note = last completed bar | Last close $79.57 · Nov 17 | $79.57 · Nov 17 | PASS |  |  |
| GDX | L-now | ladder price row = compared price; name = the basis label | $80.45 "After hours" | $80.45 "after hours" | PASS |  |  |
| GDX | L-sma200 | ladder row sma200: price and gap = price vs average | $89.43, -10.0% | $89.43, -10.0% | PASS |  |  |
| GDX | L-sma50 | ladder row sma50: price and gap = price vs average | $87.48, -8.0% | $87.48, -8.0% | PASS |  |  |
| GDX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $80.45 / entry $80.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GDX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.0 | 42.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.9% vs +11.2% | 6.9% vs 11.2% | PASS |  |  |
| GDX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDX | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.6 | 17.6 | PASS |  | Wilder, completed bars |
| GDX | T4w | words "20 or more / below 20" | below 20 | ADX 17.6 | PASS |  |  |
| GDX | T5 | "counted at the last close ($X, date)" = last completed bar | $79.57, Nov 17 | $79.57, Nov 17 | PASS |  |  |
| GDX | T6 | price vs 200-day average (S1 pattern sma values) | $79.57 vs $89.43 · -11.0% | $79.57 vs $89.43 · -11.0% | PASS |  |  |
| GDX | T6w | word "Below" | Below | Below | PASS |  |  |
| GDX | T7 | price vs 50-day average (S1 pattern sma values) | $79.57 vs $87.48 · -9.0% | $79.57 vs $87.48 · -9.0% | PASS |  |  |
| GDX | T7w | word "Below" | Below | Below | PASS |  |  |
| GDX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.8% over 30 td | -1.8% over 30 td | PASS |  |  |
| GDX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 32.1% below $117.18 | 32.1% below $117.18 | PASS |  | closing high would be 115.84 |
| GDX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 32.1% below | PASS |  |  |
| GDX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $117.18 | $117.18000030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.79%, close location 0.31, OBV falling |
| GDX | V2 | day change of the last completed bar | up 0.8% | +0.79% | PASS |  |  |
| GDX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.01× / 0.18× | 1.01× / 0.18× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 21405423) | 20 bars, last ('2026-11-17', 21405423) | PASS |  |  |
| GDXU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $24.60 | $24.60 | PASS |  |  |
| GDXU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $27.8 | $27.80 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDXU.TO | E3 | percent from the 21-day average | 11.5% below | 11.5% below | PASS |  |  |
| GDXU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GDXU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.33 | $2.33 (sr=2.3285) | PASS |  | Wilder ATR14 |
| GDXU.TO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| GDXU.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| GDXU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $27.8, -11.5% | $27.80, -11.5% | PASS |  |  |
| GDXU.TO | L-now | ladder price row = compared price; name = the basis label | $24.6 "Last close" | $24.60 "last close" | PASS |  |  |
| GDXU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $35.88, -31.4% | $35.88, -31.4% | PASS |  |  |
| GDXU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $31.37, -21.6% | $31.37, -21.6% | PASS |  |  |
| GDXU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDXU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.6 | 40.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDXU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -16.9% vs +11.2% | -16.9% vs 11.2% | PASS |  |  |
| GDXU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDXU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.4 | 18.4 | PASS |  | Wilder, completed bars |
| GDXU.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.4 | PASS |  |  |
| GDXU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $24.60 vs $35.88 · -31.4% | $24.60 vs $35.88 · -31.4% | PASS |  |  |
| GDXU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $24.60 vs $31.37 · -21.6% | $24.60 vs $31.37 · -21.6% | PASS |  |  |
| GDXU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -6.6% over 30 td | -6.6% over 30 td | PASS |  |  |
| GDXU.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDXU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDXU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 62.2% below $65.00 | 62.2% below $65.00 | PASS |  | closing high would be 63.22 |
| GDXU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 62.2% below | PASS |  |  |
| GDXU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $65.00 | $65 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDXU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 1.23%, close location 0.26, OBV falling |
| GDXU.TO | V2 | day change of the last completed bar | up 1.2% | +1.23% | PASS |  |  |
| GDXU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDXU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.50× / 0.13× | 1.50× / 0.13× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDXU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 345017) | 20 bars, last ('2026-11-17', 345017) | PASS |  |  |
| GDXU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.50, OBV falling | condition true | PASS |  |  |
| GE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $326.50 | $326.50 | PASS |  |  |
| GE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $321.2 | $321.20 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GE | E3 | percent from the 21-day average | 1.7% above | 1.7% above | PASS |  |  |
| GE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.23 | $10.23 (sr=10.2347) | PASS |  | Wilder ATR14 |
| GE | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| GE | L-ema21 | ladder row ema21: price and gap = price vs average | $321.2, 1.7% | $321.20, 1.7% | PASS |  |  |
| GE | L-note | "Last close $X · date" note = last completed bar | Last close $326.40 · Nov 17 | $326.40 · Nov 17 | PASS |  |  |
| GE | L-now | ladder price row = compared price; name = the basis label | $326.5 "After hours" | $326.50 "after hours" | PASS |  |  |
| GE | L-sma200 | ladder row sma200: price and gap = price vs average | $323.39, 1.0% | $323.39, 1.0% | PASS |  |  |
| GE | L-sma50 | ladder row sma50: price and gap = price vs average | $314.2, 3.9% | $314.20, 3.9% | PASS |  |  |
| GE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $326.50 / entry $326.50 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.0 | 54.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +9.3% vs +11.2% | 9.3% vs 11.2% | PASS |  |  |
| GE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GE | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.4 | 21.4 | PASS |  | Wilder, completed bars |
| GE | T4w | words "20 or more / below 20" | 20 or more | ADX 21.4 | PASS |  |  |
| GE | T5 | "counted at the last close ($X, date)" = last completed bar | $326.40, Nov 17 | $326.40, Nov 17 | PASS |  |  |
| GE | T6 | price vs 200-day average (S1 pattern sma values) | $326.40 vs $323.40 · +0.9% | $326.40 vs $323.39 · 0.9% | PASS |  |  |
| GE | T6w | word "Above" | Above | Above | PASS |  |  |
| GE | T7 | price vs 50-day average (S1 pattern sma values) | $326.40 vs $314.20 · +3.9% | $326.40 vs $314.20 · 3.9% | PASS |  |  |
| GE | T7w | word "Above" | Above | Above | PASS |  |  |
| GE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| GE | T8r | word "rising" | still rising | rising | PASS |  |  |
| GE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 15.9% below $388.25 | 15.9% below $388.25 | PASS |  | closing high would be 380.64 |
| GE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 15.9% below | PASS |  |  |
| GE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $388.25 | $388.2496041459131 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.38%, close location 0.43, OBV rising |
| GE | V2 | day change of the last completed bar | up 0.4% | +0.38% | PASS |  |  |
| GE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.77× / 0.12× | 0.77× / 0.12× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3745191) | 20 bars, last ('2026-11-17', 3745191) | PASS |  |  |
| GEV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $793.00 | $793.00 | PASS |  |  |
| GEV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $837.86 | $837.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV | E3 | percent from the 21-day average | 5.4% below | 5.4% below | PASS |  |  |
| GEV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GEV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $55.44 | $55.44 (sr=55.4387) | PASS |  | Wilder ATR14 |
| GEV | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| GEV | L-ema21 | ladder row ema21: price and gap = price vs average | $837.86, -5.4% | $837.86, -5.4% | PASS |  |  |
| GEV | L-note | "Last close $X · date" note = last completed bar | Last close $779.91 · Nov 17 | $779.91 · Nov 17 | PASS |  |  |
| GEV | L-now | ladder price row = compared price; name = the basis label | $793 "After hours" | $793.00 "after hours" | PASS |  |  |
| GEV | L-sma200 | ladder row sma200: price and gap = price vs average | $951.29, -16.6% | $951.29, -16.6% | PASS |  |  |
| GEV | L-sma50 | ladder row sma50: price and gap = price vs average | $905.41, -12.4% | $905.41, -12.4% | PASS |  |  |
| GEV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $793.00 / entry $793.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GEV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GEV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.0 | 40.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +35.5% vs +11.2% | 35.5% vs 11.2% | PASS |  |  |
| GEV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.5 | 24.5 | PASS |  | Wilder, completed bars |
| GEV | T4w | words "20 or more / below 20" | 20 or more | ADX 24.5 | PASS |  |  |
| GEV | T5 | "counted at the last close ($X, date)" = last completed bar | $779.91, Nov 17 | $779.91, Nov 17 | PASS |  |  |
| GEV | T6 | price vs 200-day average (S1 pattern sma values) | $779.91 vs $951.29 · -18.0% | $779.91 vs $951.29 · -18.0% | PASS |  |  |
| GEV | T6w | word "Below" | Below | Below | PASS |  |  |
| GEV | T7 | price vs 50-day average (S1 pattern sma values) | $779.91 vs $905.41 · -13.9% | $779.91 vs $905.41 · -13.9% | PASS |  |  |
| GEV | T7w | word "Below" | Below | Below | PASS |  |  |
| GEV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.4% over 30 td | +3.4% over 30 td | PASS |  |  |
| GEV | T8r | word "rising" | still rising | rising | PASS |  |  |
| GEV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GEV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.7% below $1,195.24 | 34.7% below $1195.24 | PASS |  | closing high would be 1174.17 |
| GEV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.7% below | PASS |  |  |
| GEV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,195.24 | $1195.2406896758491 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GEV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 2.14%, close location 0.60, OBV rising |
| GEV | V2 | day change of the last completed bar | up 2.1% | +2.14% | PASS |  |  |
| GEV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GEV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.59× / 0.30× | 1.59× / 0.30× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 4970531) | 20 bars, last ('2026-11-17', 4970531) | PASS |  |  |
| GEV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $52.13 | $52.13 | PASS |  |  |
| GEV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $56.03 | $56.03 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV.TO | E3 | percent from the 21-day average | 7.0% below | 7.0% below | PASS |  |  |
| GEV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GEV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.60 | $3.60 (sr=3.6033) | PASS |  | Wilder ATR14 |
| GEV.TO | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| GEV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $56.03, -7.0% | $56.03, -7.0% | PASS |  |  |
| GEV.TO | L-now | ladder price row = compared price; name = the basis label | $52.13 "Last close" | $52.13 "last close" | PASS |  |  |
| GEV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.09, -18.7% | $64.09, -18.7% | PASS |  |  |
| GEV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $60.58, -13.9% | $60.58, -13.9% | PASS |  |  |
| GEV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.9 | 39.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.8% vs +11.2% | 15.8% vs 11.2% | PASS |  |  |
| GEV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.1 | 24.1 | PASS |  | Wilder, completed bars |
| GEV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 24.1 | PASS |  |  |
| GEV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 2.16%, close location 0.61, OBV falling |
| GEV.TO | V2 | day change of the last completed bar | up 2.2% | +2.16% | PASS |  |  |
| GEV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.52× / 0.31× | 1.52× / 0.31× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 112620) | 20 bars, last ('2026-11-17', 112620) | PASS |  |  |
| GEV.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.52, OBV falling | condition true | PASS |  |  |
| GGLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $64.79 | $64.79 | PASS |  |  |
| GGLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.96 | $73.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GGLL | E3 | percent from the 21-day average | 12.4% below | 12.4% below | PASS |  |  |
| GGLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GGLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.10 | $5.10 (sr=5.0966) | PASS |  | Wilder ATR14 |
| GGLL | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| GGLL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.5 | +5.5 | PASS |  |  |
| GGLL | L-ema21 | ladder row ema21: price and gap = price vs average | $73.96, -12.4% | $73.96, -12.4% | PASS |  |  |
| GGLL | L-note | "Last close $X · date" note = last completed bar | Last close $63.05 · Nov 17 | $63.05 · Nov 17 | PASS |  |  |
| GGLL | L-now | ladder price row = compared price; name = the basis label | $64.79 "After hours" | $64.79 "after hours" | PASS |  |  |
| GGLL | L-sma200 | ladder row sma200: price and gap = price vs average | $102.04, -36.5% | $102.04, -36.5% | PASS |  |  |
| GGLL | L-sma50 | ladder row sma50: price and gap = price vs average | $89.08, -27.3% | $89.08, -27.3% | PASS |  |  |
| GGLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $64.79 / entry $64.79 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GGLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GGLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.4 | 31.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GGLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -21.9% vs +11.2% | -21.9% vs 11.2% | PASS |  |  |
| GGLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GGLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.8 | 27.8 | PASS |  | Wilder, completed bars |
| GGLL | T4w | words "20 or more / below 20" | 20 or more | ADX 27.8 | PASS |  |  |
| GGLL | T5 | "counted at the last close ($X, date)" = last completed bar | $63.05, Nov 17 | $63.05, Nov 17 | PASS |  |  |
| GGLL | T6 | price vs 200-day average (S1 pattern sma values) | $63.05 vs $102.04 · -38.2% | $63.05 vs $102.04 · -38.2% | PASS |  |  |
| GGLL | T6w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T7 | price vs 50-day average (S1 pattern sma values) | $63.05 vs $89.08 · -29.2% | $63.05 vs $89.08 · -29.2% | PASS |  |  |
| GGLL | T7w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.8% over 30 td | -2.8% over 30 td | PASS |  |  |
| GGLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GGLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GGLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 58.3% below $151.33 | 58.3% below $151.33 | PASS |  | closing high would be 147.32 |
| GGLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 58.3% below | PASS |  |  |
| GGLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $151.33 | $151.33257083400454 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GGLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.75%, close location 0.23, OBV falling |
| GGLL | V2 | day change of the last completed bar | down 2.8% | -2.75% | PASS |  |  |
| GGLL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.23 (raw 0.2302) | PASS |  |  |
| GGLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GGLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.55× / 0.34× | 0.55× / 0.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GGLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1059048) | 20 bars, last ('2026-11-17', 1059048) | PASS |  |  |
| GIB-A.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $115.07 | $115.07 | PASS |  |  |
| GIB-A.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.44 | $113.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GIB-A.TO | E3 | percent from the 21-day average | 1.4% above | 1.4% above | PASS |  |  |
| GIB-A.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GIB-A.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.72 | $2.72 (sr=2.7154) | PASS |  | Wilder ATR14 |
| GIB-A.TO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| GIB-A.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.0 | -5.0 | PASS |  |  |
| GIB-A.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.44, 1.4% | $113.44, 1.4% | PASS |  |  |
| GIB-A.TO | L-note | "Last close $X · date" note = last completed bar | Last close $115.07 · Nov 17 | $115.07 · Nov 17 | PASS |  |  |
| GIB-A.TO | L-now | ladder price row = compared price; name = the basis label | $115.07 "After hours" | $115.07 "after hours" | PASS |  |  |
| GIB-A.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $99.81, 15.3% | $99.81, 15.3% | PASS |  |  |
| GIB-A.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $105.74, 8.8% | $105.74, 8.8% | PASS |  |  |
| GIB-A.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $115.07 / entry $115.07 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GIB-A.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GIB-A.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.3 | 59.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GIB-A.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.3% vs +11.2% | -4.3% vs 11.2% | PASS |  |  |
| GIB-A.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GIB-A.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 41.7 | 41.7 | PASS |  | Wilder, completed bars |
| GIB-A.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 41.7 | PASS |  |  |
| GIB-A.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $115.07, Nov 17 | $115.07, Nov 17 | PASS |  |  |
| GIB-A.TO | T6 | price vs 200-day average (S1 pattern sma values) | $115.07 vs $99.81 · +15.3% | $115.07 vs $99.81 · 15.3% | PASS |  |  |
| GIB-A.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T7 | price vs 50-day average (S1 pattern sma values) | $115.07 vs $105.74 · +8.8% | $115.07 vs $105.74 · 8.8% | PASS |  |  |
| GIB-A.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.1% over 30 td | -2.1% over 30 td | PASS |  |  |
| GIB-A.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GIB-A.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GIB-A.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.3% below $131.27 | 12.3% below $131.27 | PASS |  | closing high would be 130.81 |
| GIB-A.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.3% below | PASS |  |  |
| GIB-A.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.27 | $131.26875042581284 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GIB-A.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -1.08%, close location 0.72, OBV rising |
| GIB-A.TO | V2 | day change of the last completed bar | down 1.1% | -1.08% | PASS |  |  |
| GIB-A.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GIB-A.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.05× / 0.46× | 1.05× / 0.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GIB-A.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 657640) | 20 bars, last ('2026-11-17', 657640) | PASS |  |  |
| GOOGL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $280.20 | $280.20 | PASS |  |  |
| GOOGL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $299.92 | $299.92 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GOOGL | E3 | percent from the 21-day average | 6.6% below | 6.6% below | PASS |  |  |
| GOOGL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GOOGL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.13 | $10.13 (sr=10.1258) | PASS |  | Wilder ATR14 |
| GOOGL | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| GOOGL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| GOOGL | L-ema21 | ladder row ema21: price and gap = price vs average | $299.92, -6.6% | $299.92, -6.6% | PASS |  |  |
| GOOGL | L-note | "Last close $X · date" note = last completed bar | Last close $280.20 · Nov 17 | $280.20 · Nov 17 | PASS |  |  |
| GOOGL | L-now | ladder price row = compared price; name = the basis label | $280.2 "After hours" | $280.20 "after hours" | PASS |  |  |
| GOOGL | L-sma200 | ladder row sma200: price and gap = price vs average | $337.62, -17.0% | $337.62, -17.0% | PASS |  |  |
| GOOGL | L-sma50 | ladder row sma50: price and gap = price vs average | $325.93, -14.0% | $325.93, -14.0% | PASS |  |  |
| GOOGL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $280.20 / entry $280.20 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GOOGL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GOOGL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.9 | 32.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GOOGL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.4% vs +11.2% | -1.4% vs 11.2% | PASS |  |  |
| GOOGL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GOOGL | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.9 | 25.9 | PASS |  | Wilder, completed bars |
| GOOGL | T4w | words "20 or more / below 20" | 20 or more | ADX 25.9 | PASS |  |  |
| GOOGL | T5 | "counted at the last close ($X, date)" = last completed bar | $280.20, Nov 17 | $280.20, Nov 17 | PASS |  |  |
| GOOGL | T6 | price vs 200-day average (S1 pattern sma values) | $280.20 vs $337.62 · -17.0% | $280.20 vs $337.62 · -17.0% | PASS |  |  |
| GOOGL | T6w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T7 | price vs 50-day average (S1 pattern sma values) | $280.20 vs $325.93 · -14.0% | $280.20 vs $325.93 · -14.0% | PASS |  |  |
| GOOGL | T7w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.4% over 30 td | -0.4% over 30 td | PASS |  |  |
| GOOGL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GOOGL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GOOGL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 31.3% below $408.10 | 31.3% below $408.10 | PASS |  | closing high would be 402.12 |
| GOOGL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 31.3% below | PASS |  |  |
| GOOGL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $408.10 | $408.10376741205215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GOOGL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.24%, close location 0.31, OBV falling |
| GOOGL | V2 | day change of the last completed bar | down 1.2% | -1.24% | PASS |  |  |
| GOOGL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GOOGL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 0.34× | 0.97× / 0.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GOOGL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 31276136) | 20 bars, last ('2026-11-17', 31276136) | PASS |  |  |
| GRID | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $155.15 | $155.15 | PASS |  |  |
| GRID | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $162.88 | $162.88 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GRID | E3 | percent from the 21-day average | 4.7% below | 4.7% below | PASS |  |  |
| GRID | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GRID | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.26 | $4.26 (sr=4.2625) | PASS |  | Wilder ATR14 |
| GRID | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| GRID | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| GRID | L-ema21 | ladder row ema21: price and gap = price vs average | $162.88, -4.7% | $162.88, -4.7% | PASS |  |  |
| GRID | L-note | "Last close $X · date" note = last completed bar | Last close $155.15 · Nov 17 | $155.15 · Nov 17 | PASS |  |  |
| GRID | L-now | ladder price row = compared price; name = the basis label | $155.15 "After hours" | $155.15 "after hours" | PASS |  |  |
| GRID | L-sma200 | ladder row sma200: price and gap = price vs average | $177.95, -12.8% | $177.95, -12.8% | PASS |  |  |
| GRID | L-sma50 | ladder row sma50: price and gap = price vs average | $171.37, -9.5% | $171.37, -9.5% | PASS |  |  |
| GRID | S5-price | S5: the same live price reads the same on the header and the Entry block | header $155.15 / entry $155.15 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GRID | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GRID | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.4 | 37.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GRID | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.9% vs +11.2% | 3.9% vs 11.2% | PASS |  |  |
| GRID | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GRID | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.8 | 29.8 | PASS |  | Wilder, completed bars |
| GRID | T4w | words "20 or more / below 20" | 20 or more | ADX 29.8 | PASS |  |  |
| GRID | T5 | "counted at the last close ($X, date)" = last completed bar | $155.15, Nov 17 | $155.15, Nov 17 | PASS |  |  |
| GRID | T6 | price vs 200-day average (S1 pattern sma values) | $155.15 vs $177.95 · -12.8% | $155.15 vs $177.95 · -12.8% | PASS |  |  |
| GRID | T6w | word "Below" | Below | Below | PASS |  |  |
| GRID | T7 | price vs 50-day average (S1 pattern sma values) | $155.15 vs $171.37 · -9.5% | $155.15 vs $171.37 · -9.5% | PASS |  |  |
| GRID | T7w | word "Below" | Below | Below | PASS |  |  |
| GRID | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.8% over 30 td | +0.8% over 30 td | PASS |  |  |
| GRID | T8r | word "rising" | still rising | rising | PASS |  |  |
| GRID | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GRID | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 22.0% below $198.79 | 22.0% below $198.79 | PASS |  | closing high would be 198.61 |
| GRID | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 22.0% below | PASS |  |  |
| GRID | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $198.79 | $198.7949156186822 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GRID | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.63%, close location 0.43, OBV falling |
| GRID | V2 | day change of the last completed bar | down 0.6% | -0.63% | PASS |  |  |
| GRID | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GRID | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.00× / 0.23× | 1.00× / 0.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GRID | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 587384) | 20 bars, last ('2026-11-17', 587384) | PASS |  |  |
| HD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $339.01 | $339.01 | PASS |  |  |
| HD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $335.85 | $335.85 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HD | E3 | percent from the 21-day average | 0.9% above | 0.9% above | PASS |  |  |
| HD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| HD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.92 | $8.92 (sr=8.9189) | PASS |  | Wilder ATR14 |
| HD | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves above |
| HD | L-ema21 | ladder row ema21: price and gap = price vs average | $335.85, 0.9% | $335.85, 0.9% | PASS |  |  |
| HD | L-note | "Last close $X · date" note = last completed bar | Last close $339.01 · Nov 17 | $339.01 · Nov 17 | PASS |  |  |
| HD | L-now | ladder price row = compared price; name = the basis label | $339.01 "After hours" | $339.01 "after hours" | PASS |  |  |
| HD | L-sma200 | ladder row sma200: price and gap = price vs average | $329.18, 3.0% | $329.18, 3.0% | PASS |  |  |
| HD | L-sma50 | ladder row sma50: price and gap = price vs average | $313.19, 8.2% | $313.19, 8.2% | PASS |  |  |
| HD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $339.01 / entry $339.01 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| HD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.3 | 55.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.6% vs +11.2% | -2.7% vs 11.2% | PASS |  |  |
| HD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HD | T4 | ADX 14 (S1 /api/sr meta.adx) | 42.7 | 42.6 | PASS |  | Wilder, completed bars |
| HD | T4w | words "20 or more / below 20" | 20 or more | ADX 42.6 | PASS |  |  |
| HD | T5 | "counted at the last close ($X, date)" = last completed bar | $339.01, Nov 17 | $339.01, Nov 17 | PASS |  |  |
| HD | T6 | price vs 200-day average (S1 pattern sma values) | $339.01 vs $329.18 · +3.0% | $339.01 vs $329.18 · 3.0% | PASS |  |  |
| HD | T6w | word "Above" | Above | Above | PASS |  |  |
| HD | T7 | price vs 50-day average (S1 pattern sma values) | $339.01 vs $313.19 · +8.2% | $339.01 vs $313.19 · 8.2% | PASS |  |  |
| HD | T7w | word "Above" | Above | Above | PASS |  |  |
| HD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.4% over 30 td | -1.4% over 30 td | PASS |  |  |
| HD | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.9% below $389.24 | 12.9% below $389.24 | PASS |  | closing high would be 382.80 |
| HD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.9% below | PASS |  |  |
| HD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $389.24 | $389.24026 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.45%, close location 0.37, OBV falling |
| HD | V2 | day change of the last completed bar | down 2.5% | -2.45% | PASS |  |  |
| HD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.41× / 0.93× | 1.41× / 0.93× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 7101969) | 20 bars, last ('2026-11-17', 7101969) | PASS |  |  |
| HURA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $37.39 | $37.39 | PASS |  |  |
| HURA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.51 | $40.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HURA.TO | E3 | percent from the 21-day average | 7.7% below | 7.7% below | PASS |  |  |
| HURA.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HURA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.39 | $1.39 (sr=1.3939) | PASS |  | Wilder ATR14 |
| HURA.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| HURA.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +9.0 | +9.0 | PASS |  |  |
| HURA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.51, -7.7% | $40.51, -7.7% | PASS |  |  |
| HURA.TO | L-now | ladder price row = compared price; name = the basis label | $37.39 "Last close" | $37.39 "last close" | PASS |  |  |
| HURA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $53.03, -29.5% | $53.03, -29.5% | PASS |  |  |
| HURA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $44.28, -15.6% | $44.28, -15.6% | PASS |  |  |
| HURA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HURA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.4 | 35.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HURA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -26.5% vs +11.2% | -26.5% vs 11.2% | PASS |  |  |
| HURA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HURA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.6 | 29.6 | PASS |  | Wilder, completed bars |
| HURA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 29.6 | PASS |  |  |
| HURA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $37.39 vs $53.03 · -29.5% | $37.39 vs $53.03 · -29.5% | PASS |  |  |
| HURA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $37.39 vs $44.28 · -15.6% | $37.39 vs $44.28 · -15.6% | PASS |  |  |
| HURA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.0% over 30 td | -5.0% over 30 td | PASS |  |  |
| HURA.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HURA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HURA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.4% below $73.95 | 49.4% below $73.95 | PASS |  | closing high would be 73.19 |
| HURA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.4% below | PASS |  |  |
| HURA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $73.95 | $73.94999694824219 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HURA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.40%, close location 1.00, OBV falling |
| HURA.TO | V2 | day change of the last completed bar | down 0.4% | -0.40% | PASS |  |  |
| HURA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 1.00 (raw 1.0000) | PASS |  |  |
| HURA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HURA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.66× / 0.11× | 0.66× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HURA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 7942) | 20 bars, last ('2026-11-17', 7942) | PASS |  |  |
| HXQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $110.63 | $110.63 | PASS |  |  |
| HXQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $115.24 | $115.24 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HXQ.TO | E3 | percent from the 21-day average | 4.0% below | 4.0% below | PASS |  |  |
| HXQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HXQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.66 | $2.66 (sr=2.6634) | PASS |  | Wilder ATR14 |
| HXQ.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| HXQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $115.24, -4.0% | $115.24, -4.0% | PASS |  |  |
| HXQ.TO | L-now | ladder price row = compared price; name = the basis label | $110.63 "Last close" | $110.63 "last close" | PASS |  |  |
| HXQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $112.24, -1.4% | $112.24, -1.4% | PASS |  |  |
| HXQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $119.19, -7.2% | $119.19, -7.2% | PASS |  |  |
| HXQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HXQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.5 | 38.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HXQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.7% vs +11.2% | 10.7% vs 11.2% | PASS |  |  |
| HXQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HXQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.9 | 30.9 | PASS |  | Wilder, completed bars |
| HXQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.9 | PASS |  |  |
| HXQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $110.63 vs $112.24 · -1.4% | $110.63 vs $112.24 · -1.4% | PASS |  |  |
| HXQ.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $110.63 vs $119.19 · -7.2% | $110.63 vs $119.19 · -7.2% | PASS |  |  |
| HXQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| HXQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| HXQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HXQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.8% below $128.37 | 13.8% below $128.37 | PASS |  | closing high would be 127.79 |
| HXQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.8% below | PASS |  |  |
| HXQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $128.37 | $128.3699951171875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HXQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.11%, close location 0.43, OBV falling |
| HXQ.TO | V2 | day change of the last completed bar | down 1.1% | -1.11% | PASS |  |  |
| HXQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HXQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 0.46× | 1.11× / 0.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HXQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 36208) | 20 bars, last ('2026-11-17', 36208) | PASS |  |  |
| JNJ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $278.70 | $278.70 | PASS |  |  |
| JNJ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $274.56 | $274.56 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JNJ | E3 | percent from the 21-day average | 1.5% above | 1.5% above | PASS |  |  |
| JNJ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JNJ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.76 | $6.76 (sr=6.7573) | PASS |  | Wilder ATR14 |
| JNJ | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| JNJ | L-ema21 | ladder row ema21: price and gap = price vs average | $274.56, 1.5% | $274.56, 1.5% | PASS |  |  |
| JNJ | L-note | "Last close $X · date" note = last completed bar | Last close $278.70 · Nov 17 | $278.70 · Nov 17 | PASS |  |  |
| JNJ | L-now | ladder price row = compared price; name = the basis label | $278.7 "After hours" | $278.70 "after hours" | PASS |  |  |
| JNJ | L-sma200 | ladder row sma200: price and gap = price vs average | $248.86, 12.0% | $248.86, 12.0% | PASS |  |  |
| JNJ | L-sma50 | ladder row sma50: price and gap = price vs average | $267.2, 4.3% | $267.20, 4.3% | PASS |  |  |
| JNJ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $278.70 / entry $278.70 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JNJ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JNJ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.5 | 56.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JNJ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +42.8% vs +11.2% | 42.8% vs 11.2% | PASS |  |  |
| JNJ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JNJ | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.0 | 26.0 | PASS |  | Wilder, completed bars |
| JNJ | T4w | words "20 or more / below 20" | 20 or more | ADX 26.0 | PASS |  |  |
| JNJ | T5 | "counted at the last close ($X, date)" = last completed bar | $278.70, Nov 17 | $278.70, Nov 17 | PASS |  |  |
| JNJ | T6 | price vs 200-day average (S1 pattern sma values) | $278.70 vs $248.86 · +12.0% | $278.70 vs $248.86 · 12.0% | PASS |  |  |
| JNJ | T6w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T7 | price vs 50-day average (S1 pattern sma values) | $278.70 vs $267.20 · +4.3% | $278.70 vs $267.20 · 4.3% | PASS |  |  |
| JNJ | T7w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| JNJ | T8r | word "rising" | still rising | rising | PASS |  |  |
| JNJ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JNJ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.0% below $290.25 | 4.0% below $290.25 | PASS |  | closing high would be 285.75 |
| JNJ | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.0% below | PASS |  |  |
| JNJ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $290.25 | $290.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JNJ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.36%, close location 0.27, OBV falling |
| JNJ | V2 | day change of the last completed bar | down 1.4% | -1.36% | PASS |  |  |
| JNJ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JNJ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.10× / 0.56× | 1.10× / 0.56× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JNJ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 8057459) | 20 bars, last ('2026-11-17', 8057459) | PASS |  |  |
| JPM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $329.96 | $329.96 | PASS |  |  |
| JPM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $339.05 | $339.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JPM | E3 | percent from the 21-day average | 2.7% below | 2.7% below | PASS |  |  |
| JPM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JPM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.46 | $7.46 (sr=7.4579) | PASS |  | Wilder ATR14 |
| JPM | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| JPM | L-ema21 | ladder row ema21: price and gap = price vs average | $339.05, -2.7% | $339.05, -2.7% | PASS |  |  |
| JPM | L-note | "Last close $X · date" note = last completed bar | Last close $329.96 · Nov 17 | $329.96 · Nov 17 | PASS |  |  |
| JPM | L-now | ladder price row = compared price; name = the basis label | $329.96 "After hours" | $329.96 "after hours" | PASS |  |  |
| JPM | L-sma200 | ladder row sma200: price and gap = price vs average | $322.75, 2.2% | $322.75, 2.2% | PASS |  |  |
| JPM | L-sma50 | ladder row sma50: price and gap = price vs average | $338.9, -2.6% | $338.89, -2.6% | PASS |  |  |
| JPM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $329.96 / entry $329.96 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JPM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JPM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.1 | 42.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JPM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +12.0% vs +11.2% | 12.0% vs 11.2% | PASS |  |  |
| JPM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JPM | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.4 | 16.4 | PASS |  | Wilder, completed bars |
| JPM | T4w | words "20 or more / below 20" | below 20 | ADX 16.4 | PASS |  |  |
| JPM | T5 | "counted at the last close ($X, date)" = last completed bar | $329.96, Nov 17 | $329.96, Nov 17 | PASS |  |  |
| JPM | T6 | price vs 200-day average (S1 pattern sma values) | $329.96 vs $322.75 · +2.2% | $329.96 vs $322.75 · 2.2% | PASS |  |  |
| JPM | T6w | word "Above" | Above | Above | PASS |  |  |
| JPM | T7 | price vs 50-day average (S1 pattern sma values) | $329.96 vs $338.90 · -2.6% | $329.96 vs $338.89 · -2.6% | PASS |  |  |
| JPM | T7w | word "Below" | Below | Below | PASS |  |  |
| JPM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.2% over 30 td | +1.2% over 30 td | PASS |  |  |
| JPM | T8r | word "rising" | still rising | rising | PASS |  |  |
| JPM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JPM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 9.5% below $364.68 | 9.5% below $364.68 | PASS |  | closing high would be 363.37 |
| JPM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 9.5% below | PASS |  |  |
| JPM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $364.68 | $364.68062001340013 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JPM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.44%, close location 0.15, OBV falling |
| JPM | V2 | day change of the last completed bar | down 2.4% | -2.44% | PASS |  |  |
| JPM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1497) | PASS |  |  |
| JPM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JPM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.07× / 1.08× | 1.07× / 1.08× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JPM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 8112161) | 20 bars, last ('2026-11-17', 8112161) | PASS |  |  |
| KEYS | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $288.70 | $288.70 | PASS |  |  |
| KEYS | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $305.76 | $305.76 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| KEYS | E3 | percent from the 21-day average | 5.6% below | 5.6% below | PASS |  |  |
| KEYS | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| KEYS | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $15.94 | $15.94 (sr=15.9426) | PASS |  | Wilder ATR14 |
| KEYS | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| KEYS | L-ema21 | ladder row ema21: price and gap = price vs average | $305.76, -5.6% | $305.76, -5.6% | PASS |  |  |
| KEYS | L-note | "Last close $X · date" note = last completed bar | Last close $284.45 · Nov 17 | $284.45 · Nov 17 | PASS |  |  |
| KEYS | L-now | ladder price row = compared price; name = the basis label | $288.7 "After hours" | $288.70 "after hours" | PASS |  |  |
| KEYS | L-sma200 | ladder row sma200: price and gap = price vs average | $321.12, -10.1% | $321.12, -10.1% | PASS |  |  |
| KEYS | L-sma50 | ladder row sma50: price and gap = price vs average | $333.21, -13.4% | $333.21, -13.4% | PASS |  |  |
| KEYS | S5-price | S5: the same live price reads the same on the header and the Entry block | header $288.70 / entry $288.70 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| KEYS | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| KEYS | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.0 | 39.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| KEYS | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +62.1% vs +11.2% | 62.1% vs 11.2% | PASS |  |  |
| KEYS | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| KEYS | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.0 | 35.0 | PASS |  | Wilder, completed bars |
| KEYS | T4w | words "20 or more / below 20" | 20 or more | ADX 35.0 | PASS |  |  |
| KEYS | T5 | "counted at the last close ($X, date)" = last completed bar | $284.45, Nov 17 | $284.45, Nov 17 | PASS |  |  |
| KEYS | T6 | price vs 200-day average (S1 pattern sma values) | $284.45 vs $321.12 · -11.4% | $284.45 vs $321.12 · -11.4% | PASS |  |  |
| KEYS | T6w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T7 | price vs 50-day average (S1 pattern sma values) | $284.45 vs $333.21 · -14.6% | $284.45 vs $333.21 · -14.6% | PASS |  |  |
| KEYS | T7w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.5% over 30 td | +5.5% over 30 td | PASS |  |  |
| KEYS | T8r | word "rising" | still rising | rising | PASS |  |  |
| KEYS | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| KEYS | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.1% below $389.93 | 27.1% below $389.93 | PASS |  | closing high would be 388.03 |
| KEYS | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.1% below | PASS |  |  |
| KEYS | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $389.93 | $389.92999267578125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| KEYS | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.41%, close location 0.42, OBV falling |
| KEYS | V2 | day change of the last completed bar | down 0.4% | -0.41% | PASS |  |  |
| KEYS | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| KEYS | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.40× / 0.07× | 1.40× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| KEYS | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1835592) | 20 bars, last ('2026-11-17', 1835592) | PASS |  |  |
| LIN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $514.18 | $514.18 | PASS |  |  |
| LIN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $513.65 | $513.65 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LIN | E3 | percent from the 21-day average | 0.1% above | 0.1% above | PASS |  |  |
| LIN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| LIN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.01 | $9.01 (sr=9.0129) | PASS |  | Wilder ATR14 |
| LIN | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| LIN | L-ema21 | ladder row ema21: price and gap = price vs average | $513.65, 0.1% | $513.65, 0.1% | PASS |  |  |
| LIN | L-note | "Last close $X · date" note = last completed bar | Last close $515.11 · Nov 17 | $515.11 · Nov 17 | PASS |  |  |
| LIN | L-now | ladder price row = compared price; name = the basis label | $514.18 "After hours" | $514.18 "after hours" | PASS |  |  |
| LIN | L-sma200 | ladder row sma200: price and gap = price vs average | $495.22, 3.8% | $495.22, 3.8% | PASS |  |  |
| LIN | L-sma50 | ladder row sma50: price and gap = price vs average | $492.05, 4.5% | $492.05, 4.5% | PASS |  |  |
| LIN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $514.18 / entry $514.18 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LIN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LIN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.0 | 53.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LIN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +24.9% vs +11.2% | 24.9% vs 11.2% | PASS |  |  |
| LIN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LIN | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.1 | 32.1 | PASS |  | Wilder, completed bars |
| LIN | T4w | words "20 or more / below 20" | 20 or more | ADX 32.1 | PASS |  |  |
| LIN | T5 | "counted at the last close ($X, date)" = last completed bar | $515.11, Nov 17 | $515.11, Nov 17 | PASS |  |  |
| LIN | T6 | price vs 200-day average (S1 pattern sma values) | $515.11 vs $495.22 · +4.0% | $515.11 vs $495.22 · 4.0% | PASS |  |  |
| LIN | T6w | word "Above" | Above | Above | PASS |  |  |
| LIN | T7 | price vs 50-day average (S1 pattern sma values) | $515.11 vs $492.05 · +4.7% | $515.11 vs $492.05 · 4.7% | PASS |  |  |
| LIN | T7w | word "Above" | Above | Above | PASS |  |  |
| LIN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| LIN | T8r | word "rising" | still rising | rising | PASS |  |  |
| LIN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LIN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.7% below $546.40 | 5.7% below $546.40 | PASS |  | closing high would be 544.85 |
| LIN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.7% below | PASS |  |  |
| LIN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $546.40 | $546.4006244123242 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LIN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.60%, close location 0.07, OBV falling |
| LIN | V2 | day change of the last completed bar | down 1.6% | -1.60% | PASS |  |  |
| LIN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0706) | PASS |  |  |
| LIN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LIN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.12× / 0.91× | 1.12× / 0.91× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LIN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2348732) | 20 bars, last ('2026-11-17', 2348732) | PASS |  |  |
| LLY | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,415.55 | $1,415.55 | PASS |  |  |
| LLY | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1366.92 | $1366.92 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LLY | E3 | percent from the 21-day average | 3.6% above | 3.6% above | PASS |  |  |
| LLY | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| LLY | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $43.51 | $43.51 (sr=43.5066) | PASS |  | Wilder ATR14 |
| LLY | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves above |
| LLY | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.9 | -5.9 | PASS |  |  |
| LLY | L-ema21 | ladder row ema21: price and gap = price vs average | $1366.92, 3.6% | $1366.92, 3.6% | PASS |  |  |
| LLY | L-note | "Last close $X · date" note = last completed bar | Last close $1,415.55 · Nov 17 | $1,415.55 · Nov 17 | PASS |  |  |
| LLY | L-now | ladder price row = compared price; name = the basis label | $1415.55 "After hours" | $1415.55 "after hours" | PASS |  |  |
| LLY | L-sma200 | ladder row sma200: price and gap = price vs average | $1110.18, 27.5% | $1110.18, 27.5% | PASS |  |  |
| LLY | L-sma50 | ladder row sma50: price and gap = price vs average | $1251.14, 13.1% | $1251.14, 13.1% | PASS |  |  |
| LLY | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,415.55 / entry $1,415.55 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LLY | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LLY | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 63.2 | 63.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LLY | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.4% vs +11.2% | 39.4% vs 11.2% | PASS |  |  |
| LLY | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LLY | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.2 | 38.2 | PASS |  | Wilder, completed bars |
| LLY | T4w | words "20 or more / below 20" | 20 or more | ADX 38.2 | PASS |  |  |
| LLY | T5 | "counted at the last close ($X, date)" = last completed bar | $1,415.55, Nov 17 | $1415.55, Nov 17 | PASS |  |  |
| LLY | T6 | price vs 200-day average (S1 pattern sma values) | $1,415.55 vs $1,110.17 · +27.5% | $1415.55 vs $1110.18 · 27.5% | PASS |  |  |
| LLY | T6w | word "Above" | Above | Above | PASS |  |  |
| LLY | T7 | price vs 50-day average (S1 pattern sma values) | $1,415.55 vs $1,251.14 · +13.1% | $1415.55 vs $1251.14 · 13.1% | PASS |  |  |
| LLY | T7w | word "Above" | Above | Above | PASS |  |  |
| LLY | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| LLY | T8r | word "rising" | still rising | rising | PASS |  |  |
| LLY | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LLY | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.0% below $1,475.25 | 4.0% below $1475.25 | PASS |  | closing high would be 1443.50 |
| LLY | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.0% below | PASS |  |  |
| LLY | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,475.25 | $1475.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LLY | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.13%, close location 0.45, OBV falling |
| LLY | V2 | day change of the last completed bar | down 1.1% | -1.13% | PASS |  |  |
| LLY | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LLY | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.96× / 0.37× | 0.96× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LLY | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2478538) | 20 bars, last ('2026-11-17', 2478538) | PASS |  |  |
| MDA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.22 | $39.22 | PASS |  |  |
| MDA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.5 | $40.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MDA.TO | E3 | percent from the 21-day average | 3.2% below | 3.2% below | PASS |  |  |
| MDA.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MDA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.27 | $2.27 (sr=2.2733) | PASS |  | Wilder ATR14 |
| MDA.TO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| MDA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.5, -3.2% | $40.50, -3.2% | PASS |  |  |
| MDA.TO | L-note | "Last close $X · date" note = last completed bar | Last close $39.22 · Nov 17 | $39.22 · Nov 17 | PASS |  |  |
| MDA.TO | L-now | ladder price row = compared price; name = the basis label | $39.22 "After hours" | $39.22 "after hours" | PASS |  |  |
| MDA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $44.7, -12.3% | $44.70, -12.3% | PASS |  |  |
| MDA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.92, -4.1% | $40.92, -4.1% | PASS |  |  |
| MDA.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $39.22 / entry $39.22 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MDA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MDA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.9 | 45.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MDA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +82.9% vs +11.2% | 82.9% vs 11.2% | PASS |  |  |
| MDA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MDA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.2 | 25.2 | PASS |  | Wilder, completed bars |
| MDA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.2 | PASS |  |  |
| MDA.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $39.22, Nov 17 | $39.22, Nov 17 | PASS |  |  |
| MDA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $39.22 vs $44.70 · -12.3% | $39.22 vs $44.70 · -12.3% | PASS |  |  |
| MDA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $39.22 vs $40.92 · -4.2% | $39.22 vs $40.92 · -4.1% | PASS |  |  |
| MDA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.0% over 30 td | +3.0% over 30 td | PASS |  |  |
| MDA.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MDA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MDA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 42.2% below $67.90 | 42.2% below $67.90 | PASS |  | closing high would be 67.13 |
| MDA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 42.2% below | PASS |  |  |
| MDA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $67.90 | $67.9000015258789 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MDA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.15%, close location 0.10, OBV flat |
| MDA.TO | V2 | day change of the last completed bar | down 2.1% | -2.15% | PASS |  |  |
| MDA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1009) | PASS |  |  |
| MDA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| MDA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.39× / 0.37× | 0.39× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MDA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 639195) | 20 bars, last ('2026-11-17', 639195) | PASS |  |  |
| META | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $623.30 | $623.30 | PASS |  |  |
| META | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $640.17 | $640.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| META | E3 | percent from the 21-day average | 2.6% below | 2.6% below | PASS |  |  |
| META | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| META | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $22.07 | $22.07 (sr=22.0699) | PASS |  | Wilder ATR14 |
| META | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| META | L-ema21 | ladder row ema21: price and gap = price vs average | $640.17, -2.6% | $640.17, -2.6% | PASS |  |  |
| META | L-note | "Last close $X · date" note = last completed bar | Last close $618.87 · Nov 17 | $618.87 · Nov 17 | PASS |  |  |
| META | L-now | ladder price row = compared price; name = the basis label | $623.3 "After hours" | $623.30 "after hours" | PASS |  |  |
| META | L-sma200 | ladder row sma200: price and gap = price vs average | $629.15, -0.9% | $629.15, -0.9% | PASS |  |  |
| META | L-sma50 | ladder row sma50: price and gap = price vs average | $680.02, -8.3% | $680.02, -8.3% | PASS |  |  |
| META | S5-price | S5: the same live price reads the same on the header and the Entry block | header $623.30 / entry $623.30 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| META | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.58× / 0.34× | 0.58× / 0.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| META | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 12795966) | 20 bars, last ('2026-11-17', 12795966) | PASS |  |  |
| METU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $21.96 | $21.96 | PASS |  |  |
| METU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $23.42 | $23.42 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| METU | E3 | percent from the 21-day average | 6.2% below | 6.2% below | PASS |  |  |
| METU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| METU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.63 | $1.63 (sr=1.6286) | PASS |  | Wilder ATR14 |
| METU | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves below |
| METU | L-ema21 | ladder row ema21: price and gap = price vs average | $23.42, -6.2% | $23.42, -6.2% | PASS |  |  |
| METU | L-note | "Last close $X · date" note = last completed bar | Last close $21.57 · Nov 17 | $21.57 · Nov 17 | PASS |  |  |
| METU | L-now | ladder price row = compared price; name = the basis label | $21.96 "After hours" | $21.96 "after hours" | PASS |  |  |
| METU | L-sma200 | ladder row sma200: price and gap = price vs average | $25.23, -13.0% | $25.23, -13.0% | PASS |  |  |
| METU | L-sma50 | ladder row sma50: price and gap = price vs average | $26.93, -18.4% | $26.93, -18.4% | PASS |  |  |
| METU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $21.96 / entry $21.96 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| METU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| METU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.6 | 40.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| METU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -19.1% vs +11.2% | -19.1% vs 11.2% | PASS |  |  |
| METU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| METU | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.2 | 24.2 | PASS |  | Wilder, completed bars |
| METU | T4w | words "20 or more / below 20" | 20 or more | ADX 24.2 | PASS |  |  |
| METU | T5 | "counted at the last close ($X, date)" = last completed bar | $21.57, Nov 17 | $21.57, Nov 17 | PASS |  |  |
| METU | T6 | price vs 200-day average (S1 pattern sma values) | $21.57 vs $25.23 · -14.5% | $21.57 vs $25.23 · -14.5% | PASS |  |  |
| METU | T6w | word "Below" | Below | Below | PASS |  |  |
| METU | T7 | price vs 50-day average (S1 pattern sma values) | $21.57 vs $26.93 · -19.9% | $21.57 vs $26.93 · -19.9% | PASS |  |  |
| METU | T7w | word "Below" | Below | Below | PASS |  |  |
| METU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.4% over 30 td | -3.4% over 30 td | PASS |  |  |
| METU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| METU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| METU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 44.6% below $38.96 | 44.6% below $38.96 | PASS |  | closing high would be 38.45 |
| METU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 44.6% below | PASS |  |  |
| METU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.96 | $38.95624380685178 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| METU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.62%, close location 0.39, OBV falling |
| METU | V2 | day change of the last completed bar | down 2.6% | -2.62% | PASS |  |  |
| METU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| METU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.24× / 0.35× | 0.24× / 0.35× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| METU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1197575) | 20 bars, last ('2026-11-17', 1197575) | PASS |  |  |
| MRVL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $148.74 | $148.74 | PASS |  |  |
| MRVL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $181.92 | $181.92 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MRVL | E3 | percent from the 21-day average | 18.2% below | 18.2% below | PASS |  |  |
| MRVL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MRVL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.37 | $16.37 (sr=16.3666) | PASS |  | Wilder ATR14 |
| MRVL | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| MRVL | L-ema21 | ladder row ema21: price and gap = price vs average | $181.92, -18.2% | $181.92, -18.2% | PASS |  |  |
| MRVL | L-note | "Last close $X · date" note = last completed bar | Last close $148.74 · Nov 17 | $148.74 · Nov 17 | PASS |  |  |
| MRVL | L-now | ladder price row = compared price; name = the basis label | $148.74 "After hours" | $148.74 "after hours" | PASS |  |  |
| MRVL | L-sma200 | ladder row sma200: price and gap = price vs average | $187.61, -20.7% | $187.61, -20.7% | PASS |  |  |
| MRVL | L-sma50 | ladder row sma50: price and gap = price vs average | $226.08, -34.2% | $226.08, -34.2% | PASS |  |  |
| MRVL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $148.74 / entry $148.74 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MRVL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MRVL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.2 | 34.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MRVL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +78.5% vs +11.2% | 78.5% vs 11.2% | PASS |  |  |
| MRVL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MRVL | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.8 | 31.8 | PASS |  | Wilder, completed bars |
| MRVL | T4w | words "20 or more / below 20" | 20 or more | ADX 31.8 | PASS |  |  |
| MRVL | T5 | "counted at the last close ($X, date)" = last completed bar | $148.74, Nov 17 | $148.74, Nov 17 | PASS |  |  |
| MRVL | T6 | price vs 200-day average (S1 pattern sma values) | $148.74 vs $187.62 · -20.7% | $148.74 vs $187.61 · -20.7% | PASS |  |  |
| MRVL | T6w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T7 | price vs 50-day average (S1 pattern sma values) | $148.74 vs $226.08 · -34.2% | $148.74 vs $226.08 · -34.2% | PASS |  |  |
| MRVL | T7w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.2% over 30 td | +11.2% over 30 td | PASS |  |  |
| MRVL | T8r | word "rising" | still rising | rising | PASS |  |  |
| MRVL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MRVL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.9% below $329.73 | 54.9% below $329.73 | PASS |  | closing high would be 316.28 |
| MRVL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.9% below | PASS |  |  |
| MRVL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $329.73 | $329.72658943397715 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MRVL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 2.33%, close location 0.78, OBV falling |
| MRVL | V2 | day change of the last completed bar | up 2.3% | +2.33% | PASS |  |  |
| MRVL | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.78 (raw 0.7809) | PASS |  |  |
| MRVL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MRVL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.08× / 0.21× | 1.08× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MRVL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 26073358) | 20 bars, last ('2026-11-17', 26073358) | PASS |  |  |
| MSFT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $505.93 | $505.93 | PASS |  |  |
| MSFT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $525.28 | $525.28 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFT | E3 | percent from the 21-day average | 3.7% below | 3.7% below | PASS |  |  |
| MSFT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MSFT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $15.39 | $15.39 (sr=15.3934) | PASS |  | Wilder ATR14 |
| MSFT | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| MSFT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.5 | -5.5 | PASS |  |  |
| MSFT | L-ema21 | ladder row ema21: price and gap = price vs average | $525.28, -3.7% | $525.28, -3.7% | PASS |  |  |
| MSFT | L-note | "Last close $X · date" note = last completed bar | Last close $506.24 · Nov 17 | $506.24 · Nov 17 | PASS |  |  |
| MSFT | L-now | ladder price row = compared price; name = the basis label | $505.93 "After hours" | $505.93 "after hours" | PASS |  |  |
| MSFT | L-sma200 | ladder row sma200: price and gap = price vs average | $441.37, 14.6% | $441.37, 14.6% | PASS |  |  |
| MSFT | L-sma50 | ladder row sma50: price and gap = price vs average | $519.61, -2.6% | $519.61, -2.6% | PASS |  |  |
| MSFT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $505.93 / entry $505.93 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.9 | 41.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.6% vs +11.2% | 0.6% vs 11.2% | PASS |  |  |
| MSFT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFT | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.7 | 17.7 | PASS |  | Wilder, completed bars |
| MSFT | T4w | words "20 or more / below 20" | below 20 | ADX 17.7 | PASS |  |  |
| MSFT | T5 | "counted at the last close ($X, date)" = last completed bar | $506.24, Nov 17 | $506.24, Nov 17 | PASS |  |  |
| MSFT | T6 | price vs 200-day average (S1 pattern sma values) | $506.24 vs $441.37 · +14.7% | $506.24 vs $441.37 · 14.7% | PASS |  |  |
| MSFT | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFT | T7 | price vs 50-day average (S1 pattern sma values) | $506.24 vs $519.61 · -2.6% | $506.24 vs $519.61 · -2.6% | PASS |  |  |
| MSFT | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.2% over 30 td | PASS |  |  |
| MSFT | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 9.5% below $559.15 | 9.5% below $559.15 | PASS |  | closing high would be 555.80 |
| MSFT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 9.5% below | PASS |  |  |
| MSFT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $559.15 | $559.1500244140625 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.27%, close location 0.51, OBV falling |
| MSFT | V2 | day change of the last completed bar | down 2.3% | -2.27% | PASS |  |  |
| MSFT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.15× / 0.75× | 1.15× / 0.75× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 27250041) | 20 bars, last ('2026-11-17', 27250041) | PASS |  |  |
| MSFU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $37.94 | $37.94 | PASS |  |  |
| MSFU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.61 | $40.61 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFU | E3 | percent from the 21-day average | 6.6% below | 6.6% below | PASS |  |  |
| MSFU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MSFU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.35 | $2.35 (sr=2.3501) | PASS |  | Wilder ATR14 |
| MSFU | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| MSFU | L-ema21 | ladder row ema21: price and gap = price vs average | $40.61, -6.6% | $40.61, -6.6% | PASS |  |  |
| MSFU | L-note | "Last close $X · date" note = last completed bar | Last close $37.34 · Nov 17 | $37.34 · Nov 17 | PASS |  |  |
| MSFU | L-now | ladder price row = compared price; name = the basis label | $37.94 "After hours" | $37.94 "after hours" | PASS |  |  |
| MSFU | L-sma200 | ladder row sma200: price and gap = price vs average | $31.05, 22.2% | $31.05, 22.2% | PASS |  |  |
| MSFU | L-sma50 | ladder row sma50: price and gap = price vs average | $40.14, -5.5% | $40.14, -5.5% | PASS |  |  |
| MSFU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $37.94 / entry $37.94 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.8 | 40.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -17.9% vs +11.2% | -17.9% vs 11.2% | PASS |  |  |
| MSFU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFU | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.6 | 17.6 | PASS |  | Wilder, completed bars |
| MSFU | T4w | words "20 or more / below 20" | below 20 | ADX 17.6 | PASS |  |  |
| MSFU | T5 | "counted at the last close ($X, date)" = last completed bar | $37.34, Nov 17 | $37.34, Nov 17 | PASS |  |  |
| MSFU | T6 | price vs 200-day average (S1 pattern sma values) | $37.34 vs $31.05 · +20.3% | $37.34 vs $31.05 · 20.3% | PASS |  |  |
| MSFU | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFU | T7 | price vs 50-day average (S1 pattern sma values) | $37.34 vs $40.14 · -7.0% | $37.34 vs $40.14 · -7.0% | PASS |  |  |
| MSFU | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| MSFU | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 19.4% below $46.31 | 19.4% below $46.31 | PASS |  | closing high would be 45.47 |
| MSFU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 19.4% below | PASS |  |  |
| MSFU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.31 | $46.31366222164748 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -4.67%, close location 0.50, OBV falling |
| MSFU | V2 | day change of the last completed bar | down 4.7% | -4.67% | PASS |  |  |
| MSFU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.14× / 0.74× | 1.14× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2768861) | 20 bars, last ('2026-11-17', 2768861) | PASS |  |  |
| MTRX.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $29.13 | $29.13 | PASS |  |  |
| MTRX.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $31.15 | $31.15 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MTRX.TO | E3 | percent from the 21-day average | 6.5% below | 6.5% below | PASS |  |  |
| MTRX.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| MTRX.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.98 | $0.98 (sr=0.98) | PASS |  | Wilder ATR14 |
| MTRX.TO | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| MTRX.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.3 | +3.3 | PASS |  |  |
| MTRX.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $31.15, -6.5% | $31.15, -6.5% | PASS |  |  |
| MTRX.TO | L-now | ladder price row = compared price; name = the basis label | $29.13 "Last close" | $29.13 "last close" | PASS |  |  |
| MTRX.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $34.34, -15.2% | $34.34, -15.2% | PASS |  |  |
| MTRX.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $33.55, -13.2% | $33.55, -13.2% | PASS |  |  |
| MTRX.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.6 | 37.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MTRX.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.1% vs +11.2% | -2.1% vs 11.2% | PASS |  |  |
| MTRX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.9 | 27.9 | PASS |  | Wilder, completed bars |
| MTRX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.9 | PASS |  |  |
| MTRX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.38%, close location 0.74, OBV falling |
| MTRX.TO | V2 | day change of the last completed bar | down 0.4% | -0.38% | PASS |  |  |
| MTRX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MTRX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.67× / 0.11× | 0.67× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MTRX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 6329) | 20 bars, last ('2026-11-17', 6329) | PASS |  |  |
| MU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $31.04 | $31.04 | PASS |  |  |
| MU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $35.61 | $35.61 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MU.TO | E3 | percent from the 21-day average | 12.8% below | 12.8% below | PASS |  |  |
| MU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| MU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.56 | $2.56 (sr=2.5559) | PASS |  | Wilder ATR14 |
| MU.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| MU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $35.61, -12.8% | $35.61, -12.8% | PASS |  |  |
| MU.TO | L-now | ladder price row = compared price; name = the basis label | $31.04 "Last close" | $31.04 "last close" | PASS |  |  |
| MU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.8, -8.2% | $33.80, -8.2% | PASS |  |  |
| MU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.81, -23.9% | $40.81, -23.9% | PASS |  |  |
| MU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.2 | 37.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +185.8% vs +11.2% | 185.8% vs 11.2% | PASS |  |  |
| MU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.0 | 35.0 | PASS |  | Wilder, completed bars |
| MU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 35.0 | PASS |  |  |
| MU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $31.04 vs $33.80 · -8.2% | $31.04 vs $33.80 · -8.2% | PASS |  |  |
| MU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $31.04 vs $40.81 · -23.9% | $31.04 vs $40.81 · -23.9% | PASS |  |  |
| MU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.3% over 30 td | +11.3% over 30 td | PASS |  |  |
| MU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 43.9% below $55.28 | 43.8% below $55.28 | PASS |  | closing high would be 53.52 |
| MU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 43.8% below | PASS |  |  |
| MU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $55.28 | $55.282308204978015 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.24%, close location 0.73, OBV falling |
| MU.TO | V2 | day change of the last completed bar | down 1.2% | -1.24% | PASS |  |  |
| MU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.17× / 0.15× | 1.17× / 0.15× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2166666) | 20 bars, last ('2026-11-17', 2166666) | PASS |  |  |
| NEE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $83.88 | $83.88 | PASS |  |  |
| NEE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.08 | $84.08 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEE | E3 | percent from the 21-day average | 0.2% below | 0.2% below | PASS |  |  |
| NEE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.64 | $1.64 (sr=1.6395) | PASS |  | Wilder ATR14 |
| NEE | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves below |
| NEE | L-ema21 | ladder row ema21: price and gap = price vs average | $84.08, -0.2% | $84.08, -0.2% | PASS |  |  |
| NEE | L-note | "Last close $X · date" note = last completed bar | Last close $84.42 · Nov 17 | $84.42 · Nov 17 | PASS |  |  |
| NEE | L-now | ladder price row = compared price; name = the basis label | $83.88 "After hours" | $83.88 "after hours" | PASS |  |  |
| NEE | L-sma200 | ladder row sma200: price and gap = price vs average | $86.53, -3.1% | $86.53, -3.1% | PASS |  |  |
| NEE | L-sma50 | ladder row sma50: price and gap = price vs average | $80.86, 3.7% | $80.86, 3.7% | PASS |  |  |
| NEE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $83.88 / entry $83.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.1 | 54.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +1.3% vs +11.2% | 1.3% vs 11.2% | PASS |  |  |
| NEE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEE | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.3 | 32.3 | PASS |  | Wilder, completed bars |
| NEE | T4w | words "20 or more / below 20" | 20 or more | ADX 32.3 | PASS |  |  |
| NEE | T5 | "counted at the last close ($X, date)" = last completed bar | $84.42, Nov 17 | $84.42, Nov 17 | PASS |  |  |
| NEE | T6 | price vs 200-day average (S1 pattern sma values) | $84.42 vs $86.53 · -2.4% | $84.42 vs $86.53 · -2.4% | PASS |  |  |
| NEE | T6w | word "Below" | Below | Below | PASS |  |  |
| NEE | T7 | price vs 50-day average (S1 pattern sma values) | $84.42 vs $80.86 · +4.4% | $84.42 vs $80.86 · 4.4% | PASS |  |  |
| NEE | T7w | word "Above" | Above | Above | PASS |  |  |
| NEE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.3% over 30 td | +0.3% over 30 td | PASS |  |  |
| NEE | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.2% below $97.30 | 13.2% below $97.30 | PASS |  | closing high would be 96.44 |
| NEE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.2% below | PASS |  |  |
| NEE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $97.30 | $97.30028062322594 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.08%, close location 0.22, OBV falling |
| NEE | V2 | day change of the last completed bar | down 1.1% | -1.08% | PASS |  |  |
| NEE | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2188) | PASS |  |  |
| NEE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NEE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.86× / 0.56× | 0.86× / 0.56× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 10927993) | 20 bars, last ('2026-11-17', 10927993) | PASS |  |  |
| NEM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $112.00 | $112.00 | PASS |  |  |
| NEM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $114.93 | $114.93 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEM | E3 | percent from the 21-day average | 2.5% below | 2.5% below | PASS |  |  |
| NEM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.51 | $4.51 (sr=4.5128) | PASS |  | Wilder ATR14 |
| NEM | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| NEM | L-ema21 | ladder row ema21: price and gap = price vs average | $114.93, -2.5% | $114.93, -2.5% | PASS |  |  |
| NEM | L-note | "Last close $X · date" note = last completed bar | Last close $111.26 · Nov 17 | $111.26 · Nov 17 | PASS |  |  |
| NEM | L-now | ladder price row = compared price; name = the basis label | $112 "After hours" | $112.00 "after hours" | PASS |  |  |
| NEM | L-sma200 | ladder row sma200: price and gap = price vs average | $111.83, 0.1% | $111.83, 0.1% | PASS |  |  |
| NEM | L-sma50 | ladder row sma50: price and gap = price vs average | $117.36, -4.6% | $117.36, -4.6% | PASS |  |  |
| NEM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $112.00 / entry $112.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.5 | 44.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.9% vs +11.2% | 29.0% vs 11.2% | PASS |  |  |
| NEM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEM | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.9 | 15.9 | PASS |  | Wilder, completed bars |
| NEM | T4w | words "20 or more / below 20" | below 20 | ADX 15.9 | PASS |  |  |
| NEM | T5 | "counted at the last close ($X, date)" = last completed bar | $111.26, Nov 17 | $111.26, Nov 17 | PASS |  |  |
| NEM | T6 | price vs 200-day average (S1 pattern sma values) | $111.26 vs $111.83 · -0.5% | $111.26 vs $111.83 · -0.5% | PASS |  |  |
| NEM | T6w | word "Below" | Below | Below | PASS |  |  |
| NEM | T7 | price vs 50-day average (S1 pattern sma values) | $111.26 vs $117.36 · -5.2% | $111.26 vs $117.36 · -5.2% | PASS |  |  |
| NEM | T7w | word "Below" | Below | Below | PASS |  |  |
| NEM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.5% over 30 td | +0.5% over 30 td | PASS |  |  |
| NEM | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.6% below $135.01 | 17.6% below $135.01 | PASS |  | closing high would be 134.86 |
| NEM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.6% below | PASS |  |  |
| NEM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $135.01 | $135.0089504972229 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.86%, close location 0.24, OBV rising |
| NEM | V2 | day change of the last completed bar | up 0.9% | +0.86% | PASS |  |  |
| NEM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.24 (raw 0.2441) | PASS |  |  |
| NEM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| NEM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.08× / 0.21× | 1.08× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 6921507) | 20 bars, last ('2026-11-17', 6921507) | PASS |  |  |
| NFLX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $59.58 | $59.58 | PASS |  |  |
| NFLX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $64.11 | $64.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFLX | E3 | percent from the 21-day average | 7.1% below | 7.1% below | PASS |  |  |
| NFLX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NFLX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.95 | $1.95 (sr=1.9471) | PASS |  | Wilder ATR14 |
| NFLX | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| NFLX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.3 | +8.3 | PASS |  |  |
| NFLX | L-ema21 | ladder row ema21: price and gap = price vs average | $64.11, -7.1% | $64.11, -7.1% | PASS |  |  |
| NFLX | L-note | "Last close $X · date" note = last completed bar | Last close $59.68 · Nov 17 | $59.68 · Nov 17 | PASS |  |  |
| NFLX | L-now | ladder price row = compared price; name = the basis label | $59.58 "After hours" | $59.58 "after hours" | PASS |  |  |
| NFLX | L-sma200 | ladder row sma200: price and gap = price vs average | $80.27, -25.8% | $80.27, -25.8% | PASS |  |  |
| NFLX | L-sma50 | ladder row sma50: price and gap = price vs average | $68.49, -13.0% | $68.49, -13.0% | PASS |  |  |
| NFLX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $59.58 / entry $59.58 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFLX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFLX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.0 | 33.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFLX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -45.9% vs +11.2% | -45.9% vs 11.2% | PASS |  |  |
| NFLX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFLX | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.2 | 24.2 | PASS |  | Wilder, completed bars |
| NFLX | T4w | words "20 or more / below 20" | 20 or more | ADX 24.2 | PASS |  |  |
| NFLX | T5 | "counted at the last close ($X, date)" = last completed bar | $59.68, Nov 17 | $59.68, Nov 17 | PASS |  |  |
| NFLX | T6 | price vs 200-day average (S1 pattern sma values) | $59.68 vs $80.27 · -25.7% | $59.68 vs $80.27 · -25.6% | PASS |  |  |
| NFLX | T6w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T7 | price vs 50-day average (S1 pattern sma values) | $59.68 vs $68.49 · -12.9% | $59.68 vs $68.49 · -12.9% | PASS |  |  |
| NFLX | T7w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.2% over 30 td | -4.2% over 30 td | PASS |  |  |
| NFLX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFLX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFLX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 48.2% below $115.25 | 48.2% below $115.25 | PASS |  | closing high would be 114.09 |
| NFLX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 48.2% below | PASS |  |  |
| NFLX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $115.25 | $115.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFLX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.76%, close location 0.17, OBV falling |
| NFLX | V2 | day change of the last completed bar | down 1.8% | -1.76% | PASS |  |  |
| NFLX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1739) | PASS |  |  |
| NFLX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFLX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.54× | 0.88× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFLX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 34730494) | 20 bars, last ('2026-11-17', 34730494) | PASS |  |  |
| NFXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.92 | $9.92 | PASS |  |  |
| NFXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.53 | $11.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFXL | E3 | percent from the 21-day average | 14.0% below | 14.0% below | PASS |  |  |
| NFXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NFXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.71 | $0.71 (sr=0.7098) | PASS |  | Wilder ATR14 |
| NFXL | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| NFXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.2 | +12.2 | PASS |  |  |
| NFXL | L-ema21 | ladder row ema21: price and gap = price vs average | $11.53, -14.0% | $11.53, -14.0% | PASS |  |  |
| NFXL | L-note | "Last close $X · date" note = last completed bar | Last close $9.86 · Nov 17 | $9.86 · Nov 17 | PASS |  |  |
| NFXL | L-now | ladder price row = compared price; name = the basis label | $9.92 "After hours" | $9.92 "after hours" | PASS |  |  |
| NFXL | L-sma200 | ladder row sma200: price and gap = price vs average | $20.19, -50.9% | $20.19, -50.9% | PASS |  |  |
| NFXL | L-sma50 | ladder row sma50: price and gap = price vs average | $13.38, -25.9% | $13.38, -25.9% | PASS |  |  |
| NFXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.92 / entry $9.92 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.4 | 32.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -77.0% vs +11.2% | -77.0% vs 11.2% | PASS |  |  |
| NFXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.1 | 26.1 | PASS |  | Wilder, completed bars |
| NFXL | T4w | words "20 or more / below 20" | 20 or more | ADX 26.1 | PASS |  |  |
| NFXL | T5 | "counted at the last close ($X, date)" = last completed bar | $9.86, Nov 17 | $9.86, Nov 17 | PASS |  |  |
| NFXL | T6 | price vs 200-day average (S1 pattern sma values) | $9.86 vs $20.19 · -51.2% | $9.86 vs $20.19 · -51.2% | PASS |  |  |
| NFXL | T6w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T7 | price vs 50-day average (S1 pattern sma values) | $9.86 vs $13.38 · -26.3% | $9.86 vs $13.38 · -26.3% | PASS |  |  |
| NFXL | T7w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -10.0% over 30 td | -10.0% over 30 td | PASS |  |  |
| NFXL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 78.9% below $46.64 | 78.9% below $46.64 | PASS |  | closing high would be 45.75 |
| NFXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 78.9% below | PASS |  |  |
| NFXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.64 | $46.64217883026212 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.52%, close location 0.17, OBV falling |
| NFXL | V2 | day change of the last completed bar | down 3.5% | -3.52% | PASS |  |  |
| NFXL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1698) | PASS |  |  |
| NFXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.70× / 0.49× | 0.70× / 0.49× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1147820) | 20 bars, last ('2026-11-17', 1147820) | PASS |  |  |
| NTR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $99.02 | $99.02 | PASS |  |  |
| NTR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $99.81 | $99.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NTR.TO | E3 | percent from the 21-day average | 0.8% below | 0.8% below | PASS |  |  |
| NTR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NTR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.80 | $2.80 (sr=2.8025) | PASS |  | Wilder ATR14 |
| NTR.TO | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| NTR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $99.81, -0.8% | $99.81, -0.8% | PASS |  |  |
| NTR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $99.02 · Nov 17 | $99.02 · Nov 17 | PASS |  |  |
| NTR.TO | L-now | ladder price row = compared price; name = the basis label | $99.02 "After hours" | $99.02 "after hours" | PASS |  |  |
| NTR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $97.76, 1.3% | $97.76, 1.3% | PASS |  |  |
| NTR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $101.32, -2.3% | $101.32, -2.3% | PASS |  |  |
| NTR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $99.02 / entry $99.02 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NTR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NTR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.3 | 47.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NTR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +27.7% vs +11.2% | 27.7% vs 11.2% | PASS |  |  |
| NTR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NTR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.5 | 18.5 | PASS |  | Wilder, completed bars |
| NTR.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.5 | PASS |  |  |
| NTR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $99.02, Nov 17 | $99.02, Nov 17 | PASS |  |  |
| NTR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $99.02 vs $97.76 · +1.3% | $99.02 vs $97.76 · 1.3% | PASS |  |  |
| NTR.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| NTR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $99.02 vs $101.32 · -2.3% | $99.02 vs $101.32 · -2.3% | PASS |  |  |
| NTR.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| NTR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.9% over 30 td | +1.9% over 30 td | PASS |  |  |
| NTR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| NTR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NTR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.3% below $114.19 | 13.3% below $114.19 | PASS |  | closing high would be 111.71 |
| NTR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.3% below | PASS |  |  |
| NTR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $114.19 | $114.18838931131123 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NTR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.41%, close location 0.46, OBV rising |
| NTR.TO | V2 | day change of the last completed bar | up 0.4% | +0.41% | PASS |  |  |
| NTR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| NTR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.41× / 0.14× | 0.41× / 0.14× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NTR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 794512) | 20 bars, last ('2026-11-17', 794512) | PASS |  |  |
| NVDA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $160.12 | $160.12 | PASS |  |  |
| NVDA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $187.5 | $187.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDA | E3 | percent from the 21-day average | 14.6% below | 14.6% below | PASS |  |  |
| NVDA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NVDA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.71 | $9.71 (sr=9.7101) | PASS |  | Wilder ATR14 |
| NVDA | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| NVDA | L-ema21 | ladder row ema21: price and gap = price vs average | $187.5, -14.6% | $187.50, -14.6% | PASS |  |  |
| NVDA | L-note | "Last close $X · date" note = last completed bar | Last close $155.46 · Nov 17 | $155.46 · Nov 17 | PASS |  |  |
| NVDA | L-now | ladder price row = compared price; name = the basis label | $160.12 "After hours" | $160.12 "after hours" | PASS |  |  |
| NVDA | L-sma200 | ladder row sma200: price and gap = price vs average | $203.6, -21.4% | $203.60, -21.4% | PASS |  |  |
| NVDA | L-sma50 | ladder row sma50: price and gap = price vs average | $211.75, -24.4% | $211.75, -24.4% | PASS |  |  |
| NVDA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $160.12 / entry $160.12 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| NVDA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.35× / 0.07× | 2.35× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 370067900) | 20 bars, last ('2026-11-17', 370067900) | PASS |  |  |
| NVDA | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.35, OBV falling | condition true | PASS |  |  |
| NVDL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.59 | $17.59 | PASS |  |  |
| NVDL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.58 | $24.58 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDL | E3 | percent from the 21-day average | 28.4% below | 28.4% below | PASS |  |  |
| NVDL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NVDL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.50 | $2.50 (sr=2.5031) | PASS |  | Wilder ATR14 |
| NVDL | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| NVDL | L-ema21 | ladder row ema21: price and gap = price vs average | $24.58, -28.4% | $24.58, -28.4% | PASS |  |  |
| NVDL | L-note | "Last close $X · date" note = last completed bar | Last close $16.22 · Nov 17 | $16.22 · Nov 17 | PASS |  |  |
| NVDL | L-now | ladder price row = compared price; name = the basis label | $17.59 "After hours" | $17.59 "after hours" | PASS |  |  |
| NVDL | L-sma200 | ladder row sma200: price and gap = price vs average | $31.3, -43.8% | $31.30, -43.8% | PASS |  |  |
| NVDL | L-sma50 | ladder row sma50: price and gap = price vs average | $31.65, -44.4% | $31.65, -44.4% | PASS |  |  |
| NVDL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $17.59 / entry $17.59 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.6 | 22.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -46.1% vs +11.2% | -46.1% vs 11.2% | PASS |  |  |
| NVDL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDL | T4 | ADX 14 (S1 /api/sr meta.adx) | 45.9 | 45.9 | PASS |  | Wilder, completed bars |
| NVDL | T4w | words "20 or more / below 20" | 20 or more | ADX 45.9 | PASS |  |  |
| NVDL | T5 | "counted at the last close ($X, date)" = last completed bar | $16.22, Nov 17 | $16.22, Nov 17 | PASS |  |  |
| NVDL | T6 | price vs 200-day average (S1 pattern sma values) | $16.22 vs $31.30 · -48.2% | $16.22 vs $31.30 · -48.2% | PASS |  |  |
| NVDL | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T7 | price vs 50-day average (S1 pattern sma values) | $16.22 vs $31.65 · -48.8% | $16.22 vs $31.65 · -48.7% | PASS |  |  |
| NVDL | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.1% over 30 td | -0.1% over 30 td | PASS |  |  |
| NVDL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NVDL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 62.5% below $43.27 | 62.5% below $43.27 | PASS |  | closing high would be 43.02 |
| NVDL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 62.5% below | PASS |  |  |
| NVDL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.27 | $43.27333450317383 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.80%, close location 0.73, OBV falling |
| NVDL | V2 | day change of the last completed bar | down 0.8% | -0.80% | PASS |  |  |
| NVDL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.32× / 0.05× | 3.32× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 57865851) | 20 bars, last ('2026-11-17', 57865851) | PASS |  |  |
| NVDL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.32, OBV falling | condition true | PASS |  |  |
| ONTO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $199.57 | $199.57 | PASS |  |  |
| ONTO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $208.89 | $208.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ONTO | E3 | percent from the 21-day average | 4.5% below | 4.5% below | PASS |  |  |
| ONTO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ONTO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.66 | $17.66 (sr=17.6588) | PASS |  | Wilder ATR14 |
| ONTO | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| ONTO | L-ema21 | ladder row ema21: price and gap = price vs average | $208.89, -4.5% | $208.89, -4.5% | PASS |  |  |
| ONTO | L-note | "Last close $X · date" note = last completed bar | Last close $199.57 · Nov 17 | $199.57 · Nov 17 | PASS |  |  |
| ONTO | L-now | ladder price row = compared price; name = the basis label | $199.57 "After hours" | $199.57 "after hours" | PASS |  |  |
| ONTO | L-sma200 | ladder row sma200: price and gap = price vs average | $259.96, -23.2% | $259.96, -23.2% | PASS |  |  |
| ONTO | L-sma50 | ladder row sma50: price and gap = price vs average | $245, -18.5% | $245.00, -18.5% | PASS |  |  |
| ONTO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $199.57 / entry $199.57 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ONTO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ONTO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.3 | 44.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ONTO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +56.8% vs +11.2% | 56.8% vs 11.2% | PASS |  |  |
| ONTO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ONTO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.8 | 27.8 | PASS |  | Wilder, completed bars |
| ONTO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.8 | PASS |  |  |
| ONTO | T5 | "counted at the last close ($X, date)" = last completed bar | $199.57, Nov 17 | $199.57, Nov 17 | PASS |  |  |
| ONTO | T6 | price vs 200-day average (S1 pattern sma values) | $199.57 vs $259.96 · -23.2% | $199.57 vs $259.96 · -23.2% | PASS |  |  |
| ONTO | T6w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T7 | price vs 50-day average (S1 pattern sma values) | $199.57 vs $245.00 · -18.5% | $199.57 vs $245.00 · -18.5% | PASS |  |  |
| ONTO | T7w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| ONTO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ONTO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ONTO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 48.4% below $386.46 | 48.4% below $386.46 | PASS |  | closing high would be 378.45 |
| ONTO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 48.4% below | PASS |  |  |
| ONTO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $386.46 | $386.4599914550781 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ONTO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 1.42%, close location 0.53, OBV rising |
| ONTO | V2 | day change of the last completed bar | up 1.4% | +1.42% | PASS |  |  |
| ONTO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ONTO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.05× / 0.16× | 1.05× / 0.16× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ONTO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1092388) | 20 bars, last ('2026-11-17', 1092388) | PASS |  |  |
| ORBX.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $14.46 | $14.46 | PASS |  |  |
| ORBX.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.2 | $15.20 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORBX.TO | E3 | percent from the 21-day average | 4.8% below | 4.8% below | PASS |  |  |
| ORBX.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ORBX.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.67 | $0.67 (sr=0.6729) | PASS |  | Wilder ATR14 |
| ORBX.TO | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| ORBX.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $15.2, -4.8% | $15.20, -4.8% | PASS |  |  |
| ORBX.TO | L-now | ladder price row = compared price; name = the basis label | $14.46 "Last close" | $14.46 "last close" | PASS |  |  |
| ORBX.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $16.15, -10.5% | $16.15, -10.5% | PASS |  |  |
| ORBX.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.8 | 42.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORBX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.8 | 26.8 | PASS |  | Wilder, completed bars |
| ORBX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.8 | PASS |  |  |
| ORBX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.96%, close location 0.28, OBV falling |
| ORBX.TO | V2 | day change of the last completed bar | down 1.0% | -0.96% | PASS |  |  |
| ORBX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORBX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.19× / 0.21× | 0.19× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORBX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1206) | 20 bars, last ('2026-11-17', 1206) | PASS |  |  |
| ORCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $120.02 | $120.02 | PASS |  |  |
| ORCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $125.41 | $125.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORCL | E3 | percent from the 21-day average | 4.3% below | 4.3% below | PASS |  |  |
| ORCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ORCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.99 | $7.99 (sr=7.9864) | PASS |  | Wilder ATR14 |
| ORCL | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| ORCL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.4 | +3.4 | PASS |  |  |
| ORCL | L-ema21 | ladder row ema21: price and gap = price vs average | $125.41, -4.3% | $125.41, -4.3% | PASS |  |  |
| ORCL | L-note | "Last close $X · date" note = last completed bar | Last close $115.00 · Nov 17 | $115.00 · Nov 17 | PASS |  |  |
| ORCL | L-now | ladder price row = compared price; name = the basis label | $120.02 "After hours" | $120.02 "after hours" | PASS |  |  |
| ORCL | L-sma200 | ladder row sma200: price and gap = price vs average | $152.73, -21.4% | $152.73, -21.4% | PASS |  |  |
| ORCL | L-sma50 | ladder row sma50: price and gap = price vs average | $134.69, -10.9% | $134.69, -10.9% | PASS |  |  |
| ORCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $120.02 / entry $120.02 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ORCL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ORCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.0 | 40.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORCL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -47.0% vs +11.2% | -47.0% vs 11.2% | PASS |  |  |
| ORCL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ORCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.9 | 12.9 | PASS |  | Wilder, completed bars |
| ORCL | T4w | words "20 or more / below 20" | below 20 | ADX 12.9 | PASS |  |  |
| ORCL | T5 | "counted at the last close ($X, date)" = last completed bar | $115.00, Nov 17 | $115.00, Nov 17 | PASS |  |  |
| ORCL | T6 | price vs 200-day average (S1 pattern sma values) | $115.00 vs $152.73 · -24.7% | $115.00 vs $152.73 · -24.7% | PASS |  |  |
| ORCL | T6w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T7 | price vs 50-day average (S1 pattern sma values) | $115.00 vs $134.69 · -14.6% | $115.00 vs $134.69 · -14.6% | PASS |  |  |
| ORCL | T7w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.3% over 30 td | -5.3% over 30 td | PASS |  |  |
| ORCL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| ORCL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ORCL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 53.7% below $248.46 | 53.7% below $248.46 | PASS |  | closing high would be 246.38 |
| ORCL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 53.7% below | PASS |  |  |
| ORCL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $248.46 | $248.4634626242363 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ORCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.43%, close location 0.25, OBV falling |
| ORCL | V2 | day change of the last completed bar | down 3.4% | -3.43% | PASS |  |  |
| ORCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.25 (raw 0.2494) | PASS |  |  |
| ORCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.69× / 0.49× | 0.69× / 0.49× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 25210397) | 20 bars, last ('2026-11-17', 25210397) | PASS |  |  |
| PG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $170.48 | $170.48 | PASS |  |  |
| PG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $164.53 | $164.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PG | E3 | percent from the 21-day average | 3.6% above | 3.6% above | PASS |  |  |
| PG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| PG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.20 | $3.20 (sr=3.2038) | PASS |  | Wilder ATR14 |
| PG | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves above |
| PG | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.1 | -5.1 | PASS |  |  |
| PG | L-ema21 | ladder row ema21: price and gap = price vs average | $164.53, 3.6% | $164.53, 3.6% | PASS |  |  |
| PG | L-note | "Last close $X · date" note = last completed bar | Last close $171.72 · Nov 17 | $171.72 · Nov 17 | PASS |  |  |
| PG | L-now | ladder price row = compared price; name = the basis label | $170.48 "After hours" | $170.48 "after hours" | PASS |  |  |
| PG | L-sma200 | ladder row sma200: price and gap = price vs average | $148.23, 15.0% | $148.23, 15.0% | PASS |  |  |
| PG | L-sma50 | ladder row sma50: price and gap = price vs average | $154.68, 10.2% | $154.68, 10.2% | PASS |  |  |
| PG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $170.48 / entry $170.48 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 69.3 | 69.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +21.2% vs +11.2% | 21.2% vs 11.2% | PASS |  |  |
| PG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PG | T4 | ADX 14 (S1 /api/sr meta.adx) | 43.1 | 43.1 | PASS |  | Wilder, completed bars |
| PG | T4w | words "20 or more / below 20" | 20 or more | ADX 43.1 | PASS |  |  |
| PG | T5 | "counted at the last close ($X, date)" = last completed bar | $171.72, Nov 17 | $171.72, Nov 17 | PASS |  |  |
| PG | T6 | price vs 200-day average (S1 pattern sma values) | $171.72 vs $148.23 · +15.8% | $171.72 vs $148.23 · 15.9% | PASS |  |  |
| PG | T6w | word "Above" | Above | Above | PASS |  |  |
| PG | T7 | price vs 50-day average (S1 pattern sma values) | $171.72 vs $154.68 · +11.0% | $171.72 vs $154.68 · 11.0% | PASS |  |  |
| PG | T7w | word "Above" | Above | Above | PASS |  |  |
| PG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.0% over 30 td | +2.0% over 30 td | PASS |  |  |
| PG | T8r | word "rising" | still rising | rising | PASS |  |  |
| PG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.1% below $173.59 | 1.1% below $173.59 | PASS |  | closing high would be 173.02 |
| PG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.1% below | PASS |  |  |
| PG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $173.59 | $173.58999633789062 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.75%, close location 0.20, OBV rising |
| PG | V2 | day change of the last completed bar | down 0.8% | -0.75% | PASS |  |  |
| PG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.20 (raw 0.2043) | PASS |  |  |
| PG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| PG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.90× / 0.40× | 0.90× / 0.40× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 8507667) | 20 bars, last ('2026-11-17', 8507667) | PASS |  |  |
| PLD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $125.56 | $125.56 | PASS |  |  |
| PLD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $128.51 | $128.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PLD | E3 | percent from the 21-day average | 2.3% below | 2.3% below | PASS |  |  |
| PLD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| PLD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.51 | $2.51 (sr=2.5068) | PASS |  | Wilder ATR14 |
| PLD | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| PLD | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| PLD | L-ema21 | ladder row ema21: price and gap = price vs average | $128.51, -2.3% | $128.51, -2.3% | PASS |  |  |
| PLD | L-note | "Last close $X · date" note = last completed bar | Last close $125.56 · Nov 17 | $125.56 · Nov 17 | PASS |  |  |
| PLD | L-now | ladder price row = compared price; name = the basis label | $125.56 "After hours" | $125.56 "after hours" | PASS |  |  |
| PLD | L-sma200 | ladder row sma200: price and gap = price vs average | $136.34, -7.9% | $136.34, -7.9% | PASS |  |  |
| PLD | L-sma50 | ladder row sma50: price and gap = price vs average | $130.09, -3.5% | $130.09, -3.5% | PASS |  |  |
| PLD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $125.56 / entry $125.56 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| PLD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.89× / 0.80× | 0.89× / 0.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PLD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3445914) | 20 bars, last ('2026-11-17', 3445914) | PASS |  |  |
| PNG.V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3.12 | $3.12 | PASS |  |  |
| PNG.V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3.66 | $3.66 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PNG.V | E3 | percent from the 21-day average | 14.6% below | 14.6% below | PASS |  |  |
| PNG.V | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| PNG.V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.23 | $0.23 (sr=0.2304) | PASS |  | Wilder ATR14 |
| PNG.V | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| PNG.V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.8 | +12.8 | PASS |  |  |
| PNG.V | L-ema21 | ladder row ema21: price and gap = price vs average | $3.66, -14.6% | $3.66, -14.6% | PASS |  |  |
| PNG.V | L-now | ladder price row = compared price; name = the basis label | $3.12 "Last close" | $3.12 "last close" | PASS |  |  |
| PNG.V | L-sma200 | ladder row sma200: price and gap = price vs average | $6.6, -52.7% | $6.60, -52.7% | PASS |  |  |
| PNG.V | L-sma50 | ladder row sma50: price and gap = price vs average | $4.17, -25.2% | $4.17, -25.2% | PASS |  |  |
| PNG.V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PNG.V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.7 | 27.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PNG.V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -39.9% vs +11.2% | -39.9% vs 11.2% | PASS |  |  |
| PNG.V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PNG.V | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.3 | 37.2 | PASS |  | Wilder, completed bars |
| PNG.V | T4w | words "20 or more / below 20" | 20 or more | ADX 37.2 | PASS |  |  |
| PNG.V | T6 | price vs 200-day average (S1 pattern sma values) | $3.12 vs $6.60 · -52.7% | $3.12 vs $6.60 · -52.7% | PASS |  |  |
| PNG.V | T6w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T7 | price vs 50-day average (S1 pattern sma values) | $3.12 vs $4.17 · -25.2% | $3.12 vs $4.17 · -25.2% | PASS |  |  |
| PNG.V | T7w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -7.4% over 30 td | -7.3% over 30 td | PASS |  |  |
| PNG.V | T8r | word "rising" | not rising | not rising | PASS |  |  |
| PNG.V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PNG.V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 70.9% below $10.72 | 70.9% below $10.72 | PASS |  | closing high would be 10.23 |
| PNG.V | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 70.9% below | PASS |  |  |
| PNG.V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $10.72 | $10.720000267028809 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PNG.V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.11%, close location 0.24, OBV falling |
| PNG.V | V2 | day change of the last completed bar | down 3.1% | -3.11% | PASS |  |  |
| PNG.V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.24 (raw 0.2381) | PASS |  |  |
| PNG.V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PNG.V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.42× / 0.42× | 1.42× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PNG.V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1700055) | 20 bars, last ('2026-11-17', 1700055) | PASS |  |  |
| QCOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $170.10 | $170.10 | PASS |  |  |
| QCOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $172.38 | $172.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QCOM | E3 | percent from the 21-day average | 1.3% below | 1.3% below | PASS |  |  |
| QCOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QCOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.87 | $8.87 (sr=8.866) | PASS |  | Wilder ATR14 |
| QCOM | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| QCOM | L-ema21 | ladder row ema21: price and gap = price vs average | $172.38, -1.3% | $172.38, -1.3% | PASS |  |  |
| QCOM | L-note | "Last close $X · date" note = last completed bar | Last close $166.67 · Nov 17 | $166.67 · Nov 17 | PASS |  |  |
| QCOM | L-now | ladder price row = compared price; name = the basis label | $170.1 "After hours" | $170.10 "after hours" | PASS |  |  |
| QCOM | L-sma200 | ladder row sma200: price and gap = price vs average | $169.35, 0.4% | $169.35, 0.4% | PASS |  |  |
| QCOM | L-sma50 | ladder row sma50: price and gap = price vs average | $178.58, -4.7% | $178.58, -4.7% | PASS |  |  |
| QCOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $170.10 / entry $170.10 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| QCOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.82× / 0.21× | 0.82× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QCOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 10935821) | 20 bars, last ('2026-11-17', 10935821) | PASS |  |  |
| QPUX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3.42 | $3.42 | PASS |  |  |
| QPUX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $5.87 | $5.87 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QPUX | E3 | percent from the 21-day average | 41.7% below | 41.7% below | PASS |  |  |
| QPUX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QPUX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.87 | $0.87 (sr=0.8738) | PASS |  | Wilder ATR14 |
| QPUX | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| QPUX | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| QPUX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +16.6 | +16.6 | PASS |  |  |
| QPUX | L-ema21 | ladder row ema21: price and gap = price vs average | $5.87, -41.7% | $5.87, -41.7% | PASS |  |  |
| QPUX | L-note | "Last close $X · date" note = last completed bar | Last close $3.32 · Nov 17 | $3.32 · Nov 17 | PASS |  |  |
| QPUX | L-now | ladder price row = compared price; name = the basis label | $3.42 "After hours" | $3.42 "after hours" | PASS |  |  |
| QPUX | L-sma200 | ladder row sma200: price and gap = price vs average | $20.37, -83.2% | $20.37, -83.2% | PASS |  |  |
| QPUX | L-sma50 | ladder row sma50: price and gap = price vs average | $9.08, -62.3% | $9.08, -62.3% | PASS |  |  |
| QPUX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3.42 / entry $3.42 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QPUX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QPUX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.3 | 29.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QPUX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -94.5% vs +11.2% | -94.5% vs 11.2% | PASS |  |  |
| QPUX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QPUX | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.3 | 37.3 | PASS |  | Wilder, completed bars |
| QPUX | T4w | words "20 or more / below 20" | 20 or more | ADX 37.3 | PASS |  |  |
| QPUX | T5 | "counted at the last close ($X, date)" = last completed bar | $3.32, Nov 17 | $3.32, Nov 17 | PASS |  |  |
| QPUX | T6 | price vs 200-day average (S1 pattern sma values) | $3.32 vs $20.37 · -83.7% | $3.32 vs $20.37 · -83.7% | PASS |  |  |
| QPUX | T6w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T7 | price vs 50-day average (S1 pattern sma values) | $3.32 vs $9.08 · -63.4% | $3.32 vs $9.08 · -63.4% | PASS |  |  |
| QPUX | T7w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -25.9% over 30 td | -25.9% over 30 td | PASS |  |  |
| QPUX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| QPUX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QPUX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 95.9% below $80.28 | 95.9% below $80.28 | PASS |  | closing high would be 79.57 |
| QPUX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 95.9% below | PASS |  |  |
| QPUX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.28 | $80.27999877929688 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QPUX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -7.52%, close location 0.34, OBV falling |
| QPUX | V2 | day change of the last completed bar | down 7.5% | -7.52% | PASS |  |  |
| QPUX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QPUX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.56× / 0.29× | 1.56× / 0.29× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QPUX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 468052) | 20 bars, last ('2026-11-17', 468052) | PASS |  |  |
| QPUX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.56, OBV falling | condition true | PASS |  |  |
| QTUM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $122.61 | $122.61 | PASS |  |  |
| QTUM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $132.72 | $132.72 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QTUM | E3 | percent from the 21-day average | 7.6% below | 7.6% below | PASS |  |  |
| QTUM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QTUM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.78 | $4.78 (sr=4.7808) | PASS |  | Wilder ATR14 |
| QTUM | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| QTUM | L-ema21 | ladder row ema21: price and gap = price vs average | $132.72, -7.6% | $132.72, -7.6% | PASS |  |  |
| QTUM | L-note | "Last close $X · date" note = last completed bar | Last close $122.42 · Nov 17 | $122.42 · Nov 17 | PASS |  |  |
| QTUM | L-now | ladder price row = compared price; name = the basis label | $122.61 "After hours" | $122.61 "after hours" | PASS |  |  |
| QTUM | L-sma200 | ladder row sma200: price and gap = price vs average | $137.95, -11.1% | $137.95, -11.1% | PASS |  |  |
| QTUM | L-sma50 | ladder row sma50: price and gap = price vs average | $142.19, -13.8% | $142.19, -13.8% | PASS |  |  |
| QTUM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $122.61 / entry $122.61 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QTUM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QTUM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.8 | 35.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QTUM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +17.7% vs +11.2% | 17.7% vs 11.2% | PASS |  |  |
| QTUM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QTUM | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.6 | 33.6 | PASS |  | Wilder, completed bars |
| QTUM | T4w | words "20 or more / below 20" | 20 or more | ADX 33.6 | PASS |  |  |
| QTUM | T5 | "counted at the last close ($X, date)" = last completed bar | $122.42, Nov 17 | $122.42, Nov 17 | PASS |  |  |
| QTUM | T6 | price vs 200-day average (S1 pattern sma values) | $122.42 vs $137.95 · -11.3% | $122.42 vs $137.95 · -11.3% | PASS |  |  |
| QTUM | T6w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T7 | price vs 50-day average (S1 pattern sma values) | $122.42 vs $142.19 · -13.9% | $122.42 vs $142.19 · -13.9% | PASS |  |  |
| QTUM | T7w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.5% over 30 td | +2.5% over 30 td | PASS |  |  |
| QTUM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QTUM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QTUM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.7% below $169.21 | 27.7% below $169.21 | PASS |  | closing high would be 167.97 |
| QTUM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.7% below | PASS |  |  |
| QTUM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $169.21 | $169.20796276695265 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QTUM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.65%, close location 0.52, OBV falling |
| QTUM | V2 | day change of the last completed bar | down 1.6% | -1.65% | PASS |  |  |
| QTUM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QTUM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.00× / 0.42× | 1.00× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QTUM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 335007) | 20 bars, last ('2026-11-17', 335007) | PASS |  |  |
| RBOT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $27.09 | $27.09 | PASS |  |  |
| RBOT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $29.31 | $29.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RBOT.TO | E3 | percent from the 21-day average | 7.6% below | 7.6% below | PASS |  |  |
| RBOT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| RBOT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.61 | $0.61 (sr=0.6077) | PASS |  | Wilder ATR14 |
| RBOT.TO | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  · 3.6 day-moves below |
| RBOT.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.6 | +6.6 | PASS |  |  |
| RBOT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $29.31, -7.6% | $29.31, -7.6% | PASS |  |  |
| RBOT.TO | L-now | ladder price row = compared price; name = the basis label | $27.09 "Last close" | $27.09 "last close" | PASS |  |  |
| RBOT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.29, -18.6% | $33.29, -18.6% | PASS |  |  |
| RBOT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $30.93, -12.4% | $30.93, -12.4% | PASS |  |  |
| RBOT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RBOT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.1 | 31.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RBOT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -14.9% vs +11.2% | -14.9% vs 11.2% | PASS |  |  |
| RBOT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RBOT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.8 | 34.8 | PASS |  | Wilder, completed bars |
| RBOT.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 34.8 | PASS |  |  |
| RBOT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $27.09 vs $33.29 · -18.6% | $27.09 vs $33.29 · -18.6% | PASS |  |  |
| RBOT.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| RBOT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $27.09 vs $30.93 · -12.4% | $27.09 vs $30.93 · -12.4% | PASS |  |  |
| RBOT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| RBOT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.0% over 30 td | -2.0% over 30 td | PASS |  |  |
| RBOT.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| RBOT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RBOT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.0% below $38.15 | 29.0% below $38.15 | PASS |  | closing high would be 38.15 |
| RBOT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.0% below | PASS |  |  |
| RBOT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.15 | $38.150001525878906 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RBOT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.60%, close location 0.18, OBV falling |
| RBOT.TO | V2 | day change of the last completed bar | down 1.6% | -1.60% | PASS |  |  |
| RBOT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.18 (raw 0.1800) | PASS |  |  |
| RBOT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RBOT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 4.74× / 0.71× | 4.74× / 0.71× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RBOT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 15113) | 20 bars, last ('2026-11-17', 15113) | PASS |  |  |
| RBOT.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 4.74, OBV falling | condition true | PASS |  |  |
| RTX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $198.00 | $198.00 | PASS |  |  |
| RTX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $196.2 | $196.20 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RTX | E3 | percent from the 21-day average | 0.9% above | 0.9% above | PASS |  |  |
| RTX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RTX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.28 | $5.28 (sr=5.2796) | PASS |  | Wilder ATR14 |
| RTX | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| RTX | L-ema21 | ladder row ema21: price and gap = price vs average | $196.2, 0.9% | $196.20, 0.9% | PASS |  |  |
| RTX | L-note | "Last close $X · date" note = last completed bar | Last close $198.00 · Nov 17 | $198.00 · Nov 17 | PASS |  |  |
| RTX | L-now | ladder price row = compared price; name = the basis label | $198 "After hours" | $198.00 "after hours" | PASS |  |  |
| RTX | L-sma200 | ladder row sma200: price and gap = price vs average | $194.48, 1.8% | $194.48, 1.8% | PASS |  |  |
| RTX | L-sma50 | ladder row sma50: price and gap = price vs average | $192.67, 2.8% | $192.67, 2.8% | PASS |  |  |
| RTX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $198.00 / entry $198.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RTX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RTX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 52.9 | 52.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RTX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.4% vs +11.2% | 14.4% vs 11.2% | PASS |  |  |
| RTX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RTX | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.4 | 18.4 | PASS |  | Wilder, completed bars |
| RTX | T4w | words "20 or more / below 20" | below 20 | ADX 18.4 | PASS |  |  |
| RTX | T5 | "counted at the last close ($X, date)" = last completed bar | $198.00, Nov 17 | $198.00, Nov 17 | PASS |  |  |
| RTX | T6 | price vs 200-day average (S1 pattern sma values) | $198.00 vs $194.48 · +1.8% | $198.00 vs $194.48 · 1.8% | PASS |  |  |
| RTX | T6w | word "Above" | Above | Above | PASS |  |  |
| RTX | T7 | price vs 50-day average (S1 pattern sma values) | $198.00 vs $192.67 · +2.8% | $198.00 vs $192.67 · 2.8% | PASS |  |  |
| RTX | T7w | word "Above" | Above | Above | PASS |  |  |
| RTX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.3% over 30 td | +0.3% over 30 td | PASS |  |  |
| RTX | T8r | word "rising" | still rising | rising | PASS |  |  |
| RTX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RTX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.5% below $226.41 | 12.5% below $226.41 | PASS |  | closing high would be 225.49 |
| RTX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.5% below | PASS |  |  |
| RTX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $226.41 | $226.41000366210938 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RTX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 1.60%, close location 1.00, OBV rising |
| RTX | V2 | day change of the last completed bar | up 1.6% | +1.60% | PASS |  |  |
| RTX | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 1.00 (raw 1.0000) | PASS |  |  |
| RTX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| RTX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.14× / 0.60× | 1.14× / 0.60× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RTX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 5509134) | 20 bars, last ('2026-11-17', 5509134) | PASS |  |  |
| RY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $280.99 | $280.99 | PASS |  |  |
| RY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $285.03 | $285.03 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RY.TO | E3 | percent from the 21-day average | 1.4% below | 1.4% below | PASS |  |  |
| RY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.63 | $4.63 (sr=4.6333) | PASS |  | Wilder ATR14 |
| RY.TO | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves below |
| RY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $285.03, -1.4% | $285.03, -1.4% | PASS |  |  |
| RY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $280.99 · Nov 17 | $280.99 · Nov 17 | PASS |  |  |
| RY.TO | L-now | ladder price row = compared price; name = the basis label | $280.99 "After hours" | $280.99 "after hours" | PASS |  |  |
| RY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $263.3, 6.7% | $263.30, 6.7% | PASS |  |  |
| RY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $282.08, -0.4% | $282.08, -0.4% | PASS |  |  |
| RY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $280.99 / entry $280.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.8 | 44.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.4% vs +11.2% | 39.4% vs 11.2% | PASS |  |  |
| RY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.0 | 14.0 | PASS |  | Wilder, completed bars |
| RY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 14.0 | PASS |  |  |
| RY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $280.99, Nov 17 | $280.99, Nov 17 | PASS |  |  |
| RY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $280.99 vs $263.30 · +6.7% | $280.99 vs $263.30 · 6.7% | PASS |  |  |
| RY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| RY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $280.99 vs $282.08 · -0.4% | $280.99 vs $282.08 · -0.4% | PASS |  |  |
| RY.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| RY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| RY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| RY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.2% below $302.65 | 7.2% below $302.65 | PASS |  | closing high would be 302.02 |
| RY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.2% below | PASS |  |  |
| RY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.65 | $302.6498839841861 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.65%, close location 0.37, OBV falling |
| RY.TO | V2 | day change of the last completed bar | down 1.6% | -1.65% | PASS |  |  |
| RY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.13× / 1.00× | 1.13× / 1.00× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3766734) | 20 bars, last ('2026-11-17', 3766734) | PASS |  |  |
| SETM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $25.18 | $25.18 | PASS |  |  |
| SETM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.89 | $24.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SETM | E3 | percent from the 21-day average | 1.2% above | 1.2% above | PASS |  |  |
| SETM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SETM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.99 | $0.99 (sr=0.9864) | PASS |  | Wilder ATR14 |
| SETM | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| SETM | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.6 | +7.6 | PASS |  |  |
| SETM | L-ema21 | ladder row ema21: price and gap = price vs average | $24.89, 1.2% | $24.89, 1.2% | PASS |  |  |
| SETM | L-note | "Last close $X · date" note = last completed bar | Last close $22.11 · Nov 17 | $22.11 · Nov 17 | PASS |  |  |
| SETM | L-now | ladder price row = compared price; name = the basis label | $25.18 "After hours" | $25.18 "after hours" | PASS |  |  |
| SETM | L-sma200 | ladder row sma200: price and gap = price vs average | $32.41, -22.3% | $32.41, -22.3% | PASS |  |  |
| SETM | L-sma50 | ladder row sma50: price and gap = price vs average | $27.62, -8.8% | $27.62, -8.8% | PASS |  |  |
| SETM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $25.18 / entry $25.18 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SETM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SETM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.5 | 31.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SETM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -13.7% vs +11.2% | -13.7% vs 11.2% | PASS |  |  |
| SETM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SETM | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.2 | 34.2 | PASS |  | Wilder, completed bars |
| SETM | T4w | words "20 or more / below 20" | 20 or more | ADX 34.2 | PASS |  |  |
| SETM | T5 | "counted at the last close ($X, date)" = last completed bar | $22.11, Nov 17 | $22.11, Nov 17 | PASS |  |  |
| SETM | T6 | price vs 200-day average (S1 pattern sma values) | $22.11 vs $32.41 · -31.8% | $22.11 vs $32.41 · -31.8% | PASS |  |  |
| SETM | T6w | word "Below" | Below | Below | PASS |  |  |
| SETM | T7 | price vs 50-day average (S1 pattern sma values) | $22.11 vs $27.62 · -19.9% | $22.11 vs $27.62 · -20.0% | PASS |  |  |
| SETM | T7w | word "Below" | Below | Below | PASS |  |  |
| SETM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.5% over 30 td | -3.5% over 30 td | PASS |  |  |
| SETM | T8r | word "rising" | not rising | not rising | PASS |  |  |
| SETM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SETM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 45.5% below $40.55 | 45.5% below $40.55 | PASS |  | closing high would be 39.73 |
| SETM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 45.5% below | PASS |  |  |
| SETM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $40.55 | $40.54999923706055 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SETM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.34%, close location 0.17, OBV falling |
| SETM | V2 | day change of the last completed bar | down 1.3% | -1.34% | PASS |  |  |
| SETM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1711) | PASS |  |  |
| SETM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SETM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.93× / 0.30× | 1.93× / 0.30× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SETM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 321446) | 20 bars, last ('2026-11-17', 321446) | PASS |  |  |
| SETM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.93, OBV falling | condition true | PASS |  |  |
| SGRD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.95 | $17.95 | PASS |  |  |
| SGRD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.63 | $18.63 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SGRD.TO | E3 | percent from the 21-day average | 3.7% below | 3.7% below | PASS |  |  |
| SGRD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SGRD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.39 | $0.39 (sr=0.3869) | PASS |  | Wilder ATR14 |
| SGRD.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| SGRD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $18.63, -3.7% | $18.63, -3.7% | PASS |  |  |
| SGRD.TO | L-now | ladder price row = compared price; name = the basis label | $17.95 "Last close" | $17.95 "last close" | PASS |  |  |
| SGRD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $19.53, -8.1% | $19.53, -8.1% | PASS |  |  |
| SGRD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.4 | 40.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SGRD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.0 | 27.0 | PASS |  | Wilder, completed bars |
| SGRD.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.0 | PASS |  |  |
| SGRD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.44%, close location 0.41, OBV falling |
| SGRD.TO | V2 | day change of the last completed bar | down 0.4% | -0.44% | PASS |  |  |
| SGRD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SGRD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.15× / 0.20× | 0.15× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SGRD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1368) | 20 bars, last ('2026-11-17', 1368) | PASS |  |  |
| SMH | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $478.75 | $478.75 | PASS |  |  |
| SMH | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $508.11 | $508.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SMH | E3 | percent from the 21-day average | 5.8% below | 5.8% below | PASS |  |  |
| SMH | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SMH | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $24.12 | $24.12 (sr=24.1204) | PASS |  | Wilder ATR14 |
| SMH | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| SMH | L-ema21 | ladder row ema21: price and gap = price vs average | $508.11, -5.8% | $508.11, -5.8% | PASS |  |  |
| SMH | L-note | "Last close $X · date" note = last completed bar | Last close $460.10 · Nov 17 | $460.10 · Nov 17 | PASS |  |  |
| SMH | L-now | ladder price row = compared price; name = the basis label | $478.75 "After hours" | $478.75 "after hours" | PASS |  |  |
| SMH | L-sma200 | ladder row sma200: price and gap = price vs average | $524.44, -8.7% | $524.44, -8.7% | PASS |  |  |
| SMH | L-sma50 | ladder row sma50: price and gap = price vs average | $555.43, -13.8% | $555.43, -13.8% | PASS |  |  |
| SMH | S5-price | S5: the same live price reads the same on the header and the Entry block | header $478.75 / entry $478.75 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SMH | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SMH | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.3 | 35.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SMH | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +35.6% vs +11.2% | 35.6% vs 11.2% | PASS |  |  |
| SMH | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SMH | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.9 | 34.9 | PASS |  | Wilder, completed bars |
| SMH | T4w | words "20 or more / below 20" | 20 or more | ADX 34.9 | PASS |  |  |
| SMH | T5 | "counted at the last close ($X, date)" = last completed bar | $460.10, Nov 17 | $460.10, Nov 17 | PASS |  |  |
| SMH | T6 | price vs 200-day average (S1 pattern sma values) | $460.10 vs $524.44 · -12.3% | $460.10 vs $524.44 · -12.3% | PASS |  |  |
| SMH | T6w | word "Below" | Below | Below | PASS |  |  |
| SMH | T7 | price vs 50-day average (S1 pattern sma values) | $460.10 vs $555.43 · -17.2% | $460.10 vs $555.43 · -17.2% | PASS |  |  |
| SMH | T7w | word "Below" | Below | Below | PASS |  |  |
| SMH | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.4% over 30 td | +4.4% over 30 td | PASS |  |  |
| SMH | T8r | word "rising" | still rising | rising | PASS |  |  |
| SMH | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SMH | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 31.5% below $671.83 | 31.5% below $671.83 | PASS |  | closing high would be 668.91 |
| SMH | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 31.5% below | PASS |  |  |
| SMH | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $671.83 | $671.8300170898438 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SMH | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.39%, close location 0.70, OBV falling |
| SMH | V2 | day change of the last completed bar | down 0.4% | -0.39% | PASS |  |  |
| SMH | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SMH | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.28× / 0.07× | 1.28× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SMH | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 11795072) | 20 bars, last ('2026-11-17', 11795072) | PASS |  |  |
| SNDK.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $19.28 | $19.28 | PASS |  |  |
| SNDK.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $25.69 | $25.69 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SNDK.TO | E3 | percent from the 21-day average | 25.0% below | 25.0% below | PASS |  |  |
| SNDK.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SNDK.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.48 | $2.48 (sr=2.4773) | PASS |  | Wilder ATR14 |
| SNDK.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| SNDK.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.4 | +3.4 | PASS |  |  |
| SNDK.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $25.69, -25.0% | $25.69, -25.0% | PASS |  |  |
| SNDK.TO | L-now | ladder price row = compared price; name = the basis label | $19.28 "Last close" | $19.28 "last close" | PASS |  |  |
| SNDK.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $34.18, -43.6% | $34.18, -43.6% | PASS |  |  |
| SNDK.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.7 | 30.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SNDK.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 39.3 | 39.3 | PASS |  | Wilder, completed bars |
| SNDK.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 39.3 | PASS |  |  |
| SNDK.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.63%, close location 0.67, OBV falling |
| SNDK.TO | V2 | day change of the last completed bar | down 1.6% | -1.63% | PASS |  |  |
| SNDK.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SNDK.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.73× / 0.13× | 1.73× / 0.13× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SNDK.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 2166206) | 20 bars, last ('2026-11-17', 2166206) | PASS |  |  |
| SNDK.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.73, OBV falling | condition true | PASS |  |  |
| SO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $93.33 | $93.33 | PASS |  |  |
| SO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $91.87 | $91.87 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SO | E3 | percent from the 21-day average | 1.6% above | 1.6% above | PASS |  |  |
| SO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.80 | $1.80 (sr=1.8002) | PASS |  | Wilder ATR14 |
| SO | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves above |
| SO | L-ema21 | ladder row ema21: price and gap = price vs average | $91.87, 1.6% | $91.87, 1.6% | PASS |  |  |
| SO | L-note | "Last close $X · date" note = last completed bar | Last close $93.60 · Nov 17 | $93.60 · Nov 17 | PASS |  |  |
| SO | L-now | ladder price row = compared price; name = the basis label | $93.33 "After hours" | $93.33 "after hours" | PASS |  |  |
| SO | L-sma200 | ladder row sma200: price and gap = price vs average | $91.17, 2.4% | $91.17, 2.4% | PASS |  |  |
| SO | L-sma50 | ladder row sma50: price and gap = price vs average | $88.22, 5.8% | $88.22, 5.8% | PASS |  |  |
| SO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $93.33 / entry $93.33 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.5 | 59.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.7% vs +11.2% | 6.7% vs 11.2% | PASS |  |  |
| SO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.9 | 27.9 | PASS |  | Wilder, completed bars |
| SO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.9 | PASS |  |  |
| SO | T5 | "counted at the last close ($X, date)" = last completed bar | $93.60, Nov 17 | $93.60, Nov 17 | PASS |  |  |
| SO | T6 | price vs 200-day average (S1 pattern sma values) | $93.60 vs $91.17 · +2.7% | $93.60 vs $91.17 · 2.7% | PASS |  |  |
| SO | T6w | word "Above" | Above | Above | PASS |  |  |
| SO | T7 | price vs 50-day average (S1 pattern sma values) | $93.60 vs $88.22 · +6.1% | $93.60 vs $88.22 · 6.1% | PASS |  |  |
| SO | T7w | word "Above" | Above | Above | PASS |  |  |
| SO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.0% over 30 td | +1.0% over 30 td | PASS |  |  |
| SO | T8r | word "rising" | still rising | rising | PASS |  |  |
| SO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.1% below $97.65 | 4.1% below $97.65 | PASS |  | closing high would be 96.70 |
| SO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.1% below | PASS |  |  |
| SO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $97.65 | $97.64764917949712 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.10%, close location 0.18, OBV rising |
| SO | V2 | day change of the last completed bar | down 1.1% | -1.10% | PASS |  |  |
| SO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.18 (raw 0.1829) | PASS |  |  |
| SO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| SO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.25× / 0.57× | 1.25× / 0.57× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 8981144) | 20 bars, last ('2026-11-17', 8981144) | PASS |  |  |
| SOXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $52.26 | $52.26 | PASS |  |  |
| SOXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.21 | $73.21 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL | E3 | percent from the 21-day average | 28.6% below | 28.6% below | PASS |  |  |
| SOXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $12.24 | $12.24 (sr=12.2363) | PASS |  | Wilder ATR14 |
| SOXL | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| SOXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| SOXL | L-ema21 | ladder row ema21: price and gap = price vs average | $73.21, -28.6% | $73.21, -28.6% | PASS |  |  |
| SOXL | L-note | "Last close $X · date" note = last completed bar | Last close $49.07 · Nov 17 | $49.07 · Nov 17 | PASS |  |  |
| SOXL | L-now | ladder price row = compared price; name = the basis label | $52.26 "After hours" | $52.26 "after hours" | PASS |  |  |
| SOXL | L-sma200 | ladder row sma200: price and gap = price vs average | $123.86, -57.8% | $123.86, -57.8% | PASS |  |  |
| SOXL | L-sma50 | ladder row sma50: price and gap = price vs average | $107.53, -51.4% | $107.53, -51.4% | PASS |  |  |
| SOXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $52.26 / entry $52.26 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.4 | 34.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +33.3% vs +11.2% | 33.3% vs 11.2% | PASS |  |  |
| SOXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.8 | 34.8 | PASS |  | Wilder, completed bars |
| SOXL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.8 | PASS |  |  |
| SOXL | T5 | "counted at the last close ($X, date)" = last completed bar | $49.07, Nov 17 | $49.07, Nov 17 | PASS |  |  |
| SOXL | T6 | price vs 200-day average (S1 pattern sma values) | $49.07 vs $123.86 · -60.4% | $49.07 vs $123.86 · -60.4% | PASS |  |  |
| SOXL | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T7 | price vs 50-day average (S1 pattern sma values) | $49.07 vs $107.53 · -54.4% | $49.07 vs $107.53 · -54.4% | PASS |  |  |
| SOXL | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.3% over 30 td | +4.3% over 30 td | PASS |  |  |
| SOXL | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 83.7% below $301.80 | 83.7% below $301.80 | PASS |  | closing high would be 300.57 |
| SOXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 83.7% below | PASS |  |  |
| SOXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $301.80 | $301.8021115035658 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.64%, close location 0.79, OBV falling |
| SOXL | V2 | day change of the last completed bar | up 0.6% | +0.64% | PASS |  |  |
| SOXL | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.79 (raw 0.7864) | PASS |  |  |
| SOXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.99× / 0.03× | 1.99× / 0.03× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 237206335) | 20 bars, last ('2026-11-17', 237206335) | PASS |  |  |
| SOXL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.99, OBV falling | condition true | PASS |  |  |
| SOXL.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.36 | $12.36 | PASS |  |  |
| SOXL.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.36 | $18.36 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL.NE | E3 | percent from the 21-day average | 32.7% below | 32.7% below | PASS |  |  |
| SOXL.NE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXL.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.02 | $2.02 (sr=2.0226) | PASS |  | Wilder ATR14 |
| SOXL.NE | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| SOXL.NE | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| SOXL.NE | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.2 | +6.2 | PASS |  |  |
| SOXL.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $18.36, -32.7% | $18.36, -32.7% | PASS |  |  |
| SOXL.NE | L-note | "Last close $X · date" note = last completed bar | Last close $12.36 · Nov 17 | $12.36 · Nov 17 | PASS |  |  |
| SOXL.NE | L-now | ladder price row = compared price; name = the basis label | $12.36 "After hours" | $12.36 "after hours" | PASS |  |  |
| SOXL.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.87, -60.0% | $30.87, -60.0% | PASS |  |  |
| SOXL.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $26.74, -53.8% | $26.74, -53.8% | PASS |  |  |
| SOXL.NE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $12.36 / entry $12.36 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| SOXX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $141.46 | $141.46 | PASS |  |  |
| SOXX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $154.59 | $154.59 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXX | E3 | percent from the 21-day average | 8.5% below | 8.5% below | PASS |  |  |
| SOXX | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SOXX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.41 | $8.41 (sr=8.4055) | PASS |  | Wilder ATR14 |
| SOXX | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| SOXX | L-ema21 | ladder row ema21: price and gap = price vs average | $154.59, -8.5% | $154.59, -8.5% | PASS |  |  |
| SOXX | L-now | ladder price row = compared price; name = the basis label | $141.46 "Last close" | $141.46 "last close" | PASS |  |  |
| SOXX | L-sma200 | ladder row sma200: price and gap = price vs average | $160.52, -11.9% | $160.52, -11.9% | PASS |  |  |
| SOXX | L-sma50 | ladder row sma50: price and gap = price vs average | $170.55, -17.1% | $170.55, -17.1% | PASS |  |  |
| SOXX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.9 | 37.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +50.1% vs +11.2% | 50.1% vs 11.2% | PASS |  |  |
| SOXX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXX | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.0 | 32.0 | PASS |  | Wilder, completed bars |
| SOXX | T4w | words "20 or more / below 20" | 20 or more | ADX 32.0 | PASS |  |  |
| SOXX | T6 | price vs 200-day average (S1 pattern sma values) | $141.46 vs $160.52 · -11.9% | $141.46 vs $160.52 · -11.9% | PASS |  |  |
| SOXX | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T7 | price vs 50-day average (S1 pattern sma values) | $141.46 vs $170.55 · -17.1% | $141.46 vs $170.55 · -17.1% | PASS |  |  |
| SOXX | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.2% over 30 td | +5.2% over 30 td | PASS |  |  |
| SOXX | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.3% below $218.51 | 35.3% below $218.51 | PASS |  | closing high would be 218.19 |
| SOXX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.3% below | PASS |  |  |
| SOXX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $218.51 | $218.50713476135667 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.17%, close location 0.78, OBV falling |
| SOXX | V2 | day change of the last completed bar | up 0.2% | +0.17% | PASS |  |  |
| SOXX | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.78 (raw 0.7757) | PASS |  |  |
| SOXX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.26× / 0.03× | 1.26× / 0.03× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 37612248) | 20 bars, last ('2026-11-17', 37612248) | PASS |  |  |
| SPCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $10.35 | $10.35 | PASS |  |  |
| SPCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.16 | $13.16 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SPCL | E3 | percent from the 21-day average | 21.3% below | 21.3% below | PASS |  |  |
| SPCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SPCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.71 | $1.71 (sr=1.7136) | PASS |  | Wilder ATR14 |
| SPCL | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| SPCL | L-ema21 | ladder row ema21: price and gap = price vs average | $13.16, -21.3% | $13.16, -21.3% | PASS |  |  |
| SPCL | L-note | "Last close $X · date" note = last completed bar | Last close $10.13 · Nov 17 | $10.13 · Nov 17 | PASS |  |  |
| SPCL | L-now | ladder price row = compared price; name = the basis label | $10.35 "After hours" | $10.35 "after hours" | PASS |  |  |
| SPCL | L-sma50 | ladder row sma50: price and gap = price vs average | $17.37, -40.4% | $17.37, -40.4% | PASS |  |  |
| SPCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $10.35 / entry $10.35 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SPCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.0 | 37.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SPCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.8 | 31.8 | PASS |  | Wilder, completed bars |
| SPCL | T4w | words "20 or more / below 20" | 20 or more | ADX 31.8 | PASS |  |  |
| SPCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.97%, close location 0.39, OBV falling |
| SPCL | V2 | day change of the last completed bar | down 3.0% | -2.97% | PASS |  |  |
| SPCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SPCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.40× / 0.18× | 0.40× / 0.18× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SPCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 15125) | 20 bars, last ('2026-11-17', 15125) | PASS |  |  |
| TSLA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $381.60 | $381.60 | PASS |  |  |
| TSLA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $382.31 | $382.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLA | E3 | percent from the 21-day average | 0.2% below | 0.2% below | PASS |  |  |
| TSLA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.00 | $16.00 (sr=15.9962) | PASS |  | Wilder ATR14 |
| TSLA | E5 | distance in normal day-moves | 0.0 | 0.0 | PASS |  | gauge dot note uses the same number:  · 0.0 day-moves below |
| TSLA | L-ema21 | ladder row ema21: price and gap = price vs average | $382.31, -0.2% | $382.31, -0.2% | PASS |  |  |
| TSLA | L-note | "Last close $X · date" note = last completed bar | Last close $380.11 · Nov 17 | $380.11 · Nov 17 | PASS |  |  |
| TSLA | L-now | ladder price row = compared price; name = the basis label | $381.6 "After hours" | $381.60 "after hours" | PASS |  |  |
| TSLA | L-sma200 | ladder row sma200: price and gap = price vs average | $382.27, -0.2% | $382.27, -0.2% | PASS |  |  |
| TSLA | L-sma50 | ladder row sma50: price and gap = price vs average | $375.49, 1.6% | $375.49, 1.6% | PASS |  |  |
| TSLA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $381.60 / entry $381.60 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.6 | 49.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -7.0% vs +11.2% | -7.0% vs 11.2% | PASS |  |  |
| TSLA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLA | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.2 | 12.2 | PASS |  | Wilder, completed bars |
| TSLA | T4w | words "20 or more / below 20" | below 20 | ADX 12.2 | PASS |  |  |
| TSLA | T5 | "counted at the last close ($X, date)" = last completed bar | $380.11, Nov 17 | $380.11, Nov 17 | PASS |  |  |
| TSLA | T6 | price vs 200-day average (S1 pattern sma values) | $380.11 vs $382.27 · -0.6% | $380.11 vs $382.27 · -0.6% | PASS |  |  |
| TSLA | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLA | T7 | price vs 50-day average (S1 pattern sma values) | $380.11 vs $375.49 · +1.2% | $380.11 vs $375.49 · 1.2% | PASS |  |  |
| TSLA | T7w | word "Above" | Above | Above | PASS |  |  |
| TSLA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.5% over 30 td | -2.5% over 30 td | PASS |  |  |
| TSLA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.8% below $498.83 | 23.8% below $498.83 | PASS |  | closing high would be 489.88 |
| TSLA | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.8% below | PASS |  |  |
| TSLA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $498.83 | $498.8299865722656 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change 0.10%, close location 0.69, OBV falling |
| TSLA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSLA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.61× / 0.02× | 0.61× / 0.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 21953771) | 20 bars, last ('2026-11-17', 21953771) | PASS |  |  |
| TSLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $10.06 | $10.06 | PASS |  |  |
| TSLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $10.12 | $10.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLL | E3 | percent from the 21-day average | 0.6% below | 0.6% below | PASS |  |  |
| TSLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.84 | $0.84 (sr=0.8446) | PASS |  | Wilder ATR14 |
| TSLL | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves below |
| TSLL | L-ema21 | ladder row ema21: price and gap = price vs average | $10.12, -0.6% | $10.12, -0.6% | PASS |  |  |
| TSLL | L-note | "Last close $X · date" note = last completed bar | Last close $9.81 · Nov 17 | $9.81 · Nov 17 | PASS |  |  |
| TSLL | L-now | ladder price row = compared price; name = the basis label | $10.06 "After hours" | $10.06 "after hours" | PASS |  |  |
| TSLL | L-sma200 | ladder row sma200: price and gap = price vs average | $11.73, -14.2% | $11.73, -14.2% | PASS |  |  |
| TSLL | L-sma50 | ladder row sma50: price and gap = price vs average | $9.97, 0.9% | $9.97, 0.9% | PASS |  |  |
| TSLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $10.06 / entry $10.06 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.7 | 47.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -38.6% vs +11.2% | -38.6% vs 11.2% | PASS |  |  |
| TSLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.0 | 12.0 | PASS |  | Wilder, completed bars |
| TSLL | T4w | words "20 or more / below 20" | below 20 | ADX 12.0 | PASS |  |  |
| TSLL | T5 | "counted at the last close ($X, date)" = last completed bar | $9.81, Nov 17 | $9.81, Nov 17 | PASS |  |  |
| TSLL | T6 | price vs 200-day average (S1 pattern sma values) | $9.81 vs $11.73 · -16.4% | $9.81 vs $11.73 · -16.4% | PASS |  |  |
| TSLL | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T7 | price vs 50-day average (S1 pattern sma values) | $9.81 vs $9.97 · -1.6% | $9.81 vs $9.97 · -1.6% | PASS |  |  |
| TSLL | T7w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -9.6% over 30 td | -9.5% over 30 td | PASS |  |  |
| TSLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 57.5% below $23.10 | 57.5% below $23.10 | PASS |  | closing high would be 22.41 |
| TSLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 57.5% below | PASS |  |  |
| TSLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $23.10 | $23.09813194913166 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| TSLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.64× / 0.01× | 0.64× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 35186206) | 20 bars, last ('2026-11-17', 35186206) | PASS |  |  |
| TSM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $377.51 | $377.51 | PASS |  |  |
| TSM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $401.53 | $401.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSM | E3 | percent from the 21-day average | 6.0% below | 6.0% below | PASS |  |  |
| TSM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.92 | $17.92 (sr=17.9164) | PASS |  | Wilder ATR14 |
| TSM | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| TSM | L-ema21 | ladder row ema21: price and gap = price vs average | $401.53, -6.0% | $401.53, -6.0% | PASS |  |  |
| TSM | L-note | "Last close $X · date" note = last completed bar | Last close $359.69 · Nov 17 | $359.69 · Nov 17 | PASS |  |  |
| TSM | L-now | ladder price row = compared price; name = the basis label | $377.51 "After hours" | $377.51 "after hours" | PASS |  |  |
| TSM | L-sma200 | ladder row sma200: price and gap = price vs average | $402, -6.1% | $402.00, -6.1% | PASS |  |  |
| TSM | L-sma50 | ladder row sma50: price and gap = price vs average | $427.3, -11.7% | $427.30, -11.7% | PASS |  |  |
| TSM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $377.51 / entry $377.51 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.7 | 35.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.9% vs +11.2% | 28.9% vs 11.2% | PASS |  |  |
| TSM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSM | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.0 | 31.0 | PASS |  | Wilder, completed bars |
| TSM | T4w | words "20 or more / below 20" | 20 or more | ADX 31.0 | PASS |  |  |
| TSM | T5 | "counted at the last close ($X, date)" = last completed bar | $359.69, Nov 17 | $359.69, Nov 17 | PASS |  |  |
| TSM | T6 | price vs 200-day average (S1 pattern sma values) | $359.69 vs $402.00 · -10.5% | $359.69 vs $402.00 · -10.5% | PASS |  |  |
| TSM | T6w | word "Below" | Below | Below | PASS |  |  |
| TSM | T7 | price vs 50-day average (S1 pattern sma values) | $359.69 vs $427.30 · -15.8% | $359.69 vs $427.30 · -15.8% | PASS |  |  |
| TSM | T7w | word "Below" | Below | Below | PASS |  |  |
| TSM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.8% over 30 td | +3.8% over 30 td | PASS |  |  |
| TSM | T8r | word "rising" | still rising | rising | PASS |  |  |
| TSM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.2% below $487.47 | 26.2% below $487.47 | PASS |  | closing high would be 485.80 |
| TSM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.2% below | PASS |  |  |
| TSM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $487.47 | $487.4700012207031 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -3.68%, close location 0.32, OBV falling |
| TSM | V2 | day change of the last completed bar | down 3.7% | -3.68% | PASS |  |  |
| TSM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.93× / 0.74× | 1.93× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 24446605) | 20 bars, last ('2026-11-17', 24446605) | PASS |  |  |
| TSM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.93, OBV falling | condition true | PASS |  |  |
| UBOT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $15.04 | $15.04 | PASS |  |  |
| UBOT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $17.76 | $17.76 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UBOT | E3 | percent from the 21-day average | 15.3% below | 15.3% below | PASS |  |  |
| UBOT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| UBOT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.84 | $0.84 (sr=0.8384) | PASS |  | Wilder ATR14 |
| UBOT | E5 | distance in normal day-moves | 3.2 | 3.2 | PASS |  | gauge dot note uses the same number:  · 3.2 day-moves below |
| UBOT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.3 | +7.3 | PASS |  |  |
| UBOT | L-ema21 | ladder row ema21: price and gap = price vs average | $17.76, -15.3% | $17.76, -15.3% | PASS |  |  |
| UBOT | L-note | "Last close $X · date" note = last completed bar | Last close $15.04 · Nov 17 | $15.04 · Nov 17 | PASS |  |  |
| UBOT | L-now | ladder price row = compared price; name = the basis label | $15.04 "After hours" | $15.04 "after hours" | PASS |  |  |
| UBOT | L-sma200 | ladder row sma200: price and gap = price vs average | $23.86, -37.0% | $23.86, -37.0% | PASS |  |  |
| UBOT | L-sma50 | ladder row sma50: price and gap = price vs average | $19.98, -24.7% | $19.98, -24.7% | PASS |  |  |
| UBOT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $15.04 / entry $15.04 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UBOT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UBOT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.8 | 30.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UBOT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -34.1% vs +11.2% | -34.1% vs 11.2% | PASS |  |  |
| UBOT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UBOT | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.3 | 38.4 | PASS |  | Wilder, completed bars |
| UBOT | T4w | words "20 or more / below 20" | 20 or more | ADX 38.4 | PASS |  |  |
| UBOT | T5 | "counted at the last close ($X, date)" = last completed bar | $15.04, Nov 17 | $15.04, Nov 17 | PASS |  |  |
| UBOT | T6 | price vs 200-day average (S1 pattern sma values) | $15.04 vs $23.86 · -37.0% | $15.04 vs $23.86 · -37.0% | PASS |  |  |
| UBOT | T6w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T7 | price vs 50-day average (S1 pattern sma values) | $15.04 vs $19.98 · -24.7% | $15.04 vs $19.98 · -24.7% | PASS |  |  |
| UBOT | T7w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.9% over 30 td | -4.9% over 30 td | PASS |  |  |
| UBOT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UBOT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UBOT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 52.9% below $31.91 | 52.9% below $31.91 | PASS |  | closing high would be 31.87 |
| UBOT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 52.9% below | PASS |  |  |
| UBOT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.91 | $31.9057638044854 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UBOT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -3.03%, close location 0.46, OBV falling |
| UBOT | V2 | day change of the last completed bar | down 3.0% | -3.03% | PASS |  |  |
| UBOT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UBOT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.39× / 0.54× | 1.39× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UBOT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 22205) | 20 bars, last ('2026-11-17', 22205) | PASS |  |  |
| UFO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.30 | $39.30 | PASS |  |  |
| UFO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.52 | $40.52 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UFO | E3 | percent from the 21-day average | 3.0% below | 3.0% below | PASS |  |  |
| UFO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| UFO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.37 | $1.37 (sr=1.3679) | PASS |  | Wilder ATR14 |
| UFO | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves below |
| UFO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.7 | +4.7 | PASS |  |  |
| UFO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.52, -3.0% | $40.52, -3.0% | PASS |  |  |
| UFO | L-note | "Last close $X · date" note = last completed bar | Last close $39.30 · Nov 17 | $39.30 · Nov 17 | PASS |  |  |
| UFO | L-now | ladder price row = compared price; name = the basis label | $39.3 "After hours" | $39.30 "after hours" | PASS |  |  |
| UFO | L-sma200 | ladder row sma200: price and gap = price vs average | $47, -16.4% | $47.00, -16.4% | PASS |  |  |
| UFO | L-sma50 | ladder row sma50: price and gap = price vs average | $41.56, -5.4% | $41.56, -5.4% | PASS |  |  |
| UFO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $39.30 / entry $39.30 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UFO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UFO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.5 | 43.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UFO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +21.5% vs +11.2% | 21.5% vs 11.2% | PASS |  |  |
| UFO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UFO | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.7 | 24.7 | PASS |  | Wilder, completed bars |
| UFO | T4w | words "20 or more / below 20" | 20 or more | ADX 24.7 | PASS |  |  |
| UFO | T5 | "counted at the last close ($X, date)" = last completed bar | $39.30, Nov 17 | $39.30, Nov 17 | PASS |  |  |
| UFO | T6 | price vs 200-day average (S1 pattern sma values) | $39.30 vs $47.00 · -16.4% | $39.30 vs $47.00 · -16.4% | PASS |  |  |
| UFO | T6w | word "Below" | Below | Below | PASS |  |  |
| UFO | T7 | price vs 50-day average (S1 pattern sma values) | $39.30 vs $41.56 · -5.4% | $39.30 vs $41.56 · -5.4% | PASS |  |  |
| UFO | T7w | word "Below" | Below | Below | PASS |  |  |
| UFO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.8% over 30 td | -0.8% over 30 td | PASS |  |  |
| UFO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UFO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UFO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 42.3% below $68.12 | 42.3% below $68.12 | PASS |  | closing high would be 67.71 |
| UFO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 42.3% below | PASS |  |  |
| UFO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $68.12 | $68.11999548611959 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UFO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.61%, close location 0.36, OBV falling |
| UFO | V2 | day change of the last completed bar | down 0.6% | -0.61% | PASS |  |  |
| UFO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UFO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.50× / 0.18× | 0.50× / 0.17× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UFO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 126910) | 20 bars, last ('2026-11-17', 126910) | PASS |  |  |
| URA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.04 | $30.04 | PASS |  |  |
| URA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.55 | $33.55 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URA | E3 | percent from the 21-day average | 10.5% below | 10.5% below | PASS |  |  |
| URA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| URA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.44 | $1.43 (sr=1.435) | PASS |  | Wilder ATR14 |
| URA | E5 | distance in normal day-moves | 2.4 | 2.4 | PASS |  | gauge dot note uses the same number:  · 2.4 day-moves below |
| URA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.5 | +8.5 | PASS |  |  |
| URA | L-ema21 | ladder row ema21: price and gap = price vs average | $33.55, -10.5% | $33.55, -10.5% | PASS |  |  |
| URA | L-note | "Last close $X · date" note = last completed bar | Last close $30.04 · Nov 17 | $30.04 · Nov 17 | PASS |  |  |
| URA | L-now | ladder price row = compared price; name = the basis label | $30.04 "After hours" | $30.04 "after hours" | PASS |  |  |
| URA | L-sma200 | ladder row sma200: price and gap = price vs average | $45.68, -34.2% | $45.68, -34.2% | PASS |  |  |
| URA | L-sma50 | ladder row sma50: price and gap = price vs average | $37.49, -19.9% | $37.49, -19.9% | PASS |  |  |
| URA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $30.04 / entry $30.04 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.3 | 32.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -28.0% vs +11.2% | -28.0% vs 11.2% | PASS |  |  |
| URA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URA | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.2 | 33.2 | PASS |  | Wilder, completed bars |
| URA | T4w | words "20 or more / below 20" | 20 or more | ADX 33.2 | PASS |  |  |
| URA | T5 | "counted at the last close ($X, date)" = last completed bar | $30.04, Nov 17 | $30.04, Nov 17 | PASS |  |  |
| URA | T6 | price vs 200-day average (S1 pattern sma values) | $30.04 vs $45.68 · -34.2% | $30.04 vs $45.68 · -34.2% | PASS |  |  |
| URA | T6w | word "Below" | Below | Below | PASS |  |  |
| URA | T7 | price vs 50-day average (S1 pattern sma values) | $30.04 vs $37.49 · -19.9% | $30.04 vs $37.49 · -19.9% | PASS |  |  |
| URA | T7w | word "Below" | Below | Below | PASS |  |  |
| URA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.0% over 30 td | -5.0% over 30 td | PASS |  |  |
| URA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.8% below $62.28 | 51.8% below $62.28 | PASS |  | closing high would be 61.81 |
| URA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.8% below | PASS |  |  |
| URA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.28 | $62.279998779296875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.31%, close location 0.40, OBV falling |
| URA | V2 | day change of the last completed bar | down 1.3% | -1.31% | PASS |  |  |
| URA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.43× / 0.27× | 1.43× / 0.28× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| URA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 5692292) | 20 bars, last ('2026-11-17', 5692292) | PASS |  |  |
| URAA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.45 | $11.45 | PASS |  |  |
| URAA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $14.17 | $14.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URAA | E3 | percent from the 21-day average | 19.2% below | 19.2% below | PASS |  |  |
| URAA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| URAA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.18 | $1.18 (sr=1.1833) | PASS |  | Wilder ATR14 |
| URAA | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| URAA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.9 | +12.9 | PASS |  |  |
| URAA | L-ema21 | ladder row ema21: price and gap = price vs average | $14.17, -19.2% | $14.17, -19.2% | PASS |  |  |
| URAA | L-note | "Last close $X · date" note = last completed bar | Last close $11.38 · Nov 17 | $11.38 · Nov 17 | PASS |  |  |
| URAA | L-now | ladder price row = compared price; name = the basis label | $11.45 "After hours" | $11.45 "after hours" | PASS |  |  |
| URAA | L-sma200 | ladder row sma200: price and gap = price vs average | $29.43, -61.1% | $29.43, -61.1% | PASS |  |  |
| URAA | L-sma50 | ladder row sma50: price and gap = price vs average | $17.6, -34.9% | $17.60, -34.9% | PASS |  |  |
| URAA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $11.45 / entry $11.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URAA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URAA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.0 | 33.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URAA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -62.5% vs +11.2% | -62.5% vs 11.2% | PASS |  |  |
| URAA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URAA | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.0 | 31.1 | PASS |  | Wilder, completed bars |
| URAA | T4w | words "20 or more / below 20" | 20 or more | ADX 31.1 | PASS |  |  |
| URAA | T5 | "counted at the last close ($X, date)" = last completed bar | $11.38, Nov 17 | $11.38, Nov 17 | PASS |  |  |
| URAA | T6 | price vs 200-day average (S1 pattern sma values) | $11.38 vs $29.43 · -61.3% | $11.38 vs $29.43 · -61.3% | PASS |  |  |
| URAA | T6w | word "Below" | Below | Below | PASS |  |  |
| URAA | T7 | price vs 50-day average (S1 pattern sma values) | $11.38 vs $17.60 · -35.3% | $11.38 vs $17.60 · -35.3% | PASS |  |  |
| URAA | T7w | word "Below" | Below | Below | PASS |  |  |
| URAA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -12.2% over 30 td | -12.2% over 30 td | PASS |  |  |
| URAA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URAA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URAA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 81.7% below $62.21 | 81.7% below $62.21 | PASS |  | closing high would be 61.16 |
| URAA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 81.7% below | PASS |  |  |
| URAA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.21 | $62.213869425407246 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URAA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.82%, close location 0.39, OBV falling |
| URAA | V2 | day change of the last completed bar | down 2.8% | -2.82% | PASS |  |  |
| URAA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URAA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.01× / 0.27× | 1.01× / 0.27× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| URAA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 71842) | 20 bars, last ('2026-11-17', 71842) | PASS |  |  |
| V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $416.77 | $416.77 | PASS |  |  |
| V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $414.55 | $414.55 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| V | E3 | percent from the 21-day average | 0.5% above | 0.5% above | PASS |  |  |
| V | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.82 | $8.82 (sr=8.8165) | PASS |  | Wilder ATR14 |
| V | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -7.7 | -7.7 | PASS |  |  |
| V | L-ema21 | ladder row ema21: price and gap = price vs average | $414.55, 0.5% | $414.55, 0.5% | PASS |  |  |
| V | L-note | "Last close $X · date" note = last completed bar | Last close $416.77 · Nov 17 | $416.77 · Nov 17 | PASS |  |  |
| V | L-now | ladder price row = compared price; name = the basis label | $416.77 "After hours" | $416.77 "after hours" | PASS |  |  |
| V | L-sma200 | ladder row sma200: price and gap = price vs average | $346.75, 20.2% | $346.75, 20.2% | PASS |  |  |
| V | L-sma50 | ladder row sma50: price and gap = price vs average | $391.72, 6.4% | $391.72, 6.4% | PASS |  |  |
| V | S5-price | S5: the same live price reads the same on the header and the Entry block | header $416.77 / entry $416.77 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.8 | 54.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.9% vs +11.2% | 28.9% vs 11.2% | PASS |  |  |
| V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| V | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.8 | 37.8 | PASS |  | Wilder, completed bars |
| V | T4w | words "20 or more / below 20" | 20 or more | ADX 37.8 | PASS |  |  |
| V | T5 | "counted at the last close ($X, date)" = last completed bar | $416.77, Nov 17 | $416.77, Nov 17 | PASS |  |  |
| V | T6 | price vs 200-day average (S1 pattern sma values) | $416.77 vs $346.75 · +20.2% | $416.77 vs $346.75 · 20.2% | PASS |  |  |
| V | T6w | word "Above" | Above | Above | PASS |  |  |
| V | T7 | price vs 50-day average (S1 pattern sma values) | $416.77 vs $391.72 · +6.4% | $416.77 vs $391.72 · 6.4% | PASS |  |  |
| V | T7w | word "Above" | Above | Above | PASS |  |  |
| V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| V | T8r | word "rising" | still rising | rising | PASS |  |  |
| V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.6% below $441.41 | 5.6% below $441.41 | PASS |  | closing high would be 435.76 |
| V | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.6% below | PASS |  |  |
| V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $441.41 | $441.4129311637065 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.27%, close location 0.04, OBV rising |
| V | V2 | day change of the last completed bar | down 2.3% | -2.27% | PASS |  |  |
| V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0410) | PASS |  |  |
| V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.87× / 1.07× | 0.87× / 1.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 5689456) | 20 bars, last ('2026-11-17', 5689456) | PASS |  |  |
| VFV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $186.14 | $186.14 | PASS |  |  |
| VFV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $189.81 | $189.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VFV.TO | E3 | percent from the 21-day average | 1.9% below | 1.9% below | PASS |  |  |
| VFV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| VFV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.88 | $2.88 (sr=2.8808) | PASS |  | Wilder ATR14 |
| VFV.TO | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| VFV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $189.81, -1.9% | $189.81, -1.9% | PASS |  |  |
| VFV.TO | L-now | ladder price row = compared price; name = the basis label | $186.14 "Last close" | $186.14 "last close" | PASS |  |  |
| VFV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $180.69, 3.0% | $180.69, 3.0% | PASS |  |  |
| VFV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $191.24, -2.7% | $191.24, -2.7% | PASS |  |  |
| VFV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VFV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.8 | 41.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VFV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +12.8% vs +11.2% | 12.8% vs 11.2% | PASS |  |  |
| VFV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VFV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.3 | 19.3 | PASS |  | Wilder, completed bars |
| VFV.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.3 | PASS |  |  |
| VFV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $186.14 vs $180.69 · +3.0% | $186.14 vs $180.69 · 3.0% | PASS |  |  |
| VFV.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| VFV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $186.14 vs $191.24 · -2.7% | $186.14 vs $191.24 · -2.7% | PASS |  |  |
| VFV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| VFV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.0% over 30 td | +2.0% over 30 td | PASS |  |  |
| VFV.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| VFV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VFV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.9% below $197.83 | 5.9% below $197.83 | PASS |  | closing high would be 197.56 |
| VFV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.9% below | PASS |  |  |
| VFV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $197.83 | $197.8300018310547 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VFV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.08%, close location 0.39, OBV falling |
| VFV.TO | V2 | day change of the last completed bar | down 1.1% | -1.08% | PASS |  |  |
| VFV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| VFV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.63× / 0.70× | 1.63× / 0.70× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VFV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 516387) | 20 bars, last ('2026-11-17', 516387) | PASS |  |  |
| VFV.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.63, OBV falling | condition true | PASS |  |  |
| VRT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $197.00 | $197.00 | PASS |  |  |
| VRT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $207.91 | $207.91 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VRT | E3 | percent from the 21-day average | 5.2% below | 5.2% below | PASS |  |  |
| VRT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| VRT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.86 | $16.86 (sr=16.8606) | PASS |  | Wilder ATR14 |
| VRT | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| VRT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| VRT | L-ema21 | ladder row ema21: price and gap = price vs average | $207.91, -5.2% | $207.91, -5.2% | PASS |  |  |
| VRT | L-note | "Last close $X · date" note = last completed bar | Last close $190.37 · Nov 17 | $190.37 · Nov 17 | PASS |  |  |
| VRT | L-now | ladder price row = compared price; name = the basis label | $197 "After hours" | $197.00 "after hours" | PASS |  |  |
| VRT | L-sma200 | ladder row sma200: price and gap = price vs average | $271.5, -27.4% | $271.50, -27.4% | PASS |  |  |
| VRT | L-sma50 | ladder row sma50: price and gap = price vs average | $227.46, -13.4% | $227.46, -13.4% | PASS |  |  |
| VRT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $197.00 / entry $197.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| VRT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VRT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.7 | 41.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VRT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.4% vs +11.2% | 14.4% vs 11.2% | PASS |  |  |
| VRT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VRT | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.8 | 21.8 | PASS |  | Wilder, completed bars |
| VRT | T4w | words "20 or more / below 20" | 20 or more | ADX 21.8 | PASS |  |  |
| VRT | T5 | "counted at the last close ($X, date)" = last completed bar | $190.37, Nov 17 | $190.37, Nov 17 | PASS |  |  |
| VRT | T6 | price vs 200-day average (S1 pattern sma values) | $190.37 vs $271.50 · -29.9% | $190.37 vs $271.50 · -29.9% | PASS |  |  |
| VRT | T6w | word "Below" | Below | Below | PASS |  |  |
| VRT | T7 | price vs 50-day average (S1 pattern sma values) | $190.37 vs $227.46 · -16.3% | $190.37 vs $227.46 · -16.3% | PASS |  |  |
| VRT | T7w | word "Below" | Below | Below | PASS |  |  |
| VRT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| VRT | T8r | word "rising" | still rising | rising | PASS |  |  |
| VRT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VRT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.9% below $379.76 | 49.9% below $379.76 | PASS |  | closing high would be 376.06 |
| VRT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.9% below | PASS |  |  |
| VRT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $379.76 | $379.76284762424655 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VRT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 1 up, 0 down, 2 flat | PASS |  | change 0.90%, close location 0.47, OBV flat |
| VRT | V2 | day change of the last completed bar | up 0.9% | +0.90% | PASS |  |  |
| VRT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| VRT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.84× / 0.10× | 0.84× / 0.10× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VRT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 5737907) | 20 bars, last ('2026-11-17', 5737907) | PASS |  |  |
| WDC.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.13 | $17.13 | PASS |  |  |
| WDC.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $19.72 | $19.72 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WDC.TO | E3 | percent from the 21-day average | 13.1% below | 13.1% below | PASS |  |  |
| WDC.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| WDC.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.52 | $1.52 (sr=1.518) | PASS |  | Wilder ATR14 |
| WDC.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| WDC.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $19.72, -13.1% | $19.72, -13.1% | PASS |  |  |
| WDC.TO | L-now | ladder price row = compared price; name = the basis label | $17.13 "Last close" | $17.13 "last close" | PASS |  |  |
| WDC.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $23.44, -26.9% | $23.44, -26.9% | PASS |  |  |
| WDC.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.4 | 36.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WDC.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.0 | 33.9 | PASS |  | Wilder, completed bars |
| WDC.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 33.9 | PASS |  |  |
| WDC.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.71%, close location 0.69, OBV falling |
| WDC.TO | V2 | day change of the last completed bar | up 0.7% | +0.71% | PASS |  |  |
| WDC.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| WDC.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.80× / 0.08× | 0.80× / 0.08× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WDC.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 129143) | 20 bars, last ('2026-11-17', 129143) | PASS |  |  |
| WELL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $245.76 | $245.76 | PASS |  |  |
| WELL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $240.8 | $240.80 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WELL | E3 | percent from the 21-day average | 2.1% above | 2.1% above | PASS |  |  |
| WELL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| WELL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.25 | $5.25 (sr=5.2528) | PASS |  | Wilder ATR14 |
| WELL | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves above |
| WELL | L-ema21 | ladder row ema21: price and gap = price vs average | $240.8, 2.1% | $240.80, 2.1% | PASS |  |  |
| WELL | L-note | "Last close $X · date" note = last completed bar | Last close $245.76 · Nov 17 | $245.76 · Nov 17 | PASS |  |  |
| WELL | L-now | ladder price row = compared price; name = the basis label | $245.76 "After hours" | $245.76 "after hours" | PASS |  |  |
| WELL | L-sma200 | ladder row sma200: price and gap = price vs average | $220.47, 11.5% | $220.47, 11.5% | PASS |  |  |
| WELL | L-sma50 | ladder row sma50: price and gap = price vs average | $234.17, 4.9% | $234.17, 4.9% | PASS |  |  |
| WELL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $245.76 / entry $245.76 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WELL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WELL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 60.6 | 60.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WELL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +26.4% vs +11.2% | 26.4% vs 11.2% | PASS |  |  |
| WELL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WELL | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.4 | 14.4 | PASS |  | Wilder, completed bars |
| WELL | T4w | words "20 or more / below 20" | below 20 | ADX 14.4 | PASS |  |  |
| WELL | T5 | "counted at the last close ($X, date)" = last completed bar | $245.76, Nov 17 | $245.76, Nov 17 | PASS |  |  |
| WELL | T6 | price vs 200-day average (S1 pattern sma values) | $245.76 vs $220.47 · +11.5% | $245.76 vs $220.47 · 11.5% | PASS |  |  |
| WELL | T6w | word "Above" | Above | Above | PASS |  |  |
| WELL | T7 | price vs 50-day average (S1 pattern sma values) | $245.76 vs $234.17 · +4.9% | $245.76 vs $234.17 · 4.9% | PASS |  |  |
| WELL | T7w | word "Above" | Above | Above | PASS |  |  |
| WELL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.7% over 30 td | +3.7% over 30 td | PASS |  |  |
| WELL | T8r | word "rising" | still rising | rising | PASS |  |  |
| WELL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WELL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.0% below $253.37 | 3.0% below $253.37 | PASS |  | closing high would be 250.26 |
| WELL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.0% below | PASS |  |  |
| WELL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $253.37 | $253.36654979575871 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WELL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 0.45%, close location 0.95, OBV rising |
| WELL | V2 | day change of the last completed bar | up 0.5% | +0.45% | PASS |  |  |
| WELL | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.95 (raw 0.9508) | PASS |  |  |
| WELL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WELL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.16× / 0.21× | 1.16× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WELL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3253031) | 20 bars, last ('2026-11-17', 3253031) | PASS |  |  |
| WMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $126.55 | $126.55 | PASS |  |  |
| WMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $123.62 | $123.62 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WMT | E3 | percent from the 21-day average | 2.4% above | 2.4% above | PASS |  |  |
| WMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| WMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.67 | $2.67 (sr=2.6692) | PASS |  | Wilder ATR14 |
| WMT | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves above |
| WMT | L-ema21 | ladder row ema21: price and gap = price vs average | $123.62, 2.4% | $123.62, 2.4% | PASS |  |  |
| WMT | L-note | "Last close $X · date" note = last completed bar | Last close $127.52 · Nov 17 | $127.52 · Nov 17 | PASS |  |  |
| WMT | L-now | ladder price row = compared price; name = the basis label | $126.55 "After hours" | $126.55 "after hours" | PASS |  |  |
| WMT | L-sma200 | ladder row sma200: price and gap = price vs average | $118.68, 6.6% | $118.68, 6.6% | PASS |  |  |
| WMT | L-sma50 | ladder row sma50: price and gap = price vs average | $115.39, 9.7% | $115.39, 9.7% | PASS |  |  |
| WMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $126.55 / entry $126.55 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 65.2 | 65.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +24.9% vs +11.2% | 24.9% vs 11.2% | PASS |  |  |
| WMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 46.9 | 46.9 | PASS |  | Wilder, completed bars |
| WMT | T4w | words "20 or more / below 20" | 20 or more | ADX 46.9 | PASS |  |  |
| WMT | T5 | "counted at the last close ($X, date)" = last completed bar | $127.52, Nov 17 | $127.52, Nov 17 | PASS |  |  |
| WMT | T6 | price vs 200-day average (S1 pattern sma values) | $127.52 vs $118.68 · +7.4% | $127.52 vs $118.68 · 7.5% | PASS |  |  |
| WMT | T6w | word "Above" | Above | Above | PASS |  |  |
| WMT | T7 | price vs 50-day average (S1 pattern sma values) | $127.52 vs $115.39 · +10.5% | $127.52 vs $115.39 · 10.5% | PASS |  |  |
| WMT | T7w | word "Above" | Above | Above | PASS |  |  |
| WMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.7% over 30 td | +0.7% over 30 td | PASS |  |  |
| WMT | T8r | word "rising" | still rising | rising | PASS |  |  |
| WMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.4% below $134.84 | 5.4% below $134.84 | PASS |  | closing high would be 133.88 |
| WMT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.4% below | PASS |  |  |
| WMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $134.84 | $134.83720000658067 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.69%, close location 0.19, OBV rising |
| WMT | V2 | day change of the last completed bar | down 0.7% | -0.69% | PASS |  |  |
| WMT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.19 (raw 0.1892) | PASS |  |  |
| WMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.90× / 0.33× | 0.90× / 0.33× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 19483025) | 20 bars, last ('2026-11-17', 19483025) | PASS |  |  |
| XCHP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $105.40 | $105.40 | PASS |  |  |
| XCHP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.95 | $113.95 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XCHP.TO | E3 | percent from the 21-day average | 7.5% below | 7.5% below | PASS |  |  |
| XCHP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XCHP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.28 | $6.28 (sr=6.2838) | PASS |  | Wilder ATR14 |
| XCHP.TO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| XCHP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.95, -7.5% | $113.95, -7.5% | PASS |  |  |
| XCHP.TO | L-now | ladder price row = compared price; name = the basis label | $105.4 "Last close" | $105.40 "last close" | PASS |  |  |
| XCHP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $116.58, -9.6% | $116.58, -9.6% | PASS |  |  |
| XCHP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $125.17, -15.8% | $125.17, -15.8% | PASS |  |  |
| XCHP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XCHP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.5 | 39.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XCHP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +53.7% vs +11.2% | 53.7% vs 11.2% | PASS |  |  |
| XCHP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XCHP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.7 | 32.7 | PASS |  | Wilder, completed bars |
| XCHP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.7 | PASS |  |  |
| XCHP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $105.40 vs $116.58 · -9.6% | $105.40 vs $116.58 · -9.6% | PASS |  |  |
| XCHP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $105.40 vs $125.17 · -15.8% | $105.40 vs $125.17 · -15.8% | PASS |  |  |
| XCHP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.7% over 30 td | +5.6% over 30 td | PASS |  |  |
| XCHP.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XCHP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XCHP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.6% below $161.26 | 34.6% below $161.26 | PASS |  | closing high would be 160.97 |
| XCHP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.6% below | PASS |  |  |
| XCHP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $161.26 | $161.25523669513825 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XCHP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.07%, close location 0.77, OBV falling |
| XCHP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.77 (raw 0.7673) | PASS |  |  |
| XCHP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XCHP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.91× / 0.01× | 1.91× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XCHP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 97799) | 20 bars, last ('2026-11-17', 97799) | PASS |  |  |
| XCHP.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.91, OBV falling | condition true | PASS |  |  |
| XDRV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.25 | $39.25 | PASS |  |  |
| XDRV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $41.33 | $41.33 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XDRV.TO | E3 | percent from the 21-day average | 5.0% below | 5.0% below | PASS |  |  |
| XDRV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XDRV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.83 | $0.83 (sr=0.8322) | PASS |  | Wilder ATR14 |
| XDRV.TO | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| XDRV.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.6 | +7.6 | PASS |  |  |
| XDRV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $41.33, -5.0% | $41.33, -5.0% | PASS |  |  |
| XDRV.TO | L-now | ladder price row = compared price; name = the basis label | $39.25 "Last close" | $39.25 "last close" | PASS |  |  |
| XDRV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $47.63, -17.6% | $47.63, -17.6% | PASS |  |  |
| XDRV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.53, -9.8% | $43.53, -9.8% | PASS |  |  |
| XDRV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XDRV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.4 | 38.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XDRV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.8% vs +11.2% | -5.9% vs 11.2% | PASS |  |  |
| XDRV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XDRV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.5 | 22.5 | PASS |  | Wilder, completed bars |
| XDRV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.5 | PASS |  |  |
| XDRV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $39.25 vs $47.63 · -17.6% | $39.25 vs $47.63 · -17.6% | PASS |  |  |
| XDRV.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $39.25 vs $43.53 · -9.8% | $39.25 vs $43.53 · -9.8% | PASS |  |  |
| XDRV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.6% over 30 td | -0.6% over 30 td | PASS |  |  |
| XDRV.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XDRV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XDRV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.0% below $61.36 | 36.0% below $61.36 | PASS |  | closing high would be 61.36 |
| XDRV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.0% below | PASS |  |  |
| XDRV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $61.36 | $61.35662078857422 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XDRV.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 43 of 50 days empty | 43 of 50 days empty | PASS |  |  |
| XEQT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $44.34 | $44.34 | PASS |  |  |
| XEQT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $45.14 | $45.14 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XEQT.TO | E3 | percent from the 21-day average | 1.8% below | 1.8% below | PASS |  |  |
| XEQT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XEQT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.58 | $0.58 (sr=0.5768) | PASS |  | Wilder ATR14 |
| XEQT.TO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| XEQT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $45.14, -1.8% | $45.14, -1.8% | PASS |  |  |
| XEQT.TO | L-now | ladder price row = compared price; name = the basis label | $44.34 "Last close" | $44.34 "last close" | PASS |  |  |
| XEQT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $43.57, 1.8% | $43.57, 1.8% | PASS |  |  |
| XEQT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $45.38, -2.3% | $45.38, -2.3% | PASS |  |  |
| XEQT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XEQT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.8 | 41.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XEQT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.9% vs +11.2% | 14.9% vs 11.2% | PASS |  |  |
| XEQT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XEQT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.4 | 15.5 | PASS |  | Wilder, completed bars |
| XEQT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.5 | PASS |  |  |
| XEQT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $44.34 vs $43.57 · +1.8% | $44.34 vs $43.57 · 1.8% | PASS |  |  |
| XEQT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| XEQT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $44.34 vs $45.38 · -2.3% | $44.34 vs $45.38 · -2.3% | PASS |  |  |
| XEQT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XEQT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| XEQT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XEQT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XEQT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.4% below $46.38 | 4.4% below $46.38 | PASS |  | closing high would be 46.27 |
| XEQT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.4% below | PASS |  |  |
| XEQT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.38 | $46.380001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XEQT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.16%, close location 0.30, OBV falling |
| XEQT.TO | V2 | day change of the last completed bar | down 1.2% | -1.16% | PASS |  |  |
| XEQT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XEQT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.46× / 0.89× | 1.46× / 0.89× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XEQT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 1321335) | 20 bars, last ('2026-11-17', 1321335) | PASS |  |  |
| XETM.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $61.17 | $61.17 | PASS |  |  |
| XETM.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $68.35 | $68.35 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XETM.TO | E3 | percent from the 21-day average | 10.5% below | 10.5% below | PASS |  |  |
| XETM.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XETM.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.45 | $2.45 (sr=2.4539) | PASS |  | Wilder ATR14 |
| XETM.TO | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| XETM.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.7 | +4.7 | PASS |  |  |
| XETM.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $68.35, -10.5% | $68.35, -10.5% | PASS |  |  |
| XETM.TO | L-now | ladder price row = compared price; name = the basis label | $61.17 "Last close" | $61.17 "last close" | PASS |  |  |
| XETM.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $79.87, -23.4% | $79.87, -23.4% | PASS |  |  |
| XETM.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $75.21, -18.7% | $75.21, -18.7% | PASS |  |  |
| XETM.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.7 | 32.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XETM.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -27.4% vs +11.2% | -27.4% vs 11.2% | PASS |  |  |
| XETM.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.8 | 21.8 | PASS |  | Wilder, completed bars |
| XETM.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 21.8 | PASS |  |  |
| XETM.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.65%, close location 0.17, OBV falling |
| XETM.TO | V2 | day change of the last completed bar | down 0.7% | -0.65% | PASS |  |  |
| XETM.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1686) | PASS |  |  |
| XETM.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XETM.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.19× / 0.16× | 1.19× / 0.16× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XETM.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3667) | 20 bars, last ('2026-11-17', 3667) | PASS |  |  |
| XGD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $51.28 | $51.28 | PASS |  |  |
| XGD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $53.11 | $53.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XGD.TO | E3 | percent from the 21-day average | 3.4% below | 3.4% below | PASS |  |  |
| XGD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XGD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.04 | $2.04 (sr=2.0372) | PASS |  | Wilder ATR14 |
| XGD.TO | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves below |
| XGD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $53.11, -3.4% | $53.11, -3.4% | PASS |  |  |
| XGD.TO | L-now | ladder price row = compared price; name = the basis label | $51.28 "Last close" | $51.28 "last close" | PASS |  |  |
| XGD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $55.14, -7.0% | $55.14, -7.0% | PASS |  |  |
| XGD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $55.23, -7.2% | $55.23, -7.2% | PASS |  |  |
| XGD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XGD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.2 | 44.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XGD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +12.8% vs +11.2% | 12.8% vs 11.2% | PASS |  |  |
| XGD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XGD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.1 | 17.1 | PASS |  | Wilder, completed bars |
| XGD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 17.1 | PASS |  |  |
| XGD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $51.28 vs $55.14 · -7.0% | $51.28 vs $55.14 · -7.0% | PASS |  |  |
| XGD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $51.28 vs $55.23 · -7.2% | $51.28 vs $55.23 · -7.2% | PASS |  |  |
| XGD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.0% over 30 td | -1.0% over 30 td | PASS |  |  |
| XGD.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XGD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XGD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.3% below $69.54 | 26.3% below $69.54 | PASS |  | closing high would be 68.70 |
| XGD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.3% below | PASS |  |  |
| XGD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $69.54 | $69.54086233267267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XGD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 1 up, 0 down, 2 flat | PASS |  | change 0.94%, close location 0.29, OBV flat |
| XGD.TO | V2 | day change of the last completed bar | up 0.9% | +0.94% | PASS |  |  |
| XGD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| XGD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.77× / 0.24× | 0.77× / 0.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XGD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 356938) | 20 bars, last ('2026-11-17', 356938) | PASS |  |  |
| XOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $167.21 | $167.21 | PASS |  |  |
| XOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $170.11 | $170.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XOM | E3 | percent from the 21-day average | 1.7% below | 1.7% below | PASS |  |  |
| XOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| XOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.18 | $4.18 (sr=4.1759) | PASS |  | Wilder ATR14 |
| XOM | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| XOM | L-ema21 | ladder row ema21: price and gap = price vs average | $170.11, -1.7% | $170.11, -1.7% | PASS |  |  |
| XOM | L-note | "Last close $X · date" note = last completed bar | Last close $167.21 · Nov 17 | $167.21 · Nov 17 | PASS |  |  |
| XOM | L-now | ladder price row = compared price; name = the basis label | $167.21 "After hours" | $167.21 "after hours" | PASS |  |  |
| XOM | L-sma200 | ladder row sma200: price and gap = price vs average | $154.62, 8.1% | $154.62, 8.1% | PASS |  |  |
| XOM | L-sma50 | ladder row sma50: price and gap = price vs average | $168.64, -0.8% | $168.63, -0.8% | PASS |  |  |
| XOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $167.21 / entry $167.21 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| XOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.0 | 45.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +45.9% vs +11.2% | 45.9% vs 11.2% | PASS |  |  |
| XOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.5 | 26.4 | PASS |  | Wilder, completed bars |
| XOM | T4w | words "20 or more / below 20" | 20 or more | ADX 26.4 | PASS |  |  |
| XOM | T5 | "counted at the last close ($X, date)" = last completed bar | $167.21, Nov 17 | $167.21, Nov 17 | PASS |  |  |
| XOM | T6 | price vs 200-day average (S1 pattern sma values) | $167.21 vs $154.62 · +8.1% | $167.21 vs $154.62 · 8.1% | PASS |  |  |
| XOM | T6w | word "Above" | Above | Above | PASS |  |  |
| XOM | T7 | price vs 50-day average (S1 pattern sma values) | $167.21 vs $168.64 · -0.8% | $167.21 vs $168.63 · -0.8% | PASS |  |  |
| XOM | T7w | word "Below" | Below | Below | PASS |  |  |
| XOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +5.0% over 30 td | PASS |  |  |
| XOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| XOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.7% below $187.32 | 10.7% below $187.32 | PASS |  | closing high would be 186.08 |
| XOM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.7% below | PASS |  |  |
| XOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $187.32 | $187.31766003760222 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 1 up, 0 down, 2 flat | PASS |  | change 0.20%, close location 0.30, OBV flat |
| XOM | V2 | day change of the last completed bar | up 0.2% | +0.20% | PASS |  |  |
| XOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| XOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.77× / 0.08× | 0.77× / 0.08× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 10403336) | 20 bars, last ('2026-11-17', 10403336) | PASS |  |  |
