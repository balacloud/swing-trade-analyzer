/**
 * Position Sizing Calculator - Van Tharp Principles
 * Day 28: The 90% that actually matters
 *
 * Core Concepts:
 * - R = Entry - Stop (initial risk per share)
 * - Position Size = (Account × Risk%) / R
 * - R-Multiple = (Exit - Entry) / R
 * - Expectancy = (Win% × Avg Win R) + (Loss% × Avg Loss R)
 */

/**
 * Calculate position size based on account risk
 * @param {number} accountSize - Total account value
 * @param {number} riskPercent - Risk per trade (e.g., 2 for 2%)
 * @param {number} entryPrice - Planned entry price
 * @param {number} stopPrice - Stop loss price
 * @param {object} options - Optional settings { maxPositionPercent, manualShares }
 * @returns {object} Position sizing details
 */
export function calculatePositionSize(accountSize, riskPercent, entryPrice, stopPrice, options = {}) {
  // Validate inputs
  if (!accountSize || accountSize <= 0) {
    return { error: 'Invalid account size' };
  }
  if (!riskPercent || riskPercent <= 0 || riskPercent > 100) {
    return { error: 'Invalid risk percentage' };
  }
  if (!entryPrice || entryPrice <= 0) {
    return { error: 'Invalid entry price' };
  }
  if (!stopPrice || stopPrice <= 0) {
    return { error: 'Invalid stop price' };
  }
  if (stopPrice >= entryPrice) {
    return { error: 'Stop must be below entry for long positions' };
  }

  // Core calculations
  const riskPerShare = entryPrice - stopPrice; // R per share
  const maxRiskAmount = accountSize * (riskPercent / 100); // Total $ at risk
  let shares = Math.floor(maxRiskAmount / riskPerShare);

  // Day 29: Apply max position size limit if specified
  const maxPositionPercent = options.maxPositionPercent || 100; // Default: no limit
  const maxPositionValue = accountSize * (maxPositionPercent / 100);
  const maxSharesByPosition = Math.floor(maxPositionValue / entryPrice);

  // Use the smaller of risk-based or position-limit shares
  let limitApplied = null;
  if (shares > maxSharesByPosition) {
    shares = maxSharesByPosition;
    limitApplied = `Position capped at ${maxPositionPercent}% of account`;
  }

  // Day 29: Allow manual share override
  if (options.manualShares && options.manualShares > 0) {
    shares = options.manualShares;
    limitApplied = 'Manual share count';
  }

  const actualRiskAmount = shares * riskPerShare;
  const positionValue = shares * entryPrice;
  const positionPercent = (positionValue / accountSize) * 100;
  const stopPercent = (riskPerShare / entryPrice) * 100;

  // Calculate suggested targets at various R-multiples
  const targets = [
    { r: 1.5, price: entryPrice + (riskPerShare * 1.5), label: '1.5R' },
    { r: 2.0, price: entryPrice + (riskPerShare * 2.0), label: '2R' },
    { r: 3.0, price: entryPrice + (riskPerShare * 3.0), label: '3R' },
  ];

  return {
    shares,
    entryPrice,
    stopPrice,
    riskPerShare,
    actualRiskAmount,
    maxRiskAmount,
    positionValue,
    positionPercent,
    stopPercent,
    targets,
    rMultiple: 1, // Initial R is always 1
    limitApplied, // Day 29: Shows if position was capped or manual
    summary: {
      position: `${shares} shares @ $${entryPrice.toFixed(2)}`,
      risk: `$${actualRiskAmount.toFixed(2)} (${riskPercent}%)`,
      stop: `$${stopPrice.toFixed(2)} (${stopPercent.toFixed(1)}% below entry)`,
    }
  };
}

/**
 * Calculate R-Multiple for a completed trade
 * @param {number} entryPrice - Entry price
 * @param {number} stopPrice - Initial stop price
 * @param {number} exitPrice - Actual exit price
 * @returns {number} R-Multiple
 */
export function calculateRMultiple(entryPrice, stopPrice, exitPrice) {
  const r = entryPrice - stopPrice;
  if (r <= 0) return 0;
  return (exitPrice - entryPrice) / r;
}

