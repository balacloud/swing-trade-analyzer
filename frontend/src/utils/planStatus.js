/**
 * Is the Trade Setup plan already behind the live price? (Day 133)
 * Plan: docs/claude/design/PLAN_VOID_BELOW_SUPPORT_PLAN_DAY133.md (Opus review applied).
 *
 * The plan (Buy / Stop / Target) is built from completed bars and does NOT move with live ticks
 * (Day 126 decision). That fails when the price falls THROUGH the plan: a "wait for a dip to support"
 * Buy that sits above the market cannot be filled. This helper says so, in numbers only: no verdict
 * words, and no new threshold (only the plan's own levels are used).
 *
 * Rule (one place, Golden Rule 59):
 *   - void 'below_support': a usable live price is strictly below the nearest support zone's LOW.
 *   - void 'below_stop':    no support zone is known (legacy payload) and the live price is strictly below the plan's stop.
 *   - only the `live` and `recent` quote states can void a plan. `pre` / `post` quotes are thin and have no
 *     age limit, so they give `factOnly` (a muted line, no void styling).
 * Equal to the zone low is NOT void. A missing or unusable input returns void:false, never throws.
 */
import { calculateRiskReward } from './riskRewardCalc';
import { basisLabel, formatCloseDate } from './liveQuote';

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);
const NONE = { void: false, factOnly: false, reason: null, zoneLow: null, zoneHigh: null, belowStop: false, livePrice: null };

/**
 * @param {{stop:?number, zones:?Array, livePrice:?number, liveState:?string}} args
 * @returns {{void:boolean, factOnly:boolean, reason:?('below_support'|'below_stop'), zoneLow:?number, zoneHigh:?number, belowStop:boolean, livePrice:?number}}
 */
export function planStatus(args) {
  try {
    const { stop = null, zones = null, livePrice = null, liveState = null } = args || {};
    if (!isNum(livePrice) || livePrice <= 0) return NONE;
    const usable = liveState === 'live' || liveState === 'recent';
    const thin = liveState === 'pre' || liveState === 'post';
    if (!usable && !thin) return NONE;                     // closed / unavailable / unknown: the card stays as it was

    const zone = (Array.isArray(zones) ? zones : []).find((z) => z && z.nearest === true && z.side === 'support' && isNum(z.low) && isNum(z.high));
    const belowStop = isNum(stop) && livePrice < stop;
    let reason = null;
    if (zone && livePrice < zone.low) reason = 'below_support';
    else if (!zone && belowStop) reason = 'below_stop';
    if (!reason) return NONE;

    return {
      void: usable, factOnly: thin, reason,
      zoneLow: zone ? zone.low : null, zoneHigh: zone ? zone.high : null,
      belowStop, livePrice,
    };
  } catch (e) {
    console.warn('[STA][planStatus] could not evaluate, plan shown as before', e);
    return NONE;
  }
}

/**
 * The card's own "last close": the last COMPLETED bar (PullbackPlan.jsx measures from the same one).
 * Taken from /api/sr, not from the quote, so the card and its note agree to the cent (Golden Rule 63).
 */
export function lastCompletedClose(srData) {
  const meta = srData?.meta;
  const forming = meta?.candle?.barComplete === false;
  const price = forming && isNum(meta?.prevBar?.close) ? meta.prevBar.close : srData?.currentPrice;
  const date = forming ? meta?.prevBar?.date : meta?.candle?.date;
  return { price: isNum(price) ? price : null, dateLabel: formatCloseDate(date) };
}

/**
 * Everything the two cards need, computed once in App.jsx.
 * @param {object|null} srData /api/sr answer
 * @param {object|null} live   useLiveQuote() result (utils/liveQuote.describeLiveQuote)
 */
export function planStatusFromSr(srData, live) {
  const plan = calculateRiskReward(srData);
  const none = { ...NONE, close: null, tradeTime: null, basis: null, levelsPrice: null };
  // The card shows no plan in these states (PullbackPlan.jsx: no_data / no_support / no_price), so there is nothing for the live price to be "behind"
  // (found in the Day 133 edge-case pass: the Key Levels note appeared next to "no pullback plan").
  if (plan.state === 'no_data' || plan.state === 'no_support' || lastCompletedClose(srData).price == null) return none;
  const st = planStatus({
    stop: isNum(plan.stop) ? plan.stop : null,
    zones: srData?.meta?.zones,
    livePrice: live?.price,
    liveState: live?.state,
  });
  if (!st.void && !st.factOnly) return { ...st, close: null, tradeTime: null, basis: null, levelsPrice: null };
  return {
    ...st,
    close: lastCompletedClose(srData),
    tradeTime: live?.tradeTime || null,
    basis: basisLabel(live),
    // the price the levels (zones, "Price is ...") were measured at when the page loaded; mid-session this can be a forming bar
    levelsPrice: isNum(srData?.currentPrice) ? srData.currentPrice : null,
    levelsAreCompletedBar: srData?.meta?.candle?.barComplete !== false,
  };
}
