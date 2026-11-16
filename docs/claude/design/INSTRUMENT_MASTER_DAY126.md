# Instrument master: what is what (Day 126)

Built by `backend/backtest/identify_instruments.py` from the user's IBKR watchlist pastes (Nov 13–14) and Yahoo. Each row is matched by **price**: the pasted IBKR last price vs the last close of every candidate Yahoo listing (US, Toronto `.TO`, Cboe Canada `.NE`, TSX Venture `.V`), tolerance ±12%. The listing whose price agrees is the instrument; exchange, currency and quote type are Yahoo's for that listing; class comes from Yahoo's quote type, the IBKR description and the list it sits on.

**How to read:** `STA symbol` is what to type in STA. `Diff` is the pasted price vs Yahoo's last close. `AMBIGUOUS` / `UNMATCHED` rows need a human look.

## Counts

| Market | Stock | ETF | Leveraged ETF | CDR |
|---|---|---|---|---|
| US | 21 | 13 | 7 | 0 |
| Canada | 13 | 15 | 2 | 8 |
| ? | 0 | 0 | 1 | 0 |

**80 distinct instruments, 79 matched cleanly, 1 need a look.**


## Stock (34)

| IBKR | Description | List(s) | Paste | STA symbol | Also trades as | Market · exchange | Cur | Yahoo close | Diff | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| ASTL | ALGOMA STEEL GROUP INC | Canadian list (8) | 7.79 | `ASTL.TO` | `ASTL.NE` | Canada · TOR | CAD | 7.79 | -0.0% | MATCHED |
| ATD | ALIMENTATION COUCHE-TARD INC | Quality_US_Canada | 82.85 | `ATD.TO` | `ATD.NE` | Canada · TOR | CAD | 82.85 | -0.0% | MATCHED |
| BDT | BIRD CONSTRUCTION INC | Canadian list (8) | 76.69 | `BDT.TO` | `BDT.NE` | Canada · TOR | CAD | 76.69 | +0.0% | MATCHED |
| CCO | CAMECO CORP | AI Supply Chain | 100.8 | `CCO.TO` | `CCO.NE` | Canada · TOR | CAD | 100.8 | +0.0% | MATCHED |
| CGY | CALIAN GROUP LTD | Canadian list (8) | 85.55 | `CGY.TO` | `CGY.NE` | Canada · TOR | CAD | 85.55 | +0.0% | MATCHED |
| CNQ | CANADIAN NATURAL RESOURCES | Quality_US_Canada | 70.91 | `CNQ.TO` | `CNQ.NE` | Canada · TOR | CAD | 70.91 | +0.0% | MATCHED |
| CNR | CANADIAN NATL RAILWAY CO | Quality_US_Canada | 181.29 | `CNR.TO` | `CNR.NE` | Canada · TOR | CAD | 181.29 | -0.0% | MATCHED |
| CSU | CONSTELLATION SOFTWARE INC | Quality_US_Canada | 3492.29 | `CSU.TO` | `CSU.NE` | Canada · TOR | CAD | 3492.29 | +0.0% | MATCHED |
| GIB.A | CGI INC | AI Supply Chain | 116.83 | `GIB-A.TO` | `GIB-A.NE` | Canada · TOR | CAD | 116.83 | +0.0% | MATCHED |
| MDA | MDA SPACE LTD | Canadian list (8) | 41.25 | `MDA.TO` | `MDA.NE` | Canada · TOR | CAD | 41.25 | +0.0% | MATCHED |
| NTR | NUTRIEN LTD | Canadian list (8) | 101.62 | `NTR.TO` | `NTR.NE` | Canada · TOR | CAD | 101.62 | +0.0% | MATCHED |
| PNG | KRAKEN ROBOTICS INC | Canadian list (8) | 3.4 | `PNG.V` | `PNG.NE` | Canada · VAN | CAD | 3.4 | +0.0% | MATCHED |
| RY | ROYAL BANK OF CANADA | Quality_US_Canada | 288.37 | `RY.TO` | `RY.NE` | Canada · TOR | CAD | 288.37 | -0.0% | MATCHED |
| ALAB | ASTERA LABS INC | AI Supply Chain | 216.35 | `ALAB` | — | US · NMS | USD | 221.83 | +2.5% | MATCHED |
| AMD | ADVANCED MICRO DEVICES | AI Supply Chain | 521.2 | `AMD` | — | US · NMS | USD | 534.06 | +2.5% | MATCHED |
| AVGO | BROADCOM INC | AI Supply Chain | 340.12 | `AVGO` | — | US · NMS | USD | 347.01 | +2.0% | MATCHED |
| BRK B | BERKSHIRE HATHAWAY INC-CL B | Quality_US_Canada | 592.3 | `BRK-B` | — | US · NYQ | USD | 592.94 | +0.1% | MATCHED |
| CAMT | CAMTEK LIMITED | AI Supply Chain | 101.5 | `CAMT` | — | US · NGM | USD | 101.73 | +0.2% | MATCHED |
| CAT | CATERPILLAR INC | Quality_US_Canada | 596.12 | `CAT` | — | US · NYQ | USD | 600.2 | +0.7% | MATCHED |
| CEG | CONSTELLATION ENERGY | AI Supply Chain | 278.2 | `CEG` | — | US · NMS | USD | 280.2 | +0.7% | MATCHED |
| ETN | EATON CORP PLC | AI Supply Chain | 350.0 | `ETN` | — | US · NYQ | USD | 352.97 | +0.8% | MATCHED |
| FCX | FREEPORT-MCMORAN INC | AI Supply Chain | 59.27 | `FCX` | — | US · NYQ | USD | 59.24 | -0.1% | MATCHED |
| GEV | GE VERNOVA INC | AI Supply Chain | 790.01 | `GEV` | — | US · NYQ | USD | 803.13 | +1.7% | MATCHED |
| GOOGL | ALPHABET INC-CL A | Quality_US_Canada | 294.05 | `GOOGL` | — | US · NMS | USD | 295.77 | +0.6% | MATCHED |
| JNJ | JOHNSON & JOHNSON | Quality_US_Canada | 286.67 | `JNJ` | — | US · NYQ | USD | 285.75 | -0.3% | MATCHED |
| JPM | JPMORGAN CHASE & CO | Quality_US_Canada | 344.79 | `JPM` | — | US · NYQ | USD | 346.19 | +0.4% | MATCHED |
| KEYS | KEYSIGHT TECHNOLOGIES IN | AI Supply Chain | 291.19 | `KEYS` | — | US · NYQ | USD | 297.68 | +2.2% | MATCHED |
| MRVL | MARVELL TECHNOLOGY INC | AI Supply Chain | 152.59 | `MRVL` | — | US · NMS | USD | 156.76 | +2.7% | MATCHED |
| NVDA | NVIDIA CORP | AI Supply Chain | 161.01 | `NVDA` | — | US · NMS | USD | 162.85 | +1.1% | MATCHED |
| ONTO | ONTO INNOVATION INC | AI Supply Chain | 197.03 | `ONTO` | — | US · NYQ | USD | 203.62 | +3.3% | MATCHED |
| ORCL | ORACLE CORP | AI Supply Chain | 123.35 | `ORCL` | — | US · NYQ | USD | 125.35 | +1.6% | MATCHED |
| QCOM | QUALCOMM INC | AI Supply Chain | 170.9 | `QCOM` | — | US · NMS | USD | 172.47 | +0.9% | MATCHED |
| TSM | TAIWAN SEMICONDUCTOR-SP ADR | AI Supply Chain | 394.5 | `TSM` | — | US · NYQ | USD | 398.73 | +1.1% | MATCHED |
| VRT | VERTIV HOLDINGS CO-A | AI Supply Chain | 197.44 | `VRT` | — | US · NYQ | USD | 202.07 | +2.3% | MATCHED |

