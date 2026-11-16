// Unit tests for scripts/lib/analyzeChecks.js (Analyze Redesign Step 8, Day 124).
// A fixture of today's page must pass every check; for each check, a fixture of
// the pre-redesign page (or a broken state) must fail it. Run:
//   cd frontend && node scripts/test_analyze_checks.mjs
import { createRequire } from 'module';
import { describeMarketBackdrop, fmtPct, fmtDate } from '../src/utils/marketBackdrop.js';
import { formatZoneRange } from '../src/utils/keyLevels.js';
import { providerLabel } from '../src/utils/dataSourcesView.js';

const require = createRequire(import.meta.url);
const { runChecks, CHECK_IDS } = require('./lib/analyzeChecks.js');
const helpers = { describeMarketBackdrop, fmtPct, fmtDate, formatZoneRange, providerLabel };

let failures = 0;
let passes = 0;
function expect(cond, msg) {
  if (cond) { passes++; console.log(`ok ${msg}`); }
  else { failures++; console.log(`FAIL ${msg}`); }
}
const clone = (o) => JSON.parse(JSON.stringify(o));
const byId = (checks, id) => checks.find(c => c.id === id);

// ---------- fixtures: today's page ----------
const trendSpy = {
  asOfDate: '2026-11-11', aboveSma200: true, pctVsSma200: 3.92, aboveSma50: false, pctVsSma50: -1.25,
  biggestDrop10d: { date: '2026-11-05', pct: -4.41 }, biggestDrop10dSince: '2025-04-04', searchedFrom: '2024-11-08',
};
const trendQqq = {
  asOfDate: '2026-11-11', aboveSma200: true, pctVsSma200: 5.0, aboveSma50: false, pctVsSma50: -2.04,
  biggestDrop10d: { date: '2026-11-05', pct: -6.49 }, biggestDrop10dSince: null, searchedFrom: '2024-11-08',
};
const API = {
  spy: { status: 200, body: { trend: trendSpy, aboveSma200: true } },
  qqq: { status: 200, body: { ticker: 'QQQ', trend: trendQqq } },
  vix: { status: 200, body: { current: 18.24, regime: 'normal' } },
  stock: { status: 200, body: { ticker: 'AAPL', currentPrice: 523.88, quoteType: 'EQUITY', exchange: 'NasdaqGS', currency: 'USD', instrumentClass: 'Stock' } },
  provenance: { status: 200, body: { ticker: 'AAPL', ohlcv: { source: 'twelvedata', status: 'cached' },
    indicators: [{ name: 'SMA 50 / 200' }, { name: 'RSI 14' }], indicators_error: null,
    quality: { state: 'ok', level: 'PASS', checks: { freshness: { level: 'PASS' }, integrity: { level: 'PASS' }, history: { level: 'PASS' }, jumps: { level: 'PASS' } } } } },
  health: { status: 200, body: { providers: { chains: { ohlcv: ['twelvedata', 'yfinance', 'tradier'] } } } },
  earnings: { status: 200, body: { has_upcoming: false, earnings_date: '2027-01-29', days_until: 78 } },
  sr: { status: 200, body: {
    support: [262.10, 250.00], resistance: [281.00], suggestedEntry: 262.10, suggestedTarget: 281.00,
    meta: { atr: 14.07, zones: [
      { low: 260.5, high: 262.10, swings: 3, side: 'support', insideZone: false, nearest: true },
      { low: 249.0, high: 250.00, swings: 1, side: 'support', insideZone: false, nearest: false },
      { low: 281.00, high: 283.40, swings: 2, side: 'resistance', insideZone: false, nearest: true },
    ] },
  } },
};
const DOM = {
  error: null,
  cards: [
    { id: 'card-market-backdrop', text: 'Market backdrop ◇ INFO · NEVER GATES THIS PAGE S&P 500 ↑ above +3.9% ...', bodyText: 'S&P 500 ↑ above +3.9% ↓ below -1.3% -4.4% on Nov 5' },
    { id: 'card-stock-header', text: 'AAPL - Apple Inc. Technology • Consumer Electronics $271.00', bodyText: 'AAPL - Apple Inc. Technology • Consumer Electronics $271.00' },
    { id: 'card-technical-read', text: '📈 Technical Read ⚙ ENGINE About this stock only. Trend, momentum and strength against the market · common rules of thumb. Below its 200-day average ...', bodyText: 'Trend, momentum and strength against the market. Below its 200-day average ...' },
    { id: 'card-mr-read', text: '🔄 Mean-Reversion Read ⚙ FORWARD-TESTED A separate question ... No signal today: RSI(2) is 54', bodyText: 'No signal today: RSI(2) is 54, the rule needs below 10' },
    { id: 'card-trade-setup', text: '🎯 Trade Setup ⚙ LEVELS The pullback plan ... Buy $262.10  Stop $250.40', bodyText: 'Buy $262.10  Stop $250.40  Target $281.00  1.6 : 1' },
    { id: 'card-fundamentals', text: '🏢 Fundamentals ◇ INFO Is the business behind the stock in trouble? No red flags.', bodyText: 'No red flags. Next earnings 2027-01-29 · in 78 days' },
    { id: 'card-breakout', text: '🚀 Breakout Not Ready More than 3% under the 60-day high.', bodyText: 'More than 3% under the 60-day high. 60-day high $280.00 · close 3.2% below' },
    { id: 'card-example-collapsible', text: '▼Example CardUptrend Higher highs and higher lows over the last 60 sessions', bodyText: 'Higher highs and higher lows over the last 60 sessions', collapsed: false },
  ],
  header: 'AAPL - Apple Inc. Technology • Consumer Electronics $271.00',
  shortTexts: [{ text: '$271.00', card: 'card-stock-header' }, { text: 'INFO', card: 'card-market-backdrop' }, { text: 'BUY', card: 'card-trade-setup' }],
  fullText: 'Market backdrop ... Technical Read ... Fundamentals ...',
  earningsBadge: false,
  planBuy: '$262.10',
  levelRows: {
    support: 'Support $260.50 – $262.10 · 3.3% below · turned here 3×',
    resistance: 'Resistance $281.00 – $283.40 · 3.7% above · turned here 2×',
  },
  backdrop: {
    rows: [
      { label: 'S&P 500', long: '↑ above +3.9%', short: '↓ below -1.3%', drop: '-4.4% on Nov 5 (largest since Apr 4, 2025)', unavailable: null },
      { label: 'Nasdaq-100 (QQQ)', long: '↑ above +5.0%', short: '↓ below -2.0%', drop: '-6.5% on Nov 5 (largest in data back to Nov 8, 2024)', unavailable: null },
    ],
    vix: 'VIX 18.2 · normal range (latest quote)',
  },
  ticker: 'AAPL',
  timing: { present: true, unavailable: null, price: '$523.88', ticks: [450.00, 510.00, 528.10] },
  ds: { present: true, error: false, symbol: 'AAPL', exchange: 'NasdaqGS', currency: 'USD', cls: 'Stock', dataFrom: 'Twelve Data', verdict: 'PASS',
    qualityRows: [], allPass: true,
    indicatorRows: [['SMA 50 / 200', 'this stock\'s daily closes', 'Average of the last 50 closes'], ['RSI 14', 'this stock\'s daily closes', 'Wilder']], indicatorsUnavailable: false, splitNotes: [],
    chainRows: [{ group: 'price', provider: 'twelvedata' }, { group: 'price', provider: 'yfinance' }, { group: 'price', provider: 'tradier' },
      { group: 'fundamentals', provider: 'finnhub' }, { group: 'fundamentals', provider: 'yfinance' }] },
  narrow: [
    { id: 'card-market-backdrop', scrollWidth: 358, clientWidth: 358 },
    { id: 'card-technical-read', scrollWidth: 358, clientWidth: 358 },
  ],
  pageOverflow: true,
};

