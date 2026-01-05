/**
 * Technical Indicators Calculator
 * 
 * SIMPLIFIED VERSION - No "indicator soup"
 * Focus on: Trend Structure, Moving Averages, Volume
 * 
 * Removed: RSI scoring, MACD scoring, Bollinger scoring, ADX scoring
 * (These are kept for reference but NOT used in scoring)
 */

/**
 * Calculate Simple Moving Average (SMA)
 * @param {number[]} prices - Array of closing prices
 * @param {number} period - SMA period
 * @returns {number|null} SMA value
 */
export function calculateSMA(prices, period) {
  if (!prices || prices.length < period) return null;
  const slice = prices.slice(-period);
  return slice.reduce((sum, price) => sum + price, 0) / period;
}

/**
 * Calculate Exponential Moving Average (EMA)
 * @param {number[]} prices - Array of closing prices
 * @param {number} period - EMA period
 * @returns {number|null} EMA value
 */
export function calculateEMA(prices, period) {
  if (!prices || prices.length < period) return null;
  
  const k = 2 / (period + 1);
  let ema = prices[0];
  
  for (let i = 1; i < prices.length; i++) {
    ema = prices[i] * k + ema * (1 - k);
  }
  
  return ema;
}

/**
 * Calculate Average True Range (ATR) - Used for stop loss calculation
 * @param {number[]} highs - Array of high prices
 * @param {number[]} lows - Array of low prices
 * @param {number[]} closes - Array of closing prices
 * @param {number} period - ATR period (default 14)
 * @returns {number|null} ATR value
 */
export function calculateATR(highs, lows, closes, period = 14) {
  if (!highs || !lows || !closes || closes.length < period + 1) return null;
  
  const trueRanges = [];
  
  for (let i = 1; i < closes.length; i++) {
    const tr = Math.max(
      highs[i] - lows[i],
      Math.abs(highs[i] - closes[i - 1]),
      Math.abs(lows[i] - closes[i - 1])
    );
    trueRanges.push(tr);
  }
  
  // Calculate ATR as SMA of true ranges
  const recentTR = trueRanges.slice(-period);
  return recentTR.reduce((sum, tr) => sum + tr, 0) / period;
}

/**
 * Calculate Relative Strength Index (RSI)
 * RSI = 100 - (100 / (1 + RS))
 * RS = Average Gain / Average Loss over period
 * 
 * @param {number[]} prices - Array of closing prices
 * @param {number} period - RSI period (default 14)
 * @returns {number|null} RSI value (0-100)
 */
export function calculateRSI(prices, period = 14) {
  if (!prices || prices.length < period + 1) return null;
  
  // Calculate price changes
  const changes = [];
  for (let i = 1; i < prices.length; i++) {
    changes.push(prices[i] - prices[i - 1]);
  }
  
  // Separate gains and losses
  const gains = changes.map(c => c > 0 ? c : 0);
  const losses = changes.map(c => c < 0 ? Math.abs(c) : 0);
  
  // Calculate initial average gain and loss (SMA for first period)
  let avgGain = gains.slice(0, period).reduce((sum, g) => sum + g, 0) / period;
  let avgLoss = losses.slice(0, period).reduce((sum, l) => sum + l, 0) / period;
  
  // Use Wilder's smoothing method for subsequent values
  for (let i = period; i < changes.length; i++) {
    avgGain = (avgGain * (period - 1) + gains[i]) / period;
    avgLoss = (avgLoss * (period - 1) + losses[i]) / period;
  }
  
  // Calculate RS and RSI
  if (avgLoss === 0) {
    return 100; // No losses = RSI is 100
  }
  
  const rs = avgGain / avgLoss;
  const rsi = 100 - (100 / (1 + rs));
  
  return parseFloat(rsi.toFixed(2));
}

/**
 * Analyze Trend Structure (40 points max)
 * This is THE core technical analysis
 * 
 * @param {Object} priceData - Price data from backend
 * @returns {Object} Trend analysis with scores
 */
