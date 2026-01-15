/**
 * Simplified Binary Scoring System
 * Day 27: Research-backed minimalist approach
 *
 * Based on:
 * - Academic momentum research (AQR, Fama-French)
 * - Turtle Trading principles
 * - Proven trend-following concepts
 *
 * 4 Binary Criteria - ALL must be YES to trade:
 * 1. TREND: Price > 50 SMA > 200 SMA
 * 2. MOMENTUM: RS > 1.0 (outperforming SPY)
 * 3. SETUP: Entry near support (stop within 7%)
 * 4. RISK: R:R ratio >= 2:1
 */

import { calculateSMA } from './technicalIndicators';

/**
 * Calculate simplified binary analysis
 * Returns pass/fail for each criterion and overall verdict
 */
export function calculateSimplifiedAnalysis(stockData, spyData, srData) {
  const results = {
    criteria: {
      trend: { pass: false, label: 'Trend', reason: '' },
      momentum: { pass: false, label: 'Momentum', reason: '' },
      setup: { pass: false, label: 'Setup', reason: '' },
      risk: { pass: false, label: 'Risk/Reward', reason: '' }
    },
    verdict: 'PASS',  // TRADE or PASS
    passCount: 0,
    totalCriteria: 4,
    confidence: 'LOW'
  };

  if (!stockData?.priceHistory || stockData.priceHistory.length < 200) {
    results.error = 'Insufficient price data (need 200+ days)';
    return results;
  }

  const prices = stockData.priceHistory.map(d => d.close);
  const currentPrice = prices[prices.length - 1];

  // ============================================
  // CRITERION 1: TREND
  // Price > 50 SMA > 200 SMA (Stage 2 uptrend)
  // ============================================
  const sma50 = calculateSMA(prices, 50);
  const sma200 = calculateSMA(prices, 200);

  if (sma50 && sma200) {
    if (currentPrice > sma50 && sma50 > sma200) {
      results.criteria.trend.pass = true;
      results.criteria.trend.reason = `Price ($${currentPrice.toFixed(2)}) > 50 SMA ($${sma50.toFixed(2)}) > 200 SMA ($${sma200.toFixed(2)})`;
    } else if (currentPrice > sma200 && currentPrice > sma50) {
      results.criteria.trend.reason = `Uptrend but 50 SMA ($${sma50.toFixed(2)}) < 200 SMA ($${sma200.toFixed(2)})`;
    } else if (currentPrice > sma200) {
      results.criteria.trend.reason = `Above 200 SMA but below 50 SMA ($${sma50.toFixed(2)})`;
    } else {
      results.criteria.trend.reason = `Below 200 SMA ($${sma200.toFixed(2)}) - downtrend`;
    }
  } else {
    results.criteria.trend.reason = 'Insufficient data for SMA calculation';
  }

  // ============================================
  // CRITERION 2: MOMENTUM (Relative Strength)
  // Stock outperforming SPY over 52 weeks
  // ============================================
  if (stockData.priceHistory.length >= 252 && spyData?.priceHistory?.length >= 252) {
    const stockPrices = stockData.priceHistory.map(d => d.close);
    const spyPrices = spyData.priceHistory.map(d => d.close);

    const stockReturn = (stockPrices[stockPrices.length - 1] / stockPrices[stockPrices.length - 252]) - 1;
    const spyReturn = (spyPrices[spyPrices.length - 1] / spyPrices[spyPrices.length - 252]) - 1;

    const rsRatio = spyReturn !== 0 ? (1 + stockReturn) / (1 + spyReturn) : 1;

    if (rsRatio >= 1.0) {
      results.criteria.momentum.pass = true;
      results.criteria.momentum.reason = `RS ${rsRatio.toFixed(2)} - outperforming SPY (Stock: ${(stockReturn * 100).toFixed(1)}% vs SPY: ${(spyReturn * 100).toFixed(1)}%)`;
    } else {
      results.criteria.momentum.reason = `RS ${rsRatio.toFixed(2)} - underperforming SPY (Stock: ${(stockReturn * 100).toFixed(1)}% vs SPY: ${(spyReturn * 100).toFixed(1)}%)`;
    }
  } else {
    results.criteria.momentum.reason = 'Insufficient data for RS calculation';
  }

  // ============================================
  // CRITERION 3: SETUP (Entry Quality)
  // Can set stop within 7% of entry
  // ============================================
  if (srData?.suggestedEntry && srData?.suggestedStop) {
    const entry = srData.suggestedEntry;
    const stop = srData.suggestedStop;
    const stopPct = ((entry - stop) / entry) * 100;

    if (stopPct <= 7 && stopPct > 0) {
      results.criteria.setup.pass = true;
      results.criteria.setup.reason = `Stop ${stopPct.toFixed(1)}% below entry - tight risk`;
    } else if (stopPct > 7) {
      results.criteria.setup.reason = `Stop ${stopPct.toFixed(1)}% below entry - too wide (max 7%)`;
    } else {
      results.criteria.setup.reason = 'Invalid stop placement';
    }
  } else if (srData?.support?.length > 0) {
    // Calculate from nearest support
    const nearestSupport = Math.max(...srData.support);
    const stopPct = ((currentPrice - nearestSupport) / currentPrice) * 100;

    if (stopPct <= 7 && stopPct > 0) {
      results.criteria.setup.pass = true;
      results.criteria.setup.reason = `Support at $${nearestSupport.toFixed(2)} (${stopPct.toFixed(1)}% below) - good entry zone`;
    } else if (stopPct > 7) {
      results.criteria.setup.reason = `Nearest support ${stopPct.toFixed(1)}% below - extended from support`;
    } else {
      results.criteria.setup.reason = 'Price at or below support';
    }
  } else {
    results.criteria.setup.reason = 'No support levels available';
  }

  // ============================================
  // CRITERION 4: RISK/REWARD
  // R:R ratio >= 2:1
  // ============================================
  if (srData?.riskReward !== null && srData?.riskReward !== undefined) {
    if (srData.riskReward >= 2.0) {
      results.criteria.risk.pass = true;
      results.criteria.risk.reason = `R:R ${srData.riskReward.toFixed(2)}:1 - favorable risk/reward`;
    } else if (srData.riskReward >= 1.5) {
      results.criteria.risk.reason = `R:R ${srData.riskReward.toFixed(2)}:1 - acceptable but not ideal (want >= 2:1)`;
    } else {
      results.criteria.risk.reason = `R:R ${srData.riskReward.toFixed(2)}:1 - unfavorable (want >= 2:1)`;
    }
  } else {
    results.criteria.risk.reason = 'Unable to calculate R:R';
  }

  // ============================================
  // FINAL VERDICT
  // ============================================
  results.passCount = Object.values(results.criteria).filter(c => c.pass).length;

  if (results.passCount === 4) {
    results.verdict = 'TRADE';
    results.confidence = 'HIGH';
    results.summary = 'All criteria met - high probability setup';
  } else if (results.passCount === 3) {
    results.verdict = 'PASS';
    results.confidence = 'MEDIUM';
    results.summary = `Close but missing: ${Object.entries(results.criteria).filter(([k, v]) => !v.pass).map(([k, v]) => v.label).join(', ')}`;
  } else if (results.passCount === 2) {
    results.verdict = 'PASS';
    results.confidence = 'LOW';
    results.summary = 'Multiple criteria failing - not a valid setup';
  } else {
    results.verdict = 'PASS';
    results.confidence = 'VERY LOW';
    results.summary = 'Most criteria failing - avoid this trade';
  }

  // Add metadata
  results.meta = {
    currentPrice,
    sma50,
    sma200,
    methodology: 'Simplified Binary System (Day 27)',
    basedOn: ['AQR Momentum Research', 'Turtle Trading Principles', 'Academic Factor Evidence']
  };

  return results;
}

/**
 * Get color class for verdict
 */
export function getVerdictColor(verdict) {
  return verdict === 'TRADE' ? 'text-green-400' : 'text-gray-400';
}

/**
 * Get background color for criterion
 */
export function getCriterionBgColor(pass) {
  return pass ? 'bg-green-900/30 border-green-700' : 'bg-red-900/20 border-red-700/50';
}
