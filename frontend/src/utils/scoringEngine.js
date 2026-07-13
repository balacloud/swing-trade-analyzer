/**
 * Scoring Engine for Swing Trade Analyzer
 * 75-point scoring system based on Minervini SEPA + CAN SLIM
 *
 * v2.0: Enhanced fundamental scoring with multi-source data (Finnhub, FMP, yfinance)
 * v2.1: Fixed API structure - clean consumer-facing return object (Day 18)
 * v2.2: Day 25 - Added ETF detection and extreme ROE/EPS context
 * v2.3: Day 26 - Fixed ATR calculation (was passing wrong args to calculateATR)
 * v2.4: Day 44 - NOTE: Numerical scoring is now supplementary to v4.5 Categorical Assessment
 *       The categorical system (categoricalAssessment.js) uses breakdown data from this engine
 *       but determines verdicts based on Strong/Decent/Weak categories rather than point totals.
 *       Score correlation to returns = 0.011 (essentially zero), hence the switch to categorical.
 * Day 83: removed determineVerdict() and the returned `verdict` field entirely —
 *       it computed a BUY/HOLD/AVOID from this file's own documented-zero-correlation
 *       score, and its only consumer was a fallback in App.jsx's Verdict Card that
 *       traced to be permanently unreachable (categoricalResult and analysisResult
 *       are always set together, never one without the other). Kept as a fallback,
 *       it was a latent risk: if that invariant ever broke, the UI would have silently
 *       shown the legacy verdict with no indication it wasn't the real one.
 *
 * Scoring Breakdown (Legacy - kept for data extraction):
 * - Technical: 40 points
 * - Fundamental: 20 points (ENHANCED)
 * - Sentiment: 10 points (placeholder - replaced by Fear & Greed in v4.5)
 * - Risk/Macro: 5 points
 */

import { calculateSMA, calculateEMA, calculateATR, calculateRSI } from './technicalIndicators';
import { calculateRelativeStrength } from './rsCalculator';
import { getLiquidityThreshold } from './liquidityThresholds';

// Day 25: Known ETF tickers - these don't have traditional fundamentals
const ETF_TICKERS = ['SPY', 'QQQ', 'IWM', 'DIA', 'VOO', 'VTI', 'VEA', 'VWO', 'VNQ',
                     'BND', 'AGG', 'GLD', 'SLV', 'USO', 'XLF', 'XLK', 'XLE', 'XLV',
                     'XLI', 'XLP', 'XLY', 'XLB', 'XLU', 'ARKK', 'ARKG', 'ARKW'];

/**
 * Day 25: Check if ticker is an ETF
 */
function isETF(ticker) {
  return ETF_TICKERS.includes(ticker?.toUpperCase());
}

/**
 * Day 25: Get context for extreme ROE/EPS values
 * Returns explanation for values that might confuse users
 */
function getExtremeValueContext(fundamentals) {
  const context = [];

  const roe = fundamentals?.roe;
  const eps = fundamentals?.epsGrowth;
  const debtToEquity = fundamentals?.debtToEquity;

  // Negative ROE
  if (roe !== null && roe !== undefined && roe < 0) {
    context.push({
      metric: 'ROE',
      value: roe,
      explanation: 'Negative ROE indicates negative shareholder equity (often from share buybacks or accumulated losses)'
    });
  }

  // Very high ROE (>100%)
  if (roe !== null && roe !== undefined && roe > 100) {
    context.push({
      metric: 'ROE',
      value: roe,
      explanation: 'Very high ROE often indicates low equity base (from buybacks/dividends) or temporary earnings spike'
    });
  }

  // Extreme EPS growth (>200% or < -100%)
  if (eps !== null && eps !== undefined && (eps > 200 || eps < -100)) {
    context.push({
      metric: 'EPS Growth',
      value: eps,
      explanation: eps > 200
        ? 'Extreme EPS growth often indicates recovery from prior losses or one-time gains'
        : 'Large EPS decline may be temporary or indicate fundamental issues'
    });
  }

  // Negative debt to equity
  if (debtToEquity !== null && debtToEquity !== undefined && debtToEquity < 0) {
    context.push({
      metric: 'Debt/Equity',
      value: debtToEquity,
      explanation: 'Negative D/E indicates negative equity (more liabilities than assets or aggressive buybacks)'
    });
  }

  return context;
}

/**
 * Calculate all technical indicators from price data
 * Day 26: Fixed ATR calculation - now receives highs/lows/closes properly
 */
