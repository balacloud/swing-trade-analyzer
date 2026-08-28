/**
 * Shared volume-confirmation threshold + read
 *
 * Day 111: a Day 107 backtest spike tried gating trades on entry-day volume
 * >=1.5x the 50-day average — it cut the trade sample 75->5, too strict to
 * evaluate. Same failure shape as the original Fundamentals/R:R/Regime gates
 * (Analyze Page Redesign, Day 109-110): a noisy signal used as a hard gate
 * throws away good setups. Fix is the same one already applied to those:
 * stop gating, surface the number as plain information instead.
 *
 * The 1.5x figure itself is NOT new here — it's the same ratio already used
 * by pattern_detection.py's check_breakout_quality() and
 * backtest_holistic.py's VOLUME_CONFIRM_RATIO. Those are separate Python
 * literals (frontend/backend can't share a JS module), so this is the single
 * frontend definition — previously duplicated as a module-local constant
 * inside priceStructureNarrative.js, now centralized here (same reason
 * liquidityThresholds.js exists: Day 83, one place instead of drifting
 * copies).
 *
 * Deliberately excluded: breakout_detection.py's rvol_confirm (also 1.50) —
 * that one measures against a 20-day average, a different question, not the
 * same threshold despite sharing a value.
 */
export const BREAKOUT_VOLUME_THRESHOLD = 1.5;

/**
 * Pure, non-gating read of relative volume. Never returns a color, a
 * className, or a pass/fail boolean — this is informational only and must
 * not be used to gate, suppress, or rank anything.
 */
export function getVolumeConfirmationRead(rvol) {
  if (rvol == null || Number.isNaN(rvol)) return null;

  const r = rvol.toFixed(2);
  let band, text;

  if (rvol >= BREAKOUT_VOLUME_THRESHOLD) {
    band = 'confirming';
    text = `Volume: ${r}× the 50-day average — real participation behind this move`;
  } else if (rvol >= 1.0) {
    band = 'normal';
    text = `Volume: ${r}× the 50-day average — about typical participation`;
  } else {
    band = 'light';
    text = `Volume: ${r}× the 50-day average — below-average, worth noting`;
  }

  return { ratio: rvol, band, text };
}

/**
 * Day 112: close-location bands for the directional-lean read below.
 * 0.75 mirrors breakout_detection.py's strong_close line (:230) so the app
 * uses one vocabulary for "closed near the high." 0.25 is its symmetric
 * mirror — the engine's own weak-side line is 0.50, but that's paired with
 * a separate upper-wick condition (rejection_candle, :236), not reusable
 * standalone, so 0.25 is deliberately a stricter, independent choice.
 */
export const CLOSE_LOCATION_STRONG = 0.75;
export const CLOSE_LOCATION_WEAK = 0.25;
const DAY_CHANGE_FLAT_PCT = 0.1;

/**
 * Non-gating directional LEAN from three daily-bar signals (day's price
 * change, where it closed inside the day's range, OBV trend). Daily bars
 * cannot show whether volume was buying or selling — that needs order-flow
 * data this app doesn't have. This returns a lean, never a verdict: no
 * color, no boolean, no ranking, never gates anything, including the
 * magnitude read above.
 *
 * Aggregation: each available signal casts +1 (bullish) / -1 (bearish) / 0
 * (neutral). If both a +1 and a -1 are present, that's 'mixed' regardless of
 * sum — a real disagreement is the most informative state, not noise to
 * average away. Otherwise |sum| >= 2 required for a 'buying'/'selling' lean;
 * missing signals degrade gracefully (with only 2 available, both must
 * agree; with 0-1 available, always 'none').
 *
 * @param {object}  args
 * @param {?number} args.changePct     - srData.change (% vs prior close)
 * @param {?number} args.closeLocation - srData.meta.candle.closeLocation (0..1)
 * @param {?string} args.obvTrend      - srData.meta.obv.trend: 'rising'|'falling'|'flat'
 * @returns {?{lean:'buying'|'selling'|'mixed'|'none', text:string}}
 *          null when no signal is available at all — render nothing, not a
 *          claim about missing data.
 */
export function getVolumeDirectionRead({ changePct, closeLocation, obvTrend }) {
  const votes = [];
  const parts = [];

  if (typeof changePct === 'number' && Number.isFinite(changePct)) {
    if (changePct > DAY_CHANGE_FLAT_PCT) { votes.push(1); parts.push(`closed up ${changePct.toFixed(1)}%`); }
    else if (changePct < -DAY_CHANGE_FLAT_PCT) { votes.push(-1); parts.push(`closed down ${Math.abs(changePct).toFixed(1)}%`); }
    else { votes.push(0); parts.push('closed flat'); }
  }

  if (typeof closeLocation === 'number' && Number.isFinite(closeLocation)) {
    if (closeLocation >= CLOSE_LOCATION_STRONG) { votes.push(1); parts.push("settled near the day's high"); }
    else if (closeLocation <= CLOSE_LOCATION_WEAK) { votes.push(-1); parts.push("near the day's low"); }
    else { votes.push(0); parts.push('mid-range'); }
  }

  if (obvTrend === 'rising') { votes.push(1); parts.push('OBV rising'); }
  else if (obvTrend === 'falling') { votes.push(-1); parts.push('OBV falling'); }
  else if (obvTrend === 'flat') { votes.push(0); parts.push('OBV flat'); }
  // any other obvTrend value (or meta.obv absent/null) casts no vote

  if (votes.length === 0) return null;

  const hasConflict = votes.includes(1) && votes.includes(-1);
  const score = votes.reduce((a, b) => a + b, 0);

  let lean, tail;
  if (hasConflict) { lean = 'mixed'; tail = 'mixed signals, no clear lean'; }
  else if (score >= 2) { lean = 'buying'; tail = 'leans toward buying pressure'; }
  else if (score <= -2) { lean = 'selling'; tail = 'leans toward selling pressure'; }
  else { lean = 'none'; tail = 'no clear lean either way'; }

  return { lean, text: `${parts.join(', ')} — ${tail}` };
}