// ---------- 1. today's page passes everything ----------
{
  const checks = runChecks(DOM, API, helpers);
  expect(checks.length === CHECK_IDS.length, `runs all ${CHECK_IDS.length} checks`);
  for (const c of checks) expect(c.pass, `current page passes ${c.id} (${c.actual})`);
  expect(!CHECK_IDS.includes('A7'), 'A7 dropped (Fable #5: vacuous)');
}

// helper: mutate, run, expect one check to fail
function mustFail(id, label, mutateDom, mutateApi) {
  const d = clone(DOM); const a = clone(API);
  if (mutateDom) mutateDom(d);
  if (mutateApi) mutateApi(a);
  const c = byId(runChecks(d, a, helpers), id);
  expect(c && !c.pass, `${id} fails: ${label}${c ? ` -> ${c.actual}` : ''}`);
}
function mustPass(id, label, mutateDom, mutateApi) {
  const d = clone(DOM); const a = clone(API);
  if (mutateDom) mutateDom(d);
  if (mutateApi) mutateApi(a);
  const c = byId(runChecks(d, a, helpers), id);
  expect(c && c.pass, `${id} passes: ${label}${c ? ` -> ${c.actual}` : ''}`);
}

// ---------- A1 card order ----------
mustFail('A1', 'backdrop below the header (pre-Step-7 order)', d => {
  [d.cards[0], d.cards[1]] = [d.cards[1], d.cards[0]];
});
mustFail('A1', 'MR card missing', d => { d.cards = d.cards.filter(c => c.id !== 'card-mr-read'); });
mustFail('A1', 'Fundamentals before Trade Setup', d => {
  const i = d.cards.findIndex(c => c.id === 'card-trade-setup');
  [d.cards[i], d.cards[i + 1]] = [d.cards[i + 1], d.cards[i]];
});
mustFail('A1', 'no cards found at all', d => { d.cards = []; });

