# UI Cohesiveness Test Report

**Date:** 2026-02-12T16:55:26.305Z
**Tickers Tested:** 10
**Holding Periods:** standard
**Total PDFs Generated:** 10

---

## Results Summary

| # | Ticker | Period | Verdict | Categories | Price | Status | PDF |
|---|--------|--------|---------|------------|-------|--------|-----|
| 1 | AAPL | standard | HOLD | T:DF:DS:NR:F | $265.25 | success | AAPL.pdf |
| 2 | JNJ | standard | AVOID | T:WF:SS:NR:F | $244.52 | success | JNJ.pdf |
| 3 | F | standard | HOLD | T:SF:WS:NR:F | $14.02 | success | F.pdf |
| 4 | COIN | standard | AVOID | T:WF:SS:NR:F | $140.29 | success | COIN.pdf |
| 5 | AFRM | standard | AVOID | T:WF:DS:NR:F | $51.02 | success | AFRM.pdf |
| 6 | XOM | standard | HOLD | T:DF:DS:NR:F | $152.74 | success | XOM.pdf |
| 7 | PLTR | standard | AVOID | T:WF:SS:NR:F | $127.18 | success | PLTR.pdf |
| 8 | VZ | standard | AVOID | T:WF:DS:NR:F | $50.17 | success | VZ.pdf |
| 9 | SMCI | standard | AVOID | T:WF:DS:NR:F | $30.66 | success | SMCI.pdf |
| 10 | META | standard | AVOID | T:WF:SS:NR:F | $649.85 | success | META.pdf |

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
