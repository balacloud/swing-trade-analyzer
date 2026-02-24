/**
 * API Service for Swing Trade Analyzer
 * Connects to Flask backend on port 5001
 *
 * v2.0: Added fundamentals endpoint for rich fundamental data
 * v2.1: Added TradingView screener endpoints for batch scanning
 * v2.2: Added Support & Resistance endpoint
 * v2.3: Added Validation Engine endpoints (Day 17)
 * v2.4: Added Cache Management endpoints (Day 29)
 * v2.5: Added Pattern Detection endpoint (Day 44)
 * v2.6: Added Fear & Greed Index endpoint (Day 44 - v4.5 Categorical Assessment)
 * v2.7: Added Earnings Calendar endpoint (Day 49 - v4.10)
 * v2.8: Added Sector Rotation endpoint (Day 58 - v4.19)
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
    // NOTE: fundamentals are NOT included here (SRP).
    // Single source of truth: /api/fundamentals/ via DataProvider.
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
 * Uses multi-source providers (Finnhub, FMP, yfinance) with fallback chain
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
      sma50Declining: data.sma50Declining || false,  // Day 57: early bear indicator
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
    // Return null VIX — let assessRiskMacro() handle missing data honestly
    // instead of pretending VIX is 20 (normal).
    return {
      ticker: 'VIX',
      current: null,
      regime: 'unknown',
      isRisky: null,
      fallback: true
    };
  }
}

/**
 * Check backend health
 * v4.14: Multi-Source Data Provider status
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
      dataProviderAvailable: data.data_provider_available || false,
      providers: data.providers || null,
      tradingviewAvailable: data.tradingview_available,
      srEngineAvailable: data.sr_engine_available,
      validationAvailable: data.validation_available,
      cacheSize: data.cache_size,
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
    
    // Attach fundamentals to stock data (single source: /api/fundamentals/)
    if (fundamentals) {
      stockData.fundamentals = {
        ...fundamentals,
        enriched: true,
        enrichedSource: fundamentals.source
      };
    } else {
      // Fundamentals fetch failed — mark explicitly so scoring engine
      // returns dataQuality: 'unavailable' instead of scoring null fields.
      stockData.fundamentals = {
        dataQuality: 'unavailable',
        enriched: false
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
 * @param {string} strategy - 'reddit', 'minervini', 'momentum', 'value', 'best'
 * @param {number} limit - max results (default 50, max 100)
 * @param {string} marketIndex - 'all', 'sp500', 'nasdaq100', 'dow30'
 * @returns {object} - { strategy, marketIndex, totalMatches, returned, candidates[] }
 */
