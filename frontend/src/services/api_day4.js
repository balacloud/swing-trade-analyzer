/**
 * API Service Layer
 * Connects React frontend to Flask backend (port 5001)
 * 
 * IMPORTANT: This transforms the backend response format to match
 * what the frontend scoring engine expects.
 */

const API_BASE = 'http://localhost:5001/api';

/**
 * Fetch stock data from backend and transform to expected format
 * @param {string} ticker - Stock symbol (e.g., 'AAPL')
 * @returns {Promise<Object>} Stock data with prices, fundamentals, etc.
 */
export async function fetchStockData(ticker) {
  try {
    const response = await fetch(`${API_BASE}/stock/${ticker.toUpperCase()}`);
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `Failed to fetch ${ticker}`);
    }
    
    const data = await response.json();
    
    // Transform backend response to frontend expected format
    return transformStockData(data);
  } catch (error) {
    console.error(`Error fetching stock data for ${ticker}:`, error);
    throw error;
  }
}

/**
 * Transform backend stock data to frontend format
 * 
 * Backend returns:
 *   - priceHistory: array of closing prices
 *   - highs: array at top level
 *   - lows: array at top level
 *   - volumes: array at top level
 * 
 * Frontend expects:
 *   - priceHistory: { closes: [], highs: [], lows: [], volumes: [] }
 *   - price52WeeksAgo, price13WeeksAgo for RS calculation
 */
function transformStockData(data) {
  const closes = data.priceHistory || [];
  const highs = data.highs || [];
  const lows = data.lows || [];
  const volumes = data.volumes || [];
  
  // Calculate prices from N weeks ago for RS calculation
  // We have ~200 data points, need to find 52 weeks (~252 trading days) and 13 weeks (~65 days)
  // Since we only have 200 points, use what we have
  const price52WeeksAgo = closes.length >= 200 
    ? closes[0]  // Oldest price (approximately 52 weeks ago with 200 data points)
    : closes[0];
    
  const price13WeeksAgo = closes.length >= 65 
    ? closes[closes.length - 65] 
    : closes[Math.floor(closes.length * 0.25)]; // ~25% from end
  
  return {
    ticker: data.ticker,
    currentPrice: data.currentPrice,
    avgVolume: data.avgVolume,
    dataPoints: data.dataPoints,
    dataSource: data.dataSource,
    lastUpdated: data.lastUpdated,
    
    // Prices for RS calculation
    price52WeeksAgo: price52WeeksAgo,
    price13WeeksAgo: price13WeeksAgo,
    
    // Price history in the format the scoring engine expects
    priceHistory: {
      closes: closes,
      highs: highs,
      lows: lows,
      volumes: volumes,
      dates: data.dates || []
    },
    
    // Fundamentals (pass through as-is)
    fundamentals: data.fundamentals || {}
  };
}

/**
 * Fetch SPY (S&P 500) data for Relative Strength calculation
 * @returns {Promise<Object>} SPY data with current price and historical prices
 */
export async function fetchSPYData() {
  try {
    const response = await fetch(`${API_BASE}/market/spy`);
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to fetch SPY data');
    }
    
    const data = await response.json();
    
    // Transform SPY data to match expected format
    return transformSPYData(data);
  } catch (error) {
    console.error('Error fetching SPY data:', error);
    throw error;
  }
}

/**
 * Transform SPY data to frontend format
 * 
 * Backend returns: price52wAgo, price13wAgo (lowercase 'w')
 * Frontend expects: price52WeeksAgo, price13WeeksAgo (camelCase)
 */
function transformSPYData(data) {
  return {
    ticker: 'SPY',
    currentPrice: data.currentPrice,
    // Map backend field names to frontend expected names
    price52WeeksAgo: data.price52wAgo,   // Backend uses 'price52wAgo'
    price13WeeksAgo: data.price13wAgo,   // Backend uses 'price13wAgo'
    sma200: data.sma200 || null,
    priceHistory: data.priceHistory || [],
    lastUpdated: data.lastUpdated
  };
}

/**
 * Check if backend is healthy
 * @returns {Promise<boolean>} True if backend is running
 */
export async function checkHealth() {
  try {
    const response = await fetch(`${API_BASE}/health`);
    return response.ok;
  } catch (error) {
    console.error('Backend health check failed:', error);
    return false;
  }
}

/**
 * Fetch both stock and SPY data in parallel
 * @param {string} ticker - Stock symbol
 * @returns {Promise<Object>} Combined stock and SPY data
 */
export async function fetchAnalysisData(ticker) {
  try {
    const [stockData, spyData] = await Promise.all([
      fetchStockData(ticker),
      fetchSPYData()
    ]);
    
    console.log('Stock data transformed:', {
      ticker: stockData.ticker,
      currentPrice: stockData.currentPrice,
      price52WeeksAgo: stockData.price52WeeksAgo,
      closesLength: stockData.priceHistory?.closes?.length,
      hasFundamentals: !!stockData.fundamentals
    });
    
    console.log('SPY data:', {
      currentPrice: spyData.currentPrice,
      price52WeeksAgo: spyData.price52WeeksAgo
    });
    
    return {
      stock: stockData,
      spy: spyData,
      fetchedAt: new Date().toISOString()
    };
  } catch (error) {
    console.error('Error fetching analysis data:', error);
    throw error;
  }
}