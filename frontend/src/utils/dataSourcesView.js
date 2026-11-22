/**
 * What the Data Sources tab says, as pure functions (Day 126, Data Sources tab v2).
 * Plan: docs/claude/design/DATA_SOURCES_TAB_V2_PLAN_DAY126.md §2, §4, §6.
 *
 * Every function takes the raw payloads (stock from /api/stock, provenance from /api/provenance, health from
 * /api/health providers, coverage from /api/data-sources/coverage) and returns plain data for the component.
 * None throws, none invents a value: missing input says "unknown", and an error payload (`{error}`) becomes a
 * visible error state, never a blank (Golden Rule: no silent failures).
 */

const DISPLAY = {
  alpaca: 'Alpaca', twelvedata: 'Twelve Data', yfinance: 'Yahoo (yfinance)', tradier: 'Tradier',
  finnhub: 'Finnhub', alphavantage: 'Alpha Vantage', fmp: 'FMP', stooq: 'Stooq', eodhd: 'EODHD',
};
export const providerLabel = (name) => DISPLAY[name] || name;

const CHECK_LABEL = {
  freshness: 'Latest bar',
  integrity: 'Bar integrity',
  history: 'History length',
  jumps: 'One-day moves over 40%',
  source: 'Data source',
};

const isObj = (x) => x && typeof x === 'object';
const hasError = (x) => isObj(x) && typeof x.error === 'string';

