/**
 * mrReadRows — turns the /api/mr/signal response into the four display rows
 * of the Mean-Reversion Read card (Day 126 redesign: one row + one gauge per rule).
 *
 * Display only. Pass / fail always comes from the backend's `conditions`.
 * The ONE override: a provider that reports zero volume on every bar (SOXL.NE
 * and other close-only funds) gives avg_dollar_volume 0. That is "no data",
 * not "nothing traded", so the volume row is shown as not checked (state null)
 * instead of a fake $0 fail. The backend (mean_reversion.py, also used by the
 * backtests) is deliberately untouched.
 */

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);

export const money = (v) => (isNum(v) ? `$${v.toFixed(2)}` : '—');
export const bigMoney = (v) => (!isNum(v) ? '—'
  : v >= 1e9 ? `$${+(v / 1e9).toFixed(1)}B`
  : v >= 1e6 ? `$${+(v / 1e6).toFixed(1)}M`
  : `$${Math.round(v).toLocaleString()}`);

/** true when the provider gave no usable volume (zero, missing, or not a number). */
export function volumeIsMissing(mrData) {
  if (!mrData) return true;
  const { avg_dollar_volume: d, avg_volume: v } = mrData;
  if (!isNum(d)) return true;
  // 0 dollars a day with a real price means the feed has no volume, not that nothing traded.
  return d === 0 && (!isNum(v) || v === 0);
}

const clamp01 = (x) => Math.min(1, Math.max(0, x));

/**
 * gauge: { pos, thresholdPos, passSide: 'left'|'right', offScale: null|'left'|'right' }
 * pos / thresholdPos are 0..1 along the bar.
 */
function gauge(value, lo, hi, threshold, passSide) {
  if (!isNum(value) || !isNum(threshold)) return null; // never draw a gauge from a missing rule number
  const raw = (value - lo) / (hi - lo);
  return {
    pos: clamp01(raw),
    thresholdPos: clamp01((threshold - lo) / (hi - lo)),
    passSide,
    offScale: raw < 0 ? 'left' : raw > 1 ? 'right' : null,
  };
}

/** @returns {{rows: object[], blockers: string[], unchecked: string[]}} */
export function buildMRRows(mrData) {
  const { rsi2, current_price: price, pct_above_sma200: pct, avg_dollar_volume: dollarVol,
    conditions = {}, rules } = mrData;
  const volMissing = volumeIsMissing(mrData);

  const rows = [
    {
      key: 'rsi2_oversold',
      label: 'Sharp drop',
      question: 'Has it dropped hard over the last 2 days?',
      value: isNum(rsi2) ? `2-day RSI ${rsi2.toFixed(0)}` : 'no data',
      needs: `needs under ${rules.rsi2_entry} (a very sharp drop)`,
      hint: 'RSI scores the last 2 days from 0 to 100. Low = it just fell fast. High = it just rose fast.',
      ends: ['sharp drop', 'sharp rise'],
      state: isNum(rsi2) ? conditions.rsi2_oversold ?? null : null,
      blocker: 'the 2-day drop is too small',
      gauge: gauge(rsi2, 0, 100, rules.rsi2_entry, 'left'),
    },
    {
      key: 'above_200sma',
      label: 'Uptrend',
      question: 'Is it in an uptrend?',
      value: !isNum(pct) ? 'no data'
        : pct === 0 ? 'right at its 200-day average'
        : `${Math.abs(pct).toFixed(1)}% ${pct > 0 ? 'above' : 'below'} its 200-day average`,
      needs: 'needs to be above it',
      hint: 'The 200-day average is the usual line between an uptrend and a downtrend.',
      ends: ['below', 'above'],
      state: isNum(pct) ? conditions.above_200sma ?? null : null,
      blocker: 'it is below its 200-day average',
      gauge: gauge(pct, -50, 50, 0, 'right'),
    },
    {
      key: 'price_filter',
      label: 'Price',
      question: 'Is the price high enough?',
      value: money(price),
      needs: `needs above $${rules.price_min}`,
      hint: 'This skips penny stocks.',
      state: isNum(price) ? conditions.price_filter ?? null : null,
      blocker: `the price is under $${rules.price_min}`,
      gauge: null,
    },
    {
      key: 'volume_filter',
      label: 'Trading volume',
      question: 'Does it trade enough to get in and out?',
      value: volMissing ? "no volume data" : `${bigMoney(dollarVol)} traded on an average day`,
      needs: volMissing ? "this data source doesn't report volume" : `needs above ${bigMoney(rules.dollar_volume_min)}`,
      hint: volMissing ? null : 'Average of the last 20 days. Enough trading means you can get in and out.',
      state: volMissing ? null : conditions.volume_filter ?? null,
      blocker: 'it does not trade enough dollars a day',
      gauge: null,
    },
  ];

  return {
    rows,
    blockers: rows.filter((r) => r.state === false).map((r) => r.blocker),
    unchecked: rows.filter((r) => r.state == null).map((r) => r.label),
  };
}