## ETF (28)

| IBKR | Description | List(s) | Paste | STA symbol | Also trades as | Market · exchange | Cur | Yahoo close | Diff | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| CARS | EVOLVE AUTOMOBILE INNOVATION | AI Supply Chain ETF | 21.04 | `CARS.TO` | `CARS.NE` | Canada · TOR | CAD | 21.04 | +0.0% | MATCHED |
| COPP | GLOBAL X COPPER PRODUCER IND | AI Supply Chain ETF | 49.57 | `COPP.TO` | `COPP.NE` | Canada · TOR | CAD | 49.52 | -0.1% | MATCHED |
| FINN | FIDELITY GL INNOVATORS ETF | Long_Term_Quality_ETFs | 32.71 | `FINN.NE` | — | Canada · NEO | CAD | 32.7 | -0.0% | MATCHED |
| HURA | GLOBAL X URANIUM INDEX ETF | AI Supply Chain ETF | 39.02 | `HURA.TO` | `HURA.NE` | Canada · TOR | CAD | 39.02 | +0.0% | MATCHED |
| HXQ | GLOBAL X NASDAQ-100 INDE-CAD | Long_Term_Quality_ETFs | 114.73 | `HXQ.TO` | `HXQ.NE` | Canada · TOR | CAD | 114.73 | +0.0% | MATCHED |
| MTRX | GLOBAL X AI INFRAS INDX | AI Supply Chain ETF | 30.59 | `MTRX.TO` | `MTRX.NE` | Canada · TOR | CAD | 30.59 | +0.0% | MATCHED |
| ORBX | GLOBAL X SPCE TECH INDEX ETF | AI Supply Chain ETF | 15.32 | `ORBX.TO` | — | Canada · TOR | CAD | 15.32 | -0.0% | MATCHED |
| RBOT | GLB X ROBOTICS &AI INDEX ETF | AI Supply Chain ETF | 28.59 | `RBOT.TO` | `RBOT.NE` | Canada · TOR | CAD | 28.59 | +0.0% | MATCHED |
| SGRD | FRST TRST NSD CLN EDG SG ETF | AI Supply Chain ETF | 18.47 | `SGRD.TO` | `SGRD.NE` | Canada · TOR | CAD | 18.59 | +0.6% | MATCHED |
| VFV | VANGUARD S&P 500 INDEX ETF | Long_Term_Quality_ETFs | 191.4 | `VFV.TO` | `VFV.NE` | Canada · TOR | CAD | 191.4 | -0.0% | MATCHED |
| XCHP | ISHARES SEMICONDUCTOR ETF | Long_Term_Quality_ETFs | 111.07 | `XCHP.TO` | `XCHP.NE` | Canada · TOR | CAD | 111.07 | -0.0% | MATCHED |
| XDRV | ISHARES GL ELECTRIC & AU VEH | AI Supply Chain ETF | 40.87 | `XDRV.TO` | — | Canada · TOR | CAD | 41.46 | +1.4% | MATCHED |
| XEQT | ISHARES CORE EQUITY ETF PORT | Long_Term_Quality_ETFs | 45.52 | `XEQT.TO` | `XEQT.NE` | Canada · TOR | CAD | 45.52 | +0.0% | MATCHED |
| XETM | ISH ENRGY TRANSITION MAT ETF | AI Supply Chain ETF | 65.54 | `XETM.TO` | `XETM.NE` | Canada · TOR | CAD | 65.54 | +0.0% | MATCHED |
| XGD | ISHARES S&P/TSX GLOBAL GOLD | AI Supply Chain ETF | 52.4 | `XGD.TO` | `XGD.NE` | Canada · TOR | CAD | 52.4 | +0.0% | MATCHED |
| AIPO | DEFIANCE AI & POWER INFR ETF | AI Supply Chain ETF | 23.35 | `AIPO` | — | US · NGM | USD | 23.66 | +1.3% | MATCHED |
| BOTZ | GLOBAL X ROBOTICS & ARTIFICI | AI Supply Chain ETF | 31.03 | `BOTZ` | — | US · NGM | USD | 31.23 | +0.6% | MATCHED |
| COPX | GLOBAL X COPPER MINERS ETF | AI Supply Chain ETF | 69.26 | `COPX` | — | US · PCX | USD | 69.23 | -0.0% | MATCHED |
| DRAM | ROUNDHILL MEMORY ETF | AI Supply Chain ETF | 41.66 | `DRAM` | — | US · BTS | USD | 42.4 | +1.8% | MATCHED |
| DRIV | GLOBAL X AUTONOMOUS&ELEC-ETF | AI Supply Chain ETF | 28.4 | `DRIV` | — | US · NGM | USD | 28.45 | +0.2% | MATCHED |
| GDX | VANECK GOLD MINERS ETF | AI Supply Chain ETF | 81.52 | `GDX` | — | US · PCX | USD | 81.64 | +0.1% | MATCHED |
| GRID | FIRST TRST NASD CL EDG SGIIF | AI Supply Chain ETF | 159.82 | `GRID` | — | US · NGM | USD | 160.29 | +0.3% | MATCHED |
| QTUM | DEFIANCE QUANTUM ETF | AI Supply Chain ETF | 128.74 | `QTUM` | — | US · NGM | USD | 130.1 | +1.1% | MATCHED |
| SETM | SPROTT CRITICAL MATERIAL ETF | AI Supply Chain ETF | 23.7 | `SETM` | — | US · NGM | USD | 23.7 | +0.0% | MATCHED |
| SMH | VANECK SEMICONDUCTOR ETF | AI Supply Chain ETF | 481.53 | `SMH` | — | US · NGM | USD | 486.75 | +1.1% | MATCHED |
| SOXX | ISHARES SEMICONDUCTOR ETF | AI Supply Chain ETF | 146.66 | `SOXX` | — | US · NGM | USD | 149.3 | +1.8% | MATCHED |
| UFO | PROCURE SPACE ETF | AI Supply Chain ETF | 40.0 | `UFO` | — | US · NGM | USD | 40.69 | +1.7% | MATCHED |
| URA | GLOBAL X URANIUM ETF | AI Supply Chain ETF | 31.74 | `URA` | — | US · PCX | USD | 31.84 | +0.3% | MATCHED |