// ---------- A2 removed elements ----------
mustFail('A2', 'old BUY/HOLD/AVOID badge', d => { d.shortTexts.push({ text: 'HOLD', card: 'card-stock-header' }); });
mustFail('A2', '"BUY" as a badge outside the Trade Setup price label', d => { d.shortTexts.push({ text: 'BUY', card: 'card-stock-header' }); });
mustFail('A2', '"AVOID" inside the Trade Setup card', d => { d.shortTexts.push({ text: 'AVOID', card: 'card-trade-setup' }); });
mustFail('A2', 'old T:/F:/S:/R: chips', d => { d.shortTexts.push({ text: 'T:S', card: 'card-stock-header' }, { text: 'R:F', card: 'card-stock-header' }); });
mustFail('A2', 'Simple Checklist toggle back (Day 126)', d => { d.fullText += ' ✅ Simple Checklist (9 criteria)'; });
mustFail('A2', '"N/9 criteria met" badge back (Day 126)', d => { d.fullText += ' ⏸️ No Trade 7/9 criteria met'; });
mustFail('A2', 'Holding Period selector', d => { d.fullText += ' Holding Period: 2-6 weeks'; });
mustFail('A2', 'Favorable market label', d => { d.cards[0].text += ' Market: Favorable'; });
mustFail('A2', 'Position Size banner', d => { d.fullText += ' Position Size: full (1% risk)'; });
mustFail('A2', 'VIABLE badge', d => { d.fullText += ' ✅ VIABLE'; });
mustFail('A2', '"Stock not recommended" warning', d => { d.fullText += ' ⚠️ Stock not recommended'; });
mustPass('A2', 'lower-case "hold through the report" is fine', d => { d.fullText += ' decide whether to hold through the report'; });

