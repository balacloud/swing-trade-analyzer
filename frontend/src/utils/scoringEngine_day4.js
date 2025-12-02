/**
 * Scoring Engine - 75 Point System
 * 
 * Based on proven swing trading methodologies:
 * - Mark Minervini's SEPA
 * - William O'Neil's CAN SLIM
 * 
 * Scoring Breakdown:
 * - Technical Analysis: 40 points (Trend 15 + Short-term 10 + RS 10 + Volume 5)
 * - Fundamental Analysis: 20 points
 * - Sentiment: 10 points (placeholder for v1.0)
 * - Risk/Macro: 5 points
 * 
 * Verdict Logic:
 * - BUY: Score ≥60/75 + No critical fails + RS >1.0
 * - HOLD: Score 40-59 OR 1 critical fail
 * - AVOID: Score <40 OR 2+ critical fails OR RS <0.8
 */

import { calculateRelativeStrength, checkRSQualityGate } from './rsCalculator';
import { analyzeTrendStructure, calculateTradeSetup } from './technicalIndicators';

/**
 * Main analysis function - combines all scoring components
 * 
 * @param {Object} stockData - Stock data from backend
 * @param {Object} spyData - SPY data from backend
 * @returns {Object} Complete analysis with scores and verdict
 */
export function analyzeStock(stockData, spyData) {
  const analysis = {
    ticker: stockData.ticker,
    currentPrice: stockData.currentPrice,
    timestamp: new Date().toISOString(),
    scores: {},
    qualityGates: [],
    criticalFails: [],
    verdict: null,
    tradeSetup: null
  };
  
  // ========================================
  // 1. RELATIVE STRENGTH (10 points)
  // ========================================
  const rsAnalysis = calculateRelativeStrength(stockData, spyData);
  analysis.relativeStrength = rsAnalysis;
  analysis.scores.rs = rsAnalysis.score || 0;
  
  // RS Quality Gate
  const rsGate = checkRSQualityGate(rsAnalysis.rs52Week);
  analysis.qualityGates.push({
    name: 'Relative Strength',
    passes: rsGate.passes,
    reason: rsGate.reason,
    severity: rsGate.severity
  });
  
  if (rsGate.severity === 'critical') {
    analysis.criticalFails.push('RS below 0.8 - significant market underperformer');
  }
  
  // ========================================
  // 2. TECHNICAL ANALYSIS (30 points + 10 RS = 40 total)
  // ========================================
  const priceData = {
    closes: stockData.priceHistory?.closes || [],
    highs: stockData.priceHistory?.highs || [],
    lows: stockData.priceHistory?.lows || [],
    volumes: stockData.priceHistory?.volumes || []
  };
  
  const technicalAnalysis = analyzeTrendStructure(priceData);
  analysis.technical = technicalAnalysis;
  
  // Individual technical scores
  analysis.scores.trendStructure = technicalAnalysis.scores?.trendStructure || 0;
  analysis.scores.shortTermTrend = technicalAnalysis.scores?.shortTermTrend || 0;
  analysis.scores.volume = technicalAnalysis.scores?.volume || 0;
  
  // Debug logging
  console.log('Technical Score Breakdown:', {
    trendStructure: analysis.scores.trendStructure,
    shortTermTrend: analysis.scores.shortTermTrend,
    volume: analysis.scores.volume,
    rs: analysis.scores.rs,
    technicalAnalysisScores: technicalAnalysis.scores,
    technicalAnalysisError: technicalAnalysis.error
  });
  
  // Technical total (including RS)
  analysis.scores.technicalTotal = 
    analysis.scores.trendStructure + 
    analysis.scores.shortTermTrend + 
    analysis.scores.volume + 
    analysis.scores.rs;
  
  // 200 SMA Quality Gate
  if (!technicalAnalysis.qualityGate?.passes) {
    analysis.criticalFails.push('Below 200 SMA - not in uptrend');
    analysis.qualityGates.push({
      name: '200 SMA Trend',
      passes: false,
      reason: 'Stock is below 200 SMA - not in Stage 2 uptrend',
      severity: 'critical'
    });
  } else {
    analysis.qualityGates.push({
      name: '200 SMA Trend',
      passes: true,
      reason: 'Stock is above 200 SMA - in uptrend',
      severity: 'none'
    });
  }
  
  // ========================================
  // 3. FUNDAMENTAL ANALYSIS (20 points)
  // ========================================
  const fundamentalAnalysis = analyzeFundamentals(stockData.fundamentals);
  analysis.fundamental = fundamentalAnalysis;
  analysis.scores.fundamentalTotal = fundamentalAnalysis.totalScore;
  
  // ========================================
  // 4. SENTIMENT (10 points) - Placeholder
  // ========================================
  // For v1.0, we'll use a neutral score
  // Real sentiment will be added in v2.0
  analysis.scores.sentiment = 5; // Neutral placeholder
  analysis.sentiment = {
    score: 5,
    note: 'Sentiment analysis placeholder - will be enhanced in v2.0'
  };
  
  // ========================================
  // 5. RISK/MACRO (5 points)
  // ========================================
  const riskAnalysis = analyzeRiskMacro(spyData);
  analysis.risk = riskAnalysis;
  analysis.scores.riskTotal = riskAnalysis.totalScore;
  
  // VIX Quality Gate (if available)
  if (riskAnalysis.vixLevel && riskAnalysis.vixLevel > 30) {
    analysis.criticalFails.push('VIX > 30 - high volatility regime');
    analysis.qualityGates.push({
      name: 'VIX Level',
      passes: false,
      reason: 'VIX above 30 indicates high market fear',
      severity: 'critical'
    });
  }
  
  // ========================================
  // 6. LIQUIDITY QUALITY GATE
  // ========================================
  const avgDollarVolume = stockData.avgVolume * stockData.currentPrice;
  if (avgDollarVolume < 10000000) { // $10M minimum
    analysis.criticalFails.push('Average daily dollar volume < $10M - illiquid');
    analysis.qualityGates.push({
      name: 'Liquidity',
      passes: false,
      reason: `Average dollar volume $${(avgDollarVolume/1000000).toFixed(1)}M is below $10M threshold`,
      severity: 'critical'
    });
  } else {
    analysis.qualityGates.push({
      name: 'Liquidity',
      passes: true,
      reason: `Average dollar volume $${(avgDollarVolume/1000000).toFixed(1)}M is adequate`,
      severity: 'none'
    });
  }
  
  // ========================================
  // TOTAL SCORE (75 points max)
  // ========================================
  analysis.scores.total = 
    analysis.scores.technicalTotal +      // 40 max
    analysis.scores.fundamentalTotal +    // 20 max
    analysis.scores.sentiment +           // 10 max
    analysis.scores.riskTotal;            // 5 max
  
  analysis.scores.maxPossible = 75;
  analysis.scores.percentage = Math.round((analysis.scores.total / 75) * 100);
  
  // ========================================
  // VERDICT DETERMINATION
  // ========================================
  analysis.verdict = determineVerdict(analysis);
  
  // ========================================
  // TRADE SETUP (if BUY verdict)
  // ========================================
  if (analysis.verdict.action === 'BUY') {
    const atr = technicalAnalysis.metrics?.atr?.value;
    analysis.tradeSetup = calculateTradeSetup(stockData.currentPrice, atr);
  }
  
  return analysis;
}

