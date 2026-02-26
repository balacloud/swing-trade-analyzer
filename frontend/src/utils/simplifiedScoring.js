/**
 * Simplified Binary Scoring System
 * Day 27: Research-backed minimalist approach
 * Day 60: Enhanced from 4 to 9 criteria (Minervini SEPA + backtest-validated filters)
 *
 * Based on:
 * - Academic momentum research (AQR, Fama-French)
 * - Turtle Trading principles
 * - Minervini SEPA (Specific Entry Point Analysis) criteria
 * - Holistic 3-Layer Backtest validation (Day 55-56)
 *
 * 9 Binary Criteria - ALL must be YES to trade:
 * 1. TREND: Price > 50 SMA > 200 SMA
 * 2. MOMENTUM: RS > 1.0 (outperforming SPY)
 * 3. SETUP: Entry near support (stop within 7%)
 * 4. RISK: R:R ratio >= 2:1
 * 5. 52-WK RANGE: Price within top 25% of 52-week range (Minervini)
 * 6. VOLUME: Avg daily dollar volume >= $10M (swing trade liquidity)
 * 7. ADX: >= 20 (confirmed trend, backtest-validated)
 * 8. MARKET: SPY > 200 SMA (bull regime, backtest-validated)
 * 9. 200 SMA TREND: 200 SMA rising over 22 trading days (Minervini)
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
      risk: { pass: false, label: 'Risk/Reward', reason: '' },
      range52wk: { pass: false, label: '52-Wk Range', reason: '' },
      volume: { pass: false, label: 'Volume', reason: '' },
      adx: { pass: false, label: 'ADX', reason: '' },
      market: { pass: false, label: 'Market', reason: '' },
      smaTrend: { pass: false, label: '200 SMA Trend', reason: '' }
    },
    verdict: 'PASS',  // TRADE or PASS
    passCount: 0,
    totalCriteria: 9,
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
  // CRITERION 5: 52-WEEK RANGE (Minervini #4/#5)
  // Price within top 25% of 52-week range
  // ============================================
  if (prices.length >= 252) {
    const last252 = prices.slice(-252);
    const high52 = Math.max(...last252);
    const low52 = Math.min(...last252);
    const range = high52 - low52;

    if (range > 0) {
      const rangePosition = ((currentPrice - low52) / range) * 100;
      if (rangePosition >= 75) {
        results.criteria.range52wk.pass = true;
        results.criteria.range52wk.reason = `${rangePosition.toFixed(0)}% of range - near 52-wk highs ($${high52.toFixed(2)})`;
      } else if (rangePosition >= 50) {
        results.criteria.range52wk.reason = `${rangePosition.toFixed(0)}% of range - mid-range (need >= 75%)`;
      } else {
        results.criteria.range52wk.reason = `${rangePosition.toFixed(0)}% of range - near 52-wk lows ($${low52.toFixed(2)})`;
      }
    } else {
      results.criteria.range52wk.reason = 'Unable to calculate range (flat price)';
    }
  } else {
    results.criteria.range52wk.reason = 'Insufficient data for 52-week range';
  }

  // ============================================
  // CRITERION 6: VOLUME (Liquidity)
  // Avg daily dollar volume >= $10M
  // ============================================
  const avgVolume = stockData.avgVolume;
  if (avgVolume && avgVolume > 0) {
    const dollarVolume = avgVolume * currentPrice;
    const dollarVolM = dollarVolume / 1e6;
    if (dollarVolume >= 10e6) {
      results.criteria.volume.pass = true;
      results.criteria.volume.reason = `$${dollarVolM.toFixed(0)}M daily - sufficient liquidity`;
    } else {
      results.criteria.volume.reason = `$${dollarVolM.toFixed(1)}M daily - thin liquidity (need >= $10M)`;
    }
  } else {
    // Fallback: calculate from price history volume
    const volumes = stockData.priceHistory.map(d => d.volume).filter(v => v > 0);
    if (volumes.length >= 50) {
      const avg50Vol = volumes.slice(-50).reduce((a, b) => a + b, 0) / 50;
      const dollarVolume = avg50Vol * currentPrice;
      const dollarVolM = dollarVolume / 1e6;
      if (dollarVolume >= 10e6) {
        results.criteria.volume.pass = true;
        results.criteria.volume.reason = `$${dollarVolM.toFixed(0)}M daily - sufficient liquidity`;
      } else {
        results.criteria.volume.reason = `$${dollarVolM.toFixed(1)}M daily - thin liquidity (need >= $10M)`;
      }
    } else {
      results.criteria.volume.reason = 'Volume data unavailable';
    }
  }

  // ============================================
  // CRITERION 7: ADX (Trend Strength)
  // ADX >= 20 (backtest-validated filter)
  // ============================================
  const adxValue = srData?.meta?.adx;
  if (adxValue !== null && adxValue !== undefined) {
    if (adxValue >= 20) {
      results.criteria.adx.pass = true;
      results.criteria.adx.reason = `ADX ${adxValue.toFixed(1)} - confirmed trend (>= 20)`;
    } else {
      results.criteria.adx.reason = `ADX ${adxValue.toFixed(1)} - no trend (need >= 20)`;
    }
  } else {
    results.criteria.adx.reason = 'ADX data unavailable';
  }

  // ============================================
  // CRITERION 8: MARKET REGIME
  // SPY > 200 SMA (bull market filter)
  // ============================================
  if (spyData?.priceHistory?.length >= 200) {
    const spyPrices = spyData.priceHistory.map(d => d.close);
    const spyCurrentPrice = spyPrices[spyPrices.length - 1];
    const spySma200 = calculateSMA(spyPrices, 200);

    if (spySma200) {
      if (spyCurrentPrice > spySma200) {
        results.criteria.market.pass = true;
        results.criteria.market.reason = `SPY ($${spyCurrentPrice.toFixed(2)}) above 200 SMA ($${spySma200.toFixed(2)}) - bull regime`;
      } else {
        const pctBelow = ((spySma200 - spyCurrentPrice) / spySma200 * 100).toFixed(1);
        results.criteria.market.reason = `SPY ${pctBelow}% below 200 SMA - bear regime`;
      }
    } else {
      results.criteria.market.reason = 'Insufficient SPY data for 200 SMA';
    }
  } else {
    results.criteria.market.reason = 'SPY data unavailable';
  }

  // ============================================
  // CRITERION 9: 200 SMA TREND (Minervini #3)
  // 200 SMA rising over past 22 trading days
  // ============================================
  if (sma200 && prices.length >= 222) {
    // Calculate 200 SMA as of 22 days ago
    const pricesOlder = prices.slice(0, prices.length - 22);
    const sma200Ago = calculateSMA(pricesOlder, 200);

    if (sma200Ago) {
      const smaDelta = ((sma200 - sma200Ago) / sma200Ago) * 100;
      if (sma200 > sma200Ago) {
        results.criteria.smaTrend.pass = true;
        results.criteria.smaTrend.reason = `200 SMA rising +${smaDelta.toFixed(2)}% over 22 days`;
      } else {
        results.criteria.smaTrend.reason = `200 SMA declining ${smaDelta.toFixed(2)}% over 22 days`;
      }
    } else {
      results.criteria.smaTrend.reason = 'Insufficient data for historical SMA';
    }
  } else if (!sma200) {
    results.criteria.smaTrend.reason = 'Insufficient data for 200 SMA';
  } else {
    results.criteria.smaTrend.reason = 'Insufficient data for 22-day SMA comparison';
  }

  // ============================================
  // FINAL VERDICT
  // ============================================
  results.passCount = Object.values(results.criteria).filter(c => c.pass).length;

  if (results.passCount === 9) {
    results.verdict = 'TRADE';
    results.confidence = 'HIGH';
    results.summary = 'All 9 criteria met - high probability setup';
  } else if (results.passCount >= 7) {
    results.verdict = 'PASS';
    results.confidence = 'MEDIUM';
    const missing = Object.values(results.criteria).filter(c => !c.pass).map(c => c.label);
    results.summary = `Close but missing: ${missing.join(', ')}`;
  } else if (results.passCount >= 5) {
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
    methodology: 'Simplified Binary System (Day 27, enhanced Day 60)',
    basedOn: ['AQR Momentum Research', 'Turtle Trading Principles', 'Minervini SEPA Criteria', 'Holistic 3-Layer Backtest (Day 55-56)']
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
