// Live quote label/state logic (Day 126). Run: cd frontend && node scripts/test_live_quote.mjs
import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { basisLabel, describeLiveQuote, acceptQuote, formatTradeTime, formatCloseDate, nextPollDelayMs, signedPct } =
  await import('../src/utils/liveQuote.js');

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };
const NOW = new Date('2026-11-16T20:00:00Z');
const base = { available: true, ticker: 'NVDA', session: 'regular', price: 156.05, change: -6.8, change_pct: -4.18,
  last_trade_at: '2026-11-16T14:51:00-05:00', age_minutes: 4, last_close: { price: 162.85, date: '2026-11-13' }, source: 'tradier' };

let d = describeLiveQuote(base, NOW);
ok(d.state === 'recent' && d.statusText === 'Last trade 4 min ago', '4 minutes old reads "Last trade 4 min ago"');
ok(d.tradeTime === '2:51pm ET', 'trade time is 2:51pm ET');
ok(d.price === 156.05 && d.changePct === -4.18, 'price and change pass through');
ok(d.lastClose.price === 162.85 && d.lastClose.dateLabel === 'Nov 13', 'last close line: $162.85, Nov 13');
d = describeLiveQuote({ ...base, age_minutes: 2 }, NOW);
ok(d.state === 'live' && d.statusText === 'Live', '2 minutes or less reads Live');
d = describeLiveQuote({ ...base, age_minutes: 2.1 }, NOW);
ok(d.state === 'recent', 'just over 2 minutes is not Live');
d = describeLiveQuote({ ...base, age_minutes: 15 }, NOW);
ok(d.state === 'recent' && d.statusText === 'Last trade 15 min ago', 'a 15-minute-delayed feed is labelled with its real age');
d = describeLiveQuote({ ...base, session: 'pre', age_minutes: 30 }, NOW);
ok(d.state === 'pre' && d.statusText === 'Pre-market' && d.price === 156.05, 'pre-market is labelled');
d = describeLiveQuote({ ...base, session: 'post', last_trade_at: '2026-11-16T17:40:00-05:00' }, NOW);
ok(d.state === 'post' && d.statusText === 'After hours' && d.tradeTime === '5:40pm ET', 'after hours is labelled');
d = describeLiveQuote({ ...base, session: 'closed', price: null, change: null, change_pct: null }, NOW);
ok(d.state === 'closed' && d.price === null && d.statusText === 'Market closed, last close shown' && d.lastClose.price === 162.85, 'closed: no live price, close line kept');
d = describeLiveQuote({ available: false, reason: 'no recent trades', ticker: 'THIN' }, NOW);
ok(d.state === 'unavailable' && d.price === null && d.statusText === 'Live price unavailable (no recent trades)', 'unavailable names the reason');
d = describeLiveQuote({ available: false }, NOW);
ok(d.state === 'unavailable' && d.reason === 'source down', 'unavailable with no reason still says something');
ok(describeLiveQuote(null).state === 'none' && describeLiveQuote(undefined).state === 'none' && describeLiveQuote('x').state === 'none', 'null / undefined / junk = none');

// never show a price we cannot trust
for (const bad of [NaN, Infinity, -1, 0, '156', null]) {
  const r = describeLiveQuote({ ...base, price: bad }, NOW);
  ok(r.price === null && r.state === 'unavailable', `bad price ${String(bad)} is never shown`);
}
d = describeLiveQuote({ ...base, last_trade_at: 'garbage' }, NOW);
ok(d.state === 'unavailable' && d.price === null, 'price with an unreadable time is not shown as live');
d = describeLiveQuote({ ...base, last_trade_at: undefined }, NOW);
ok(d.state === 'unavailable' && d.price === null, 'price with no time is not shown as live');
d = describeLiveQuote({ ...base, change_pct: NaN, change: undefined }, NOW);
ok(d.price === 156.05 && d.changePct === null && d.change === null, 'NaN change drops the change, keeps the price');
d = describeLiveQuote({ ...base, last_close: null, change: null, change_pct: null }, NOW);
ok(d.lastClose === null && d.price === 156.05, 'no last close: price still shows, no close line');
d = describeLiveQuote({ ...base, last_close: { price: NaN, date: '2026-11-13' } }, NOW);
ok(d.lastClose === null, 'a NaN last close is dropped');
d = describeLiveQuote({ ...base, age_minutes: -3 }, NOW);
ok(d.state === 'live', 'a negative age (clock skew) is treated as 0');
d = describeLiveQuote({ ...base, age_minutes: undefined }, NOW);
ok(d.state === 'recent' && d.statusText === 'Last trade time shown', 'missing age: no invented minutes');
d = describeLiveQuote({ ...base, last_close: { price: 14.69, date: '2025-12-31' } }, NOW);
ok(d.lastClose.dateLabel === 'Dec 31, 2025', 'a close from another year shows the year');

// wrong ticker dropped
ok(acceptQuote(base, 'NVDA') === base && acceptQuote(base, 'nvda') === base, 'same ticker accepted (any case)');
ok(acceptQuote(base, 'AAPL') === null, 'a reply for another ticker is dropped');
ok(acceptQuote({ available: false }, 'NVDA') === null, 'a reply with no ticker is dropped');
ok(acceptQuote(null, 'NVDA') === null && acceptQuote(base, undefined) === null, 'null reply / no ticker is dropped');

ok(formatTradeTime('nope') === null && formatTradeTime(undefined) === null, 'bad time string gives null');
ok(formatTradeTime('2026-11-16T12:05:00-05:00') === '12:05pm ET', 'noon reads 12:05pm');
ok(formatTradeTime('2026-11-16T09:30:00-05:00') === '9:30am ET', 'morning reads am');
ok(formatTradeTime('2026-11-16T19:51:00Z') === '2:51pm ET', 'UTC input is shown in New York time');
ok(formatCloseDate('13/11/2026') === null && formatCloseDate(null) === null, 'bad close date gives null');
ok(nextPollDelayMs('live') === 60000 && nextPollDelayMs('post') === 60000 && nextPollDelayMs('pre') === 60000, 'open sessions poll every minute');
ok(nextPollDelayMs('closed') === 300000 && nextPollDelayMs('unavailable') === 300000 && nextPollDelayMs('none') === 300000, 'closed / failing re-check every 5 minutes');
ok(signedPct(-4.18) === '−4.18%' && signedPct(1.2) === '+1.20%' && signedPct(0) === '+0.00%' && signedPct(NaN) === '', 'signed percent');

// words for which price a number is measured from
ok(basisLabel(describeLiveQuote({ ...base, age_minutes: 1 }, NOW)) === 'now', 'Live reads "now"');
ok(basisLabel(describeLiveQuote({ ...base, age_minutes: 9 }, NOW)) === 'last trade 2:51pm ET', 'an older trade reads "last trade 2:51pm ET", never "now"');
ok(basisLabel(describeLiveQuote({ ...base, session: 'pre' }, NOW)) === 'pre-market', 'pre-market is named');
ok(basisLabel(describeLiveQuote({ ...base, session: 'post' }, NOW)) === 'after hours', 'after hours is named');
ok(basisLabel(describeLiveQuote({ ...base, session: 'closed', price: null }, NOW)) === 'last close', 'closed reads "last close"');
ok(basisLabel(null) === 'last close' && basisLabel(undefined) === 'last close' && basisLabel({}) === 'last close', 'no live data reads "last close"');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
