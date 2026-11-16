/**
 * Technical Read card — display-only reads (Analyze Page Redesign Step 4, Day 123)
 *
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP4_PLAN_DAY123.md (Fable-reviewed).
 * Nothing here feeds determineVerdict() or any gate.
 * Every function is pure, never throws, and returns { state, reason } when an
 * input is missing, so the card can say why instead of showing a made-up value.
 */
import { BREAKOUT_VOLUME_THRESHOLD, getVolumeDirectionRead } from './volumeThresholds';

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);
const pctDiff = (a, b) => (isNum(a) && isNum(b) && b !== 0 ? ((a - b) / b) * 100 : null);

/** Minervini Trend Template needs a year of daily bars (pattern_detection.py). */
export const TREND_TEMPLATE_MIN_BARS = 252;
/** /api/patterns returns 400 below this many bars (backend.py patterns route). */
export const PATTERNS_MIN_BARS = 100;

/**
 * The 4 trend checks shown on the card, read from the same
 * check_trend_template() result the engine counts. The other 4 criteria stay
 * in the engine's 8-check score (decisions doc, Day 122).
 *
 * @param {object|null} patternsData - fetchPatterns() result; null when /api/patterns failed
 * @param {?number} historyBars - stock.priceHistory length, to tell a young ticker
 *   (/api/patterns refuses under 100 bars) from a real failure
 * @returns {object} { state: 'ok', checks, met, total } |
 *   { state: 'unavailable', reason: 'patterns_failed' | 'short_history', bars }
 */
export function deriveTrendChecks(patternsData, historyBars = null) {
  if (!patternsData) {
    return isNum(historyBars) && historyBars < PATTERNS_MIN_BARS
      ? { state: 'unavailable', reason: 'short_history', bars: historyBars }
      : { state: 'unavailable', reason: 'patterns_failed' };
  }
  const tt = patternsData.trendTemplate;
  if (!tt || !tt.criteria) {
    return { state: 'unavailable', reason: 'short_history', bars: isNum(patternsData.dataPoints) ? patternsData.dataPoints : null };
  }

  const c = tt.criteria;
  const price = tt.price_position?.current;
  const sma50 = tt.sma_values?.sma_50;
  const sma200 = tt.sma_values?.sma_200;
  const sma200Ago = tt.sma_values?.sma_200_30d_ago;  // null on responses cached before Day 123
  const high = tt.price_position?.high_52w;
  const fromHigh = tt.price_position?.pct_from_high;
  const money = (v) => (isNum(v) ? `$${v.toFixed(2)}` : '—');
  const signed = (v) => (isNum(v) ? `${v >= 0 ? '+' : '−'}${Math.abs(v).toFixed(1)}%` : '');

  const checks = [
    {
      key: 'above_200sma',
      pass: c.above_200sma === true,
      label: c.above_200sma ? 'Above its 200-day average' : 'Below its 200-day average',
      why: c.above_200sma ? 'The long-term trend is up.' : 'The long-term trend is down.',
      detail: `${money(price)} vs ${money(sma200)} · ${signed(pctDiff(price, sma200))}`,
    },
    {
      key: 'sma_200_trending_up',
      pass: c.sma_200_trending_up === true,
      label: c.sma_200_trending_up ? 'The 200-day average is still rising' : 'The 200-day average is not rising',
      why: c.sma_200_trending_up ? "The long-term trend hasn't stalled." : 'The long-term trend has stalled or turned down.',
      detail: isNum(sma200Ago) ? `${signed(pctDiff(sma200, sma200Ago))} from a month ago` : 'vs a month ago',
    },
    {
      key: 'above_50sma',
      pass: c.above_50sma === true,
      label: c.above_50sma ? 'Above its 50-day average' : 'Below its 50-day average',
      why: c.above_50sma ? 'The recent trend is up too.' : 'The recent trend is down.',
      detail: `${money(price)} vs ${money(sma50)} · ${signed(pctDiff(price, sma50))}`,
    },
    {
      key: 'within_25pct_52w_high',
      pass: c.within_25pct_52w_high === true,
      label: c.within_25pct_52w_high ? 'Within 25% of its 1-year high' : 'More than 25% below its 1-year high',
      why: c.within_25pct_52w_high ? "It's a leader, not a laggard." : 'Leaders trade near their highs; this one is well off its high.',
      detail: isNum(fromHigh) ? `${Math.abs(fromHigh).toFixed(1)}% below the ${money(high)} high` : '',
    },
  ];

  return { state: 'ok', checks, met: tt.criteria_met, total: tt.total_criteria || 8 };
}

