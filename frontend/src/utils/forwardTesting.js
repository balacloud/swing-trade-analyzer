/**
 * Forward Testing Utility - v4.7
 * Track paper trades, calculate R-multiples, build expectancy over time
 *
 * Day 47: Initial implementation
 *
 * Key Concepts (Van Tharp):
 * - R = Initial Risk (Entry - Stop)
 * - R-Multiple = (Exit - Entry) / R (how many R's you made/lost)
 * - Expectancy = (Win% × Avg Win R) + (Loss% × Avg Loss R)
 * - SQN = (Mean R / StdDev R) × sqrt(N) (System Quality Number)
 */

const STORAGE_KEY = 'swing_trade_forward_testing';

/**
 * Trade Status
 */
export const TradeStatus = {
  OPEN: 'open',
  CLOSED_WIN: 'closed_win',
  CLOSED_LOSS: 'closed_loss',
  CLOSED_BREAKEVEN: 'closed_breakeven',
  STOPPED_OUT: 'stopped_out',
  CANCELLED: 'cancelled'
};

/**
 * Create a new trade entry
 *
 * @param {object} params - Trade parameters
 * @returns {object} New trade object
 */
export function createTrade({
  ticker,
  entryPrice,
  stopPrice,
  targetPrice,
  shares,
  entryType = 'momentum',  // 'momentum' or 'pullback'
  pattern = null,
  categoricalVerdict = null,
  notes = ''
}) {
  const initialRisk = entryPrice - stopPrice;
  const potentialReward = targetPrice - entryPrice;

  return {
    id: Date.now().toString(36) + Math.random().toString(36).substr(2),
    ticker: ticker.toUpperCase(),
    entryDate: new Date().toISOString(),
    entryPrice,
    stopPrice,
    targetPrice,
    shares,
    entryType,
    pattern,
    categoricalVerdict,
    notes,

    // Calculated fields
    initialRisk,
    potentialReward,
    plannedRR: potentialReward / initialRisk,
    positionValue: entryPrice * shares,
    maxLoss: initialRisk * shares,

    // Exit fields (filled when closed)
    exitDate: null,
    exitPrice: null,
    exitReason: null,
    status: TradeStatus.OPEN,

    // R-Multiple (calculated on close)
    rMultiple: null,
    profitLoss: null,
    profitLossPct: null
  };
}

/**
 * Close a trade
 *
 * @param {object} trade - The trade to close
 * @param {number} exitPrice - Exit price
 * @param {string} exitReason - Reason for exit
 * @returns {object} Updated trade with exit data
 */
export function closeTrade(trade, exitPrice, exitReason = 'manual') {
  const profitLoss = (exitPrice - trade.entryPrice) * trade.shares;
  const profitLossPct = ((exitPrice - trade.entryPrice) / trade.entryPrice) * 100;
  const rMultiple = (exitPrice - trade.entryPrice) / trade.initialRisk;

  let status;
  if (Math.abs(rMultiple) < 0.1) {
    status = TradeStatus.CLOSED_BREAKEVEN;
  } else if (rMultiple > 0) {
    status = TradeStatus.CLOSED_WIN;
  } else {
    status = exitReason === 'stopped_out' ? TradeStatus.STOPPED_OUT : TradeStatus.CLOSED_LOSS;
  }

  return {
    ...trade,
    exitDate: new Date().toISOString(),
    exitPrice,
    exitReason,
    status,
    rMultiple: Math.round(rMultiple * 100) / 100,
    profitLoss: Math.round(profitLoss * 100) / 100,
    profitLossPct: Math.round(profitLossPct * 100) / 100
  };
}

/**
 * Calculate forward testing statistics
 *
 * @param {Array} trades - Array of trade objects
 * @returns {object} Statistics
 */