// ---------- A3 backdrop vs API ----------
mustFail('A3', 'S&P long-term % off by 0.1', d => { d.backdrop.rows[0].long = '↑ above +4.0%'; });
mustFail('A3', 'S&P direction flipped', d => { d.backdrop.rows[0].short = '↑ above -1.3%'; });
mustFail('A3', 'QQQ drop date wrong', d => { d.backdrop.rows[1].drop = '-6.5% on Nov 4 (largest in data back to Nov 8, 2024)'; });
mustFail('A3', 'VIX value wrong', d => { d.backdrop.vix = 'VIX 19.2 · normal range (latest quote)'; });
mustFail('A3', 'VIX band word wrong (old "calm")', d => { d.backdrop.vix = 'VIX 18.2 · calm (latest quote)'; });
mustFail('A3', 'QQQ row missing', d => { d.backdrop.rows = d.backdrop.rows.slice(0, 1); });
mustFail('A3', 'spy payload not captured', null, a => { a.spy = { status: null, body: null }; });
mustPass('A3', 'rounding boundary: payload 2.25 rendered with toFixed(1)', d => {
  d.backdrop.rows[0].long = `↑ above ${fmtPct(2.25)}`;
}, a => { a.spy.body.trend.pctVsSma200 = 2.25; });
mustPass('A3', 'no down day state', d => {
  d.backdrop.rows[0].drop = 'no down day in the last 10 sessions';
}, a => { a.spy.body.trend.biggestDrop10d = { noDownDay: true }; });
mustFail('A3', 'no down day in API but UI shows a drop', null, a => { a.spy.body.trend.biggestDrop10d = { noDownDay: true }; });
mustPass('A3', 'short history -> "not enough history"', d => {
  d.backdrop.rows[1].long = 'not enough history';
}, a => { a.qqq.body.trend.aboveSma200 = null; a.qqq.body.trend.pctVsSma200 = null; });
mustPass('A3', 'QQQ 500 -> "couldn\'t load" row', d => {
  d.backdrop.rows[1] = { label: 'Nasdaq-100 (QQQ)', long: null, short: null, drop: null, unavailable: "couldn't load (boom)" };
}, a => { a.qqq = { status: 500, body: { error: 'boom' } }; });
mustFail('A3', 'QQQ 500 but UI shows numbers', null, a => { a.qqq = { status: 500, body: { error: 'boom' } }; });
mustPass('A3', 'unknown VIX regime -> no band word', d => {
  d.backdrop.vix = 'VIX 18.2 (latest quote)';
}, a => { a.vix.body.regime = 'unknown'; });
mustFail('A3', 'unknown VIX regime but UI shows a word', null, a => { a.vix.body.regime = 'unknown'; });

// ---------- A4 classification ----------
mustFail('A4', 'raw "Unknown • Unknown" (pre-Step-7 ETF header)', d => {
  d.header = 'SMH - VanEck Semiconductor ETF Unknown • Unknown';
});
mustFail('A4', 'ETF payload but header lacks the ETF wording', d => {
  d.header = 'SMH - VanEck Semiconductor ETF Sector and industry not reported';
}, a => { a.stock.body.quoteType = 'ETF'; });
mustPass('A4', 'ETF header', d => {
  d.header = 'SMH - VanEck Semiconductor ETF Exchange-traded fund (ETF)';
}, a => { a.stock.body.quoteType = 'ETF'; });
mustFail('A4', 'stock payload not captured', null, a => { a.stock = { status: null, body: null }; });

// ---------- A5 earnings ----------
mustFail('A5', 'badge shown but has_upcoming false', d => { d.earningsBadge = true; });
mustFail('A5', 'has_upcoming true but no badge', null, a => { a.earnings.body.has_upcoming = true; });
mustPass('A5', 'has_upcoming true with badge', d => { d.earningsBadge = true; }, a => { a.earnings.body.has_upcoming = true; });
mustFail('A5', 'earnings 500 but Fundamentals does not say it couldn\'t check', null, a => { a.earnings = { status: 500, body: { error: 'x' } }; });
mustPass('A5', 'earnings 500 and Fundamentals says so', d => {
  d.cards.find(c => c.id === 'card-fundamentals').text += " Couldn't check the earnings calendar.";
}, a => { a.earnings = { status: 500, body: { error: 'x' } }; });
mustFail('A5', 'earnings OK but Fundamentals says it couldn\'t check', d => {
  d.cards.find(c => c.id === 'card-fundamentals').text += " Couldn't check the earnings calendar.";
});
mustFail('A5', 'earnings payload not captured', null, a => { a.earnings = { status: null, body: null }; });

