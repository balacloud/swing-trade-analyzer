# Indicator divergence (Day 126)

Source: `backend/validation_results/indicator_golden_after.json` (saved audit frames, no network).

- ATR: the JS simple-mean copy (no consumer) is median 10.0% / max 17.1% away from the live Wilder ATR.
- ATR: the paper-trading stop ATR (51-bar window) is median 0.63% / max 2.85% away from it.
- RSI: JS (drives the verdict) vs backend RSI differ by at most 0.03 points at the last bar across 24 tickers.

| Ticker | Bars | ATR JS vs live % | ATR paper-51 vs live % | ATR legacy vs live % | RSI JS - backend |
|---|---|---|---|---|---|
| AMD.TO | 503 | +14.12 | +1.03 | +0.000 | +0.00 |
| ATD.TO | 503 | +3.09 | +0.12 | -0.000 | +0.00 |
| AVGO.TO | 225 | +13.07 | +0.63 | +0.000 | -0.01 |
| BRK-B | 501 | +17.09 | +0.80 | +0.000 | +0.00 |
| CAT | 501 | +8.95 | +0.04 | +0.000 | +0.00 |
| CNR.TO | 503 | +12.83 | +0.25 | -0.000 | +0.00 |
| CSU.TO | 503 | -3.67 | -0.02 | +0.000 | +0.00 |
| DRAL | 100 | +4.81 | -0.91 | +0.000 | -0.03 |
| GDX | 501 | +7.49 | -0.16 | -0.000 | +0.00 |
| GDXU.TO | 503 | +4.19 | -0.28 | -0.000 | +0.00 |
| HXQ.TO | 503 | +11.91 | +0.97 | +0.000 | +0.00 |
| JPM | 501 | +9.48 | +0.44 | +0.000 | +0.00 |
| MU.TO | 273 | +8.59 | +0.03 | +0.000 | +0.00 |
| QPUX | 321 | -5.00 | -2.85 | -0.000 | +0.00 |
| RY.TO | 503 | +6.65 | -0.23 | +0.000 | +0.00 |
| SMH | 501 | +12.46 | +0.66 | +0.000 | +0.00 |
| SNDK.TO | 131 | +5.70 | -0.62 | +0.000 | +0.00 |
| SOXL.NE | 311 | +11.17 | -0.29 | +0.000 | +0.00 |
| SOXX | 501 | +12.92 | +0.63 | +0.000 | +0.00 |
| SPCL | 154 | -2.80 | -0.97 | +0.000 | +0.00 |
| UBOT | 501 | +10.81 | +0.27 | +0.000 | +0.00 |
| VFV.TO | 503 | +13.08 | +1.04 | +0.000 | +0.00 |
| XCHP.TO | 503 | +12.28 | +0.74 | +0.000 | +0.00 |
| XEQT.TO | 503 | +10.53 | +0.89 | +0.000 | +0.01 |