function getIndicators(prices, volumes, highs, lows) {
  if (!prices || prices.length < 200) {
    return null;
  }

  return {
    sma50: calculateSMA(prices, 50),
    sma200: calculateSMA(prices, 200),
    ema8: calculateEMA(prices, 8),
    ema21: calculateEMA(prices, 21),
    atr: calculateATR(highs, lows, prices, 14),  // Day 26: Fixed - was passing wrong args
    rsi: calculateRSI(prices, 14),
    avgVolume50: volumes.slice(-50).reduce((a, b) => a + b, 0) / 50
  };
}

/**
 * Calculate Technical Analysis Score (40 points)
 * Day 26: Now extracts highs/lows for proper ATR calculation
 */
function calculateTechnicalScore(stockData, spyData) {
  const prices = stockData.priceHistory.map(d => d.close);
  const volumes = stockData.priceHistory.map(d => d.volume);
  const highs = stockData.priceHistory.map(d => d.high);    // Day 26: Added for ATR
  const lows = stockData.priceHistory.map(d => d.low);      // Day 26: Added for ATR

  if (prices.length < 50) {
    return { score: 0, maxScore: 40, details: {}, error: 'Insufficient price data' };
  }

  const indicators = getIndicators(prices, volumes, highs, lows);  // Day 26: Pass highs/lows
  const currentPrice = prices[prices.length - 1];
  
  let scores = {
    trendStructure: 0,
    shortTermTrend: 0,
    volume: 0,
    rs: 0
  };
  
  // 1. Trend Structure (15 points): Price > 50 SMA > 200 SMA
  if (indicators.sma50 && indicators.sma200) {
    if (currentPrice > indicators.sma50 && indicators.sma50 > indicators.sma200) {
      scores.trendStructure = 15; // Perfect Stage 2 uptrend
    } else if (currentPrice > indicators.sma200) {
      scores.trendStructure = 5; // Above 200 SMA but not ideal structure
    }
  }
  
  // 2. Short-term Trend (10 points): Price > 8 EMA > 21 EMA
  if (indicators.ema8 && indicators.ema21) {
    if (currentPrice > indicators.ema8 && indicators.ema8 > indicators.ema21) {
      scores.shortTermTrend = 10; // Strong short-term momentum
    } else if (currentPrice > indicators.ema21) {
      scores.shortTermTrend = 3; // Above 21 EMA
    }
  }
  
  // 3. Volume (5 points): Recent volume vs 50-day average
  if (indicators.avgVolume50) {
    const recentVolume = volumes.slice(-5).reduce((a, b) => a + b, 0) / 5;
    const volumeRatio = recentVolume / indicators.avgVolume50;
    
    if (volumeRatio >= 1.5) {
      scores.volume = 5; // High volume interest
    } else if (volumeRatio >= 1.0) {
      scores.volume = 2; // Normal volume
    }
  }
  
  // 4. Relative Strength (10 points)
  const rsData = calculateRelativeStrength(stockData, spyData);
  if (rsData && rsData.rs52Week) {
    if (rsData.rs52Week >= 1.5) {
      scores.rs = 10; // Strong outperformance
    } else if (rsData.rs52Week >= 1.2) {
      scores.rs = 7; // Good outperformance
    } else if (rsData.rs52Week >= 1.0) {
      scores.rs = 4; // Slight outperformance
    } else if (rsData.rs52Week >= 0.8) {
      scores.rs = 1; // Slight underperformance
    }
  }
  
  const totalScore = scores.trendStructure + scores.shortTermTrend + scores.volume + scores.rs;
  
  return {
    score: totalScore,
    maxScore: 40,
    details: {
      trendStructure: { score: scores.trendStructure, max: 15 },
      shortTermTrend: { score: scores.shortTermTrend, max: 10 },
      volume: { score: scores.volume, max: 5 },
      relativeStrength: { score: scores.rs, max: 10 }
    },
    indicators: indicators,
    rsData: rsData
  };
}

/**
 * Calculate Fundamental Score (20 points)
 * ENHANCED with multi-source data (ROE, ROIC, EPS Growth, etc.)
 * Day 25: Added ETF detection and extreme value context
 */
