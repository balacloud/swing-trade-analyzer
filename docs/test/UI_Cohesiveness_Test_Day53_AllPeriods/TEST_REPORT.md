# UI Cohesiveness Test Report

**Date:** 2026-02-12T17:05:00.114Z
**Tickers Tested:** 10
**Holding Periods:** quick, standard, position
**Total PDFs Generated:** 30

---

## Results Summary

| # | Ticker | Period | Verdict | Categories | Price | Status | PDF |
|---|--------|--------|---------|------------|-------|--------|-----|
| 1 | AAPL | quick | HOLD | T:DF:DS:NR:F | $265.25 | success | AAPL_quick.pdf |
| 2 | AAPL | standard | HOLD | T:DF:DS:NR:F | $265.25 | success | AAPL.pdf |
| 3 | AAPL | position | HOLD | T:DF:DS:NR:F | $265.25 | success | AAPL_position.pdf |
| 4 | JNJ | quick | AVOID | T:WF:SS:NR:F | $244.52 | success | JNJ_quick.pdf |
| 5 | JNJ | standard | AVOID | T:WF:SS:NR:F | $244.52 | success | JNJ.pdf |
| 6 | JNJ | position | AVOID | T:WF:SS:NR:F | $244.52 | success | JNJ_position.pdf |
| 7 | F | quick | BUY | T:SF:WS:NR:F | $14.02 | success | F_quick.pdf |
| 8 | F | standard | HOLD | T:SF:WS:NR:F | $14.02 | success | F.pdf |
| 9 | F | position | AVOID | T:SF:WS:NR:F | $14.02 | success | F_position.pdf |
| 10 | COIN | quick | AVOID | T:WF:SS:NR:F | $140.29 | success | COIN_quick.pdf |
| 11 | COIN | standard | AVOID | T:WF:SS:NR:F | $140.29 | success | COIN.pdf |
| 12 | COIN | position | AVOID | T:WF:SS:NR:F | $140.29 | success | COIN_position.pdf |
| 13 | AFRM | quick | AVOID | T:WF:DS:NR:F | $51.02 | success | AFRM_quick.pdf |
| 14 | AFRM | standard | AVOID | T:WF:DS:NR:F | $51.02 | success | AFRM.pdf |
| 15 | AFRM | position | AVOID | T:WF:DS:NR:F | $51.02 | success | AFRM_position.pdf |
| 16 | XOM | quick | AVOID | T:DF:DS:NR:N | $152.71 | success | XOM_quick.pdf |
| 17 | XOM | standard | AVOID | T:DF:DS:NR:N | $152.71 | success | XOM.pdf |
| 18 | XOM | position | HOLD | T:DF:DS:NR:F | $152.71 | success | XOM_position.pdf |
| 19 | PLTR | quick | AVOID | T:WF:SS:NR:F | $127.18 | success | PLTR_quick.pdf |
| 20 | PLTR | standard | AVOID | T:WF:SS:NR:N | $127.18 | success | PLTR.pdf |
| 21 | PLTR | position | AVOID | T:WF:SS:NR:N | $127.18 | success | PLTR_position.pdf |
| 22 | VZ | quick | AVOID | T:WF:DS:NR:N | $50.17 | success | VZ_quick.pdf |
| 23 | VZ | standard | AVOID | T:WF:DS:NR:N | $50.17 | success | VZ.pdf |
| 24 | VZ | position | AVOID | T:WF:DS:NR:N | $50.17 | success | VZ_position.pdf |
| 25 | SMCI | quick | AVOID | T:WF:DS:NR:N | $30.66 | success | SMCI_quick.pdf |
| 26 | SMCI | standard | AVOID | T:WF:DS:NR:N | $30.66 | success | SMCI.pdf |
| 27 | SMCI | position | AVOID | T:WF:DS:NR:N | $30.66 | success | SMCI_position.pdf |
| 28 | META | quick | AVOID | T:WF:SS:NR:N | $649.85 | success | META_quick.pdf |
| 29 | META | standard | AVOID | T:WF:SS:NR:N | $649.85 | success | META.pdf |
| 30 | META | position | AVOID | T:WF:SS:NR:N | $649.85 | success | META_position.pdf |

---

## Checklist (Manual Review)

For each PDF, verify:
- [ ] Verdict (BUY/HOLD/AVOID) is consistent with category assessments
- [ ] Bottom Line Card shows correct holding period weight note
- [ ] Entry cards match ADX-based entry preference
- [ ] Position Size banner hidden when AVOID or ADX < 20
- [ ] R:R badge shows correctly (grayed out if < 1.0)
- [ ] No conflicting signals (AVOID verdict + VIABLE badge)
- [ ] Data source badges show correctly
- [ ] Earnings warning shown if applicable