/**
 * Analyze fundamental metrics (20 points max)
 */
function analyzeFundamentals(fundamentals) {
  if (!fundamentals) {
    return {
      totalScore: 0,
      error: 'No fundamental data available'
    };
  }
  
  let totalScore = 0;
  const breakdown = {};
  
  // EPS Growth (6 points)
  const epsGrowth = fundamentals.epsGrowth;
  if (epsGrowth !== null && epsGrowth !== undefined) {
    if (epsGrowth > 25) breakdown.epsGrowth = 6;
    else if (epsGrowth > 15) breakdown.epsGrowth = 4;
    else if (epsGrowth > 10) breakdown.epsGrowth = 2;
    else breakdown.epsGrowth = 0;
    totalScore += breakdown.epsGrowth;
  }
  
  // Revenue Growth (5 points)
  const revenueGrowth = fundamentals.revenueGrowth;
  if (revenueGrowth !== null && revenueGrowth !== undefined) {
    if (revenueGrowth > 20) breakdown.revenueGrowth = 5;
    else if (revenueGrowth > 10) breakdown.revenueGrowth = 3;
    else if (revenueGrowth > 5) breakdown.revenueGrowth = 1;
    else breakdown.revenueGrowth = 0;
    totalScore += breakdown.revenueGrowth;
  }
  
  // ROE (4 points)
  const roe = fundamentals.roe;
  if (roe !== null && roe !== undefined) {
    if (roe > 15) breakdown.roe = 4;
    else if (roe > 10) breakdown.roe = 2;
    else breakdown.roe = 0;
    totalScore += breakdown.roe;
  }
  
  // Debt/Equity (3 points)
  const debtEquity = fundamentals.debtToEquity;
  if (debtEquity !== null && debtEquity !== undefined) {
    if (debtEquity < 1.0) breakdown.debtEquity = 3;
    else if (debtEquity < 1.5) breakdown.debtEquity = 1;
    else breakdown.debtEquity = 0;
    totalScore += breakdown.debtEquity;
  }
  
  // Forward P/E (2 points)
  const forwardPE = fundamentals.forwardPE;
  if (forwardPE !== null && forwardPE !== undefined && forwardPE > 0) {
    if (forwardPE < 20) breakdown.forwardPE = 2;
    else if (forwardPE < 25) breakdown.forwardPE = 1;
    else breakdown.forwardPE = 0;
    totalScore += breakdown.forwardPE;
  }
  
  return {
    totalScore,
    maxScore: 20,
    breakdown,
    rawData: fundamentals
  };
}