function calculateFundamentalScore(fundamentals, ticker) {
  let scores = {
    epsGrowth: 0,
    revenueGrowth: 0,
    roe: 0,
    debtToEquity: 0,
    forwardPe: 0
  };

  let dataSource = fundamentals?.enrichedSource || fundamentals?.source || 'unknown';
  let dataQuality = 'limited';
  let isEtfTicker = isETF(ticker);
  let extremeContext = [];
  let dataUnavailableReason = null;

  // Day 25: Handle ETF tickers specially
  if (isEtfTicker) {
    return {
      score: 0,
      maxScore: 20,
      details: {
        epsGrowth: { score: 0, max: 6, value: null },
        revenueGrowth: { score: 0, max: 5, value: null },
        roe: { score: 0, max: 4, value: null },
        debtToEquity: { score: 0, max: 3, value: null },
        forwardPe: { score: 0, max: 2, value: null }
      },
      dataSource: 'N/A',
      dataQuality: 'N/A',
      isETF: true,
      etfNote: 'ETFs do not have traditional fundamentals (EPS, ROE, etc.). Score based on technical analysis only.'
    };
  }

  // v4.14: Check data quality from multi-source provider system
  if (fundamentals?.dataQuality === 'unavailable') {
    dataQuality = 'unavailable';
    dataUnavailableReason = 'All data providers failed (Finnhub, AlphaVantage, yfinance). Fundamental score may be incomplete.';
  } else if (fundamentals?.dataQuality === 'yfinance_fallback' || fundamentals?.fallbackUsed) {
    dataQuality = 'fallback';
    dataUnavailableReason = 'Primary providers unavailable. Using yfinance fallback with limited data.';
  } else if (fundamentals?.enriched || fundamentals?.source === 'defeatbeta' || fundamentals?.source === 'finnhub' || fundamentals?.source === 'fmp' || fundamentals?.source === 'alphavantage' || fundamentals?.source === 'multi') {
    // Rich data from multi-source providers (Finnhub, AlphaVantage, or merged)
    dataQuality = 'rich';
  }

  // Day 31: Also detect all-null fundamentals (provider failed silently)
  const keyFields = ['roe', 'epsGrowth', 'revenueGrowth', 'debtToEquity'];
  const allNull = keyFields.every(field => fundamentals?.[field] === null || fundamentals?.[field] === undefined);
  if (allNull && dataQuality !== 'unavailable') {
    dataQuality = 'unavailable';
    dataUnavailableReason = 'Fundamental data temporarily unavailable for this stock.';
  }

  // Day 25: Get context for extreme values
  extremeContext = getExtremeValueContext(fundamentals);
  
  // 1. EPS Growth (6 points)
  // Target: >25% YoY = 6pts, 15-25% = 4pts, 10-15% = 2pts
  const epsGrowth = fundamentals?.epsGrowth;
  if (epsGrowth !== null && epsGrowth !== undefined && epsGrowth !== 0) {
    if (epsGrowth >= 25) {
      scores.epsGrowth = 6;
    } else if (epsGrowth >= 15) {
      scores.epsGrowth = 4;
    } else if (epsGrowth >= 10) {
      scores.epsGrowth = 2;
    } else if (epsGrowth > 0) {
      scores.epsGrowth = 1;
    }
  }
  
  // 2. Revenue Growth (5 points)
  // Target: >20% = 5pts, 10-20% = 3pts, 5-10% = 1pt
  const revenueGrowth = fundamentals?.revenueGrowth;
  if (revenueGrowth !== null && revenueGrowth !== undefined && revenueGrowth !== 0) {
    if (revenueGrowth >= 20) {
      scores.revenueGrowth = 5;
    } else if (revenueGrowth >= 10) {
      scores.revenueGrowth = 3;
    } else if (revenueGrowth >= 5) {
      scores.revenueGrowth = 1;
    }
  }
  
  // 3. ROE (4 points)
  // Target: >15% = 4pts, 10-15% = 2pts
  const roe = fundamentals?.roe;
  if (roe !== null && roe !== undefined && roe !== 0) {
    if (roe >= 15) {
      scores.roe = 4;
    } else if (roe >= 10) {
      scores.roe = 2;
    } else if (roe > 0) {
      scores.roe = 1;
    }
  }
  
  // 4. Debt/Equity (3 points)
  // Target: <1.0 = 3pts, 1.0-1.5 = 1pt
  const debtToEquity = fundamentals?.debtToEquity;
  if (debtToEquity !== null && debtToEquity !== undefined) {
    if (debtToEquity < 0.5) {
      scores.debtToEquity = 3; // Very low debt
    } else if (debtToEquity < 1.0) {
      scores.debtToEquity = 2;
    } else if (debtToEquity < 1.5) {
      scores.debtToEquity = 1;
    }
  }
  
  // 5. Forward P/E (2 points)
  // Target: <20 = 2pts, 20-25 = 1pt (reasonable valuation)
  const forwardPe = fundamentals?.forwardPe;
  if (forwardPe !== null && forwardPe !== undefined && forwardPe > 0) {
    if (forwardPe < 20) {
      scores.forwardPe = 2;
    } else if (forwardPe < 25) {
      scores.forwardPe = 1;
    }
  }
  
  const totalScore = scores.epsGrowth + scores.revenueGrowth + scores.roe + 
                     scores.debtToEquity + scores.forwardPe;
  
  return {
    score: totalScore,
    maxScore: 20,
    details: {
      epsGrowth: { score: scores.epsGrowth, max: 6, value: epsGrowth },
      revenueGrowth: { score: scores.revenueGrowth, max: 5, value: revenueGrowth },
      roe: { score: scores.roe, max: 4, value: roe },
      debtToEquity: { score: scores.debtToEquity, max: 3, value: debtToEquity },
      forwardPe: { score: scores.forwardPe, max: 2, value: forwardPe }
    },
    dataSource: dataSource,
    dataQuality: dataQuality,
    dataUnavailableReason: dataUnavailableReason,  // Day 31: Explanation when data unavailable
    isETF: false,
    extremeValueContext: extremeContext  // Day 25: Context for unusual values
  };
}