export function calculateStatistics(trades) {
  const closedTrades = trades.filter(t =>
    t.status !== TradeStatus.OPEN && t.status !== TradeStatus.CANCELLED
  );

  if (closedTrades.length === 0) {
    return {
      totalTrades: trades.length,
      openTrades: trades.filter(t => t.status === TradeStatus.OPEN).length,
      closedTrades: 0,
      wins: 0,
      losses: 0,
      breakevens: 0,
      winRate: 0,
      avgWinR: 0,
      avgLossR: 0,
      expectancy: 0,
      expectancyDollar: 0,
      totalPL: 0,
      sqn: 0,
      largestWin: 0,
      largestLoss: 0,
      avgHoldingDays: 0
    };
  }

  const wins = closedTrades.filter(t =>
    t.status === TradeStatus.CLOSED_WIN
  );
  const losses = closedTrades.filter(t =>
    t.status === TradeStatus.CLOSED_LOSS || t.status === TradeStatus.STOPPED_OUT
  );
  const breakevens = closedTrades.filter(t =>
    t.status === TradeStatus.CLOSED_BREAKEVEN
  );

  const winRate = wins.length / closedTrades.length;

  const avgWinR = wins.length > 0
    ? wins.reduce((sum, t) => sum + t.rMultiple, 0) / wins.length
    : 0;

  const avgLossR = losses.length > 0
    ? losses.reduce((sum, t) => sum + t.rMultiple, 0) / losses.length
    : 0;

  // Expectancy = (Win% × Avg Win R) + (Loss% × Avg Loss R)
  const expectancy = (winRate * avgWinR) + ((1 - winRate) * avgLossR);

  // Average initial risk for dollar expectancy
  const avgRisk = closedTrades.reduce((sum, t) => sum + t.initialRisk * t.shares, 0) / closedTrades.length;
  const expectancyDollar = expectancy * avgRisk;

  // Total P/L
  const totalPL = closedTrades.reduce((sum, t) => sum + (t.profitLoss || 0), 0);

  // SQN calculation
  const rMultiples = closedTrades.map(t => t.rMultiple);
  const meanR = rMultiples.reduce((a, b) => a + b, 0) / rMultiples.length;
  const stdDevR = Math.sqrt(
    rMultiples.reduce((sum, r) => sum + Math.pow(r - meanR, 2), 0) / rMultiples.length
  );
  const sqn = stdDevR > 0 ? (meanR / stdDevR) * Math.sqrt(closedTrades.length) : 0;

  // Largest win/loss
  const largestWin = wins.length > 0
    ? Math.max(...wins.map(t => t.rMultiple))
    : 0;
  const largestLoss = losses.length > 0
    ? Math.min(...losses.map(t => t.rMultiple))
    : 0;

  // Average holding period
  const avgHoldingDays = closedTrades.reduce((sum, t) => {
    if (t.entryDate && t.exitDate) {
      const days = (new Date(t.exitDate) - new Date(t.entryDate)) / (1000 * 60 * 60 * 24);
      return sum + days;
    }
    return sum;
  }, 0) / closedTrades.length;

  return {
    totalTrades: trades.length,
    openTrades: trades.filter(t => t.status === TradeStatus.OPEN).length,
    closedTrades: closedTrades.length,
    wins: wins.length,
    losses: losses.length,
    breakevens: breakevens.length,
    winRate: Math.round(winRate * 1000) / 10, // e.g., 45.5%
    avgWinR: Math.round(avgWinR * 100) / 100,
    avgLossR: Math.round(avgLossR * 100) / 100,
    expectancy: Math.round(expectancy * 100) / 100,
    expectancyDollar: Math.round(expectancyDollar * 100) / 100,
    totalPL: Math.round(totalPL * 100) / 100,
    sqn: Math.round(sqn * 100) / 100,
    largestWin: Math.round(largestWin * 100) / 100,
    largestLoss: Math.round(largestLoss * 100) / 100,
    avgHoldingDays: Math.round(avgHoldingDays * 10) / 10
  };
}

/**
 * Get SQN quality rating
 *
 * @param {number} sqn - System Quality Number
 * @returns {object} { rating, description, color }
 */