export function analyzeTrendStructure(priceData) {
  const { closes, highs, lows, volumes } = priceData;
  
  if (!closes || closes.length < 200) {
    return {
      error: 'Insufficient price history for trend analysis',
      totalScore: 0
    };
  }
  
  const currentPrice = closes[closes.length - 1];
  
  // Calculate moving averages
  const sma50 = calculateSMA(closes, 50);
  const sma200 = calculateSMA(closes, 200);
  const ema8 = calculateEMA(closes, 8);
  const ema21 = calculateEMA(closes, 21);
  
  // Calculate average volume
  const avgVolume50 = calculateSMA(volumes, 50);
  const currentVolume = volumes[volumes.length - 1];
  
  // Calculate ATR for trade setup
  const atr = calculateATR(highs, lows, closes, 14);
  
  // ========================================
  // SCORING (40 points total for technical)
  // ========================================
  
  let trendStructureScore = 0;    // Max 15 points
  let shortTermTrendScore = 0;    // Max 10 points
  let volumeScore = 0;            // Max 5 points
  // Note: RS score (10 points) is calculated separately
  
  const analysis = {
    metrics: {},
    scores: {},
    flags: []
  };
  
  // -----------------------------------------
  // 1. TREND STRUCTURE (15 points)
  // Price > 50 SMA > 200 SMA = Stage 2 uptrend
  // -----------------------------------------
  const priceAbove50 = currentPrice > sma50;
  const priceAbove200 = currentPrice > sma200;
  const sma50Above200 = sma50 > sma200;
  
  analysis.metrics.trendStructure = {
    currentPrice,
    sma50,
    sma200,
    priceAbove50,
    priceAbove200,
    sma50Above200,
    isStage2: priceAbove50 && priceAbove200 && sma50Above200
  };
  
  if (priceAbove50 && priceAbove200 && sma50Above200) {
    // Perfect Stage 2 uptrend
    trendStructureScore = 15;
    analysis.flags.push({ type: 'positive', message: 'Stage 2 uptrend confirmed' });
  } else if (priceAbove50 && priceAbove200) {
    // Price above both MAs but not perfectly stacked
    trendStructureScore = 10;
    analysis.flags.push({ type: 'positive', message: 'Price above major moving averages' });
  } else if (priceAbove200) {
    // Only above 200 SMA
    trendStructureScore = 5;
    analysis.flags.push({ type: 'warning', message: 'Above 200 SMA but below 50 SMA' });
  } else {
    // Below 200 SMA - CRITICAL FAIL
    trendStructureScore = 0;
    analysis.flags.push({ type: 'critical', message: 'Below 200 SMA - Not in uptrend' });
  }
  
  analysis.scores.trendStructure = trendStructureScore;
  
  // -----------------------------------------
  // 2. SHORT-TERM TREND (10 points)
  // Price > 8 EMA > 21 EMA
  // -----------------------------------------
  const priceAboveEma8 = currentPrice > ema8;
  const priceAboveEma21 = currentPrice > ema21;
  const ema8AboveEma21 = ema8 > ema21;
  
  analysis.metrics.shortTermTrend = {
    ema8,
    ema21,
    priceAboveEma8,
    priceAboveEma21,
    ema8AboveEma21,
    isShortTermBullish: priceAboveEma8 && ema8AboveEma21
  };
  
  if (priceAboveEma8 && ema8AboveEma21) {
    shortTermTrendScore = 10;
    analysis.flags.push({ type: 'positive', message: 'Short-term momentum bullish' });
  } else if (priceAboveEma21) {
    shortTermTrendScore = 5;
    analysis.flags.push({ type: 'neutral', message: 'Short-term momentum mixed' });
  } else {
    shortTermTrendScore = 0;
    analysis.flags.push({ type: 'warning', message: 'Short-term momentum bearish' });
  }
  
  analysis.scores.shortTermTrend = shortTermTrendScore;
  
  // -----------------------------------------
  // 3. VOLUME (5 points)
  // Current volume > 1.5x 50-day average = accumulation
  // -----------------------------------------
  const volumeRatio = currentVolume / avgVolume50;
  
  analysis.metrics.volume = {
    currentVolume,
    avgVolume50,
    volumeRatio,
    isHighVolume: volumeRatio > 1.5
  };
  
  if (volumeRatio > 2.0) {
    volumeScore = 5;
    analysis.flags.push({ type: 'positive', message: 'Very high volume - strong interest' });
  } else if (volumeRatio > 1.5) {
    volumeScore = 4;
    analysis.flags.push({ type: 'positive', message: 'Above average volume' });
  } else if (volumeRatio > 1.0) {
    volumeScore = 2;
  } else {
    volumeScore = 0;
    analysis.flags.push({ type: 'neutral', message: 'Below average volume' });
  }
  
  analysis.scores.volume = volumeScore;
  
  // -----------------------------------------
  // TOTAL TECHNICAL SCORE (without RS)
  // -----------------------------------------
  const technicalScoreWithoutRS = trendStructureScore + shortTermTrendScore + volumeScore;
  
  analysis.scores.technicalTotal = technicalScoreWithoutRS;
  analysis.scores.maxPossible = 30; // 40 total - 10 for RS which is separate
  
  // -----------------------------------------
  // ATR for trade setup (not scored)
  // -----------------------------------------
  analysis.metrics.atr = {
    value: atr,
    atrPercent: atr ? (atr / currentPrice * 100) : null
  };
  
  // -----------------------------------------
  // Quality Gate: Below 200 SMA
  // -----------------------------------------
  analysis.qualityGate = {
    passes: priceAbove200,
    reason: priceAbove200 
      ? 'Stock is in uptrend (above 200 SMA)' 
      : 'CRITICAL: Stock below 200 SMA - automatic AVOID'
  };
  
  return analysis;
}

