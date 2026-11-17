/**
 * Nearest support and resistance for the Trade Setup card (Day 125 cleanup,
 * rebuilt Day 126 on the simple S&R engine).
 * Plans: docs/claude/design/SIMPLE_SR_PLAN_DAY125.md, SIMPLE_SR_SWITCH_PLAN_DAY126.md §2.
 *
 * Display only. Reads /api/sr `meta.zones` (backend/simple_sr.py): swing highs/lows
 * grouped into zones, nearest zone below/at price and nearest above. Each zone has
 * { low, high, mid, swings, side, insideZone, nearest }.
 * - `swings` = how many times price turned there ("turned here N×"). One turn is a
 *   real level too; the user judges whether it is enough, nothing here ranks it.
 * - Distance is to the zone edge nearest price (support: its high, resistance: its low),
 *   the same edge the Buy and Target use (Golden Rule 63: one label, one number).
 * - No projected/ATR/Fibonacci levels exist on this engine. Missing zones are never
 *   replaced with a made-up level.
 * Common trader rules, not tested.
 */

import { formatMoney } from './formatMoney.js';   // explicit extension: the page-check scripts load this file with plain node ESM

const isNum = (x) => typeof x === 'number' && Number.isFinite(x);

/** "$94.00 – $95.10", or one price when the zone is a single price. Shared with the page checker (A10). */
export function formatZoneRange(low, high) {
  const m = (x) => formatMoney(x);   // Day 126: the page's one money format (commas, half-up)
  return m(low) === m(high) ? m(low) : `${m(low)} – ${m(high)}`;
}

function sideLimitPct(meta, key, fallback) {
  const v = meta?.proximityFilter?.[key];
  return isNum(v) ? Math.round(v * 100) : fallback;
}

function describeSide(zones, side, { currentPrice, limitPct }) {
  const z = zones.find((q) => q && q.nearest === true && q.side === side && isNum(q.low) && isNum(q.high));
  if (!z) return { kind: 'none', limitPct };
  const isCeiling = side === 'resistance';
  const edge = isCeiling ? z.low : z.high;
  const inside = z.insideZone === true && !isCeiling;
  return {
    kind: inside ? 'inside' : 'level',
    limitPct,
    low: z.low,
    high: z.high,
    edge,
    swings: isNum(z.swings) ? z.swings : null,
    pctAway: inside ? 0 : Math.abs((edge - currentPrice) / currentPrice) * 100,
  };
}

/**
 * @param {object} srData - /api/sr/<ticker> payload
 * @returns {null | {unavailable: true} | {ceiling, floor, realResistance: number[], realSupport: number[], insideSupport: boolean, nearHigh52w: boolean}}
 *   null: no srData or no price (the card above already says why).
 *   {unavailable}: srData arrived without `meta.zones` (an old-format response); the card says so.
 */
export function describeKeyLevels(srData) {
  const currentPrice = srData?.currentPrice;
  if (!srData || !isNum(currentPrice) || currentPrice <= 0) return null;
  const meta = srData.meta || {};
  if (!Array.isArray(meta.zones)) return { unavailable: true };
  const ceiling = describeSide(meta.zones, 'resistance', { currentPrice, limitPct: sideLimitPct(meta, 'resistancePct', 30) });
  const floor = describeSide(meta.zones, 'support', { currentPrice, limitPct: sideLimitPct(meta, 'supportPct', 20) });
  return {
    ceiling,
    floor,
    realResistance: (srData.resistance || []).filter(isNum),
    realSupport: (srData.support || []).filter(isNum),
    insideSupport: floor.kind === 'inside',
    nearHigh52w: meta.nearHigh52w === true,
  };
}

/**
 * Where a zone sits on a price bar, as percentages of the bar's width.
 * The bar's price scale runs from scaleLo to scaleHi (the same scale the Stop/Buy/Target/Now
 * ticks use). A zone partly outside is clipped; entirely outside, or bad input -> null
 * (the zone is simply not shaded; its row still lists it).
 * @returns {null | {left: number, width: number}}
 */
export function zoneSpan(zone, scaleLo, scaleHi) {
  if (!zone || !isNum(zone.low) || !isNum(zone.high) || !isNum(scaleLo) || !isNum(scaleHi) || scaleHi <= scaleLo) return null;
  const p = (v) => ((v - scaleLo) / (scaleHi - scaleLo)) * 100;
  const left = Math.max(0, p(Math.min(zone.low, zone.high)));
  const right = Math.min(100, p(Math.max(zone.low, zone.high)));
  if (right <= 0 || left >= 100 || right < left) return null;
  // A one-price zone would be invisible; give it a 0.6% sliver so it can still be seen.
  const width = Math.max(right - left, 0.6);
  return { left, width };
}

/** "Near" = inside the zone, or within 2× ATR (the stock's normal daily noise) of its edge. */
function isNearLevel(currentPrice, level, atr) {
  if (!isNum(level) || !isNum(atr) || atr <= 0) return false;
  return Math.abs(currentPrice - level) <= 2.0 * atr;
}

/**
 * One-line price state (moved from the removed Price Structure card, Day 125).
 * Same 12 rules as before, with these fixes:
 *  - R1/S1 are the NEAREST levels (min above / max below). The old code took
 *    support[0], the deepest support (Day 112 BUG-B, Fable #4).
 *  - Missing trend data returns null (no line) instead of counting as 0 and reading "Downtrend".
 *  - Day 126: `limits.insideSupport` = price is inside the nearest support zone, so S1 is
 *    the price itself (distance 0, "near"). The zone edge (its high) is above price and
 *    would otherwise be filtered out as "not below".
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
  const S1 = limits.insideSupport === true ? currentPrice : (below.length ? Math.max(...below) : null);
  const tt = trendCriteria;
  const adxVal = isNum(adx?.adx) ? adx.adx : null;

  if (!R1 && !S1) return { state: 'Insufficient data', color: 'gray', rule: 1 };
  if (!R1 && S1) {
    // Day 126 (Statement Audit): numbers, not "strong/weak trend" verdict words
    if (tt >= 5) return { state: `No resistance within ${resPct}% above · ${tt} of 8 trend checks pass`, color: 'green', rule: 2 };
    return { state: `No resistance within ${resPct}% above · ${tt} of 8 trend checks pass`, color: 'yellow', rule: 2 };
  }
  if (R1 && !S1) return { state: `No support within ${supPct}% below`, color: 'red', rule: 3 };
  if (isNearLevel(currentPrice, R1, atr) && isNearLevel(currentPrice, S1, atr)) {
    return { state: 'Close to both support and resistance', color: 'yellow', rule: 4 };   // Day 126: nothing measures "narrowing"; the rule is only "near both"
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
  // Day 126: ADX has no direction, so "Downtrend" over-read it; the state quotes the two numbers it rests on
  if (adxVal < 15) return { state: `${tt} of 8 trend checks pass · ADX ${adxVal.toFixed(1)}, under 15`, color: 'red', rule: 11 };
  return { state: `${tt} of 8 trend checks pass · ADX ${adxVal.toFixed(1)}`, color: 'red', rule: 12 };
}
