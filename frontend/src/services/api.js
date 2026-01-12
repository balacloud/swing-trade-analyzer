/**
 * API Service for Swing Trade Analyzer
 * Connects to Flask backend on port 5001
 * 
 * v2.0: Added fundamentals endpoint for rich fundamental data
 * v2.1: Added TradingView screener endpoints for batch scanning
 * v2.2: Added Support & Resistance endpoint
 * v2.3: Added Validation Engine endpoints (Day 17)
 */

const API_BASE_URL = 'http://localhost:5001/api';

/**
 * Fetch stock data for a given ticker
 * Returns price history, basic info, and volume data
 */
export async function fetchStockData(ticker) {
  try {
    const response = await fetch(`${API_BASE_URL}/stock/${ticker.toUpperCase()}`);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || `Failed to fetch ${ticker}`);
    }
    
    const data = await response.json();
    
    // Transform data for frontend consumption
    return {
      ticker: data.ticker,
      name: data.name,
      sector: data.sector,
      industry: data.industry,
      currentPrice: data.currentPrice,
      price52wAgo: data.price52wAgo,
      price13wAgo: data.price13wAgo,
      fiftyTwoWeekHigh: data.fiftyTwoWeekHigh,
      fiftyTwoWeekLow: data.fiftyTwoWeekLow,
      avgVolume: data.avgVolume,
      avgVolume10d: data.avgVolume10d,
      priceHistory: data.priceHistory,
      fundamentals: data.fundamentals,
      dataPoints: data.dataPoints,
      oldestDate: data.oldestDate,
      newestDate: data.newestDate
    };
    
  } catch (error) {
    console.error('Error fetching stock data:', error);
    throw error;
  }
}

/**
 * Fetch rich fundamental data for scoring
 * Uses Defeat Beta if available, falls back to yfinance
 * 
 * Returns:
 * - ROE, ROIC, ROA
 * - EPS Growth, Revenue Growth
 * - Debt/Equity, Profit Margins
 */
export async function fetchFundamentals(ticker) {
  try {
    const response = await fetch(`${API_BASE_URL}/fundamentals/${ticker.toUpperCase()}`);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || `Failed to fetch fundamentals for ${ticker}`);
    }
    
    const data = await response.json();
    
    // Return normalized fundamental data
    return {
      source: data.source,
      ticker: data.ticker,
      roe: data.roe,
      roic: data.roic,
      roa: data.roa,
      epsGrowth: data.epsGrowth,
      revenueGrowth: data.revenueGrowth,
      debtToEquity: data.debtToEquity,
      profitMargin: data.profitMargin,
      operatingMargin: data.operatingMargin,
      pegRatio: data.pegRatio,
      pe: data.pe,
      forwardPe: data.forwardPe,
      marketCap: data.marketCap,
      beta: data.beta,
      dividendYield: data.dividendYield,
      timestamp: data.timestamp
    };
    
  } catch (error) {
    console.error('Error fetching fundamentals:', error);
    // Return null to indicate failure - caller can handle gracefully
    return null;
  }
}

/**
 * Fetch SPY data for relative strength calculations
 */
export async function fetchSPYData() {
  try {
    const response = await fetch(`${API_BASE_URL}/market/spy`);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to fetch SPY data');
    }
    
    const data = await response.json();
    
    return {
      ticker: data.ticker,
      currentPrice: data.currentPrice,
      price52wAgo: data.price52wAgo,
      price13wAgo: data.price13wAgo,
      sma200: data.sma200,
      aboveSma200: data.aboveSma200,
      priceHistory: data.priceHistory,
      dataPoints: data.dataPoints
    };
    
  } catch (error) {
    console.error('Error fetching SPY data:', error);
    throw error;
  }
}

/**
 * Fetch VIX data for risk assessment
 */