/**
 * Calculate trade setup (entry, stop, target)
 * 
 * @param {number} currentPrice - Current stock price
 * @param {number} atr - Average True Range
 * @param {number} accountSize - Trading account size (default $10,000)
 * @returns {Object} Trade setup details
 */
export function calculateTradeSetup(currentPrice, atr, accountSize = 10000) {
  if (!currentPrice || !atr) {
    return { error: 'Insufficient data for trade setup' };
  }
  
  // Stop loss = 1.2x ATR below entry
  const stopLoss = currentPrice - (1.2 * atr);
  const riskPerShare = currentPrice - stopLoss;
  
  // Target = 2:1 reward-to-risk minimum
  const target = currentPrice + (2 * riskPerShare);
  
  // Position sizing (1% account risk)
  const riskAmount = accountSize * 0.01;
  const shares = Math.floor(riskAmount / riskPerShare);
  const positionValue = shares * currentPrice;
  
  return {
    entry: parseFloat(currentPrice.toFixed(2)),
    stopLoss: parseFloat(stopLoss.toFixed(2)),
    target: parseFloat(target.toFixed(2)),
    riskPerShare: parseFloat(riskPerShare.toFixed(2)),
    rewardRisk: 2.0,
    shares,
    positionValue: parseFloat(positionValue.toFixed(2)),
    riskAmount: parseFloat(riskAmount.toFixed(2)),
    atr: parseFloat(atr.toFixed(2)),
    atrMultiplier: 1.2
  };
}

/**
 * Calculate 52-week high proximity
 * Stocks near 52-week high often continue higher
 * 
 * @param {number} currentPrice - Current price
 * @param {number} high52Week - 52-week high price
 * @returns {Object} High proximity analysis
 */
export function calculate52WeekHighProximity(currentPrice, high52Week) {
  if (!currentPrice || !high52Week) return null;
  
  const percentFromHigh = ((currentPrice / high52Week) - 1) * 100;
  const isNearHigh = percentFromHigh > -10; // Within 10% of high
  
  return {
    high52Week,
    percentFromHigh: parseFloat(percentFromHigh.toFixed(2)),
    isNearHigh,
    interpretation: isNearHigh 
      ? 'Near 52-week high - showing strength' 
      : 'More than 10% from high'
  };
}