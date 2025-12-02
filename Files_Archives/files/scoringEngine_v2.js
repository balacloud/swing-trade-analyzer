/**
 * Scoring Engine for Swing Trade Analyzer
 * 75-point scoring system based on Minervini SEPA + CAN SLIM
 * 
 * v2.0: Enhanced fundamental scoring with Defeat Beta data
 * 
 * Scoring Breakdown:
 * - Technical: 40 points
 * - Fundamental: 20 points (ENHANCED)
 * - Sentiment: 10 points (placeholder)
 * - Risk/Macro: 5 points
 */

import { calculateIndicators } from './technicalIndicators';
import { calculateRS } from './rsCalculator';

/**
 * Calculate Technical Analysis Score (40 points)
 */
function calculateTechnicalScore(stockData, spyData) {
  const prices = stockData.priceHistory.map(d => d.close);
  const volumes = stockData.priceHistory.map(d => d.volume);
  
  if (prices.length < 50) {
    return { score: 0, maxScore: 40, details: {}, error: 'Insufficient price data' };
  }
  
  const indicators = calculateIndicators(prices, volumes);
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
  const rsData = calculateRS(stockData, spyData);
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
 * ENHANCED with Defeat Beta data (ROE, ROIC, EPS Growth, etc.)
 */
function calculateFundamentalScore(fundamentals) {
  let scores = {
    epsGrowth: 0,
    revenueGrowth: 0,
    roe: 0,
    debtToEquity: 0,
    forwardPe: 0
  };
  
  let dataSource = fundamentals?.enrichedSource || fundamentals?.source || 'unknown';
  let dataQuality = 'limited';
  
  // Check if we have enriched data from Defeat Beta
  if (fundamentals?.enriched || fundamentals?.source === 'defeatbeta') {
    dataQuality = 'rich';
  }
  
  // 1. EPS Growth (6 points)
  // Target: >25% YoY = 6pts, 15-25% = 4pts, 10-15% = 2pts
  const epsGrowth = fundamentals?.epsGrowth;
  if (epsGrowth !== null && epsGrowth !== undefined) {
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
  if (revenueGrowth !== null && revenueGrowth !== undefined) {
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
  if (roe !== null && roe !== undefined) {
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
    dataQuality: dataQuality
  };
}

/**
 * Calculate Sentiment Score (10 points)
 * Placeholder - real sentiment analysis in v2.0
 */
function calculateSentimentScore() {
  // TODO: Implement real sentiment analysis
  // For now, return neutral score
  return {
    score: 5,
    maxScore: 10,
    details: {
      newsScore: { score: 5, max: 10 }
    },
    note: 'Placeholder - real sentiment coming in v2.0'
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
  
  // 3. Market Breadth (1 point) - placeholder
  // Would need % of stocks above 50 SMA
  scores.breadth = 1; // Default to neutral
  
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
  if (rsData?.rs52Week && rsData.rs52Week < 0.8) {
    gates.push({
      name: 'RS Below Threshold',
      value: rsData.rs52Week.toFixed(2),
      threshold: '< 0.8',
      critical: true
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
  
  // 3. Average daily volume < $10M (illiquid)
  const avgVolume = stockData.avgVolume || 0;
  const avgDollarVolume = avgVolume * currentPrice;
  if (avgDollarVolume < 10000000) {
    gates.push({
      name: 'Low Liquidity',
      value: `$${(avgDollarVolume / 1000000).toFixed(1)}M`,
      threshold: '> $10M',
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
 * Determine Verdict based on score and quality gates
 */
function determineVerdict(totalScore, qualityGates, rsData) {
  // Auto-AVOID conditions
  if (qualityGates.criticalFails >= 2) {
    return {
      verdict: 'AVOID',
      reason: `${qualityGates.criticalFails} critical failures`,
      color: 'red'
    };
  }
  
  if (rsData?.rs52Week && rsData.rs52Week < 0.8) {
    return {
      verdict: 'AVOID',
      reason: 'RS significantly below market',
      color: 'red'
    };
  }
  
  // Score-based verdict
  if (totalScore >= 60 && qualityGates.criticalFails === 0) {
    // Additional check: RS must be >= 1.0 for BUY
    if (rsData?.rs52Week && rsData.rs52Week >= 1.0) {
      return {
        verdict: 'BUY',
        reason: `Strong score (${totalScore}/75) with good RS`,
        color: 'green'
      };
    } else {
      return {
        verdict: 'HOLD',
        reason: 'Good score but RS below 1.0',
        color: 'yellow'
      };
    }
  }
  
  if (totalScore >= 40) {
    return {
      verdict: 'HOLD',
      reason: `Moderate score (${totalScore}/75)`,
      color: 'yellow'
    };
  }
  
  return {
    verdict: 'AVOID',
    reason: `Low score (${totalScore}/75)`,
    color: 'red'
  };
}

/**
 * Main scoring function
 * Calculates complete analysis for a stock
 */
export function calculateScore(stockData, spyData, vixData) {
  // Calculate individual scores
  const technicalAnalysis = calculateTechnicalScore(stockData, spyData);
  const fundamentalAnalysis = calculateFundamentalScore(stockData.fundamentals);
  const sentimentAnalysis = calculateSentimentScore();
  const riskAnalysis = calculateRiskScore(spyData, vixData);
  
  // Total score
  const totalScore = technicalAnalysis.score + fundamentalAnalysis.score + 
                     sentimentAnalysis.score + riskAnalysis.score;
  
  // Quality gates
  const qualityGates = checkQualityGates(stockData, spyData, technicalAnalysis);
  
  // Verdict
  const verdict = determineVerdict(totalScore, qualityGates, technicalAnalysis.rsData);
  
  // Debug logging
  console.log('=== SCORING ENGINE DEBUG ===');
  console.log('Stock:', stockData.ticker);
  console.log('Technical Score:', technicalAnalysis.score, '/', technicalAnalysis.maxScore);
  console.log('Technical Details:', technicalAnalysis.details);
  console.log('Fundamental Score:', fundamentalAnalysis.score, '/', fundamentalAnalysis.maxScore);
  console.log('Fundamental Details:', fundamentalAnalysis.details);
  console.log('Fundamental Data Source:', fundamentalAnalysis.dataSource);
  console.log('Fundamental Data Quality:', fundamentalAnalysis.dataQuality);
  console.log('Sentiment Score:', sentimentAnalysis.score, '/', sentimentAnalysis.maxScore);
  console.log('Risk Score:', riskAnalysis.score, '/', riskAnalysis.maxScore);
  console.log('Total Score:', totalScore, '/ 75');
  console.log('Quality Gates:', qualityGates);
  console.log('Verdict:', verdict);
  console.log('============================');
  
  return {
    ticker: stockData.ticker,
    name: stockData.name,
    currentPrice: stockData.currentPrice,
    totalScore: totalScore,
    maxScore: 75,
    verdict: verdict,
    qualityGates: qualityGates,
    breakdown: {
      technical: technicalAnalysis,
      fundamental: fundamentalAnalysis,
      sentiment: sentimentAnalysis,
      risk: riskAnalysis
    },
    rsData: technicalAnalysis.rsData,
    indicators: technicalAnalysis.indicators,
    timestamp: new Date().toISOString()
  };
}
