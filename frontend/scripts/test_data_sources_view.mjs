// Data Sources tab helpers (Day 126). Run: cd frontend && node scripts/test_data_sources_view.mjs
import { describeIdentity, describeQuality, describeFundamentals, describeChains, providerLabel, shortTime, provenanceFor } from '../src/utils/dataSourcesView.js';

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };

const checks = (o = {}) => ({
  freshness: { level: 'PASS', note: 'last bar 2026-11-13' },
  integrity: { level: 'PASS', note: '0% of bars flat' },
  history: { level: 'PASS', note: '504 bars' },
  jumps: { level: 'PASS', note: 'no one-day move over 40%' }, ...o,
});
const prov = (o = {}) => ({
  ticker: 'AAPL',
  ohlcv: { source: 'twelvedata', status: 'cached', this_session: 'cache', rows: 504 },
  fundamentals: { source: 'finnhub', age_days: 0.3, has_data: true },
  quality: { state: 'ok', level: 'PASS', checks: checks(), facts: { bars: 504, last_date: '2026-11-13', sessions_behind: 0 }, period: '2y', cached_at: '2026-11-14T08:00:00-05:00', expired: false },
  audit: null, ...o,
});
const stock = (o = {}) => ({ ticker: 'AAPL', exchange: 'NasdaqGS', currency: 'USD', instrumentClass: 'Stock', classBasis: 'quote type EQUITY', quoteType: 'EQUITY', ...o });

// ---------- identity
let i = describeIdentity(stock(), prov());
ok(i.symbol === 'AAPL' && i.exchange === 'NasdaqGS' && i.currency === 'USD' && i.cls === 'Stock', 'identity: symbol, exchange, currency, class');
ok(i.basis === 'inferred: quote type EQUITY', 'identity: the class is labelled inferred');
ok(i.dataFrom === 'Twelve Data' && i.cache.label === 'cached', 'identity: data from the cache row source, cached');
ok(i.session === 'served from cache this session', 'identity: last_sources "cache" -> served from cache (not named as a provider)');
i = describeIdentity(stock(), prov({ ohlcv: { source: 'yfinance', status: 'just_fetched', this_session: 'yfinance' } }));
ok(i.cache.label === 'just fetched' && i.session === 'fetched live from Yahoo (yfinance) this session', 'identity: just fetched, live provider named');
i = describeIdentity(stock(), prov({ ohlcv: { source: 'yfinance', status: 'live', this_session: 'stale_cache' } }));
ok(i.cache.label.includes('not cached') && i.session.includes('expired cache'), 'identity: backend key "live" reads as not cached; stale_cache explained');
i = describeIdentity(stock(), prov({ quality: { state: 'ok', expired: true, checks: checks(), facts: {} } }));
ok(i.cache.label === 'expired, will refetch on next analysis' && i.cache.tone === 'warn', 'identity: expired frame says so');
i = describeIdentity(stock(), prov({ ohlcv: { source: 'unknown', status: 'live', this_session: null } }));
ok(i.dataFrom === null && i.session === null, 'identity: unknown source and no session entry -> null, never invented');
i = describeIdentity({ ticker: 'X' }, null);
ok(i.exchange === null && i.currency === null && i.cls === null && i.basis === null && i.cache === null, 'identity: missing fields stay null (component shows "unknown")');
ok(describeIdentity(null, null) === null && describeIdentity(undefined, { error: 'x' }) === null, 'identity: nothing known -> null');

