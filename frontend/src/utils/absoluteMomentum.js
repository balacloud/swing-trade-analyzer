/**
 * Absolute momentum — dual momentum's second leg. Informational read only.
 *
 * Antonacci, Dual Momentum Investing (2014): relative strength is half the
 * rule. A stock can be the strongest name in a falling market and still lose
 * money, so the second leg asks whether the stock's OWN trailing return beat
 * a risk-free/cash return in absolute terms. STA has gated on the first leg
 * since Day 27 (simplifiedScoring.js Criterion 2, RS >= 1.0) and has never
 * had the second leg anywhere, gated or informational. This adds it as a
 * sentence a human reads. It is NOT a gate, and that is a closed decision:
 *
 * WHY NOT A GATE. Day 107's pre-committed research spike backtested exactly
 * this filter as Config G (backtest_holistic.py:491-501) — Config C plus
 * "trailing 252-day return > 5% risk-free proxy" — 400 tickers, seed 42,
 * 2020-2025, survivorship-free. Stored result:
 * backend/backtest_results_holistic/research_spike_volume_momentum_20260813_202107.json
 * — Config C 75 trades, Config G 74. It excluded exactly ONE trade. Day 111
 * closed the item "correct but pointless" (KNOWN_ISSUES_DAY110.md:336-342).
 *
 * WHY IT IS NEAR-INERT, ALGEBRAICALLY. The RS gate is
 * (1+stockRet)/(1+spyRet) >= 1.0, i.e. exactly stockRet >= spyRet. So
 * whenever SPY's own trailing 252-day return already clears the cash bar,
 * passing the RS gate ALREADY implies clearing this one — this read can only
 * say something new when SPY's own trailing year is below the bar. Measured
 * on 24 years of SPY (6,038 sessions, 2002-09-17..2026-09-16): SPY's trailing
 * 252-day return was under 5% on 24.7% of days and under 0% on 17.2%. So this
 * read is expected to agree with the gate roughly 3 days in 4 and to be the
 * one thing on the page that speaks up in the 4th. When SPY's year is strong,
 * every RS-passing ticker reading "clears the bar" is correct, not a bug.
 *
 * THE THRESHOLD. 5.0 is not chosen here. It is the same number
 * backtest_holistic.py:108 used for the Config G run above
 * (ABSOLUTE_MOMENTUM_RISK_FREE_RATE = 0.05, itself mirroring metrics.py:68's
 * compute_metrics(risk_free_rate=0.05) default). Frontend and backend can't
 * share a module, so this is the single frontend definition — same situation
 * and same handling as BREAKOUT_VOLUME_THRESHOLD (volumeThresholds.js:24).
 * It is a STATIC PROXY, not a live T-bill yield: STA has no risk-free-rate
 * feed, and adding one would be a new data dependency, not a display change.
 * Antonacci's literal bar is the 3-month T-bill (see
 * docs/research/TRADING_PRINCIPLES_100YR_RESEARCH.md:112), not zero; 5% is a
 * stale approximation of the right bar, 0% would be a different rule. The
 * text always prints the actual signed return, so a reader who prefers the
 * plain zero line can read it straight off the sentence.
 *
 * Day 117: docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md
 */
export const ABSOLUTE_MOMENTUM_CASH_PCT = 5.0;

/**
 * Pure, non-gating read of a stock's own ~1-year absolute return.
 *
 * Never returns a color, a className, or a pass/fail boolean — informational
 * only, and must not be used to gate, suppress, rank, or score anything. No
 * code path from here reaches the verdict, any score, or the Simple
 * Checklist's pass/fail outcome or passCount. `state` is a descriptive string
 * for copy selection and test assertions only, never a verdict.
 *
 * Deliberately says NOTHING about relative strength. Its two call sites sit
 * under different RS contexts (the Simple Checklist's RS >= 1.0 gate; the
 * Full Analysis RS card, which has no such gate), so any sentence claiming
 * the two legs "agree" would be false on one of them.
 *
 * Computes nothing: callers pass a 1-year return their own view already
 * has. This function exists so the two views can't word it differently, not
 * so a third calculation can exist (Golden Rule 19/21).
 *
 * @param {?number} returnPct - trailing ~1-year return in PERCENT (-3.64 for
 *                              -3.64%), NOT a ratio. Simple Checklist passes
 *                              criteria.momentum.stockReturnPct; Full
 *                              Analysis passes rsData.stock52wReturn.
 * @returns {?{state:'above_cash'|'below_cash'|'negative', text:string}}
 *          null when the return is unavailable — render nothing, not a claim
 *          about missing data. Same convention as volumeThresholds.js.
 */
export function getAbsoluteMomentumRead(returnPct) {
  if (typeof returnPct !== 'number' || !Number.isFinite(returnPct)) return null;

  const r = `${returnPct >= 0 ? '+' : ''}${returnPct.toFixed(1)}%`;

  if (returnPct < 0) {
    return {
      state: 'negative',
      text: `${r} over the past year — negative in absolute terms. Relative strength can pass in a falling market; dual momentum's second leg would not.`,
    };
  }
  if (returnPct < ABSOLUTE_MOMENTUM_CASH_PCT) {
    return {
      state: 'below_cash',
      text: `${r} over the past year — positive, but under the ${ABSOLUTE_MOMENTUM_CASH_PCT}% cash proxy. Roughly what a T-bill would have returned.`,
    };
  }
  return {
    state: 'above_cash',
    text: `${r} over the past year — clears the ${ABSOLUTE_MOMENTUM_CASH_PCT}% cash proxy, so absolute momentum is positive.`,
  };
}
