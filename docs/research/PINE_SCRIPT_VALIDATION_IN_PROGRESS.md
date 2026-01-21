# Pine Script v2 Validation - In Progress

> **Date:** January 21, 2026
> **Day:** 34
> **Status:** COLLECTING SCREENSHOTS (5/9 received)

---

## Purpose

Manual comparison of TradingView Pine Script (STA S&R v2) levels against backend S&R levels.
Following CLAUDE_CONTEXT.md protocols and Golden Rules.

---

## Screenshots Collected

### 1. SOFI (Small-cap Fintech)
| Field | Value |
|-------|-------|
| Price | $25.49 |
| Strong Levels | 6 |
| Medium Levels | 3 |
| Weak Levels | ? |

**Resistance Levels (from Pine Script):**
- R: $28, $30, $32.73

**Support Levels (from Pine Script):**
- S: $25, $14-15, $8.60

**Notes:** High volatility stock, many historical levels visible

---

### 2. AMD (Semiconductor)
| Field | Value |
|-------|-------|
| Price | $231.92 |
| Strong Levels | 4 |
| Medium Levels | 2 |
| Weak Levels | 2 |

**Resistance Levels (from Pine Script):**
- R: $234, $240, $267

**Support Levels (from Pine Script):**
- S: $225, $170, $150

**Notes:** Volatile semiconductor, clear level structure

---

### 3. JPM (Financials)
| Field | Value |
|-------|-------|
| Price | $302.74 |
| Strong Levels | 9 |
| Medium Levels | 1 |
| Weak Levels | 0 |

**Resistance Levels (from Pine Script):**
- R: $310, $320, $337

**Support Levels (from Pine Script):**
- S: $300, $270, $255, $240, $220, $210

**Notes:** Stable financial, many strong levels (9!) indicates well-established price zones

---

### 4. META (Mega-cap Tech)
| Field | Value |
|-------|-------|
| Price | $604.12 |
| Strong Levels | 10 |
| Medium Levels | 0 |
| Weak Levels | 1 |

**Resistance Levels (from Pine Script):**
- R: $620, $640, $680, $720, $740

**Support Levels (from Pine Script):**
- S: $580, $560, $540, $520

**Notes:** Very strong level structure (10 strong levels!), mega-cap stability. (User initially labeled as "GOOGL" - corrected to META based on chart data.)

---

### 5. GOOGL (Mega-cap Tech)
| Field | Value |
|-------|-------|
| Price | $322.00 |
| Strong Levels | 12 |
| Medium Levels | 1 |
| Weak Levels | 0 |

**Resistance Levels (from Pine Script):**
- R: ~$322 (at ATH area - no clear overhead resistance)

**Support Levels (from Pine Script):**
- S: $190, $180, $170, $160 (all historical - far below)

**Notes:** Strong uptrend with 12 strong levels. Most support far below current price. ATH territory = Fibonacci extensions should activate in backend.

---

### 6. AAPL (Mega-cap Tech)
| Field | Value |
|-------|-------|
| Price | $246.70 |
| Strong Levels | 11 |
| Medium Levels | 0 |
| Weak Levels | 1 |

**Resistance Levels (from Pine Script):**
- R: ~$250 (near current price)

**Support Levels (from Pine Script):**
- S: $232, $220, $210, $207

**Notes:** Strong level structure (11 strong levels). Clear support zones. Pulled back from $288 high.

---

### 7. PENDING
*Awaiting screenshot*

---

### 8. PENDING
*Awaiting screenshot*

---

### 9. PENDING
*Awaiting screenshot*

---

## Expected Stocks (from MANUAL_VALIDATION_DAY34.md)

| Stock | Type | Expected MTF% | Screenshot Status |
|-------|------|---------------|-------------------|
| AAPL | Mega-cap Tech | 62.5% | PENDING |
| NVDA | High-growth Tech | 45.5% | PENDING |
| TSLA | Momentum | 35.0% | PENDING |
| MSFT | Mega-cap Tech | 60.0% | PENDING |
| GOOGL | Mega-cap Tech | 64.3% | ✅ RECEIVED |
| META | Mega-cap Tech | 62.5% | ✅ RECEIVED |
| JPM | Financials | 64.3% | ✅ RECEIVED |
| AMD | Semiconductor | 47.1% | ✅ RECEIVED |
| SOFI | Small-cap Fintech | 23.8% | ✅ RECEIVED |
| PLTR | Growth Tech | 33.3% | PENDING |

---

## Backend Comparison (To Be Completed)

Once all screenshots are received, will run:
```bash
cd /Users/balajik/projects/swing-trade-analyzer/backend
source venv/bin/activate
python tradingview_comparison.py SOFI AMD JPM [other tickers...]
```

Then compare:
- Level counts (Strong/Medium/Weak)
- Nearest levels within 2% tolerance
- MTF confluence alignment
- Major historical levels

---

## Validation Criteria

| Criteria | Target | Status |
|----------|--------|--------|
| Level Detection | Similar pivot areas (within 2%) | PENDING |
| Methodology Match | Both use swing trade rules | PENDING |
| Practical Use | Actionable levels available | PENDING |

---

*File created to preserve context across session reloads*
*Last Updated: After screenshot 3 (JPM)*