/**
 * Where is price against its 21-day average? (Day 126 redesign: a RULER, not a verdict.)
 * The user decides; this only measures. Distance is also expressed in "a normal day's move" (ATR, the same Wilder ATR the Trade Setup
 * stop uses), and the ruler's tick marks are real prices: the 21, 50 and 200-day averages (a missing one is left out). The marks are a
 * measuring stick, not signals, and are not tested by STA. No gating on the Technical Read: it shows for every stock.
 *
 * @param {object} args
 * @param {?number} args.price - analysisResult.currentPrice (same frame as ema21)
 * @param {?number} args.ema21 - analysisResult.indicators.ema21 (scoringEngine; null under 200 bars)
 * @param {?number} args.sma50 - analysisResult.indicators.sma50 (optional)
 * @param {?number} args.sma200 - analysisResult.indicators.sma200 (optional)
 * @param {?number} args.atr - srData.meta.atr (Wilder ATR(14) on completed bars)
 */
const RULER_MARKS = [['ema21', '21-day avg'], ['sma50', '50-day avg'], ['sma200', '200-day avg']];

export function deriveEntryTiming({ price, ema21, sma50, sma200, atr }) {
  if (!isNum(price)) return { state: 'unavailable', reason: 'price missing' };
  if (!isNum(ema21) || ema21 <= 0) return { state: 'unavailable', reason: '21-day average not computed (needs 200 days of history)' };
  if (!isNum(atr) || atr <= 0) return { state: 'unavailable', reason: 'ATR unavailable' };

  const atrUnits = (price - ema21) / atr;
  const pctFromEma = pctDiff(price, ema21);
  const vals = { ema21, sma50, sma200 };
  // real averages only, left to right by price; one that is missing is left out, never invented
  const marks = RULER_MARKS.filter(([k]) => isNum(vals[k]) && vals[k] > 0)
    .map(([key, caption]) => ({ key, price: vals[key], caption }))
    .sort((a, b) => a.price - b.price);
  // the ruler always contains the price and every mark, with a little room at both ends
  const all = [price, ...marks.map((m) => m.price)];
  const min = Math.min(...all), max = Math.max(...all);
  const pad = (max - min) * 0.12 || max * 0.01;
  const side = Math.abs(pctFromEma) < 0.05 ? 'at' : pctFromEma > 0 ? 'above' : 'below';
  return {
    state: 'ok',
    price,
    ema21,
    atr,
    atrUnits,
    pctFromEma,
    side,
    marks,
    lo: min - pad,
    hi: max + pad,
  };
}

/** Today's date in New York (market time), YYYY-MM-DD. */
export function todayInNewYork() {
  return new Date().toLocaleDateString('en-CA', { timeZone: 'America/New_York' });
}

const LEAN_ANSWERS = {
  buying: 'Yes',
  mixed: 'Mixed',
  selling: 'No, sellers lead',
  none: 'No clear lean',
};

/**
 * "Are buyers behind the move?" — 20 volume bars plus the 3 engine votes.
 *
 * Partial-bar rule (Day 116): when today's bar is still forming, votes and
 * RVOL use the last complete bar (meta.prevBar). The bars come from
 * /api/stock while barComplete comes from /api/sr, a different fetch; when
 * /api/sr is missing the last bar's state is 'unknown', never assumed
 * complete, and when the two disagree on dates the last bar is also 'unknown'.
 *
 * @param {object} args
 * @param {?Array} args.priceHistory - stock.priceHistory [{date, close, volume}]
 * @param {?object} args.srData - fetchSupportResistance() result, or null
 * @param {string} args.todayEt - today's date in New York, YYYY-MM-DD (injected so the function stays pure)
 */