export function getSQNRating(sqn) {
  if (sqn >= 7) {
    return { rating: 'Holy Grail', description: 'Extremely rare, exceptional system', color: 'purple' };
  } else if (sqn >= 5) {
    return { rating: 'Excellent', description: 'Superb system', color: 'green' };
  } else if (sqn >= 3) {
    return { rating: 'Very Good', description: 'Good system worth trading', color: 'lime' };
  } else if (sqn >= 2) {
    return { rating: 'Average', description: 'Tradeable with discipline', color: 'yellow' };
  } else if (sqn >= 1.5) {
    return { rating: 'Below Average', description: 'Difficult to trade profitably', color: 'orange' };
  } else {
    return { rating: 'Poor', description: 'System needs improvement', color: 'red' };
  }
}

/**
 * Load trades from localStorage
 *
 * @returns {Array} Array of trades
 */
export function loadTrades() {
  try {
    const data = localStorage.getItem(STORAGE_KEY);
    if (data) {
      return JSON.parse(data);
    }
  } catch (error) {
    console.error('Error loading trades:', error);
  }
  return [];
}

/**
 * Save trades to localStorage
 *
 * @param {Array} trades - Array of trades to save
 */
export function saveTrades(trades) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(trades));
  } catch (error) {
    console.error('Error saving trades:', error);
  }
}

/**
 * Add a trade and save
 *
 * @param {Array} trades - Current trades array
 * @param {object} newTrade - Trade to add
 * @returns {Array} Updated trades array
 */
export function addTrade(trades, newTrade) {
  const updated = [...trades, newTrade];
  saveTrades(updated);
  return updated;
}

/**
 * Update a trade and save
 *
 * @param {Array} trades - Current trades array
 * @param {string} tradeId - ID of trade to update
 * @param {object} updates - Fields to update
 * @returns {Array} Updated trades array
 */
export function updateTrade(trades, tradeId, updates) {
  const updated = trades.map(t =>
    t.id === tradeId ? { ...t, ...updates } : t
  );
  saveTrades(updated);
  return updated;
}

/**
 * Delete a trade and save
 *
 * @param {Array} trades - Current trades array
 * @param {string} tradeId - ID of trade to delete
 * @returns {Array} Updated trades array
 */
export function deleteTrade(trades, tradeId) {
  const updated = trades.filter(t => t.id !== tradeId);
  saveTrades(updated);
  return updated;
}

/**
 * Export trades to CSV
 *
 * @param {Array} trades - Trades to export
 * @returns {string} CSV string
 */
export function exportToCSV(trades) {
  const headers = [
    'ID', 'Ticker', 'Entry Date', 'Entry Price', 'Stop Price', 'Target Price',
    'Shares', 'Entry Type', 'Pattern', 'Exit Date', 'Exit Price', 'Exit Reason',
    'Status', 'R-Multiple', 'P/L $', 'P/L %', 'Notes'
  ];

  const rows = trades.map(t => [
    t.id,
    t.ticker,
    t.entryDate,
    t.entryPrice,
    t.stopPrice,
    t.targetPrice,
    t.shares,
    t.entryType,
    t.pattern || '',
    t.exitDate || '',
    t.exitPrice || '',
    t.exitReason || '',
    t.status,
    t.rMultiple || '',
    t.profitLoss || '',
    t.profitLossPct || '',
    t.notes || ''
  ]);

  const csvContent = [
    headers.join(','),
    ...rows.map(row => row.map(cell =>
      typeof cell === 'string' && cell.includes(',') ? `"${cell}"` : cell
    ).join(','))
  ].join('\n');

  return csvContent;
}

/**
 * Download trades as CSV file
 *
 * @param {Array} trades - Trades to export
 */
export function downloadTradesCSV(trades) {
  const csv = exportToCSV(trades);
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = `forward_testing_${new Date().toISOString().split('T')[0]}.csv`;
  link.click();
}