/**
 * Calculate Sentiment Score (10 points)
 * NOT IMPLEMENTED in legacy scoring — returns 0/10 (honest).
 * Real sentiment analysis uses CNN Fear & Greed Index in
 * categoricalAssessment.js → assessSentiment().
 */
function calculateSentimentScore() {
  return {
    score: 0,
    maxScore: 10,
    details: {
      newsScore: { score: 0, max: 10 }
    },
    note: 'Not scored here — real sentiment via categorical assessment (Fear & Greed Index)'
  };
}

/**
 * Calculate Risk/Macro Score (5 points)
 */
function calculateRiskScore(spyData, vixData) {
  let scores = {
    vix: 0,
    spyRegime: 0,
    breadth: 0
  };
  
  // 1. VIX Level (2 points)
  const vix = vixData?.current;
  if (vix !== null && vix !== undefined) {
    if (vix < 15) {
      scores.vix = 2; // Low volatility - favorable
    } else if (vix < 20) {
      scores.vix = 1; // Normal volatility
    }
    // VIX > 20 = 0 points (elevated risk)
  }
  
  // 2. S&P 500 Regime (2 points)
  if (spyData?.aboveSma200) {
    scores.spyRegime = 2; // Bullish market regime
  }
  
  // 3. Market Breadth (1 point) - NOT IMPLEMENTED
  // Would need % of stocks above 50 SMA — no data source available.
  // Returns 0 (honest) instead of hardcoded 1 that inflated every score.
  scores.breadth = 0;
  
  const totalScore = scores.vix + scores.spyRegime + scores.breadth;
  
  return {
    score: totalScore,
    maxScore: 5,
    details: {
      vix: { score: scores.vix, max: 2, value: vix },
      spyRegime: { score: scores.spyRegime, max: 2, aboveSma200: spyData?.aboveSma200 },
      breadth: { score: scores.breadth, max: 1 }
    }
  };
}

/**
 * Check Quality Gates (Auto-AVOID triggers)
 */
function checkQualityGates(stockData, spyData, technicalResult) {
  const gates = [];
  const rsData = technicalResult?.rsData;
  const indicators = technicalResult?.indicators;
  const prices = stockData.priceHistory.map(d => d.close);
  const currentPrice = prices[prices.length - 1];
  
  // 1. RS below 0.8 (significant underperformance)
  // Day 83 fix: previously `rsData?.rs52Week && ...` silently skipped this
  // gate entirely whenever rs52Week was null/undefined (uncomputable) — a
  // stock with genuinely missing RS data raised no warning at all, the
  // opposite of what a quality gate should do on missing data. Now flags it
  // as a non-critical, informational gate entry instead of staying silent.
  if (rsData?.rs52Week != null) {
    if (rsData.rs52Week < 0.8) {
      gates.push({
        name: 'RS Below Threshold',
        value: rsData.rs52Week.toFixed(2),
        threshold: '< 0.8',
        critical: true
      });
    }
  } else {
    gates.push({
      name: 'RS Unavailable',
      value: 'N/A',
      threshold: 'data missing',
      critical: false
    });
  }

  // 2. Stock below 200 SMA (downtrend)
  if (indicators?.sma200 && currentPrice < indicators.sma200) {
    gates.push({
      name: 'Below 200 SMA',
      value: `$${currentPrice.toFixed(2)}`,
      threshold: `> $${indicators.sma200.toFixed(2)}`,
      critical: true
    });
  }

  // 3. Illiquid for its cap tier (Day 70B cap-aware threshold)
  // Day 83 fix: was a flat $10M cutoff regardless of market cap — inconsistent
  // with the Simple Checklist's cap-aware tiers ($2M small / $5M mid / $10M
  // large), so the same stock's liquidity could pass here and fail there (or
  // vice versa). Now sourced from the same shared threshold both views use.
  const marketCap = stockData.fundamentals?.marketCap || stockData.marketCap || 0;
  const { threshold: liquidityThreshold, label: liquidityLabel } = getLiquidityThreshold(marketCap);
  const avgVolume = stockData.avgVolume || 0;
  const avgDollarVolume = avgVolume * currentPrice;
  if (avgDollarVolume < liquidityThreshold) {
    gates.push({
      name: 'Low Liquidity',
      value: `$${(avgDollarVolume / 1000000).toFixed(1)}M`,
      threshold: `> ${liquidityLabel}`,
      critical: true
    });
  }
  
  // Count critical failures
  const criticalFails = gates.filter(g => g.critical).length;
  
  return {
    passed: criticalFails === 0,
    gates: gates,
    criticalFails: criticalFails
  };
}