export async function fetchVIXData() {
  try {
    const response = await fetch(`${API_BASE_URL}/market/vix`);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to fetch VIX data');
    }
    
    const data = await response.json();
    
    return {
      ticker: data.ticker,
      current: data.current,
      regime: data.regime,
      isRisky: data.isRisky
    };
    
  } catch (error) {
    console.error('Error fetching VIX data:', error);
    // Return safe defaults if VIX fetch fails
    return {
      ticker: 'VIX',
      current: 20,
      regime: 'normal',
      isRisky: false
    };
  }
}

/**
 * Check backend health
 */
export async function checkBackendHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    
    if (!response.ok) {
      return { healthy: false, error: 'Backend not responding' };
    }
    
    const data = await response.json();
    
    return {
      healthy: data.status === 'healthy',
      version: data.version,
      defeatbetaAvailable: data.defeatbeta_available,
      tradingviewAvailable: data.tradingview_available,
      srEngineAvailable: data.sr_engine_available,
      validationAvailable: data.validation_available,
      timestamp: data.timestamp
    };
    
  } catch (error) {
    return { healthy: false, error: error.message };
  }
}

/**
 * Fetch all data needed for analysis
 * Combines stock, fundamentals, SPY, and VIX in parallel
 */
export async function fetchAnalysisData(ticker) {
  try {
    // Fetch all data in parallel for speed
    const [stockData, fundamentals, spyData, vixData] = await Promise.all([
      fetchStockData(ticker),
      fetchFundamentals(ticker),
      fetchSPYData(),
      fetchVIXData()
    ]);
    
    // Merge fundamentals into stock data if available
    if (fundamentals) {
      stockData.fundamentals = {
        ...stockData.fundamentals,
        ...fundamentals,
        // Keep track of data source
        enriched: true,
        enrichedSource: fundamentals.source
      };
    }
    
    return {
      stock: stockData,
      spy: spyData,
      vix: vixData,
      fundamentals: fundamentals
    };
    
  } catch (error) {
    console.error('Error fetching analysis data:', error);
    throw error;
  }
}

// ============================================
// TRADINGVIEW SCREENER ENDPOINTS (Day 11/12)
// ============================================

/**
 * Fetch available scanning strategies
 * Returns list of strategies with descriptions
 */
export async function fetchScanStrategies() {
  try {
    const response = await fetch(`${API_BASE_URL}/scan/strategies`);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to fetch scan strategies');
    }
    
    const data = await response.json();
    
    return {
      tradingviewAvailable: data.tradingview_available,
      strategies: data.strategies,
      notes: data.notes
    };
    
  } catch (error) {
    console.error('Error fetching scan strategies:', error);
    throw error;
  }
}

/**
 * Scan for swing trade candidates using TradingView screener
 * 
 * @param {string} strategy - 'reddit', 'minervini', 'momentum', 'value'
 * @param {number} limit - max results (default 50, max 100)
 * @returns {object} - { strategy, totalMatches, returned, candidates[] }
 */
export async function fetchScanResults(strategy = 'reddit', limit = 50) {
  try {
    const response = await fetch(
      `${API_BASE_URL}/scan/tradingview?strategy=${strategy}&limit=${limit}`
    );
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to scan for candidates');
    }
    
    const data = await response.json();
    
    return {
      strategy: data.strategy,
      totalMatches: data.totalMatches,
      returned: data.returned,
      limit: data.limit,
      timestamp: data.timestamp,
      candidates: data.candidates || []
    };
    
  } catch (error) {
    console.error('Error scanning for candidates:', error);
    throw error;
  }
}

// ============================================ 
// SUPPORT & RESISTANCE ENDPOINT (Day 14)
// ============================================

/**
 * Fetch Support & Resistance levels for a ticker
 * 
 * Returns:
 * - support: Array of support price levels
 * - resistance: Array of resistance price levels  
 * - method: 'pivot', 'kmeans', or 'volume_profile'
 * - suggestedEntry: Nearest support (entry point)
 * - suggestedStop: Stop loss level (3% below entry)
 * - suggestedTarget: Nearest resistance (profit target)
 * - riskReward: Risk/Reward ratio
 * - meta: Additional info (ATR, projection flags)
 */
