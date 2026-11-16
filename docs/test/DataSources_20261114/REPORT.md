# Data source audit: truth-free checks (2026-11-14)

Plan: `docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md` step 1. Script: `backend/backtest/audit_data_sources.py`.
Checks C2 fresh, C4 integrity, C5 jumps, C6 history, C8 tab honest, C9 cross-source. **Not yet checked (needs IBKR, step 2): identity, close accuracy vs broker, volume vs broker.**
"STA uses" = the first source in the real chain that returned data. ✅ pass ⚠️ warn ❌ fail — not applicable.

## Matrix

| Class | Ticker | STA uses | Bars | C2 | C4 | C5 | C6 | C8 | C9 |
|---|---|---|---|---|---|---|---|---|---|
| US stock | `JPM` | twelvedata | 504 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US stock | `CAT` | twelvedata | 504 | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| US stock | `BRK-B` | yfinance | 501 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| US ETF | `SMH` | twelvedata | 504 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US ETF | `SOXX` | twelvedata | 504 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US ETF | `GDX` | yfinance | 501 | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ |
| US leveraged | `QPUX` | yfinance | 321 | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ |
| US leveraged | `DRAL` | yfinance | 100 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `SPCL` | yfinance | 154 | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `UBOT` | yfinance | 501 | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ |
| CA stock | `RY.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CNR.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `ATD.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CSU.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XEQT.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `VFV.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `HXQ.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XCHP.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA leveraged | `GDXU.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA leveraged | `SOXL.NE` | yfinance | 311 | ✅ | ❌ | ⚠️ | ✅ | ❌ | ✅ |
| CDR | `AMD.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CDR | `AVGO.TO` | yfinance | 225 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CDR | `MU.TO` | yfinance | 273 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CDR | `SNDK.TO` | yfinance | 131 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |

## Verdict per class

- **US stock** (3): no failures; warnings: CAT C4, BRK-B C8
- **US ETF** (3): no failures; warnings: GDX C4, GDX C8
- **US leveraged** (4): FAILS: QPUX C5; warnings: QPUX C8, DRAL C6, DRAL C8, SPCL C5, SPCL C6, SPCL C8, UBOT C4, UBOT C8
- **CA stock** (4): no failures
- **CA ETF** (4): no failures
- **CA leveraged** (2): FAILS: SOXL.NE C4, SOXL.NE C8; warnings: SOXL.NE C5
- **CDR** (4): no failures; warnings: AVGO.TO C6, SNDK.TO C6

## Every finding (warn and fail), with evidence

**CAT** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0

**BRK-B** (US stock, dash symbol); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**GDX** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**QPUX** (US leveraged, 1:3 reverse split 2026-03-23); sources {'twelvedata': 321, 'yfinance': 321, 'tradier': 321}
- ❌ C5: twelvedata: 2026-05-21 +48%: also in yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-05-21 +48%: also in twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2026-03-20 -69%: ONLY here; twelvedata,yfinance are continuous -> tradier has a split error | 2026-05-21 +48%: also in twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C8: tab says yfinance / 321 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters); a source later in the chain fails: tradier C5

**DRAL** (US leveraged, ~100 days); sources {'twelvedata': 100, 'yfinance': 100, 'tradier': 100}
- ⚠️ C6: twelvedata: 100 bars from 2026-06-25 || yfinance: 100 bars from 2026-06-25 || tradier: 100 bars from 2026-06-25
- ⚠️ C8: tab says yfinance / 100 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SPCL** (US leveraged, ~154 days); sources {'twelvedata': 150, 'yfinance': 154, 'tradier': 154}
- ⚠️ C5: twelvedata: 2026-06-12 +57%: also in yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-06-12 +57%: also in twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2026-06-12 +57%: also in twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: twelvedata: 150 bars from 2026-04-14; starts 6 days after yfinance (2026-04-08, 154 bars); starts 6 days after tradier (2026-04-08, 154 bars) || yfinance: 154 bars from 2026-04-08 || tradier: 154 bars from 2026-04-08
- ⚠️ C8: tab says yfinance / 154 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**UBOT** (US leveraged, control); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SOXL.NE** (CA leveraged, known bad: Cboe Canada only); sources {'yfinance': 311, 'eodhd': 251}
- ❌ C4: yfinance: flat zero-volume 100%; bad OHLC rows 0; zero-volume in last 5: 5
- ⚠️ C5: yfinance: 2026-05-25 -67%: also in eodhd (real move, or unadjusted everywhere: needs IBKR)
- ❌ C8: tab says yfinance / 311 rows / just_fetched but yfinance fails C4: the tab shows no warning

**AVGO.TO** (CDR); sources {'yfinance': 225}
- ⚠️ C6: yfinance: 225 bars from 2025-12-22

**SNDK.TO** (CDR, short history); sources {'yfinance': 131, 'eodhd': 132}
- ⚠️ C6: yfinance: 131 bars from 2026-05-08


## Source errors (a source that could not serve a ticker)


## Known limits of this audit (read before trusting the matrix)

- **Agreement is not accuracy.** If two sources share the same defect they agree (SOXL.NE on Yahoo and EODHD are both close-only), so C9 passes. Only the IBKR truth step (step 2) can settle those; C5 marks them "needs IBKR".
- **"STA uses" comes from the tab.** The tab's source was read right after this script spent Twelve Data credits on the same key, so some "fell through to Yahoo" results may be partly self-inflicted. Either way, every source in the chain is graded, because any of them can serve a request.
- **Canada has one source for most tickers.** Only the tickers listed with EODHD had a second opinion (free quota: 20 calls a day). The rest show `—` in C9, which means unchecked, not clean.
- **Freshness ignores market holidays** (it uses weekdays).
- **Tradier is not dividend-adjusted**, so its old closes differ slightly from Yahoo's on ex-dividend days; the close check only looks at the last 20 sessions.
- Not run: identity/currency (C1), close accuracy vs the broker (C3), volume vs the broker (C7), fundamentals and classification (C10), Alpha Vantage.

