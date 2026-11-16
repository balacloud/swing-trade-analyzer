// Entry-timing ruler logic (Day 126). Run: cd frontend && node scripts/test_entry_timing.mjs
import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { deriveEntryTiming, deriveEntryVolume } = await import('../src/utils/technicalReadChecks.js');

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };
const near = (a, b, t = 1e-9) => Math.abs(a - b) <= t;

// the user's real example: $523.88 vs $528.10, 0.3 ATR below -> ATR about 14.07
const t = deriveEntryTiming({ price: 523.88, ema21: 528.10, atr: 14.07 });
ok(t.state === 'ok' && t.side === 'below', 'below the average: side = below');
ok(near(t.atrUnits, (523.88 - 528.10) / 14.07) && Math.abs(t.atrUnits).toFixed(1) === '0.3', 'distance in normal days = 0.3');
ok(near(t.pctFromEma, ((523.88 - 528.10) / 528.10) * 100) && t.pctFromEma.toFixed(1) === '-0.8', 'percent from the average = -0.8');
ok(t.marks.length === 1 && t.marks[0].key === 'ema21' && near(t.marks[0].price, 528.10) && t.marks[0].caption === '21-day avg', 'only the 21-day average when 50 and 200 are missing');
const t3 = deriveEntryTiming({ price: 523.88, ema21: 528.10, sma50: 510, sma200: 450, atr: 14.07 });
ok(t3.marks.map((m) => m.key).join() === 'sma200,sma50,ema21', 'three marks, left to right by price');
ok(t3.marks.map((m) => m.caption).join() === '200-day avg,50-day avg,21-day avg', 'captions say 200-day, 50-day and 21-day average');
ok(t3.marks.every((m) => /^(sma200|sma50|ema21)$/.test(m.key)) && near(t3.marks[0].price, 450) && near(t3.marks[1].price, 510), 'tick prices are the real averages');
ok(t3.lo < 450 && t3.hi > 528.10, 'ruler spans every mark with room at both ends');
const above = deriveEntryTiming({ price: 700, ema21: 528.10, sma50: 510, sma200: 450, atr: 14.07 });
ok(above.hi > 700 && above.lo < 450, 'price far above every average still sits on the ruler');
const below = deriveEntryTiming({ price: 300, ema21: 528.10, sma50: 510, sma200: 450, atr: 14.07 });
ok(below.lo < 300 && below.hi > 528.10, 'price far below every average still sits on the ruler');
ok(deriveEntryTiming({ price: 100, ema21: 100, sma50: null, sma200: NaN, atr: 2 }).marks.length === 1, 'a missing or NaN average is left out, never invented');
ok(!('zone' in t) && !('good' in t) && !('answer' in t) && !('why' in t), 'no verdict fields (zone / good / answer) are returned');

ok(deriveEntryTiming({ price: 600, ema21: 528.10, atr: 14.07 }).side === 'above', 'above the average: side = above');
ok(deriveEntryTiming({ price: 528.10, ema21: 528.10, atr: 14.07 }).side === 'at', 'exactly on the average: side = at');
ok(deriveEntryTiming({ price: 528.20, ema21: 528.10, atr: 14.07 }).side === 'at', 'within 0.05% of the average counts as at');

// no gating on the Technical Read: a Weak stock gets the same ruler (the function does not even take the read)
ok(deriveEntryTiming({ read: 'Weak', price: 100, ema21: 105, atr: 2 }).state === 'ok', 'shown for every stock, whatever the read');

// failure states are explicit, never a made-up number
ok(deriveEntryTiming({ price: null, ema21: 100, atr: 2 }).state === 'unavailable', 'price missing -> unavailable');
ok(/200 days/.test(deriveEntryTiming({ price: 100, ema21: null, atr: 2 }).reason), 'no 21-day average -> says it needs 200 days of history');
ok(deriveEntryTiming({ price: 100, ema21: 0, atr: 2 }).state === 'unavailable', 'average of zero -> unavailable (no divide by zero)');
ok(deriveEntryTiming({ price: 100, ema21: 100, atr: 0 }).state === 'unavailable', 'ATR of zero -> unavailable');
ok(deriveEntryTiming({ price: 100, ema21: 100, atr: -1 }).state === 'unavailable', 'negative ATR -> unavailable');
ok(deriveEntryTiming({ price: NaN, ema21: 100, atr: 2 }).state === 'unavailable', 'NaN price -> unavailable');
ok(deriveEntryTiming({ price: 100, ema21: 100, atr: undefined }).state === 'unavailable', 'undefined ATR -> unavailable');
ok(deriveEntryTiming({}).state === 'unavailable', 'empty input -> unavailable, no throw');

