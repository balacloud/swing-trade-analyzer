/**
 * Fundamentals card — display-only reads (Analyze Page Redesign Step 6, Day 123)
 *
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP6_PLAN_DAY123.md (Fable-reviewed).
 * Pure, never throw, never feed a verdict. The red-flag screen itself is
 * screenFundamentalRedFlags() in categoricalAssessment.js.
 */

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);

/**
 * Next-earnings line. Uses the backend's own daysUntil and hasUpcoming (its
 * 7-day window) — never re-parses the date string (UTC-midnight trap).
 *
 * @param {?object} earnings - fetchEarnings() result
 * @returns {{state: 'error'|'none'|'past'|'today'|'soon'|'later', date?, days?}}
 */
export function describeEarnings(earnings) {
  if (!earnings || earnings.hasUpcoming === null || earnings.hasUpcoming === undefined) return { state: 'error' };
  if (!earnings.earningsDate) return { state: 'none' };
  const days = isNum(earnings.daysUntil) ? earnings.daysUntil : null;
  const date = String(earnings.earningsDate).slice(0, 10);
  if (days === null) return { state: 'error' };
  if (days < 0) return { state: 'past', date, days };
  if (days === 0) return { state: 'today', date, days };
  return { state: earnings.hasUpcoming ? 'soon' : 'later', date, days };
}

/**
 * Is this an ETF? Display only; the engine's ETF list is unchanged.
 * Order: engine list -> provider quoteType -> name contains "ETF" (only when
 * quoteType is missing).
 *
 * @returns {{etf: boolean, basis: 'engine_list'|'quote_type'|'name'|null}}
 */
export function detectEtf({ fundamentalAssessment, quoteType, name }) {
  if (fundamentalAssessment === 'N/A') return { etf: true, basis: 'engine_list' };
  if (typeof quoteType === 'string' && quoteType) {
    return quoteType.toUpperCase() === 'ETF' ? { etf: true, basis: 'quote_type' } : { etf: false, basis: null };
  }
  if (typeof name === 'string' && /\bETF\b/i.test(name)) return { etf: true, basis: 'name' };
  return { etf: false, basis: null };
}

/**
 * What the revenue-growth number measures, by the provider that supplied it.
 * yfinance and Alpha Vantage (quarterlyReports[0] vs [4]): latest quarter vs
 * the same quarter a year ago. FMP (period=annual): last fiscal year.
 */
export function revenueBasis(fieldSources) {
  const src = String(fieldSources?.revenueGrowth || '').toLowerCase();
  if (src.includes('yfinance') || src.includes('alpha')) return 'latest quarter vs a year ago';
  if (src.includes('fmp')) return 'last fiscal year';
  return null;
}

const PROVIDER_NAMES = { finnhub: 'Finnhub', yfinance: 'yfinance', fmp: 'FMP', alphavantage: 'Alpha Vantage' };
const SOURCE_FIELDS = [['revenueGrowth', 'sales'], ['roe', 'ROE'], ['debtToEquity', 'debt']];  // Day 125: P/E no longer shown

/**
 * Which provider supplied each number on the card, grouped by provider:
 * "Finnhub (ROE) · Alpha Vantage (sales) · yfinance (debt)".
 * Falls back to the primary source name when per-field sources are missing.
 */
export function describeSources(fieldSources, primarySource) {
  if (!fieldSources) return primarySource ? (PROVIDER_NAMES[primarySource] || primarySource) : null;
  const byProvider = new Map();
  for (const [field, label] of SOURCE_FIELDS) {
    const p = fieldSources[field];
    if (!p) continue;
    const name = PROVIDER_NAMES[p] || p;
    byProvider.set(name, [...(byProvider.get(name) || []), label]);
  }
  if (byProvider.size === 0) return primarySource ? (PROVIDER_NAMES[primarySource] || primarySource) : null;
  return [...byProvider].map(([name, labels]) => `${name} (${labels.join(', ')})`).join(' · ');
}
