/**
 * "Are these prices current?" line for the Analyze header (Day 135, plan STALE_PRICE_AND_LEVERAGED_PLAN_DAY135.md).
 * Input: /api/stock `priceFreshness` ({newestDate, expectedDate, sessionsBehind, behindLevel, servedFromStaleCache, maybePartial}),
 * built by backend data_quality.price_freshness. The thresholds live ONLY there (it reuses the Data Sources tab's tolerant rule), so this
 * file has no number of its own: it says something only when the backend says the copy is saved, or the tab's rule says WARN/FAIL.
 * Plain facts, no verdict words, no changed numbers. Pure, never throws; anything missing returns null.
 */
const CANADA = /\.(TO|NE|NEO|V|CN)$/i;

function dayLabel(iso) {
  if (typeof iso !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(iso)) return null;
  const d = new Date(`${iso}T12:00:00`);
  if (Number.isNaN(d.getTime())) return null;
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

export function describePriceFreshness(pf, ticker) {
  try {
    if (!pf || typeof pf !== 'object') return null;
    const newest = dayLabel(pf.newestDate);
    if (pf.servedFromStaleCache) {
      const canada = typeof ticker === 'string' && CANADA.test(ticker);
      const upTo = newest ? ` up to ${newest}` : '';
      let text = `Showing saved prices${upTo}: every price source failed just now.`;
      if (canada) text += ' Yahoo is the only price source for Canadian tickers.';
      if (pf.maybePartial) text += ' The last saved bar may be unfinished.';
      return text;
    }
    if ((pf.behindLevel === 'WARN' || pf.behindLevel === 'FAIL') && newest) {
      const exp = dayLabel(pf.expectedDate);
      const n = Number.isFinite(pf.sessionsBehind) ? pf.sessionsBehind : null;
      return `Latest price bar is ${newest}${exp ? `, but the last completed trading day is ${exp}` : ''}${n != null ? ` (${n} trading days behind)` : ''}.`;
    }
    return null;
  } catch (e) {
    return null;
  }
}