## Leveraged ETF (10)

| IBKR | Description | List(s) | Paste | STA symbol | Also trades as | Market · exchange | Cur | Yahoo close | Diff | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGC | (no description or price in the paste) | AI_Leveraged | — | — | — | ? · — | — | — | — | NO PRICE IN PASTE |
| GDXU | BETAPRO CANADIAN GOLD MINERS | AI_Leveraged | 26.36 | `GDXU.TO` | `GDXU.NE` | Canada · TOR | CAD | 26.05 | -1.2% | MATCHED |
| SOXL | BETAPRO 3X SC DAILY LEV BA | AI Supply Chain ETF, AI_Leveraged | 14.72 | `SOXL.NE` | — | Canada · NEO | CAD | 14.69 | -0.2% | MATCHED |
| COPZ | DEFIANCE DAILY TARGET 2X LON | AI_Leveraged | 9.77 | `COPZ` | — | US · PCX | USD | 9.75 | -0.2% | MATCHED |
| DRAL | DEF DLY TGT 2X LG DRAM ETF | AI_Leveraged | 4.77 | `DRAL` | — | US · BTS | USD | 4.91 | +2.9% | MATCHED |
| QPUX | DFINC 2X D LNG PURE QUNT ETF | AI_Leveraged | 4.23 | `QPUX` | — | US · NGM | USD | 4.28 | +1.2% | MATCHED |
| SOXL | DIREX DAIL SEMI BU 3X ET-USD | AI Supply Chain ETF | 55.68 | `SOXL` | — | US · PCX | USD | 58.32 | +4.7% | MATCHED |
| SPCL | DEFIANC DAILY 2X SPC ETF-USD | AI_Leveraged | 11.93 | `SPCL` | — | US · BTS | USD | 12.15 | +1.8% | MATCHED |
| UBOT | DD RA INT & AUTO IB 2X ETF-U | AI_Leveraged | 16.6 | `UBOT` | — | US · PCX | USD | 16.68 | +0.5% | MATCHED |
| URAA | DIR DA URA IND BU 2X ETF-USD | AI_Leveraged | 12.25 | `URAA` | — | US · PCX | USD | 12.7 | +3.7% | MATCHED |