/**
 * Main scoring function
 * Calculates complete analysis for a stock
 * 
 * v2.1: Returns a clean, consumer-facing API structure
 */
export function calculateScore(stockData, spyData, vixData) {
  // Calculate individual scores
  const technicalAnalysis = calculateTechnicalScore(stockData, spyData);
  const fundamentalAnalysis = calculateFundamentalScore(stockData.fundamentals, stockData.ticker);  // Day 25: Pass ticker for ETF detection
  const sentimentAnalysis = calculateSentimentScore();
  const riskAnalysis = calculateRiskScore(spyData, vixData);
  
  // Total score
  const totalScore = technicalAnalysis.score + fundamentalAnalysis.score + 
                     sentimentAnalysis.score + riskAnalysis.score;
  
  // Quality gates
  const qualityGates = checkQualityGates(stockData, spyData, technicalAnalysis);

  // Get RS data for clean API
  const rsData = technicalAnalysis.rsData || {};
  
  // Calculate % from 52-week high
  const fiftyTwoWeekHigh = stockData.fiftyTwoWeekHigh;
  const fiftyTwoWeekLow = stockData.fiftyTwoWeekLow;
  const currentPrice = stockData.currentPrice;
  const pctFromHigh = fiftyTwoWeekHigh ? 
    ((currentPrice - fiftyTwoWeekHigh) / fiftyTwoWeekHigh) * 100 : null;
  
  // =========================================================
  // CLEAN API RETURN STRUCTURE (v2.1)
  // UI can consume this directly without knowing internals
  // =========================================================
  return {
    // Basic info
    ticker: stockData.ticker,
    name: stockData.name,
    sector: stockData.sector,
    industry: stockData.industry,
    
    // Price data (for UI display)
    currentPrice: currentPrice,
    fiftyTwoWeekHigh: fiftyTwoWeekHigh,
    fiftyTwoWeekLow: fiftyTwoWeekLow,
    pctFromHigh: pctFromHigh,
    
    // Scores - FLAT structure for easy UI consumption
    totalScore: totalScore,
    maxScore: 75,
    scores: {
      technical: technicalAnalysis.score,
      fundamental: fundamentalAnalysis.score,
      sentiment: sentimentAnalysis.score,
      risk: riskAnalysis.score
    },
    
    qualityGates: qualityGates,
    
    // RS Data - Normalized field names for UI
    rsData: {
      rsRatio: rsData.rs52Week,              // UI expects rsRatio
      rs52Week: rsData.rs52Week,
      rs13Week: rsData.rs13Week,
      rsRating: rsData.rsRating,
      rsTrend: rsData.rsTrend,
      stock52wReturn: rsData.stockReturn52w,  // UI expects stock52wReturn
      spy52wReturn: rsData.spyReturn52w,      // UI expects spy52wReturn
      interpretation: rsData.interpretation,
      passesQualityGate: rsData.passesQualityGate,
      // Tier 2B: Blended RS — informational only, NOT used for verdicts
      rsBlended: rsData.rsBlended || null,
      rs21d: rsData.rs21d || null,
      rs63d: rsData.rs63d || null,
      rs126d: rsData.rs126d || null,
    },
    
    // Technical indicators
    indicators: technicalAnalysis.indicators,
    
    // Detailed breakdown (for debugging/advanced UI)
    breakdown: {
      technical: technicalAnalysis,
      fundamental: fundamentalAnalysis,
      sentiment: sentimentAnalysis,
      risk: riskAnalysis
    },
    
    // Metadata
    timestamp: new Date().toISOString()
  };
}