// ---------- A6 blank cards ----------
// Realistic blank states (Fable code review #1): the title row + subtitle alone are
// longer than 40 chars, so the check must measure only what is below them.
mustFail('A6', 'Fundamentals shows title row + subtitle but an empty body', d => {
  const c = d.cards.find(x => x.id === 'card-fundamentals');
  c.text = '🏢 Fundamentals◇ INFOIs the business behind the stock in trouble? Facts, not a score.'; c.bodyText = '';
});
mustFail('A6', 'Trade Setup body empty (PullbackPlan rendered nothing)', d => {
  const c = d.cards.find(x => x.id === 'card-trade-setup');
  c.text = '🎯 Trade Setup⚙ LEVELS◇ YOUR CALLThe pullback plan: wait for a dip to support, then buy.'; c.bodyText = '  ';
});
mustFail('A6', 'Technical Read body missing from extraction (no vacuous pass)', d => {
  delete d.cards.find(x => x.id === 'card-technical-read').bodyText;
});
mustPass('A6', 'short but real body ("Couldn\'t load …") counts', d => {
  d.cards.find(x => x.id === 'card-mr-read').bodyText = "Couldn't load the dip rules (no response)";
});
mustFail('A6', 'no cards found', d => { d.cards = []; });
mustPass('A6', 'collapsed card showing title + status word (RIVN Example Card)', d => {
  const c = d.cards.find(x => x.id === 'card-example-collapsible'); c.text = '▶Example CardDowntrend'; c.bodyText = ''; c.collapsed = true;
});
mustFail('A6', 'collapsed card with only its title', d => {
  const c = d.cards.find(x => x.id === 'card-example-collapsible'); c.text = '▶Example Card'; c.bodyText = ''; c.collapsed = true;
});


// ---------- A10 Buy and level rows match /api/sr (Day 126) ----------
mustFail('A10', 'Buy tile differs from max(support)', d => { d.planBuy = '$250.00'; });
mustFail('A10', 'support row shows the wrong zone', d => { d.levelRows.support = 'Support $249.00 – $250.00 · 8.0% below · turned here 1×'; });
mustFail('A10', 'resistance row missing', d => { d.levelRows.resistance = null; });
mustFail('A10', 'api suggestedEntry disagrees with max(support)', null, a => { a.sr.body.suggestedEntry = 250.00; });
mustFail('A10', 'zone high no longer equals suggestedEntry', null, a => { a.sr.body.meta.zones[0].high = 262.50; });
mustFail('A10', '/api/sr response not captured', null, a => { a.sr = { status: null, body: null }; });
mustFail('A10', 'payload in the old format (no meta.zones)', null, a => { delete a.sr.body.meta.zones; });
mustFail('A10', 'a side with no zone must say "None within"', null, a => { a.sr.body.meta.zones = a.sr.body.meta.zones.filter(z => z.side !== 'resistance'); a.sr.body.resistance = []; a.sr.body.suggestedTarget = null; });
mustPass('A10', 'a side with no zone says "None within 30% above"', d => { d.levelRows.resistance = 'Resistance None within 30% above. The stock is at its 52-week high.'; },
  a => { a.sr.body.meta.zones = a.sr.body.meta.zones.filter(z => z.side !== 'resistance'); a.sr.body.resistance = []; a.sr.body.suggestedTarget = null; });
mustPass('A10', 'one-price zone shows one price', d => { d.levelRows.support = 'Support $262.10 · 3.3% below · turned here 1×'; },
  a => { a.sr.body.meta.zones[0].low = 262.10; });
mustPass('A10', '/api/sr failed and the page shows no Buy or rows', d => { d.planBuy = null; d.levelRows = { support: null, resistance: null }; }, a => { a.sr = { status: 500, body: null }; });
mustFail('A10', '/api/sr failed but the page still shows a Buy', null, a => { a.sr = { status: 500, body: null }; });
mustPass('A10', 'ATR missing: no Buy tile, Trade Setup text still shows the Buy', d => { d.planBuy = null; d.cards.find(c => c.id === 'card-trade-setup').text = 'Trade Setup Buy near support at $262.10, target $281.00.'; });

