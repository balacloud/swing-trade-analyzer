/**
 * Shared Risk/Reward Calculator
 * Day 61: Extracted from 4 duplicated locations to single source of truth
 *
 * Used by: App.jsx (viability badge + contradiction), DecisionMatrix.jsx, BottomLineCard.jsx
 *
 * Pullback entry: Buy at nearest support, stop 2×ATR below support
 * Momentum entry: Buy at current price, stop 1.5×ATR below support
 */

/**
 * Calculate R:R for both pullback and momentum entry types
 *
 * @param {object} srData - Support/Resistance data from backend
 * @param {number} currentPrice - Current stock price
 * @returns {object} { pullbackRR, momentumRR, pullbackViable, momentumViable, anyViable, nearestSupport, target, atr }
 */
export function calculateRiskReward(srData, currentPrice) {
  const nearestSupport = srData?.support?.length > 0 ? Math.max(...srData.support) : null;
  const atr = srData?.meta?.atr || 0;
  const target = srData?.suggestedTarget || (currentPrice ? currentPrice * 1.10 : 0);

  // Pullback R:R: entry at support, stop 2×ATR below
  const pullbackEntry = nearestSupport;
  const pullbackStop = nearestSupport ? nearestSupport - (atr * 2) : 0;
  const pullbackRisk = pullbackEntry ? pullbackEntry - pullbackStop : 0;
  const pullbackReward = pullbackEntry ? target - pullbackEntry : 0;
  const pullbackRR = pullbackRisk > 0 ? pullbackReward / pullbackRisk : 0;

  // Momentum R:R: entry at current price, stop 1.5×ATR below support
  const momentumStop = nearestSupport ? nearestSupport - (atr * 1.5) : 0;
  const momentumRisk = currentPrice && momentumStop ? currentPrice - momentumStop : 0;
  const momentumReward = currentPrice ? target - currentPrice : 0;
  const momentumRR = momentumRisk > 0 ? momentumReward / momentumRisk : 0;

  const pullbackViable = pullbackRR >= 1.0;
  const momentumViable = momentumRR >= 1.0;

  return {
    pullbackRR,
    momentumRR,
    pullbackViable,
    momentumViable,
    anyViable: pullbackViable || momentumViable,
    nearestSupport,
    target,
    atr,
    // Pre-computed stop prices for display
    pullbackStop,
    momentumStop,
    pullbackRisk,
    pullbackReward,
    momentumRisk,
    momentumReward,
  };
}

/**
 * Detect contradiction between backend viability and frontend R:R
 * Backend says "structurally sound" but both R:R < 1.0
 *
 * @param {object} srData - S&R data with meta.tradeViability
 * @param {object} rr - Result from calculateRiskReward()
 * @returns {boolean} true if contradiction detected
 */
export function hasViabilityContradiction(srData, rr) {
  const backendViable = srData?.meta?.tradeViability?.viable;
  return backendViable === 'YES' && !rr.anyViable;
}

/**
 * Get viability badge label for Trade Setup card
 *
 * @param {object} rr - Result from calculateRiskReward()
 * @returns {{ label: string, bg: string, icon: string }}
 */
export function getViabilityBadge(rr) {
  if (rr.pullbackViable && rr.momentumViable) {
    return { label: 'BOTH VIABLE', bg: 'bg-green-600', icon: '✅' };
  } else if (rr.pullbackViable) {
    return { label: 'PULLBACK OK', bg: 'bg-green-700', icon: '✅' };
  } else if (rr.momentumViable) {
    return { label: 'MOMENTUM OK', bg: 'bg-blue-600', icon: '✅' };
  }
  return { label: 'NOT VIABLE', bg: 'bg-red-600', icon: '🚫' };
}