## CDR (Canadian receipt of a US stock) (8)

| IBKR | Description | List(s) | Paste | STA symbol | Also trades as | Market · exchange | Cur | Yahoo close | Diff | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | ADVANCED MICRO DEVICES CDR | AI Supply Chain | 13.76 | `AMD.TO` | `AMD.NE` | Canada · TOR | CAD | 13.76 | +0.0% | MATCHED |
| ANET | ARISTA NETWORKS INC | AI Supply Chain | 35.25 | `ANET.TO` | `ANET.NE` | Canada · TOR | CAD | 35.25 | +0.0% | MATCHED |
| ASML | ASML HOLDING NV | AI Supply Chain | 44.3 | `ASML.TO` | `ASML.NE` | Canada · TOR | CAD | 44.3 | -0.0% | MATCHED |
| AVGO | BROADCOM INC-CDR | AI Supply Chain | 13.14 | `AVGO.TO` | `AVGO.NE` | Canada · TOR | CAD | 13.14 | +0.0% | MATCHED |
| GEV | GE VERNOVA INC-CDR | AI Supply Chain | 53.67 | `GEV.TO` | `GEV.NE` | Canada · TOR | CAD | 53.67 | -0.0% | MATCHED |
| MU | MICRON TECHNOLOGY INC | AI Supply Chain | 33.99 | `MU.TO` | `MU.NE` | Canada · TOR | CAD | 33.99 | +0.0% | MATCHED |
| SNDK | SANDISK CORP/DE | AI Supply Chain | 21.41 | `SNDK.TO` | `SNDK.NE` | Canada · TOR | CAD | 21.41 | -0.0% | MATCHED |
| WDC | WESTERN DIGITAL CORP | AI Supply Chain | 17.88 | `WDC.TO` | `WDC.NE` | Canada · TOR | CAD | 17.89 | +0.1% | MATCHED |

## Needs a human look

- **AVGC** ((no description or price in the paste)), paste None: NO PRICE IN PASTE. Yahoo candidates: AVGC=18.98
