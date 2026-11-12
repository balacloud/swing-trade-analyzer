/**
 * Shared Risk/Reward Calculator
 * Day 61: Extracted from 4 duplicated locations to single source of truth
 *
 * Used by: components/PullbackPlan.jsx (Trade Setup card)
 *
 * Pullback plan: buy at the nearest support, stop 2×ATR below it, target the
 * nearest resistance (backend `suggestedTarget`, which is a projection when
 * `meta.resistanceProjected` is true).
 * Day 83: removed a stale "max stop cap: 7% from entry" claim — that cap
 * belongs to the backtest's own position-sizing layer (trade_simulator.py),
 * not this function, which is purely ATR-based with a $0.01 floor.
 * Day 123 (redesign Step 3): momentum plan, viability flags and the
 * getViabilityBadge / hasViabilityContradiction helpers removed with the
 * momentum panel (STA's momentum system failed every test). The
 * `currentPrice * 1.10` target fallback is gone too — it invented a target
 * when no resistance was found (Code Architecture Rule 6); target is now null.
 */

/**
 * Calculate the pullback plan's levels and reward:risk.
 *
 * Day 123 (engineering-standard pass): every outcome carries an explicit
 * `state` so the card can say *why* something is missing instead of hiding
 * or inventing it. Never throws.
 *   'no_data'    — srData is null (the /api/sr fetch failed)
 *   'no_support' — no support level below today's price
 *   'no_atr'     — support found but ATR missing/zero, so no stop can be placed
 *                  (was `atr || 0`, which put the stop on the buy price)
 *   'ok'         — full plan
 *
 * @param {object|null} srData - Support/Resistance data from backend
 * @returns {object} { state, entry?, stop?, target?, atr?, risk?, reward?, rr?, targetProjected? }
 *   target/reward/rr are null when the backend found no resistance target.
 */
export function calculateRiskReward(srData) {
  if (srData == null) return { state: 'no_data' };

  const supports = Array.isArray(srData.support) ? srData.support.filter(Number.isFinite) : [];
  if (supports.length === 0) return { state: 'no_support' };

  const entry = Math.max(...supports);
  const target = Number.isFinite(srData.suggestedTarget) ? srData.suggestedTarget : null;
  const targetProjected = srData.meta?.resistanceProjected === true;
  const atr = srData.meta?.atr;

  if (!Number.isFinite(atr) || atr <= 0) {
    return { state: 'no_atr', entry, stop: null, target, atr: null, risk: null, reward: null, rr: null, targetProjected };
  }

  // Floor at $0.01 — stop price can never be negative or zero
  const stop = Math.max(0.01, entry - (atr * 2));
  const risk = entry - stop;
  const reward = target != null ? target - entry : null;
  const rr = reward != null && risk > 0 ? reward / risk : null;

  return { state: 'ok', entry, stop, target, atr, risk, reward, rr, targetProjected };
}
