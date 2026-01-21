# Perplexity Deep Research Prompt: Free-Tier Data Strategy for Swing Trade Screener

## Context
Building a swing trade stock screener that needs to analyze 563 stocks daily (S&P 500 + TSX 60). Currently hitting rate limits on yfinance. Need a robust, free-tier data strategy with fallbacks.

---

## Research Questions

### 1. Free-Tier API Comparison for Stock Data

Compare these APIs for a swing trade screener (NOT day trading - end-of-day data is fine):

| API | Need to Research |
|-----|------------------|
| **yfinance** | Rate limits? Reliability? Best practices? |
| **Twelve Data** | Free tier limits (800/day shown), what endpoints cost what credits? |
| **Alpha Vantage** | Free tier (5 calls/min, 500/day), batch endpoints? |
| **Finnhub** | Free tier (60/min), what's included? |
| **Polygon.io** | Free tier limits? Historical data access? |
| **Yahoo Finance v7/v8** | Direct API vs yfinance wrapper? |
| **EODHD** | Free tier? Batch download capability? |
| **Tiingo** | Free tier limits? Good for EOD data? |

For each, research:
- Daily/minute rate limits
- What data is included (OHLCV, fundamentals, technicals)
- Batch request capability
- Reliability/uptime
- Best for: real-time vs EOD vs fundamentals

### 2. Data We Actually Need (EXACT Requirements from Our Codebase)

For swing trading (1-8 week holds), here's our EXACT data usage:

**OHLCV Data (per stock) - CRITICAL:**
- 2 years historical OHLCV (for S&R calculation)
- Daily timeframe (EOD is fine)
- We calculate LOCALLY from OHLCV (no API needed):
  - SMA50, SMA200, EMA8, EMA21
  - ATR (14-period)
  - RSI (14-period)
  - Volume averages (20/50 day)
  - Support/Resistance levels (agglomerative clustering)

**Fundamentals (per stock) - Currently from yfinance:**
```python
# What we fetch from yfinance stock.info:
'trailingPE'       # P/E Ratio
'forwardPE'        # Forward P/E
'pegRatio'         # PEG Ratio
'marketCap'        # Market Cap
'returnOnEquity'   # ROE (we also calculate from financials)
'returnOnAssets'   # ROA
'earningsGrowth'   # EPS Growth %
'revenueGrowth'    # Revenue Growth %
'debtToEquity'     # Debt/Equity ratio
'profitMargins'    # Profit Margin
'operatingMargins' # Operating Margin
'beta'             # Beta
'dividendYield'    # Dividend Yield

# Additional from stock.quarterly_financials:
'Total Revenue'    # For revenue growth calculation
'Net Income'       # For ROE/ROA calculation

# From stock.quarterly_balance_sheet:
'Stockholders Equity'  # For ROE calculation
'Total Assets'         # For ROA calculation
'Total Debt'           # For D/E ratio
```

**Market/Index Data:**
- SPY OHLCV (for Relative Strength calculation vs market)
- VIX current value (for market conditions score)

**Question:** Which APIs provide these specific fundamentals in free tier? Can we batch fundamental requests? Do all APIs have quarterly_financials/quarterly_balance_sheet equivalents?

### 3. Nightly Batch Download Strategy

Since swing trading doesn't need real-time data:

**Proposal:**
```
Daily Universe: 563 stocks (S&P 500 + TSX 60)

Nightly Download (after market close):
├─ Download OHLCV for all 563 stocks
├─ Store in local SQLite/Parquet
├─ Calculate technicals locally (RSI, ATR, SMA)
├─ Fetch fundamentals weekly (not daily - they don't change)
└─ Run screener against local data

Questions:
1. Which API is best for bulk EOD OHLCV download?
2. Can we batch 500+ stocks in one call?
3. What's the optimal batching strategy (50 stocks/request)?
4. How to handle API rotation (use yfinance until rate limited, then Twelve Data, etc.)?
```

### 4. TradingView Screener Integration

Should we outsource initial screening to TradingView?

**TradingView Screener can filter:**
- Technical patterns
- Volume conditions
- Price above/below MAs
- RSI overbought/oversold

**Research:**
1. Can TradingView screener results be exported/scraped?
2. Is there a TradingView API (official or unofficial)?
3. What's the workflow: TV screener -> our app for S&R analysis?
4. Pine Script screener alerts -> webhook to our system?

### 5. Rate Limit Handling Patterns

Research best practices for:

```python
# Desired behavior:
def fetch_with_fallback(ticker):
    try:
        return yfinance.get(ticker)  # Primary
    except RateLimitError:
        try:
            return twelvedata.get(ticker)  # Fallback 1
        except RateLimitError:
            return alphavantage.get(ticker)  # Fallback 2
```

Questions:
1. How do developers typically rotate between free tier APIs?
2. Exponential backoff strategies?
3. Request queuing/throttling patterns?
4. Caching strategies (how long is EOD data valid)?

### 6. Stock Universe Management