// ---------- A11 Data Sources tab matches the backend (Day 126) ----------
mustFail('A11', 'tab did not render', d => { d.ds = { present: false, note: 'Data Sources tab button not found' }; });
mustFail('A11', 'wrong exchange shown', d => { d.ds.exchange = 'Toronto'; });
mustFail('A11', 'wrong currency shown', d => { d.ds.currency = 'CAD'; });
mustFail('A11', 'wrong class shown', d => { d.ds.cls = 'ETF'; });
mustFail('A11', 'data-from does not match the provenance source', d => { d.ds.dataFrom = 'Yahoo (yfinance)'; });
mustFail('A11', 'verdict differs from the backend level', d => { d.ds.verdict = 'WARN'; });
const FAILING = a => { a.provenance.body.quality = { state: 'ok', level: 'FAIL', checks: { integrity: { level: 'FAIL', note: '100% flat' }, jumps: { level: 'WARN', note: 'x' }, freshness: { level: 'PASS' }, history: { level: 'PASS' } } }; };
mustFail('A11', 'backend FAIL hidden by a PASS verdict and no rows (the original bug)', null, FAILING);
mustFail('A11', 'backend FAIL shown as FAIL but the failing row is missing', d => { d.ds.verdict = 'FAIL'; d.ds.allPass = false; d.ds.qualityRows = [{ level: 'WARN', text: 'jumps' }]; }, FAILING);
mustPass('A11', 'backend FAIL shown with its rows', d => { d.ds.verdict = 'FAIL'; d.ds.allPass = false; d.ds.qualityRows = [{ level: 'FAIL', text: 'integrity' }, { level: 'WARN', text: 'jumps' }]; }, FAILING);
mustFail('A11', 'all checks pass but the tab does not say so', d => { d.ds.allPass = false; });
mustFail('A11', 'SOXL.NE must show FAIL even if the backend and tab both said PASS', d => { d.ticker = 'SOXL.NE'; });
mustPass('A11', 'SOXL.NE shows FAIL', d => { d.ticker = 'SOXL.NE'; d.ds.verdict = 'FAIL'; d.ds.allPass = false; d.ds.qualityRows = [{ level: 'FAIL', text: 'integrity' }]; d.ds.splitNotes = ['Split-adjusted by STA: 3-for-1 on 2026-05-25. x']; },
  a => { a.provenance.body.quality = { state: 'ok', level: 'FAIL', checks: { integrity: { level: 'FAIL' } }, facts: { splits: [{ text: '3-for-1 on 2026-05-25', status: 'unadjusted' }] } }; });
mustFail('A11', 'SOXL.NE without the split-adjusted line', d => { d.ticker = 'SOXL.NE'; d.ds.verdict = 'FAIL'; d.ds.allPass = false; d.ds.qualityRows = [{ level: 'FAIL', text: 'integrity' }]; },
  a => { a.provenance.body.quality = { state: 'ok', level: 'FAIL', checks: { integrity: { level: 'FAIL' } } }; });
