/**
 * Relative Strength (RS) Calculator
 * 
 * RS is THE #1 predictor for swing trading success.
 * Based on Mark Minervini's SEPA and William O'Neil's methodology.
 * 
 * Formula: RS = (Stock % Change) / (SPY % Change)
 * - RS > 1.0 = Outperforming the market
 * - RS < 1.0 = Underperforming the market
 * 
 * Day 7 FIX: Corrected field names to match api.js
 * - price52WeeksAgo → price52wAgo
 * - price13WeeksAgo → price13wAgo
 */

/**
 * Calculate Relative Strength vs S&P 500
 * 
 * @param {Object} stockData - Stock data from backend
 * @param {Object} spyData - SPY data from backend
 * @returns {Object} RS metrics
 */
export function calculateRelativeStrength(stockData, spyData) {
  try {
    // DEBUG: Log incoming data to verify structure
    console.log('=== RS CALCULATOR DEBUG ===');
    console.log('stockData received:', {
      ticker: stockData?.ticker,
      currentPrice: stockData?.currentPrice,
      price52wAgo: stockData?.price52wAgo,
      price13wAgo: stockData?.price13wAgo
    });
    console.log('spyData received:', {
      ticker: spyData?.ticker,
      currentPrice: spyData?.currentPrice,
      price52wAgo: spyData?.price52wAgo,
      price13wAgo: spyData?.price13wAgo
    });
    
    // Extract prices - FIXED: Use correct field names matching api.js
    const stockCurrent = stockData?.currentPrice;
    const stock52wAgo = stockData?.price52wAgo;      // FIXED: was price52WeeksAgo
    const stock13wAgo = stockData?.price13wAgo;      // FIXED: was price13WeeksAgo
    
    const spyCurrent = spyData?.currentPrice;
    const spy52wAgo = spyData?.price52wAgo;          // FIXED: was price52WeeksAgo
    const spy13wAgo = spyData?.price13wAgo;          // FIXED: was price13WeeksAgo
    
    // Validate we have all required data
    if (!stockCurrent || !stock52wAgo || !spyCurrent || !spy52wAgo) {
      console.error('Missing price data for RS calculation:', {
        stockCurrent,
        stock52wAgo,
        spyCurrent,
        spy52wAgo
      });
      return {
        rs52Week: null,
        rs13Week: null,
        rsRating: null,
        rsTrend: 'unknown',
        error: 'Insufficient data for RS calculation'
      };
    }
    
    // Calculate 52-week RS
    // RS = (Stock Today / Stock 52w Ago) / (SPY Today / SPY 52w Ago)
    const stockReturn52w = stockCurrent / stock52wAgo;
    const spyReturn52w = spyCurrent / spy52wAgo;
    const rs52Week = stockReturn52w / spyReturn52w;
    
    console.log('RS Calculation:', {
      stockReturn52w: stockReturn52w.toFixed(3),
      spyReturn52w: spyReturn52w.toFixed(3),
      rs52Week: rs52Week.toFixed(3)
    });
    
    // Calculate 13-week RS (short-term momentum)
    let rs13Week = null;
    if (stock13wAgo && spy13wAgo) {
      const stockReturn13w = stockCurrent / stock13wAgo;
      const spyReturn13w = spyCurrent / spy13wAgo;
      rs13Week = stockReturn13w / spyReturn13w;
    }
    
    // Determine RS trend
    // Improving: 13-week RS > 52-week RS (recent outperformance accelerating)
    let rsTrend = 'stable';
    if (rs13Week !== null) {
      if (rs13Week > rs52Week * 1.05) {
        rsTrend = 'improving';
      } else if (rs13Week < rs52Week * 0.95) {
        rsTrend = 'declining';
      }
    }
    
    // Calculate RS Rating (0-100 scale)
    // This is a simplified version - ideally would be percentile vs all stocks
    // For now: RS of 1.5 = 90, RS of 1.0 = 50, RS of 0.5 = 10
    const rsRating = Math.min(99, Math.max(1, Math.round((rs52Week - 0.5) * 80 + 10)));
    
    // Calculate percentage returns for display
    const stockPctChange52w = ((stockCurrent / stock52wAgo) - 1) * 100;
    const spyPctChange52w = ((spyCurrent / spy52wAgo) - 1) * 100;
    
    let stockPctChange13w = null;
    let spyPctChange13w = null;
    if (stock13wAgo && spy13wAgo) {
      stockPctChange13w = ((stockCurrent / stock13wAgo) - 1) * 100;
      spyPctChange13w = ((spyCurrent / spy13wAgo) - 1) * 100;
    }
    
    console.log('RS Result:', {
      rs52Week: rs52Week.toFixed(3),
      rs13Week: rs13Week?.toFixed(3),
      rsRating,
      rsTrend,
      stockPctChange52w: stockPctChange52w.toFixed(2) + '%',
      spyPctChange52w: spyPctChange52w.toFixed(2) + '%'
    });
    console.log('=== END RS DEBUG ===');
    
    return {
      // Core RS values
      rs52Week: parseFloat(rs52Week.toFixed(3)),
      rs13Week: rs13Week ? parseFloat(rs13Week.toFixed(3)) : null,
      rsRating: rsRating,
      rsTrend: rsTrend,
      
      // Supporting data
      stockReturn52w: parseFloat(stockPctChange52w.toFixed(2)),
      spyReturn52w: parseFloat(spyPctChange52w.toFixed(2)),
      stockReturn13w: stockPctChange13w ? parseFloat(stockPctChange13w.toFixed(2)) : null,
      spyReturn13w: spyPctChange13w ? parseFloat(spyPctChange13w.toFixed(2)) : null,
      
      // Interpretation
      interpretation: interpretRS(rs52Week, rs13Week, rsTrend),
      
      // Scoring for the 75-point system (RS is worth 10 points)
      score: calculateRSScore(rs52Week),
      
      // Quality gate check
      passesQualityGate: rs52Week >= 0.8,

      // Tier 2B: Blended RS (informational only — backtest showed degradation:
      // PF 1.90→1.51, Sharpe 1.17→0.68. rs52Week remains the verdict driver.)
      ...(() => {
        const stockPrices = stockData?.priceHistory?.map(d => d.close);
        const spyPrices = spyData?.priceHistory?.map(d => d.close);
        const blended = calculateBlendedRS(stockPrices, spyPrices);
        return blended ? {
          rsBlended: blended.rsBlended,
          rs21d: blended.rs21d,
          rs63d: blended.rs63d,
          rs126d: blended.rs126d,
        } : {
          rsBlended: null, rs21d: null, rs63d: null, rs126d: null,
        };
      })(),

      error: null
    };
  } catch (error) {
    console.error('Error calculating RS:', error);
    return {
      rs52Week: null,
      rs13Week: null,
      rsRating: null,
      rsTrend: 'unknown',
      error: error.message
    };
  }
}