export function deriveEntryVolume({ priceHistory, srData, todayEt = todayInNewYork() }) {
  const history = Array.isArray(priceHistory) ? priceHistory.filter((b) => b && b.date && isNum(b.volume) && isNum(b.close)) : [];
  const warnings = [];
  if (history.length < 2) warnings.push('price history missing or empty, no volume bars');

  // Last bar state: 'complete' | 'partial' | 'unknown'
  let lastBar = 'unknown';
  const meta = srData?.meta;
  if (srData) {
    lastBar = meta?.candle?.barComplete === false ? 'partial' : 'complete';
    const prevDate = meta?.prevBar?.date;
    const histPrevDate = history.length >= 2 ? history[history.length - 2].date : null;
    if (prevDate && histPrevDate && prevDate !== histPrevDate) {
      lastBar = 'unknown';
      warnings.push(`price history (${histPrevDate}) and S&R (${prevDate}) disagree on the prior bar date; bar chart average and RVOL may use different windows`);
    }
  } else {
    warnings.push('/api/sr missing, today\'s bar state unknown');
  }

  // Bars: last 20 sessions, up/down vs the prior close.
  let bars = [];
  if (history.length >= 2) {
    const start = Math.max(1, history.length - 20);
    bars = history.slice(start).map((b, i) => {
      const prev = history[start + i - 1];
      const isLast = start + i === history.length - 1;
      return { date: b.date, volume: b.volume, up: b.close > prev.close, state: isLast ? lastBar : 'complete' };
    });
  }

  // 50-day average, defined as the backend's RVOL denominator: last 50 bars
  // when the last bar is complete, the 50 before it when it is forming.
  const vols = history.map((b) => b.volume);
  const base = lastBar === 'complete' ? vols : vols.slice(0, -1);
  const window = base.slice(-50);
  const avg50 = window.length > 0 ? window.reduce((a, b) => a + b, 0) / window.length : null;
  if (window.length > 0 && window.length < 50) warnings.push(`average uses ${window.length} days, not 50`);

  if (!srData) {
    return { state: 'partial', reason: 'S&R data unavailable, so the buyer/seller votes can\'t be read', bars, avg50, lastBar, warnings };
  }

  // Votes come from the S&R frame alone, so they follow its own barComplete
  // flag even when the bar chart's last bar is 'unknown' (date mismatch).
  const useToday = meta?.candle?.barComplete !== false;
  const prevBar = meta?.prevBar;
  const rvol = useToday ? meta?.rvol : (prevBar?.rvol ?? null);
  const changePct = useToday ? srData.change : (prevBar?.changePct ?? null);
  const closeLocation = useToday ? meta?.candle?.closeLocation : (prevBar?.closeLocation ?? null);
  const obvTrend = meta?.obv?.trend;

  const dir = getVolumeDirectionRead({ changePct, closeLocation, obvTrend });
  if (!dir) {
    return { state: 'partial', reason: 'none of the three volume signals came back', bars, avg50, lastBar, rvol, warnings };
  }

  const agreeing = dir.signals.filter((s) => (dir.lean === 'selling' ? s.vote < 0 : s.vote > 0)).length;
  let answer = LEAN_ANSWERS[dir.lean];
  if (dir.lean === 'selling' && isNum(rvol) && rvol >= BREAKOUT_VOLUME_THRESHOLD) answer = 'No, heavy selling';

  // Distribution warning: same expression the old ⚠️ DIST chip used (Day 49/116).
  const distribution = isNum(rvol) && rvol >= BREAKOUT_VOLUME_THRESHOLD && obvTrend === 'falling';

  return {
    state: 'ok',
    answer,
    lean: dir.lean,
    signals: dir.signals,
    agreeing,
    voted: dir.signals.length,
    // plain count of the three signals (what the card shows instead of a one-word answer)
    tally: {
      up: dir.signals.filter((x) => x.vote > 0).length,
      down: dir.signals.filter((x) => x.vote < 0).length,
      flat: dir.signals.filter((x) => x.vote === 0).length,
    },
    rvol: isNum(rvol) ? rvol : null,
    // Which session the votes describe, when it isn't today: the last complete
    // bar while today's is forming, or a past session before the open/weekends.
    asOf: !useToday ? (prevBar?.date || null)
      : (meta?.candle?.date && meta.candle.date !== todayEt ? meta.candle.date : null),
    distribution,
    bars,
    avg50,
    lastBar,
    warnings,
  };
}