/**
 * Analyze risk/macro factors (5 points max)
 */
function analyzeRiskMacro(spyData) {
  let totalScore = 0;
  const breakdown = {};
  
  // VIX Level (2 points) - placeholder for v1.0
  // Will add real VIX data in v1.1
  breakdown.vix = 1; // Assume moderate VIX
  totalScore += 1;
  
  // S&P 500 Regime (2 points)
  // SPY above 200 SMA = bullish regime
  if (spyData?.sma200 && spyData?.currentPrice) {
    if (spyData.currentPrice > spyData.sma200) {
      breakdown.spyRegime = 2;
      totalScore += 2;
    } else {
      breakdown.spyRegime = 0;
    }
  } else {
    breakdown.spyRegime = 1; // Neutral if no data
    totalScore += 1;
  }
  
  // Market Breadth (1 point) - placeholder
  breakdown.breadth = 1; // Assume neutral
  totalScore += 1;
  
  return {
    totalScore,
    maxScore: 5,
    breakdown,
    vixLevel: null, // Will be real in v1.1
    spyAbove200: spyData?.currentPrice > spyData?.sma200
  };
}

/**
 * Determine final verdict based on score and quality gates
 */
function determineVerdict(analysis) {
  const score = analysis.scores.total;
  const criticalFails = analysis.criticalFails.length;
  const rs = analysis.relativeStrength?.rs52Week;
  
  // AVOID conditions (checked first)
  if (criticalFails >= 2) {
    return {
      action: 'AVOID',
      confidence: 'high',
      reason: `${criticalFails} critical quality gate failures`,
      color: 'red'
    };
  }
  
  if (rs !== null && rs < 0.8) {
    return {
      action: 'AVOID',
      confidence: 'high',
      reason: 'RS below 0.8 - significant market underperformer',
      color: 'red'
    };
  }
  
  if (score < 40) {
    return {
      action: 'AVOID',
      confidence: 'medium',
      reason: `Score ${score}/75 is below minimum threshold`,
      color: 'red'
    };
  }
  
  // HOLD conditions
  if (criticalFails === 1) {
    return {
      action: 'HOLD',
      confidence: 'medium',
      reason: '1 critical quality gate failure - wait for improvement',
      color: 'yellow'
    };
  }
  
  if (score >= 40 && score < 60) {
    return {
      action: 'HOLD',
      confidence: 'medium',
      reason: `Score ${score}/75 is moderate - not a strong setup`,
      color: 'yellow'
    };
  }
  
  if (rs !== null && rs < 1.0) {
    return {
      action: 'HOLD',
      confidence: 'medium',
      reason: 'RS below 1.0 - underperforming market',
      color: 'yellow'
    };
  }
  
  // BUY conditions
  if (score >= 60 && criticalFails === 0 && (rs === null || rs >= 1.0)) {
    let confidence = 'medium';
    if (score >= 65 && rs >= 1.2) confidence = 'high';
    if (score >= 70 && rs >= 1.3) confidence = 'very high';
    
    return {
      action: 'BUY',
      confidence,
      reason: `Score ${score}/75 with strong RS of ${rs?.toFixed(2) || 'N/A'}`,
      color: 'green'
    };
  }
  
  // Default to HOLD
  return {
    action: 'HOLD',
    confidence: 'low',
    reason: 'Mixed signals - proceed with caution',
    color: 'yellow'
  };
}

/**
 * Format analysis for display
 */
export function formatAnalysisForDisplay(analysis) {
  return {
    ticker: analysis.ticker,
    price: `$${analysis.currentPrice?.toFixed(2)}`,
    verdict: analysis.verdict,
    score: `${analysis.scores.total}/${analysis.scores.maxPossible}`,
    scorePercentage: `${analysis.scores.percentage}%`,
    breakdown: {
      technical: `${analysis.scores.technicalTotal}/40`,
      fundamental: `${analysis.scores.fundamentalTotal}/20`,
      sentiment: `${analysis.scores.sentiment}/10`,
      risk: `${analysis.scores.riskTotal}/5`
    },
    rs: analysis.relativeStrength,
    qualityGates: analysis.qualityGates,
    criticalFails: analysis.criticalFails,
    tradeSetup: analysis.tradeSetup,
    timestamp: analysis.timestamp
  };
}