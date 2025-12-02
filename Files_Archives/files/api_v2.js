/**
 * API Service for Swing Trade Analyzer
 * Connects to Flask backend on port 5001
 * 
 * v2.0: Added fundamentals endpoint for rich fundamental data
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
