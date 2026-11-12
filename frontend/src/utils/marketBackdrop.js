/**
 * Market backdrop card — display-only facts (Analyze Page Redesign Step 7, Day 124)
 *
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP7_PLAN_DAY124.md (Fable-reviewed).
 * Replaces describeRegimeRead(): the card no longer repeats the engine's
 * Favorable / Neutral / Unfavorable call. It shows facts and the user decides.
 * Nothing here feeds assessRiskMacro(), determineVerdict() or any gate.
 * Pure, never throws; a missing piece gets its own state, never a made-up value.
 */

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);

// Words for the backend's VIX bands (backend/vix_bands.py); no thresholds here.
// Shared with the Context tab's Market Phase banner so one VIX reads the same everywhere.
export const VIX_BAND_LABELS = {
  low_volatility: 'low',
  normal: 'normal range',
  elevated: 'elevated',
  high: 'high',
  extreme: 'extreme',
};

function describeLine(above, pct) {
  return typeof above === 'boolean' && isNum(pct)
    ? { state: 'ok', above, pct }
    : { state: 'no_history' };
}

// searchedFrom: the first date the backend actually searched, so "largest since
// the start of the data" is stated from the data, never assumed to be 2 years.
function describeDrop(drop, since, searchedFrom) {
  if (!drop) return { state: 'no_history' };
  if (drop.noDownDay) return { state: 'no_down_day' };
  if (!isNum(drop.pct) || !drop.date) return { state: 'no_history' };
  return { state: 'drop', pct: drop.pct, date: drop.date, since: since || null, searchedFrom: searchedFrom || null };
}

function describeRow(label, source) {
  const trend = source?.trend;
  if (!trend) {
    return { label, state: 'unavailable', reason: source?.error || 'no data returned' };
  }
  return {
    label,
    state: 'ok',
    asOfDate: trend.asOfDate || null,
    longTerm: describeLine(trend.aboveSma200, trend.pctVsSma200),
    shortTerm: describeLine(trend.aboveSma50, trend.pctVsSma50),
    drop: describeDrop(trend.biggestDrop10d, trend.biggestDrop10dSince, trend.searchedFrom),
  };
}

/**
 * @param {object} p
 * @param {object} p.spy - fetchSPYData() result (uses .trend)
 * @param {object} p.qqq - fetchIndexTrend('QQQ') result, or { error }
 * @param {object} p.vix - fetchVIXData() result ({ current, regime })
 * @returns {{ rows, vix, asOfDate, missing, allUnavailable }}
 */
export function describeMarketBackdrop({ spy, qqq, vix } = {}) {
  const rows = [describeRow('S&P 500', spy), describeRow('Nasdaq-100 (QQQ)', qqq)];

  const vixRead = isNum(vix?.current)
    ? { state: 'ok', value: vix.current, label: VIX_BAND_LABELS[vix.regime] || null }
    : { state: 'unavailable' };

  const dates = [...new Set(rows.filter(r => r.state === 'ok').map(r => r.asOfDate))];
  const missing = rows.filter(r => r.state !== 'ok').map(r => r.label);
  if (vixRead.state !== 'ok') missing.push('VIX');

  return {
    rows,
    vix: vixRead,
    asOfDate: dates.length === 1 ? dates[0] : null,
    missing,
    allUnavailable: missing.length === rows.length + 1,
  };
}
