// planStatus: is the Trade Setup plan already behind the live price? (Day 133)
//   cd frontend && node scripts/test_plan_status.mjs
import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { planStatus, planStatusFromSr, lastCompletedClose } = await import('../src/utils/planStatus.js');

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };

// SOXL.NE on 2026-11-24 (measured): support zone 9.22 - 10.73, stop 6.78, live 8.54
const zones = [
  { low: 9.22, high: 10.73, side: 'support', nearest: true, insideZone: false },
  { low: 12.05, high: 13.46, side: 'resistance', nearest: true },
];
const S = (o) => planStatus({ stop: 6.78, zones, livePrice: 8.54, liveState: 'recent', ...o });

// ---- the real case
let r = S({});
ok(r.void === true && r.reason === 'below_support' && r.zoneLow === 9.22 && r.zoneHigh === 10.73, 'SOXL.NE 8.54 is below the 9.22 zone low: void below_support');
ok(r.belowStop === false, 'SOXL.NE 8.54 is above the 6.78 stop: no stop clause');
ok(S({ liveState: 'live' }).void === true, 'state live voids');

// ---- boundary: strict <
ok(S({ livePrice: 9.22 }).void === false, 'equal to the zone low is NOT void');
ok(S({ livePrice: 9.21 }).void === true, 'one cent below the zone low is void');
ok(S({ livePrice: 9.23 }).void === false, 'inside the zone (arriving at the buy) is not void');
ok(S({ livePrice: 10.99 }).void === false, 'above the zone is not void');
ok(S({ livePrice: 6.78 }).void === true && S({ livePrice: 6.78 }).belowStop === false, 'equal to the stop: still void by zone, not below the stop');
ok(S({ livePrice: 6.77 }).belowStop === true && S({ livePrice: 6.77 }).void === true, 'below the stop adds the stop clause');

// ---- quote state gates
r = S({ liveState: 'pre' });
ok(r.void === false && r.factOnly === true && r.reason === 'below_support', 'pre-market: fact line only, not void');
r = S({ liveState: 'post' });
ok(r.void === false && r.factOnly === true, 'after hours: fact line only, not void');
for (const st of ['closed', 'unavailable', 'none', null, undefined, 'weird']) {
  r = S({ liveState: st });
  ok(r.void === false && r.factOnly === false, `quote state ${String(st)}: card unchanged`);
}

// ---- bad live prices are ignored
for (const bad of [null, undefined, 0, -1, NaN, Infinity, -Infinity, '8.54', {}, []]) {
  r = S({ livePrice: bad });
  ok(r.void === false && r.factOnly === false, `live price ${JSON.stringify(bad) ?? String(bad)} is ignored`);
}

// ---- no zone information
r = planStatus({ stop: 6.78, zones: null, livePrice: 6.5, liveState: 'live' });
ok(r.void === true && r.reason === 'below_stop' && r.zoneLow === null, 'legacy payload (no zones): below the stop voids (below_stop)');
ok(planStatus({ stop: 6.78, zones: [], livePrice: 6.78, liveState: 'live' }).void === false, 'no zones, equal to the stop: not void');
ok(planStatus({ stop: null, zones: null, livePrice: 1, liveState: 'live' }).void === false, 'no zones and no stop: nothing to compare, not void');
ok(planStatus({ stop: 6.78, zones: 'x', livePrice: 1, liveState: 'live' }).reason === 'below_stop', 'zones not an array is treated as no zones');
ok(planStatus({ stop: 6.78, zones: [{ low: NaN, high: 10, side: 'support', nearest: true }], livePrice: 1, liveState: 'live' }).reason === 'below_stop', 'a zone with a NaN edge is not used');
ok(S({ zones: [{ low: 9.22, high: 10.73, side: 'support', nearest: false }] }).void === false, 'a support zone not flagged nearest is not the plan zone (stop 6.78 not crossed: not void)');
ok(S({ zones: [{ low: 9.22, high: 10.73, side: 'support', nearest: false }], stop: 8.6 }).reason === 'below_stop', '...so with no nearest support zone the stop rule applies');
ok(S({ zones: [{ low: 9.22, high: 10.73, side: 'resistance', nearest: true }] }).void === false, 'a resistance zone is never the plan zone (stop 6.78 is not crossed)');
ok(S({ zones: undefined, stop: undefined }).void === false, 'undefined inputs do not throw');
ok(planStatus().void === false && planStatus(null) !== undefined, 'called with nothing, it does not throw');