export async function fetchSupportResistance(ticker) {
  try {
    const response = await fetch(`${API_BASE_URL}/sr/${ticker.toUpperCase()}`);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || `Failed to fetch S&R for ${ticker}`);
    }
    
    const data = await response.json();
    
    return {
      ticker: data.ticker,
      currentPrice: data.currentPrice,
      method: data.method,
      support: data.support || [],
      resistance: data.resistance || [],
      allSupport: data.allSupport || [],      // Day 26: Include all historical support levels
      allResistance: data.allResistance || [], // Day 26: Include all historical resistance levels
      suggestedEntry: data.suggestedEntry,
      suggestedStop: data.suggestedStop,
      suggestedTarget: data.suggestedTarget,
      riskReward: data.riskReward,
      dataPoints: data.dataPoints,
      timestamp: data.timestamp,
      meta: data.meta || {}
    };
    
  } catch (error) {
    console.error('Error fetching S&R:', error);
    return null;
  }
}

/**
 * Fetch analysis data WITH Support & Resistance
 * Enhanced version that includes S&R levels in parallel
 */
export async function fetchFullAnalysisData(ticker) {
  try {
    const [stockData, fundamentals, spyData, vixData, srData] = await Promise.all([
      fetchStockData(ticker),
      fetchFundamentals(ticker),
      fetchSPYData(),
      fetchVIXData(),
      fetchSupportResistance(ticker)
    ]);
    
    if (fundamentals) {
      stockData.fundamentals = {
        ...stockData.fundamentals,
        ...fundamentals,
        enriched: true,
        enrichedSource: fundamentals.source
      };
    }
    
    return {
      stock: stockData,
      spy: spyData,
      vix: vixData,
      fundamentals: fundamentals,
      sr: srData
    };
    
  } catch (error) {
    console.error('Error fetching full analysis data:', error);
    throw error;
  }
}

// ============================================ 
// VALIDATION ENGINE ENDPOINTS (Day 17)
// ============================================

/**
 * Run validation for specified tickers
 * Compares our data against external sources (StockAnalysis, Finviz)
 * 
 * @param {string[]} tickers - Array of ticker symbols to validate
 * @returns {object} - Validation report with metrics and results
 */
export async function runValidation(tickers) {
  try {
    const response = await fetch(`${API_BASE_URL}/validation/run`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ tickers })
    });
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to run validation');
    }
    
    const data = await response.json();
    
    return {
      runId: data.run_id,
      timestamp: data.timestamp,
      tickers: data.tickers,
      overallPassRate: data.overall_pass_rate,
      summary: {
        totalChecks: data.summary.total_checks,
        validated: data.summary.validated,
        skipped: data.summary.skipped,
        passed: data.summary.passed,
        failed: data.summary.failed,
        warnings: data.summary.warnings,
        coverageRate: data.summary.coverage_rate,
        accuracyRate: data.summary.accuracy_rate,
        qualityScore: data.summary.quality_score
      },
      tickerResults: data.ticker_results.map(tr => ({
        ticker: tr.ticker,
        overallStatus: tr.overall_status,
        passCount: tr.pass_count,
        failCount: tr.fail_count,
        warningCount: tr.warning_count,
        skipCount: tr.skip_count,
        results: tr.results.map(r => ({
          metric: r.metric,
          ourValue: r.our_value,
          externalValue: r.external_value,
          externalSource: r.external_source,
          variancePct: r.variance_pct,
          tolerancePct: r.tolerance_pct,
          status: r.status,
          notes: r.notes
        }))
      }))
    };
    
  } catch (error) {
    console.error('Error running validation:', error);
    throw error;
  }
}

/**
 * Fetch validation history (list of past runs)
 * @returns {object[]} - Array of past validation runs
 */
export async function fetchValidationHistory() {
  try {
    const response = await fetch(`${API_BASE_URL}/validation/history`);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to fetch validation history');
    }
    
    return await response.json();
    
  } catch (error) {
    console.error('Error fetching validation history:', error);
    return [];
  }
}