/** "2026-11-14T08:03:54-05:00" -> "Nov 14, 8:03 AM" (local); null when it cannot be read. */
export function shortTime(iso) {
  if (!iso) return null;
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return null;
  return d.toLocaleString('en-US', { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' });
}

/**
 * Guard against stale pairing (review pass 2): switching tickers with the tab open leaves the PREVIOUS ticker's provenance
 * in state until the new fetch lands. Return it only when it is for this ticker (or is an error), else null, which the tab
 * treats as "not loaded yet" instead of showing one ticker's identity next to another's data source.
 */
export function provenanceFor(provenance, ticker) {
  if (!isObj(provenance)) return null;
  if (hasError(provenance)) return provenance;
  if (!ticker || !provenance.ticker) return provenance;
  return String(provenance.ticker).toUpperCase() === String(ticker).toUpperCase() ? provenance : null;
}

/** Block A: who this instrument is, and where its data came from. */
export function describeIdentity(stock, provenance) {
  if (!isObj(stock) && !(isObj(provenance) && !hasError(provenance))) return null;
  const prov = isObj(provenance) && !hasError(provenance) ? provenance : null;
  const ohlcv = prov?.ohlcv || null;
  const q = prov?.quality || null;
  const src = ohlcv?.source && ohlcv.source !== 'unknown' ? ohlcv.source : null;

  let cache = null;
  if (ohlcv) {
    if (q?.expired === true) cache = { label: 'expired, will refetch on next analysis', tone: 'warn' };
    else if (ohlcv.status === 'just_fetched') cache = { label: 'just fetched', tone: 'good' };
    else if (ohlcv.status === 'cached') cache = { label: 'cached', tone: 'good' };
    else cache = { label: 'not cached, will fetch on next analysis', tone: 'muted' };   // backend key 'live'
  }
  const s = ohlcv?.this_session;
  const session = s === 'cache' ? 'served from cache this session'
    : s === 'stale_cache' ? 'served from an expired cache (every provider failed)'
    : s ? `fetched live from ${providerLabel(s)} this session`
    : null;

  return {
    symbol: stock?.ticker || prov?.ticker || null,
    exchange: stock?.exchange || null,
    currency: stock?.currency || null,
    cls: stock?.instrumentClass || null,
    basis: stock?.classBasis ? `inferred: ${stock.classBasis}` : null,
    dataFrom: src ? providerLabel(src) : null,
    cache,
    session,
  };
}

/** Block B: data quality. Only WARN/FAIL rows are listed; passes collapse into a count. */
export function describeQuality(provenance, { loading = false } = {}) {
  if (loading) return { state: 'loading' };
  if (hasError(provenance)) return { state: 'error', message: provenance.error };
  if (!isObj(provenance)) return { state: 'unavailable', message: 'No provenance data yet.' };
  const q = provenance.quality;
  if (!isObj(q)) return { state: 'unavailable', message: 'This backend did not send a quality block (old version?). Restart the backend.' };
  if (q.state === 'not_cached') return { state: 'not_cached', message: 'Nothing is cached for this ticker yet. Analyze it first.' };
  if (q.state === 'error') return { state: 'error', message: q.reason || 'The quality check failed.' };

  const f = q.facts || {};
  const checks = isObj(q.checks) ? q.checks : {};
  const rows = Object.entries(checks)
    .filter(([, c]) => c && (c.level === 'WARN' || c.level === 'FAIL'))
    .map(([name, c]) => ({ name, label: CHECK_LABEL[name] || name, level: c.level, note: c.note }));
  const passed = Object.values(checks).filter((c) => c && c.level === 'PASS').length;

  const behind = f.sessions_behind > 0 ? `, ${f.sessions_behind} session${f.sessions_behind === 1 ? '' : 's'} behind` : '';
  const when = shortTime(q.cached_at);
  const header = [
    `Checked ${f.bars ?? '?'} bars (period ${q.period ?? '?'})`,
    when ? `cached ${when}${q.expired ? ' (expired)' : ''}` : null,
    f.last_date ? `last bar ${f.last_date}${behind}` : null,
    f.forming_bar_dropped ? "today's unfinished bar left out" : null,
  ].filter(Boolean).join(' · ');

  let audit = null;
  const a = provenance.audit;
  if (isObj(a) && (a.level === 'WARN' || a.level === 'FAIL')) {
    audit = { level: a.level, date: a.date, stale: typeof a.age_days === 'number' && a.age_days > 30, ageDays: a.age_days, line: a.line };
  }
  // Day 126: say it only when STA changed the prices ("unadjusted" = STA divides the older prices); nothing for splits a provider already fixed.
  const splits = (Array.isArray(f.splits) ? f.splits : []).filter((x) => x && x.status === 'unadjusted')
    .map((x) => `Split-adjusted by STA: ${x.text}. The data provider left the older prices unadjusted.`);
  return { state: 'ok', level: q.level, header, rows, passedCount: passed, total: Object.keys(checks).length, audit, splits };
}

/** Fundamentals line: a fund has none; an all-null stub is not data. */
export function describeFundamentals(stock, provenance) {
  if (stock?.quoteType === 'ETF') return { text: 'No fundamentals for a fund.', tone: 'muted' };
  const fu = isObj(provenance) && !hasError(provenance) ? provenance.fundamentals : null;
  if (!fu) return { text: 'Fundamentals not loaded yet.', tone: 'muted' };
  if (fu.has_data === false) return { text: 'No fundamentals on file (the cached record is empty).', tone: 'muted' };
  if (fu.has_data === true) {
    const age = typeof fu.age_days === 'number' ? `, ${fu.age_days < 1 ? 'today' : `${Math.round(fu.age_days)} day${Math.round(fu.age_days) === 1 ? '' : 's'} old`}` : '';
    return { text: `Fundamentals from ${providerLabel(fu.source)}${age}.`, tone: 'good' };
  }
  return { text: 'Fundamentals not loaded yet.', tone: 'muted' };
}

/** Block C: the real chains, with health, quota and tested coverage. `health` is /api/health `providers`. */
export function describeChains(health, coverage) {
  if (!isObj(health) || !isObj(health.chains)) {
    return { available: false, message: 'Provider health unavailable.' };
  }
  const covOk = isObj(coverage) && !hasError(coverage) && isObj(coverage.providers);
  const row = (name) => {
    const p = health.providers?.[name] || {};
    const c = covOk ? (coverage.providers[name] || {}) : null;   // loaded but absent from the file -> every market 'not tested'
    const left = typeof p.daily_remaining === 'number' && p.daily_remaining >= 0 ? p.daily_remaining : null;
    return {
      name,
      label: providerLabel(name),
      role: p.role || null,
      health: p.health || 'unknown',
      callsLeft: left,
      markets: c ? (coverage.markets || []).map((m) => ({ market: m, status: c[m] || 'not tested' })) : [],
      note: c?.note || null,
    };
  };
  const priceNames = new Set(Array.isArray(health.chains.ohlcv) ? health.chains.ohlcv : []);
  const chain = (key) => (Array.isArray(health.chains[key]) ? health.chains[key].map(row) : []);
  // Coverage is about PRICE history. Under Fundamentals a provider already listed under Prices shows only its health and
  // quota (no repeated chips or note); fundamentals-only providers keep their note (what they are for) but no price chips.
  const fund = chain('fundamentals').map((r) => (priceNames.has(r.name) ? { ...r, markets: [], note: null } : { ...r, markets: [] }));
  return {
    available: true,
    price: chain('ohlcv'),
    fundamentals: fund,
    other: [
      { key: 'intraday', title: 'Intraday', rows: chain('intraday') },
      { key: 'quote', title: 'Quote', rows: chain('quote') },
      { key: 'stock_info', title: 'Stock info', rows: chain('stock_info') },
      { key: 'earnings', title: 'Earnings', rows: chain('earnings') },
    ],
    disabled: (Array.isArray(health.disabled) ? health.disabled : []).map(providerLabel),
    coverage: covOk
      ? { tested: coverage.tested || null, report: coverage.report || null }
      : { error: hasError(coverage) ? coverage.error : 'Coverage table not loaded.' },
  };
}