// ---- wrapper: planStatusFromSr
const sr = {
  currentPrice: 10.99, support: [10.73, 9.22], suggestedEntry: 10.73, suggestedTarget: 12.05,
  meta: { atr: 1.975, zones, candle: { barComplete: true, date: '2026-11-23' }, prevBar: { close: 7.79, date: '2026-11-20' } },
};
const live = { price: 8.54, state: 'recent', tradeTime: '2:51pm ET', lastClose: { price: 10.99 } };
let w = planStatusFromSr(sr, live);
ok(w.void === true && w.reason === 'below_support', 'wrapper: SOXL.NE payload and live 8.54 -> void');
ok(w.close.price === 10.99 && w.close.dateLabel === 'Nov 23', 'wrapper: last close comes from /api/sr (10.99, Nov 23)');
ok(w.tradeTime === '2:51pm ET' && w.basis === 'last trade 2:51pm ET', 'wrapper: trade time and basis label come from the quote');
ok(w.levelsPrice === 10.99 && w.levelsAreCompletedBar === true, 'wrapper: levels were measured at 10.99, a completed bar');

// stop rule uses the PLAN stop (entry - 2 ATR): 10.73 - 3.95 = 6.78
w = planStatusFromSr(sr, { ...live, price: 6.5 });
ok(w.void === true && w.belowStop === true, 'wrapper: stop is entry - 2 ATR (6.78); 6.50 is below it');

// forming bar: the card's last close is prevBar
const srForming = { ...sr, currentPrice: 9.0, meta: { ...sr.meta, candle: { barComplete: false, date: '2026-11-24' }, prevBar: { close: 10.99, date: '2026-11-23' } } };
ok(lastCompletedClose(srForming).price === 10.99 && lastCompletedClose(srForming).dateLabel === 'Nov 23', 'forming bar: last close is prevBar (10.99, Nov 23)');
w = planStatusFromSr(srForming, live);
ok(w.levelsPrice === 9.0 && w.levelsAreCompletedBar === false, 'forming bar: levels were measured at the forming price, flagged not completed');

// states that must leave the card alone
w = planStatusFromSr(sr, { price: null, state: 'closed' });
ok(w.void === false && w.factOnly === false && w.close === null, 'closed market: no status, no extra fields');
ok(planStatusFromSr(null, live).void === false, 'no /api/sr data: not void');
ok(planStatusFromSr(sr, null).void === false, 'no live quote at all: not void');
ok(planStatusFromSr({ ...sr, support: [] }, live).void === false, 'no_support: the card shows no plan, so the live price is never "behind" it (edge pass, Day 133)');
ok(planStatusFromSr({ ...sr, support: [] }, live).levelsPrice === null, 'no_support: no Key Levels note either');
ok(planStatusFromSr({ ...sr, currentPrice: null, meta: { ...sr.meta, candle: { barComplete: true } } }, live).void === false, 'no usable last close (the card says "last close didn\'t load"): not void');
ok(planStatusFromSr({ ...sr, currentPrice: NaN }, live).void === false, 'NaN price in /api/sr: not void');
ok(planStatusFromSr({ ...sr, currentPrice: 9.0, meta: { ...sr.meta, candle: { barComplete: false, date: '2026-11-24' }, prevBar: { close: null, date: '2026-11-23' } } }, live).void === true, 'forming bar with no prevBar close falls back to currentPrice (same as the card): still evaluated');
// no_atr: plan has no stop, zone rule still works
w = planStatusFromSr({ ...sr, meta: { ...sr.meta, atr: null } }, live);
ok(w.void === true && w.belowStop === false, 'no_atr payload: zone rule still voids, no stop clause');
// pre-market passes through as fact only
w = planStatusFromSr(sr, { ...live, state: 'pre' });
ok(w.void === false && w.factOnly === true && w.basis === 'pre-market', 'wrapper: pre-market is fact only and labelled pre-market');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
