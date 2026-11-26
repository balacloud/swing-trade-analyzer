// describePriceFreshness: the Analyze header's "are these prices current?" line (Day 135).
//   cd frontend && node scripts/test_price_freshness.mjs
import { describePriceFreshness } from '../src/utils/priceFreshness.js';

let pass = 0, fail = 0;
const expect = (got, want, m) => { if (got === want) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}: got ${JSON.stringify(got)}, want ${JSON.stringify(want)}`); } };
const has = (got, part, m) => { if (typeof got === 'string' && got.includes(part)) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}: ${JSON.stringify(got)} lacks ${JSON.stringify(part)}`); } };
const lacks = (got, part, m) => { if (typeof got === 'string' && !got.includes(part)) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}: ${JSON.stringify(got)}`); } };

const base = { newestDate: '2026-11-24', expectedDate: '2026-11-25', sessionsBehind: 1, behindLevel: 'PASS', servedFromStaleCache: false, maybePartial: false };
expect(describePriceFreshness(base, 'AAPL'), null, 'current copy: says nothing');
expect(describePriceFreshness({ ...base, sessionsBehind: 2 }, 'AAPL'), null, 'PASS level (0-2 behind, a holiday can explain it): says nothing');

const stale = describePriceFreshness({ ...base, servedFromStaleCache: true }, 'VFV.TO');
has(stale, 'Showing saved prices up to Nov 24', 'saved copy: states the date');
has(stale, 'Yahoo is the only price source for Canadian tickers', 'Canada ticker: names the single source');
lacks(describePriceFreshness({ ...base, servedFromStaleCache: true }, 'AAPL'), 'Canadian', 'US ticker: no Canada sentence');
has(describePriceFreshness({ ...base, servedFromStaleCache: true, maybePartial: true }, 'AAPL'), 'may be unfinished', 'maybePartial: says so');
lacks(stale, 'unfinished', 'not partial: no partial sentence');
for (const t of ['X.NE', 'X.NEO', 'PNG.V', 'X.CN', 'x.to']) has(describePriceFreshness({ ...base, servedFromStaleCache: true }, t), 'Canadian', `Canadian suffix ${t}`);
lacks(describePriceFreshness({ ...base, servedFromStaleCache: true }, 'TO'), 'Canadian', 'a US ticker named TO is not Canadian');

const behind = describePriceFreshness({ newestDate: '2026-11-19', expectedDate: '2026-11-25', sessionsBehind: 4, behindLevel: 'WARN', servedFromStaleCache: false, maybePartial: false }, 'AAPL');
has(behind, 'Latest price bar is Nov 19', 'WARN level: names the bar date');
has(behind, 'last completed trading day is Nov 25', 'WARN level: names the expected day');
has(behind, '4 trading days behind', 'WARN level: names the gap');
has(describePriceFreshness({ newestDate: '2026-11-10', expectedDate: '2026-11-25', sessionsBehind: 11, behindLevel: 'FAIL' }, 'AAPL'), '11 trading days behind', 'FAIL level also shown');

// stale copy with no date known still speaks (the flag is the fact)
has(describePriceFreshness({ servedFromStaleCache: true, newestDate: null }, 'AAPL'), 'Showing saved prices: every', 'saved copy without a date');
// never throws, never guesses
expect(describePriceFreshness(null, 'AAPL'), null, 'null -> null');
expect(describePriceFreshness(undefined, 'AAPL'), null, 'undefined -> null');
expect(describePriceFreshness('garbage', 'AAPL'), null, 'string -> null');
expect(describePriceFreshness({}, 'AAPL'), null, 'empty object -> null');
expect(describePriceFreshness({ behindLevel: 'WARN', newestDate: 'garbage' }, 'AAPL'), null, 'WARN with a bad date -> null');
expect(describePriceFreshness({ ...base, servedFromStaleCache: true }, undefined) !== null, true, 'missing ticker still works');
// facts, not verdicts
for (const s of [stale, behind]) for (const w of ['Strong', 'Weak', 'Good', 'Bad', 'Unreliable', 'Danger']) lacks(s, w, `no verdict word "${w}"`);

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