// ---------- quality
let q = describeQuality(prov());
ok(q.state === 'ok' && q.level === 'PASS' && q.rows.length === 0 && q.passedCount === 4 && q.total === 4, 'quality: clean ticker -> no rows, 4 of 4 passed');
ok(q.header.startsWith('Checked 504 bars (period 2y) · cached ') && q.header.endsWith('last bar 2026-11-13'), `quality: header says what was checked (got "${q.header}")`);
q = describeQuality(prov({ quality: { state: 'ok', level: 'FAIL', period: '2y', checks: checks({ integrity: { level: 'FAIL', note: '100% of bars flat' }, jumps: { level: 'WARN', note: '2026-05-25 -67%' } }), facts: { bars: 311, last_date: '2026-11-13', sessions_behind: 0 } } }));
ok(q.level === 'FAIL' && q.rows.length === 2 && q.rows[0].label === 'Bar integrity' && q.rows[1].label === 'One-day moves over 40%', 'quality: only WARN/FAIL rows, with plain labels');
ok(q.passedCount === 2 && q.total === 4, 'quality: passes collapse into a count');
ok(q.header.includes('311 bars'), 'quality: a 311-bar history is shown, not hidden');
q = describeQuality(prov({ quality: { state: 'ok', level: 'PASS', checks: checks(), facts: { bars: 100, last_date: '2026-11-12', sessions_behind: 1 }, period: '1y', expired: true, cached_at: '2026-11-13T10:00:00-05:00' } }));
ok(q.header.includes('period 1y') && q.header.includes('(expired)') && q.header.includes('1 session behind'), 'quality: period, expired and lag are stated');
ok(describeQuality(prov({ quality: { state: 'not_cached' } })).state === 'not_cached', 'quality: not cached -> its own state with an instruction');
q = describeQuality(prov({ quality: { state: 'error', reason: 'ValueError: x' } }));
ok(q.state === 'error' && q.message === 'ValueError: x', 'quality: a backend error shows its reason');
q = describeQuality({ error: 'Failed to fetch provenance' });
ok(q.state === 'error' && q.message === 'Failed to fetch provenance', 'quality: provenance {error} -> error state (the Retry state), never a crash');
ok(describeQuality(null).state === 'unavailable', 'quality: null provenance -> unavailable');
ok(describeQuality({ ticker: 'X' }).state === 'unavailable', 'quality: payload without a quality block -> unavailable with a hint');
ok(describeQuality(prov(), { loading: true }).state === 'loading', 'quality: loading');
q = describeQuality(prov({ audit: { level: 'FAIL', date: '2026-11-14', age_days: 2, line: 'tradier C5: x3.00' } }));
ok(q.audit && q.audit.level === 'FAIL' && q.audit.stale === false && q.audit.line.includes('x3.00'), 'quality: a failing audit line is carried');
q = describeQuality(prov({ audit: { level: 'WARN', date: '2026-09-01', age_days: 74, line: 'y' } }));
ok(q.audit.stale === true, 'quality: an audit older than 30 days is marked stale');
ok(describeQuality(prov({ audit: { level: 'PASS', date: '2026-11-14', age_days: 0, line: '' } })).audit === null, 'quality: a passing audit adds nothing to read');
q = describeQuality(prov({ quality: { state: 'ok', level: 'PASS', checks: null, facts: null } }));
ok(q.state === 'ok' && q.rows.length === 0 && q.total === 0, 'quality: null checks and facts do not throw');

// ---------- fundamentals
ok(describeFundamentals(stock({ quoteType: 'ETF' }), prov()).text === 'No fundamentals for a fund.', 'fundamentals: a fund has none');
ok(describeFundamentals(stock(), prov({ fundamentals: { source: 'yfinance', has_data: false, age_days: 0.7 } })).text.includes('record is empty'), 'fundamentals: an all-null cached stub is not data (the SOXL.NE bug)');
ok(describeFundamentals(stock(), prov()).text === 'Fundamentals from Finnhub, today.', 'fundamentals: real data names the source and age');
ok(describeFundamentals(stock(), prov({ fundamentals: { source: 'finnhub', has_data: true, age_days: 3.2 } })).text.includes('3 days old'), 'fundamentals: age in days');
ok(describeFundamentals(stock(), prov({ fundamentals: { source: 'unknown', has_data: null } })).text === 'Fundamentals not loaded yet.', 'fundamentals: not cached -> not loaded');
ok(describeFundamentals(stock(), { error: 'x' }).text === 'Fundamentals not loaded yet.', 'fundamentals: provenance error does not throw');

// ---------- chains
const health = {
  providers: {
    twelvedata: { role: 'primary', health: 'degraded', daily_remaining: 776 },
    yfinance: { role: 'fallback', health: 'ok', daily_remaining: -1 },
    tradier: { role: 'fallback', health: 'ok', daily_remaining: -1 },
    finnhub: { role: 'primary', health: 'ok', daily_remaining: -1 },
    alphavantage: { role: 'growth', health: 'open', daily_remaining: 17 },
  },
  chains: { ohlcv: ['twelvedata', 'yfinance', 'tradier'], intraday: ['twelvedata', 'yfinance'], fundamentals: ['finnhub', 'alphavantage', 'yfinance'], quote: ['yfinance', 'finnhub', 'tradier'], stock_info: ['yfinance'], earnings: ['yfinance'] },
  disabled: ['stooq'],
};
const coverage = { tested: '2026-11-14', report: 'docs/test/x.md', markets: ['US', 'Toronto', 'Cboe Canada'],
  providers: { twelvedata: { US: 'works', Toronto: 'no', 'Cboe Canada': 'no', note: 'no Canada' }, yfinance: { US: 'works', Toronto: 'works', 'Cboe Canada': 'partial', note: 'only Canada source' }, tradier: { US: 'works', Toronto: 'no', 'Cboe Canada': 'no', note: 'reverse split x3' } } };