/**
 * Tier 2B: Calculate blended RS using 3 lookbacks (21d, 63d, 126d).
 * INFORMATIONAL ONLY — backtest showed blended RS degrades verdict quality
 * (PF 1.90→1.51, Sharpe 1.17→0.68). rs52Week remains the verdict driver.
 *
 * @param {number[]} stockPrices - Array of stock close prices (oldest first)
 * @param {number[]} spyPrices - Array of SPY close prices (oldest first)
 * @returns {Object|null} { rsBlended, rs21d, rs63d, rs126d } or null if insufficient data
 */
function calculateBlendedRS(stockPrices, spyPrices) {
  if (!stockPrices || !spyPrices || stockPrices.length < 127 || spyPrices.length < 127) {
    return null;
  }

  const n = stockPrices.length;
  const spyN = spyPrices.length;

  // 21-day: stock ROC normalized to RS-like scale (1 + ROC)
  const rs21 = n > 21 ? stockPrices[n - 1] / stockPrices[n - 22] : 1.0;

  // 63-day RS vs SPY
  const stockRet63 = n > 63 ? (stockPrices[n - 1] / stockPrices[n - 64]) - 1 : 0;
  const spyRet63 = spyN > 63 ? (spyPrices[spyN - 1] / spyPrices[spyN - 64]) - 1 : 0;
  const rs63 = (1 + spyRet63) !== 0 ? (1 + stockRet63) / (1 + spyRet63) : 1.0;

  // 126-day RS vs SPY
  const stockRet126 = n > 126 ? (stockPrices[n - 1] / stockPrices[n - 127]) - 1 : 0;
  const spyRet126 = spyN > 126 ? (spyPrices[spyN - 1] / spyPrices[spyN - 127]) - 1 : 0;
  const rs126 = (1 + spyRet126) !== 0 ? (1 + stockRet126) / (1 + spyRet126) : 1.0;

  // Equal-weight blend
  const rsBlended = (rs21 + rs63 + rs126) / 3.0;

  return {
    rsBlended: Math.round(rsBlended * 1000) / 1000,
    rs21d: Math.round(rs21 * 1000) / 1000,
    rs63d: Math.round(rs63 * 1000) / 1000,
    rs126d: Math.round(rs126 * 1000) / 1000,
  };
}

