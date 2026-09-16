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
    text = `${r}× the 50-day average — real participation behind this move`;
  } else if (rvol >= 1.0) {
    band = 'normal';
    text = `${r}× the 50-day average — about typical participation`;
  } else {
    band = 'light';
    text = `${r}× the 50-day average — below-average, worth noting`;
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

/**
 * Day 116: the 20-session effort-vs-result read, rendered as a sentence.
 *
 * This computes NOTHING new. backend.py's calculate_obv() (added Day 49) has
 * always produced exactly the Wyckoff "effort vs. result" comparison — 20-day
 * price change % against 20-day OBV change % — and already emits
 * 'Bearish divergence - distribution warning' (price up, net volume leaving)
 * and 'Weak trend - price rising without volume support'. It was reachable
 * only through the hover tooltip on the small OBV arrow chip. This function
 * is a presentation adapter: it surfaces a field that already crosses the
 * API, it does not derive a new one.
 *
 * Kept separate from getVolumeConfirmationRead/getVolumeDirectionRead above
 * rather than merged into them: those two describe TODAY'S bar, this one
 * describes the last 20 sessions. Same deliberate non-merge as this file's
 * exclusion of breakout_detection.py's rvol_confirm (see the header comment)
 * — a shared arithmetic shape is not a shared question, and collapsing the
 * horizons would make "20-day accumulation fine, today weak" unsayable.
 *
 * Deliberately prints ONLY the backend's own `signal` sentence rather than
 * also deriving a "net volume rising/falling N%" headline from
 * obv_change_pct: that headline and `trend` can genuinely disagree in sign
 * on the same ticker (trend is position-vs-20-day-average, obv_change_pct is
 * endpoint-to-endpoint), which would print two contradicting OBV directions
 * on the same card. `signal` is the one field with a single, coherent story.
 *
 * @param {?object} obv - srData.meta.obv, i.e. calculate_obv()'s dict:
 *                        {obv, obv_prev, obv_change_pct, trend, divergence, signal}
 * @returns {?{divergence:'bullish'|'bearish'|'none', text:string}}
 *          null when meta.obv is absent (calculate_obv returns None on <21
 *          bars or any internal error) — render nothing, not a claim about
 *          missing data. Same convention as getVolumeDirectionRead.
 */
export function getObvHorizonRead(obv) {
  if (!obv || typeof obv.signal !== 'string') return null;

  // Lowercase the backend's leading capital and normalize its " - " clause
  // separator to an em dash for inline reading, without touching the words.
  const text = obv.signal.replace(/^[A-Z]/, (c) => c.toLowerCase()).replace(' - ', ' — ');

  return { divergence: obv.divergence || 'none', text };
}

/**
 * Day 116: same-day effort vs. result — the classic Wyckoff check, on ONE
 * bar (today's if complete, otherwise the last complete one — see
 * `barComplete`/`asOf` below). Additive to, and deliberately separate from,
 * the two reads above and from getObvHorizonRead's 20-session view.
 *
 * Why this is not already covered. calculate_obv() has always done
 * effort-vs-result over a 20-SESSION window and does it well. What no
 * existing read does is cross ONE DAY'S effort (rvol) against that SAME
 * day's result (price progress) — getVolumeConfirmationRead computes the
 * magnitude and getVolumeDirectionRead computes the direction, but they are
 * computed independently and never checked against each other. That gap is
 * the breakout-day case this was built for: heavy volume with no price
 * progress is a warning, not confirmation (Wyckoff's effort-vs-result).
 *
 * RESULT is normalized by ATR, not a raw %: a 1.0% day is a large move for a
 * low-volatility name and a rounding error for a high-volatility one. Caller
 * passes atrPct = meta.atr (a dollar value) / price * 100.
 *
 * THRESHOLDS ARE FIRST-PRINCIPLES, NOT BACKTESTED, and the returned text
 * says so. 1.5 reuses BREAKOUT_VOLUME_THRESHOLD above (one definition, Day
 * 111's whole point). 0.5/1.0 ATR for "little"/"real" progress are chosen,
 * not derived — a Day 107 backtest spike already showed that turning a
 * volume number into a hard rule cut the trade sample 75->5, which is
 * exactly why this returns a SENTENCE and not a score. Must never gate.
 *
 * PARTIAL-BAR HONESTY (why this takes barComplete/asOf at all). meta.rvol is
 * computed from the still-forming intraday bar with no guard — measured
 * 2026-09-15 mid-session: RVOL median 0.45 on the forming bar vs 0.92 on the
 * prior complete one. An effort read on a half-formed bar would call
 * everything "light volume" every day. So when barComplete is false the
 * caller passes the last COMPLETE bar's numbers (meta.prevBar) and this
 * function says which date it is describing.
 *
 * Non-gating, per this file's standing contract: no color, no className, no
 * boolean, no score. `state` is a descriptive string for copy selection and
 * test assertions only, never a pass/fail. No code path from here reaches
 * the verdict, the score, or the Simple Checklist.
 *
 * @param {object}   args
 * @param {?number}  args.rvol          - relative volume for the bar described
 * @param {?number}  args.changePct     - that bar's close vs. prior close, %
 * @param {?number}  args.atrPct        - meta.atr / price * 100
 * @param {?number}  args.closeLocation - (close-low)/(high-low), 0..1
 * @param {boolean} [args.barComplete]  - false => `asOf` describes a prior session
 * @param {?string}  [args.asOf]        - date of the bar described, e.g. '2026-09-12'
 * @returns {?{state:string, text:string}}
 *          null when effort or result is unavailable — render nothing.
 */
export const EFFORT_RESULT_LITTLE_PROGRESS_ATR = 0.5;
export const EFFORT_RESULT_REAL_PROGRESS_ATR = 1.0;

export function getEffortVsResultRead({ rvol, changePct, atrPct, closeLocation, barComplete = true, asOf = null }) {
  const haveEffort = typeof rvol === 'number' && Number.isFinite(rvol);
  const haveResult = typeof changePct === 'number' && Number.isFinite(changePct)
    && typeof atrPct === 'number' && Number.isFinite(atrPct) && atrPct > 0;
  if (!haveEffort || !haveResult) return null;

  const progressAtr = Math.abs(changePct) / atrPct;
  const heavy = rvol >= BREAKOUT_VOLUME_THRESHOLD;
  const little = progressAtr <= EFFORT_RESULT_LITTLE_PROGRESS_ATR;
  const real = progressAtr >= EFFORT_RESULT_REAL_PROGRESS_ATR;

  const effortStr = `${rvol.toFixed(2)}× volume`;
  const resultStr = `${progressAtr.toFixed(2)}× its own ATR of price progress`;

  let state, tail;
  if (heavy && little) {
    state = 'effort_without_result';
    tail = 'heavy participation, little price progress — effort without result, historically a warning rather than confirmation';
  } else if (heavy && real) {
    state = 'effort_with_result';
    tail = closeLocation != null && closeLocation >= CLOSE_LOCATION_STRONG
      ? "real volume behind a real move, and it held into the close — effort and result agree"
      : 'real volume behind a real move — effort and result agree';
  } else if (!heavy && real) {
    state = 'result_without_effort';
    tail = 'a real move on unremarkable volume — the move is there, the participation behind it is not';
  } else if (!heavy && little) {
    state = 'quiet';
    tail = 'quiet on both counts — nothing to read here either way';
  } else {
    state = 'mid';
    tail = 'in between on both counts — no clear effort/result story';
  }

  const stamp = barComplete
    ? ''
    : ` (last completed session${asOf ? `, ${asOf}` : ''} — today's bar is still forming, so today's volume isn't comparable yet)`;

  return { state, text: `${effortStr} for ${resultStr}${stamp} — ${tail} (thresholds are first-principles, not backtested)` };
}