mustFail('A11', 'indicator table has fewer rows than the backend sent', d => { d.ds.indicatorRows.pop(); });
mustFail('A11', 'indicator row name differs from the backend', d => { d.ds.indicatorRows[1][0] = 'RSI 21'; });
mustFail('A11', 'indicator row with an empty From', d => { d.ds.indicatorRows[0][1] = ''; });
mustFail('A11', 'backend sent no indicators and the tab says nothing', null, a => { a.provenance.body.indicators = null; });
mustPass('A11', 'backend sent no indicators and the tab says so', d => { d.ds.indicatorRows = []; d.ds.indicatorsUnavailable = true; }, a => { a.provenance.body.indicators = null; });
mustFail('A11', 'backend adjusted a split but the tab shows no split line', null, a => { a.provenance.body.quality.facts = { splits: [{ text: '3-for-1 on 2026-05-25', status: 'unadjusted' }] }; });
mustPass('A11', 'backend adjusted a split and the tab shows the line', d => { d.ds.splitNotes = ['Split-adjusted by STA: 3-for-1 on 2026-05-25.']; }, a => { a.provenance.body.quality.facts = { splits: [{ text: '3-for-1 on 2026-05-25', status: 'unadjusted' }] }; });
mustFail('A11', 'tab shows a split line the backend did not adjust', d => { d.ds.splitNotes = ['Split-adjusted by STA: 3-for-1 on 2026-05-25.']; });
mustPass('A11', 'a split the provider already adjusted needs no line', null, a => { a.provenance.body.quality.facts = { splits: [{ text: '3-for-1', status: 'already_adjusted' }] }; });
mustPass('A12', 'ruler matches the page price and shows the averages');
mustFail('A12', 'dot shows a different price than the page', d => { d.timing.price = '$523.00'; });
mustFail('A12', 'ruler marks out of price order', d => { d.timing.ticks = [528.10, 510.00, 450.00]; });
mustFail('A12', 'no ruler marks at all', d => { d.timing.ticks = []; });
mustFail('A12', 'ruler marks contain NaN', d => { d.timing.ticks = [450.00, NaN, 528.10]; });
mustFail('A12', 'ruler drawn but /api/sr has no ATR', null, a => { delete a.sr.body.meta.atr; });
mustFail('A12', 'neither ruler nor a reason is shown', d => { d.timing = { present: false, unavailable: null, price: null, ticks: [] }; });
mustFail('A12', 'cannot be drawn although an ATR exists', d => { d.timing = { present: false, unavailable: "Can't tell: ATR unavailable.", price: null, ticks: [] }; });
mustPass('A12', 'not drawn, honest reason: needs 200 days of history', d => { d.timing = { present: false, unavailable: "Can't tell: 21-day average not computed (needs 200 days of history).", price: null, ticks: [] }; });
mustFail('A12', 'the Weak headline sentence is still on the Technical Read card', d => { d.cards.find(c => c.id === 'card-technical-read').text += " This doesn't look like a market leader right now"; });
mustFail('A12', 'the old volume verdict is still on the card', d => { d.cards.find(c => c.id === 'card-technical-read').text += ' No, sellers lead'; });
mustFail('A12', 'the facts block title is missing', d => { const c = d.cards.find(x => x.id === 'card-technical-read'); c.text = c.text.replace('Trend, momentum and strength against the market', ''); });
mustFail('A12', 'old verdict wording still on the Technical Read card', d => { d.cards.find(c => c.id === 'card-technical-read').text += ' Not yet, below it'; });
mustFail('A11', 'Stooq listed in a chain', d => { d.ds.chainRows.push({ group: 'price', provider: 'stooq' }); });
mustFail('A11', 'Tradier missing from the price chain', d => { d.ds.chainRows = d.ds.chainRows.filter(r => r.provider !== 'tradier'); });
mustFail('A11', 'health chains not captured', null, a => { a.health = { status: null, body: null }; });
mustFail('A11', '/api/stock not captured', null, a => { a.stock = { status: null, body: null }; });
mustFail('A11', 'provenance failed but the tab shows no error and Retry', null, a => { a.provenance = { status: 500, body: null }; });
mustPass('A11', 'provenance failed and the tab shows an error', d => { d.ds.error = true; }, a => { a.provenance = { status: 500, body: null }; });
mustFail('A11', 'provenance answered but the tab shows an error', d => { d.ds.error = true; });
mustPass('A11', 'quality state not_cached and no verdict shown', d => { d.ds.verdict = null; d.ds.allPass = false; }, a => { a.provenance.body.quality = { state: 'not_cached' }; });
mustFail('A11', 'nothing cached but a verdict is shown', null, a => { a.provenance.body.quality = { state: 'not_cached' }; });
mustPass('A11', 'quality state error shows an error', d => { d.ds.error = true; d.ds.verdict = null; }, a => { a.provenance.body.quality = { state: 'error', reason: 'x' }; });
mustFail('A11', 'unknown exchange must say unknown, not blank', d => { d.ds.exchange = ''; }, a => { a.stock.body.exchange = null; });
mustPass('A11', 'unknown exchange shown as unknown', d => { d.ds.exchange = 'unknown'; }, a => { a.stock.body.exchange = null; });

// ---------- A9 390px ----------
mustFail('A9', 'card wider than its box', d => { d.narrow[1].scrollWidth = 420; });
mustFail('A9', 'nothing measured', d => { d.narrow = []; });
mustPass('A9', 'page-level overflow alone is reported, not failed', d => { d.pageOverflow = true; });

// ---------- load error ----------
{
  const d = clone(DOM); d.error = 'Failed to fetch stock data';
  const checks = runChecks(d, API, helpers);
  expect(checks.every(c => !c.pass), 'error banner -> every check fails (no vacuous pass)');
}

// ---------- never throws ----------
{
  let threw = false;
  try { runChecks({}, {}, helpers); runChecks(null, null, helpers); } catch { threw = true; }
  expect(!threw, 'empty / null input does not throw');
  const checks = runChecks({}, {}, helpers);
  expect(checks.every(c => !c.pass), 'empty input -> every check fails');
}

console.log(`\n${passes} passed, ${failures} failed`);
process.exit(failures ? 1 : 0);
