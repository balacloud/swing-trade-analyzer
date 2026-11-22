# UI Cohesiveness Test Report

**Date:** 2026-11-12T15:31:51.860Z
**Tickers Tested:** 1
**Total PDFs Generated:** 1

---

## Results Summary

| # | Ticker | Name | Classification | Simple view | Cards | Status | PDF |
|---|--------|------|----------------|-------------|-------|--------|-----|
| 1 | SMH | SMH - VanEck Semiconductor ETF | Exchange-traded fund (ETF) | ⏸️ No Trade 6/9 criteria met | 7 | success | SMH.pdf |

---

## Checklist (Manual Review)

For each PDF, verify:
- [ ] Market backdrop is the first card and shows facts only (no Favorable/Unfavorable label)
- [ ] No BUY/HOLD/AVOID verdict anywhere; the Simple view says TRADE or No Trade
- [ ] Each card says what its read is based on (rules, data source, dates)
- [ ] Anything that could not load says so plainly; no blank or made-up values
- [ ] An ETF says "Exchange-traded fund (ETF)", never "Unknown"
- [ ] Earnings date (Fundamentals) and header badge agree
- [ ] Trade Setup stop/target come from real support/resistance, or the card says why not

Automated checks: `node scripts/ui-verify-checklist.js`.