/**
 * Calculate expectancy from a series of R-multiples
 * @param {number[]} rMultiples - Array of R-multiples from trades
 * @returns {object} Expectancy metrics
 */
export function calculateExpectancy(rMultiples) {
  if (!rMultiples || rMultiples.length === 0) {
    return { expectancy: 0, winRate: 0, avgWinR: 0, avgLossR: 0, totalTrades: 0 };
  }

  const wins = rMultiples.filter(r => r > 0);
  const losses = rMultiples.filter(r => r <= 0);

  const winRate = wins.length / rMultiples.length;
  const avgWinR = wins.length > 0 ? wins.reduce((a, b) => a + b, 0) / wins.length : 0;
  const avgLossR = losses.length > 0 ? losses.reduce((a, b) => a + b, 0) / losses.length : 0;

  // Expectancy formula
  const expectancy = (winRate * avgWinR) + ((1 - winRate) * avgLossR);

  return {
    expectancy,
    winRate: winRate * 100,
    avgWinR,
    avgLossR,
    totalTrades: rMultiples.length,
    wins: wins.length,
    losses: losses.length
  };
}

/**
 * Calculate System Quality Number (SQN)
 * SQN = (Mean R / StdDev R) × sqrt(N)
 * @param {number[]} rMultiples - Array of R-multiples
 * @returns {object} SQN and interpretation
 */
export function calculateSQN(rMultiples) {
  if (!rMultiples || rMultiples.length < 20) {
    return {
      sqn: null,
      interpretation: 'Need at least 20 trades for meaningful SQN',
      quality: 'insufficient_data'
    };
  }

  const n = rMultiples.length;
  const mean = rMultiples.reduce((a, b) => a + b, 0) / n;
  const variance = rMultiples.reduce((sum, r) => sum + Math.pow(r - mean, 2), 0) / n;
  const stdDev = Math.sqrt(variance);

  if (stdDev === 0) {
    return { sqn: null, interpretation: 'No variance in trades', quality: 'error' };
  }

  const sqn = (mean / stdDev) * Math.sqrt(n);

  // Van Tharp's SQN interpretation
  let interpretation, quality;
  if (sqn >= 7.0) {
    interpretation = 'Holy Grail';
    quality = 'exceptional';
  } else if (sqn >= 5.1) {
    interpretation = 'Superb';
    quality = 'excellent';
  } else if (sqn >= 3.0) {
    interpretation = 'Excellent';
    quality = 'very_good';
  } else if (sqn >= 2.5) {
    interpretation = 'Very Good';
    quality = 'good';
  } else if (sqn >= 2.0) {
    interpretation = 'Average';
    quality = 'average';
  } else if (sqn >= 1.6) {
    interpretation = 'Below Average';
    quality = 'below_average';
  } else {
    interpretation = 'Poor - Difficult to trade';
    quality = 'poor';
  }

  return { sqn, interpretation, quality, mean, stdDev, n };
}

/**
 * Get default settings
 */
export function getDefaultSettings() {
  return {
    accountSize: 10000,
    riskPercent: 2,
    minRiskPercent: 2,
    maxRiskPercent: 5,
    maxPositionPercent: 25, // Day 29: Max % of account in single position (default 25%)
    useManualShares: false, // Day 29: Allow manual share override
    manualShares: 0         // Day 29: Manual share count if useManualShares is true
  };
}

/**
 * Load settings from localStorage
 */
export function loadSettings() {
  try {
    const saved = localStorage.getItem('swingTradeSettings');
    if (saved) {
      return { ...getDefaultSettings(), ...JSON.parse(saved) };
    }
  } catch (e) {
    console.error('Failed to load settings:', e);
  }
  return getDefaultSettings();
}

/**
 * Save settings to localStorage
 */
export function saveSettings(settings) {
  try {
    localStorage.setItem('swingTradeSettings', JSON.stringify(settings));
    return true;
  } catch (e) {
    console.error('Failed to save settings:', e);
    return false;
  }
}