// far off the ruler stays a real number (the card shows an "off the ruler" note; the dot clamps)
const far = deriveEntryTiming({ price: 200, ema21: 100, atr: 5 });
ok(far.state === 'ok' && near(far.atrUnits, 20), 'far above: 20 normal days, real number kept');
const low = deriveEntryTiming({ price: 50, ema21: 100, atr: 5 });
ok(low.state === 'ok' && near(low.atrUnits, -10) && low.side === 'below', 'far below: -10 normal days, real number kept');

// volume card: a plain count of the three signals (the user's own example: closed up 0.4%, near the low, OBV falling -> 1 up, 2 down)
const hist = Array.from({ length: 60 }, (_, i) => ({ date: `2026-09-${String(i + 1).padStart(2, '0')}`, close: 100 + i, volume: 1000 }));
const vol = deriveEntryVolume({ priceHistory: hist, todayEt: '2026-11-16',
  srData: { change: 0.4, meta: { rvol: 0.9, candle: { barComplete: true, closeLocation: 0.1 }, obv: { trend: 'falling' } } } });
ok(vol.state === 'ok' && vol.tally.up === 1 && vol.tally.down === 2 && vol.tally.flat === 0 && vol.voted === 3, 'volume tally: 1 up, 2 down, 0 flat');
const vol2 = deriveEntryVolume({ priceHistory: hist, todayEt: '2026-11-16',
  srData: { change: 0.0, meta: { rvol: 1.0, candle: { barComplete: true, closeLocation: 0.5 }, obv: { trend: 'flat' } } } });
ok(vol2.tally.up === 0 && vol2.tally.down === 0 && vol2.tally.flat === 3, 'volume tally: all flat');

// Day 126: with a usable live price the block measures from it; averages and ATR are untouched.
const base3 = { ema21: 528.10, sma50: 510, sma200: 450, atr: 14.07 };
const lv = deriveEntryTiming({ price: 523.88, ...base3, livePrice: 520.10 });
ok(lv.basis === 'live' && lv.price === 520.10, 'live price becomes the compared price, basis = live');
ok(near(lv.atrUnits, (520.10 - 528.10) / 14.07) && near(lv.pctFromEma, ((520.10 - 528.10) / 528.10) * 100), 'distance and ATR units are measured from the live price');
ok(lv.ema21 === 528.10 && lv.atr === 14.07 && lv.marks.length === 3, 'averages and ATR are the same inputs, no extra mark');
ok(!('live' in lv) && !('lastClose' in lv), 'no second marker field and no lastClose field (the note comes from the quote)');
ok(t3.basis === 'close' && t3.price === 523.88, 'no live price: basis = close, price = the bar price');
const lvLow = deriveEntryTiming({ price: 523.88, ...base3, livePrice: 380 });
ok(lvLow.lo < 380 && lvLow.hi > 528.10 && lvLow.side === 'below', 'live far below every average sits on the ruler');
const lvHigh = deriveEntryTiming({ price: 523.88, ...base3, livePrice: 640 });
ok(lvHigh.hi > 640 && lvHigh.side === 'above', 'live above every average sits on the ruler');
ok(deriveEntryTiming({ price: 523.88, ...base3, livePrice: 540 }).side === 'above' && deriveEntryTiming({ price: 540, ...base3, livePrice: 520 }).side === 'below', 'live price decides the side, not the bar price');
ok(deriveEntryTiming({ price: 523.88, ...base3, livePrice: 528.10 }).side === 'at', 'live exactly on the 21-day average = at');
ok(deriveEntryTiming({ price: 523.88, ...base3, livePrice: 523.88 }).pctFromEma === t3.pctFromEma, 'live equal to the bar price gives the same numbers');
for (const bad of [NaN, Infinity, -5, 0, undefined, null, '520']) {
  const r = deriveEntryTiming({ price: 523.88, ...base3, livePrice: bad });
  ok(r.basis === 'close' && r.price === 523.88 && r.lo === t3.lo && r.hi === t3.hi, `bad live price ${String(bad)} falls back to the bar price`);
}
ok(deriveEntryTiming({ price: null, ...base3, livePrice: 520 }).state === 'ok', 'bar price missing but live present still works');
ok(deriveEntryTiming({ price: null, ...base3, livePrice: null }).state === 'unavailable', 'both missing: unavailable');
ok(deriveEntryTiming({ price: 100, ema21: 100, atr: 2, livePrice: 100 }).hi > 100, 'live equal to everything still gets room');
ok(deriveEntryTiming({ price: 523.88, ema21: null, atr: 14.07, livePrice: 520 }).state === 'unavailable', 'missing 21-day average stays unavailable even with a live price');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