For 563 stocks (S&P 500 + TSX 60):

**Questions:**
1. Where to get authoritative S&P 500 constituent list (free)?
2. Where to get TSX 60 constituent list?
3. How often do constituents change?
4. Should we pre-filter to reduce universe (e.g., only stocks >$10, >1M avg volume)?

### 7. Architecture Recommendation

Based on research, recommend:

```
Optimal Free-Tier Architecture:
├─ Primary OHLCV source: ________
├─ Fallback OHLCV source: ________
├─ Fundamentals source: ________
├─ Real-time quotes (optional): ________
├─ Local storage: SQLite / Parquet / CSV?
├─ Update frequency: Nightly / Hourly / On-demand?
└─ Estimated monthly API usage: ________
```

---

## Our Modules and Data Dependencies

**Module-by-Module Breakdown:**

| Module | Data Needed | Current Source | Can Batch? |
|--------|-------------|----------------|------------|
| **S&R Engine** (`support_resistance.py`) | OHLCV 2yr + Weekly OHLCV | yfinance | Yes |
| **Scoring Engine** (`scoringEngine.js`) | All technicals + fundamentals | yfinance | Partial |
| **RS Calculator** (`rsCalculator.js`) | Stock OHLCV + SPY OHLCV | yfinance | Yes |
| **Fundamentals** (`backend.py`) | stock.info + financials | yfinance / Defeat Beta | Yes |
| **Market Data** (`backend.py`) | SPY, VIX quotes | yfinance | Yes |

**API Calls Per Stock Analysis:**
1. OHLCV history (2 years) - 1 call
2. Weekly OHLCV (for MTF) - 1 call
3. Fundamentals (stock.info) - 1 call
4. Quarterly financials - 1 call
5. Quarterly balance sheet - 1 call
**Total: ~5 calls per stock = 2,815 calls for 563 stocks**

---

## Current System State

**What we fetch today:**
- yfinance: OHLCV (2 years), basic fundamentals
- Defeat Beta: Fundamentals (broken - TProtocolException)
- No fallbacks implemented
- No local caching
- Fetch on-demand (not batched)

**Pain points:**
- Rate limit errors during batch operations (showing in Twelve Data screenshot)
- Slow individual stock lookups
- No graceful degradation
- yfinance sometimes gets rate limited by Yahoo

---

## Deliverables Requested

1. **Comparison table** of all free-tier APIs with limits
2. **Recommended architecture** for 563-stock daily screening
3. **Code patterns** for rate limit handling and API rotation
4. **Batch download strategy** with specific API recommendations
5. **TradingView integration options** (if viable)
6. **Estimated API usage** per day for our use case

---

## Constraints

- Budget: $0/month (free tiers only)
- Stock universe: 563 stocks (S&P 500 + TSX 60)
- Update frequency: Once per day (after market close)
- Data freshness: EOD is acceptable (not day trading)
- Fundamentals: Weekly update is fine
- Must be Python-compatible

---

## Alternative Approaches to Consider

### Option A: Full Local Download (Current Direction)
- Download all 563 stocks nightly
- Calculate everything locally
- Pros: Full control, no real-time rate limits
- Cons: Complex, needs storage, API limits still apply to download

### Option B: TradingView Screener Outsourcing
- Use TradingView screener to filter from 563 → ~50 candidates
- Only fetch detailed data for candidates
- Pros: Dramatic API reduction (50 vs 563)
- Cons: Dependency on TV, lose custom filtering

### Option C: Hybrid Approach
- TradingView screener for initial filter
- Fetch OHLCV only for screener output (~50 stocks)
- Calculate S&R and RS locally
- Fundamentals from free API for top 20
- **API calls: ~100-150/day instead of 2,815**

### Option D: Pre-built Stock Lists
- Subscribe to curated momentum stock lists
- Only analyze stocks already passing basic screens
- Finviz Elite, IBD lists, etc.

**Research Question:** What's the most practical approach for a solo developer on free tier?

---

## Specific Questions for Perplexity

1. **yfinance rate limits**: What are the actual documented limits? How to avoid getting blocked?
2. **Batch downloads**: Can yfinance.download(['AAPL', 'MSFT', ...]) batch 500+ tickers efficiently?
3. **Twelve Data free tier**: What's the 800/day credit breakdown for different endpoints?
4. **Alpha Vantage batch**: Does AV support batch fundamental data?
5. **Local OHLCV storage**: SQLite vs Parquet vs CSV for 563 stocks x 2yr history?
6. **TradingView scraping**: Is TV screener data accessible without paid API?
7. **Finnhub fundamentals**: Does free tier include financial statements?
8. **Polygon.io free**: What data is actually available on basic plan?

---

## Success Criteria

A good solution would:
1. Screen 563 stocks daily without hitting rate limits
2. Cost $0/month
3. Run in <15 minutes
4. Have automatic fallbacks when one API fails
5. Store historical data locally to reduce repeated API calls
6. Support our exact data requirements (OHLCV 2yr, fundamentals listed above)
