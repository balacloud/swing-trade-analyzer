/**
 * Nearest floor and ceiling for the Trade Setup card (Day 125, Analyze cleanup).
 * Plan: docs/claude/design/ANALYZE_CLEANUP_PLAN_DAY125.md §3.2 + §7.
 *
 * Display only — the S&R engine (support_resistance.py) is unchanged.
 * Widely agreed (not proven) rules this follows: levels are zones, not lines;
 * a level price came back to more than once matters more; keep only a few.
 *
 * - Zone = level ± 0.5%, the engine's own touch band (touch_threshold), so the
 *   zone and the "near it on N days" count describe the same band.
 * - daysNear = srData.meta.levelScores[level.toFixed(2)]: the number of daily
 *   bars (about the last year) whose high or low came within 0.5% of the level.
 *   It is NOT a count of turns. Missing key -> null (never shown as 0).
 * - Projected levels (ATR/Fibonacci, used when no real level exists) are never
 *   shown as a real floor/ceiling.
 */

export const ZONE_PCT = 0.5;

const isNum = (x) => typeof x === 'number' && Number.isFinite(x);

function sideLimitPct(meta, key, fallback) {
  const v = meta?.proximityFilter?.[key];
  return isNum(v) ? Math.round(v * 100) : fallback;
}

function describeSide(levels, { currentPrice, projected, limitPct, meta, isCeiling }) {
  const real = (levels || []).filter((l) => isNum(l) && (isCeiling ? l > currentPrice : l < currentPrice));
  if (projected) {
    const p = real.length ? (isCeiling ? Math.min(...real) : Math.max(...real)) : null;
    return { kind: 'projected', limitPct, projectedPrice: p };
  }
  if (!real.length) return { kind: 'none', limitPct };
  const price = isCeiling ? Math.min(...real) : Math.max(...real);
  const key = price.toFixed(2);
  const scores = meta?.levelScores;
  const daysNear = scores && isNum(scores[key]) ? scores[key] : null;
  const mtf = meta?.mtf?.confluence_map?.[key];
  return {
    kind: 'level',
    limitPct,
    price,
    low: price * (1 - ZONE_PCT / 100),
    high: price * (1 + ZONE_PCT / 100),
    pctAway: Math.abs((price - currentPrice) / currentPrice) * 100,
    daysNear,
    weekly: mtf?.confluent === true,
    weeklyStrength: mtf?.confluent === true ? (mtf.strength_label || null) : null,
  };
}

/**
 * @param {object} srData - /api/sr/<ticker> payload
 * @returns {null | {ceiling, floor, realResistance: number[], realSupport: number[]}}
 */
export function describeKeyLevels(srData) {
  const currentPrice = srData?.currentPrice;
  if (!srData || !isNum(currentPrice) || currentPrice <= 0) return null;
  const meta = srData.meta || {};
  const ceiling = describeSide(srData.resistance, {
    currentPrice, projected: meta.resistanceProjected === true,
    limitPct: sideLimitPct(meta, 'resistancePct', 30), meta, isCeiling: true,
  });
  const floor = describeSide(srData.support, {
    currentPrice, projected: meta.supportProjected === true,
    limitPct: sideLimitPct(meta, 'supportPct', 20), meta, isCeiling: false,
  });
  // Real (non-projected) levels, for the one-line price state.
  const realResistance = meta.resistanceProjected === true ? [] : (srData.resistance || []).filter(isNum);
  const realSupport = meta.supportProjected === true ? [] : (srData.support || []).filter(isNum);
  return { ceiling, floor, realResistance, realSupport };
}

/** "Near" = within 2× ATR (the stock's normal daily noise), as in the old Price Structure card. */
function isNearLevel(currentPrice, level, atr) {
  if (!isNum(level) || !isNum(atr) || atr <= 0) return false;
  return Math.abs(currentPrice - level) <= 2.0 * atr;
}

/**
 * One-line price state (moved from the removed Price Structure card, Day 125).
 * Same 12 rules as before, with two fixes:
 *  - R1/S1 are the NEAREST levels (min above / max below). The old code took
 *    support[0], the deepest support, because the API sends support ascending
 *    (Day 112 BUG-B, fixed then only in the card's level list — Fable #4).
 *  - Missing trend data returns null (no line) instead of counting as 0 and
 *    reading "Downtrend".
 * Pass only real levels (describeKeyLevels().realResistance/realSupport).
 *
 * @returns {null | {state: string, color: string, rule: number}}
 */
export function deriveStructureState(currentPrice, resistance, support, trendCriteria, adx, atr, limits = {}) {
  // Levels arrive proximity-filtered (resistance within 30% above, support within 20% below),
  // so "none" means none in that window, not none at all (Fable code review #3).
  const resPct = isNum(limits.resistancePct) ? limits.resistancePct : 30;
  const supPct = isNum(limits.supportPct) ? limits.supportPct : 20;
  if (!isNum(currentPrice) || !isNum(trendCriteria)) return null;
  const above = (resistance || []).filter((l) => isNum(l) && l > currentPrice);
  const below = (support || []).filter((l) => isNum(l) && l < currentPrice);
  const R1 = above.length ? Math.min(...above) : null;
  const S1 = below.length ? Math.max(...below) : null;
  const tt = trendCriteria;
  const adxVal = isNum(adx?.adx) ? adx.adx : null;

  if (!R1 && !S1) return { state: 'Insufficient data', color: 'gray', rule: 1 };
  if (!R1 && S1) {
    if (tt >= 5) return { state: `No resistance within ${resPct}% above — strong trend`, color: 'green', rule: 2 };
    return { state: `No resistance within ${resPct}% above — weak trend`, color: 'yellow', rule: 2 };
  }
  if (R1 && !S1) return { state: `No support within ${supPct}% below`, color: 'red', rule: 3 };
  if (isNearLevel(currentPrice, R1, atr) && isNearLevel(currentPrice, S1, atr)) {
    return { state: 'Compression — range narrowing', color: 'yellow', rule: 4 };
  }
  if (tt >= 7) {
    if (isNearLevel(currentPrice, R1, atr)) return { state: 'Uptrend testing resistance', color: 'green', rule: 5 };
    if (isNearLevel(currentPrice, S1, atr)) return { state: 'Uptrend pulling back to support', color: 'green', rule: 6 };
    return { state: 'Uptrend — between levels', color: 'green', rule: 7 };
  }
  if (tt >= 4) {
    if (isNearLevel(currentPrice, S1, atr)) return { state: 'Weakening trend — testing support', color: 'yellow', rule: 8 };
    if (isNearLevel(currentPrice, R1, atr)) return { state: 'Transitioning — testing resistance', color: 'yellow', rule: 9 };
    return { state: 'Mixed trend — between levels', color: 'yellow', rule: 10 };
  }
  if (adxVal == null) return null;   // can't tell choppy from downtrend without ADX
  if (adxVal < 15) return { state: 'Choppy — no clear trend', color: 'red', rule: 11 };
  return { state: 'Downtrend', color: 'red', rule: 12 };
}