/**
 * Calculate RS score for the 75-point scoring system
 * RS is worth 10 points max
 * 
 * @param {number} rs52Week - 52-week RS value
 * @returns {number} Score from 0-10
 */
function calculateRSScore(rs52Week) {
  if (rs52Week === null) return 0;
  
  // Scoring thresholds based on Minervini's guidelines
  if (rs52Week >= 1.3) return 10;      // Top performers (RS 130%+)
  if (rs52Week >= 1.2) return 9;       // Strong outperformance
  if (rs52Week >= 1.1) return 7;       // Good outperformance
  if (rs52Week >= 1.0) return 5;       // Market performer
  if (rs52Week >= 0.9) return 3;       // Slight underperformance
  if (rs52Week >= 0.8) return 1;       // Underperforming (quality gate threshold)
  return 0;                             // Significant underperformer
}

/**
 * Provide human-readable interpretation of RS
 * 
 * @param {number} rs52Week - 52-week RS
 * @param {number} rs13Week - 13-week RS
 * @param {string} rsTrend - Trend direction
 * @returns {string} Interpretation text
 */
function interpretRS(rs52Week, rs13Week, rsTrend) {
  if (rs52Week === null) return 'Unable to calculate RS';
  
  let interpretation = '';
  
  // Base interpretation
  if (rs52Week >= 1.3) {
    interpretation = 'Exceptional strength - Top tier performer';
  } else if (rs52Week >= 1.2) {
    interpretation = 'Strong outperformance vs market';
  } else if (rs52Week >= 1.1) {
    interpretation = 'Good relative strength';
  } else if (rs52Week >= 1.0) {
    interpretation = 'Performing in-line with market';
  } else if (rs52Week >= 0.9) {
    interpretation = 'Slight underperformance';
  } else if (rs52Week >= 0.8) {
    interpretation = 'Underperforming - Caution advised';
  } else {
    interpretation = 'Significant laggard - Avoid for swing trades';
  }
  
  // Add trend context
  if (rsTrend === 'improving') {
    interpretation += ' (momentum accelerating)';
  } else if (rsTrend === 'declining') {
    interpretation += ' (momentum fading)';
  }
  
  return interpretation;
}

/**
 * Check if RS passes quality gate
 * Stocks with RS < 0.8 should be auto-avoided
 * 
 * @param {number} rs52Week - 52-week RS value
 * @returns {Object} Quality gate result
 */
export function checkRSQualityGate(rs52Week) {
  if (rs52Week === null) {
    return {
      passes: false,
      reason: 'Unable to calculate RS',
      severity: 'critical'
    };
  }
  
  if (rs52Week < 0.8) {
    return {
      passes: false,
      reason: `RS of ${rs52Week.toFixed(2)} is below 0.8 threshold - significant market underperformer`,
      severity: 'critical'
    };
  }
  
  if (rs52Week < 1.0) {
    return {
      passes: true,
      reason: `RS of ${rs52Week.toFixed(2)} is below market - proceed with caution`,
      severity: 'warning'
    };
  }
  
  return {
    passes: true,
    reason: `RS of ${rs52Week.toFixed(2)} shows market outperformance`,
    severity: 'none'
  };
}

/**
 * Format RS for display
 * 
 * @param {number} rs - RS value
 * @returns {string} Formatted RS string
 */
export function formatRS(rs) {
  if (rs === null || rs === undefined) return 'N/A';
  return rs.toFixed(2);
}

/**
 * Get RS color for UI display
 * 
 * @param {number} rs - RS value
 * @returns {string} Tailwind color class
 */
export function getRSColor(rs) {
  if (rs === null || rs === undefined) return 'text-gray-500';
  if (rs >= 1.2) return 'text-green-600';
  if (rs >= 1.0) return 'text-green-500';
  if (rs >= 0.9) return 'text-yellow-500';
  if (rs >= 0.8) return 'text-orange-500';
  return 'text-red-500';
}

/**
 * Get RS trend icon
 * 
 * @param {string} trend - RS trend ('improving', 'declining', 'stable')
 * @returns {string} Emoji or icon character
 */
export function getRSTrendIcon(trend) {
  switch (trend) {
    case 'improving': return '↗️';
    case 'declining': return '↘️';
    case 'stable': return '→';
    default: return '?';
  }
}