export async function fetchScanResults(strategy = 'reddit', limit = 50, marketIndex = 'all') {
  try {
    const response = await fetch(
      `${API_BASE_URL}/scan/tradingview?strategy=${strategy}&limit=${limit}&market_index=${marketIndex}`
    );

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to scan for candidates');
    }

    const data = await response.json();

    return {
      strategy: data.strategy,
      marketIndex: data.marketIndex,
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
 * Fetch analysis data WITH Support & Resistance + Pattern Detection + Fear & Greed + Earnings
 * Enhanced version that includes S&R levels, patterns, sentiment, and earnings in parallel
 * v4.5: Added Fear & Greed Index for categorical assessment
 * v4.10: Added Earnings Calendar for event risk warning
 */
export async function fetchFullAnalysisData(ticker) {
  try {
    const [stockData, fundamentals, spyData, vixData, srData, patterns, fearGreed, earnings, sectorData] = await Promise.all([
      fetchStockData(ticker),
      fetchFundamentals(ticker),
      fetchSPYData(),
      fetchVIXData(),
      fetchSupportResistance(ticker),
      fetchPatterns(ticker),
      fetchFearGreed(),
      fetchEarnings(ticker),
      fetchSectorRotation()  // Day 58: Fetch sector rotation (cached per trading day)
    ]);

    // Attach fundamentals to stock data (single source: /api/fundamentals/)
    if (fundamentals) {
      stockData.fundamentals = {
        ...fundamentals,
        enriched: true,
        enrichedSource: fundamentals.source
      };
    } else {
      // Fundamentals fetch failed — mark explicitly so scoring engine
      // returns dataQuality: 'unavailable' instead of scoring null fields.
      stockData.fundamentals = {
        dataQuality: 'unavailable',
        enriched: false
      };
    }

    return {
      stock: stockData,
      spy: spyData,
      vix: vixData,
      fundamentals: fundamentals,
      sr: srData,
      patterns: patterns,
      fearGreed: fearGreed,
      earnings: earnings,
      sectorRotation: sectorData  // Day 58: Sector rotation data
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

// ============================================
// CACHE MANAGEMENT (Day 29)
// ============================================

/**
 * Clear backend cache to ensure fresh data
 * Use at start of session or when data seems stale
 *
 * @returns {object} - { success, message, cleared_count }
 */
export async function clearBackendCache() {
  try {
    const response = await fetch(`${API_BASE_URL}/cache/clear`, {
      method: 'POST'
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to clear cache');
    }

    return await response.json();

  } catch (error) {
    console.error('Error clearing cache:', error);
    throw error;
  }
}

/**
 * Get cache status
 * @returns {object} - { cache_size, ttl_seconds }
 */
export async function getCacheStatus() {
  try {
    const response = await fetch(`${API_BASE_URL}/cache/status`);

    if (!response.ok) {
      return { cache_size: 0, error: 'Failed to get cache status' };
    }

    return await response.json();

  } catch (error) {
    console.error('Error getting cache status:', error);
    return { cache_size: 0, error: error.message };
  }
}

// ============================================
// DATA PROVENANCE (Day 38)
// ============================================

/**
 * Fetch data source provenance for a ticker
 * Shows where each data point comes from, cache status, and calculation formulas
 *
 * @param {string} ticker - Stock ticker symbol
 * @returns {object} - Provenance info with sources, cache status, and formulas
 */
export async function fetchDataProvenance(ticker) {
  try {
    const response = await fetch(`${API_BASE_URL}/provenance/${ticker.toUpperCase()}`);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || `Failed to fetch provenance for ${ticker}`);
    }

    return await response.json();

  } catch (error) {
    console.error('Error fetching data provenance:', error);
    return null;
  }
}

// ============================================
// PATTERN DETECTION (Day 44 - v4.2)
// ============================================

/**
 * Fetch pattern detection results for a ticker
 * Detects VCP, Cup & Handle, and Flat Base patterns
 * Also includes Minervini's Trend Template check
 *
 * @param {string} ticker - Stock ticker symbol
 * @returns {object} - Pattern detection results
 */
export async function fetchPatterns(ticker) {
  try {
    const response = await fetch(`${API_BASE_URL}/patterns/${ticker.toUpperCase()}`);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || `Failed to fetch patterns for ${ticker}`);
    }

    const data = await response.json();

    return {
      ticker: data.ticker,
      dataPoints: data.data_points,
      analysisDate: data.analysis_date,
      patterns: {
        vcp: data.patterns.vcp,
        cupHandle: data.patterns.cup_handle,
        flatBase: data.patterns.flat_base
      },
      summary: {
        patternsDetected: data.summary.patterns_detected,
        count: data.summary.count,
        bestPattern: data.summary.best_pattern,
        bestConfidence: data.summary.best_confidence
      },
      trendTemplate: data.trend_template
    };

  } catch (error) {
    console.error('Error fetching patterns:', error);
    return null;
  }
}

// ============================================
// FEAR & GREED INDEX (Day 44 - v4.5 Categorical Assessment)
// ============================================

/**
 * Fetch CNN Fear & Greed Index for sentiment assessment
 * Part of v4.5 Categorical Assessment System
 *
 * @returns {object} - Fear & Greed data with value, rating, assessment
 */
export async function fetchFearGreed() {
  try {
    const response = await fetch(`${API_BASE_URL}/fear-greed`);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to fetch Fear & Greed Index');
    }

    const data = await response.json();

    return {
      value: data.value,
      rating: data.rating,
      assessment: data.assessment,
      timestamp: data.timestamp,
      previousClose: data.previousClose,
      source: data.source,
      error: data.error || null
    };

  } catch (error) {
    console.error('Error fetching Fear & Greed Index:', error);
    // Return null — let categorical assessment handle "no data" honestly
    // instead of pretending we have neutral sentiment.
    // assessSentiment() checks for null and returns gray "Neutral" with
    // "data unavailable" reason, which is the honest answer.
    return null;
  }
}

// ============================================
// EARNINGS CALENDAR (Day 49 - v4.10)
// ============================================

/**
 * Fetch earnings calendar for a ticker
 * Warns about upcoming earnings to avoid event/gap risk
 * Part of v4.10 Earnings Calendar Warning
 *
 * @param {string} ticker - Stock ticker symbol
 * @param {number} days - Warning window in days (default 7)
 * @returns {object} - Earnings info with warning if applicable
 */
export async function fetchEarnings(ticker, days = 7) {
  try {
    const response = await fetch(`${API_BASE_URL}/earnings/${ticker.toUpperCase()}?days=${days}`);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || `Failed to fetch earnings for ${ticker}`);
    }

    const data = await response.json();

    return {
      ticker: data.ticker,
      hasUpcoming: data.has_upcoming,
      earningsDate: data.earnings_date,
      daysUntil: data.days_until,
      warning: data.warning,
      recommendation: data.recommendation,
      source: data.source
    };

  } catch (error) {
    console.error('Error fetching earnings:', error);
    // Return safe default on error
    return {
      ticker: ticker,
      hasUpcoming: false,
      earningsDate: null,
      daysUntil: null,
      warning: null,
      recommendation: 'Could not fetch earnings data',
      source: null,
      error: error.message
    };
  }
}

// ============================================
// SECTOR ROTATION (Day 58 - v4.19)
// ============================================

/**
 * Fetch sector rotation data for all 11 SPDR sector ETFs
 * Returns RS ratio vs SPY and RRG quadrant classification
 *
 * @returns {object} - { sectors[], mapping, sectorCount, timestamp }
 */
export async function fetchSectorRotation() {
  try {
    const response = await fetch(`${API_BASE_URL}/sectors/rotation`);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to fetch sector rotation data');
    }

    const data = await response.json();

    return {
      sectors: data.sectors || [],
      sectorCount: data.sectorCount,
      mapping: data.mapping || {},
      timestamp: data.timestamp,
      period: data.period,
    };

  } catch (error) {
    console.error('Error fetching sector rotation:', error);
    return null;
  }
}