let c = describeChains(health, coverage);
ok(c.available && c.price.map((r) => r.name).join() === 'twelvedata,yfinance,tradier', 'chains: the real price chain, in order');
ok(c.price.some((r) => r.name === 'tradier') && !JSON.stringify(c).toLowerCase().includes('"label":"stooq"'), 'chains: Tradier is listed, Stooq is not in a chain');
ok(c.disabled.join() === 'Stooq', 'chains: Stooq only as disabled');
ok(c.price[0].callsLeft === 776 && c.price[1].callsLeft === null, 'chains: calls left for limited providers only (-1 = unlimited -> null)');
ok(c.price[0].health === 'degraded' && c.fundamentals[1].health === 'open', 'chains: health passes through');
ok(c.price[2].markets.length === 3 && c.price[2].markets[0].status === 'works' && c.price[2].note === 'reverse split x3', 'chains: markets covered and the known issue');
c = describeChains({ ...health, chains: { ...health.chains, ohlcv: ['finnhub'] } }, coverage);
ok(c.price[0].markets.map((m) => m.status).join() === 'not tested,not tested,not tested', 'chains: a price provider absent from the coverage file says "not tested", not a guess');
c = describeChains(health, coverage);
ok(c.fundamentals.every((r) => r.markets.length === 0), 'chains: no price-coverage chips under Fundamentals');
ok(c.fundamentals.find((r) => r.name === 'yfinance').note === null, 'chains: a provider already shown under Prices does not repeat its note under Fundamentals');
ok(c.fundamentals.find((r) => r.name === 'finnhub').note === null || typeof c.fundamentals.find((r) => r.name === 'finnhub').note === 'string', 'chains: a fundamentals-only provider keeps its own note if it has one');
ok(c.coverage.tested === '2026-11-14', 'chains: coverage shows its test date');
ok(c.other.length === 4 && c.other[0].title === 'Intraday' && c.other[0].rows.length === 2, 'chains: the other chains are available behind a toggle');
c = describeChains(health, { error: 'coverage file unreadable' });
ok(c.available && c.coverage.error === 'coverage file unreadable' && c.price[0].markets.length === 0, 'chains: coverage failure is shown, the chain still renders');
c = describeChains(health, null);
ok(c.coverage.error === 'Coverage table not loaded.', 'chains: coverage not loaded yet is said');
ok(describeChains(null, coverage).available === false, 'chains: health unavailable -> message, no throw');
ok(describeChains({ providers: {} }, coverage).available === false, 'chains: an old backend without chains -> unavailable, not a stale hard-coded chain');
c = describeChains({ ...health, chains: { ohlcv: ['unknownprov'] } }, coverage);
ok(c.price[0].label === 'unknownprov' && c.price[0].health === 'unknown', 'chains: an unknown provider name is shown as is, health unknown');

// ---------- stale pairing guard (review pass 2)
ok(provenanceFor(prov(), 'AAPL') !== null && provenanceFor(prov(), 'aapl') !== null, 'guard: same ticker, any case -> kept');
ok(provenanceFor(prov(), 'NVDA') === null, 'guard: provenance for another ticker is dropped (shown as not loaded)');
ok(provenanceFor({ error: 'x' }, 'NVDA').error === 'x', 'guard: an error is always shown');
ok(provenanceFor(null, 'AAPL') === null && provenanceFor(prov(), null) !== null, 'guard: null stays null; no ticker keeps what there is');
q = describeQuality(prov({ quality: { state: 'ok', level: 'PASS', checks: checks(), facts: { bars: 299, last_date: '2026-11-12', sessions_behind: 1, forming_bar_dropped: true }, period: '2y' } }));
ok(q.header.includes("today's unfinished bar left out"), 'quality: a dropped forming bar is stated, so the bar count is not a mystery');

// ---------- small helpers
ok(providerLabel('yfinance') === 'Yahoo (yfinance)' && providerLabel('zzz') === 'zzz', 'labels: known and unknown providers');
ok(shortTime(null) === null && shortTime('not a date') === null && typeof shortTime('2026-11-14T08:03:54-05:00') === 'string', 'shortTime: null on bad input');

// Day 126 (split mechanism): the tab says so only when STA adjusted the prices
q = describeQuality(prov({ quality: { state: 'ok', level: 'FAIL', period: '2y', checks: checks(), facts: { bars: 311, last_date: '2026-11-13', sessions_behind: 0,
  splits: [{ text: '3-for-1 on 2026-05-25', status: 'unadjusted', bar_date: '2026-05-25' }] } } }));
ok(q.splits.length === 1 && q.splits[0].includes('Split-adjusted by STA: 3-for-1 on 2026-05-25'), 'split line: shown when STA adjusted the prices');
q = describeQuality(prov({ quality: { state: 'ok', level: 'PASS', period: '2y', checks: checks(), facts: { bars: 504, last_date: '2026-11-13', sessions_behind: 0,
  splits: [{ text: '3-for-1 on 2026-05-25', status: 'already_adjusted' }, { text: '1-for-3 on 2026-03-23', status: 'wrong_way' }] } } }));
ok(Array.isArray(q.splits) && q.splits.length === 0, 'split line: nothing for a split the provider already fixed (or one STA did not adjust)');
q = describeQuality(prov({ quality: { state: 'ok', level: 'PASS', period: '2y', checks: checks(), facts: { bars: 504, last_date: '2026-11-13', sessions_behind: 0 } } }));
ok(Array.isArray(q.splits) && q.splits.length === 0, 'split line: an old backend without facts.splits still works');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
