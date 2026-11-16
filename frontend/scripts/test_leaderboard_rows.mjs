import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { buildLeaderboardRows, sparkPoints, BAR_SCALE } = await import('../src/utils/leaderboardRows.js');

let fails = 0;
const check = (n, c, d) => { console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : '  ' + JSON.stringify(d))); if (!c) fails++; };
const tp = (r, m, q) => ({ rs_ratio: r, rs_momentum: m, quadrant: q });
const item = (o) => ({ key: o.etf, name: o.etf, etf: o.etf, quadrant: 'Leading', rsRatio: 101, rsMomentum: 1, tail: [], ...o });

const rows = buildLeaderboardRows([
  item({ etf: 'B', rsRatio: 98, quadrant: 'Improving' }),
  item({ etf: 'A', rsRatio: 106.4 }),
  item({ etf: 'C', rsRatio: 95.4, rsMomentum: -0.5, quadrant: 'Lagging' }),
]);
check('sorted strongest first', rows.map((r) => r.etf).join('') === 'ABC', rows.map((r) => r.etf));
check('above 100: bar goes right', rows[0].bar.side === 'right' && rows[0].bar.pct > 0);
check('below 100: bar goes left', rows[2].bar.side === 'left');
check('bar is capped at the scale (106.4 -> 100%-wide half)', rows[0].bar.pct <= 50 + 1e-9 && Math.abs(rows[0].bar.pct - (6 / BAR_SCALE) * 50) < 1e-9, rows[0].bar);
const huge = buildLeaderboardRows([item({ etf: 'H', rsRatio: 150 }), item({ etf: 'L', rsRatio: 50 })]);
check('extreme values stay on the bar', huge.every((r) => r.bar.pct <= 50), huge.map((r) => r.bar));
check('exactly 100 -> empty bar', buildLeaderboardRows([item({ etf: 'Z', rsRatio: 100 })])[0].bar.pct === 0);

// moved badge
const moved = buildLeaderboardRows([item({ etf: 'M', quadrant: 'Leading', tail: [tp(99, 0.5, 'Improving'), tp(99.6, 0.6, 'Improving'), tp(100.3, 0.7, 'Leading')] })])[0];
check('corner changed a week ago -> moved', moved.moved && moved.prevCorner === 'Improving', moved);
const same = buildLeaderboardRows([item({ etf: 'S', tail: [tp(101, 1, 'Leading'), tp(101.2, 1, 'Leading')] })])[0];
check('same corner -> not moved', !same.moved);
const old = buildLeaderboardRows([item({ etf: 'O', tail: [{ rs_ratio: 101, rs_momentum: 1 }, { rs_ratio: 101.2, rs_momentum: 1 }] })])[0];
check('old cached tail without corners -> not moved, no crash', !old.moved && old.prevCorner === null);
check('one-point tail -> not moved', !buildLeaderboardRows([item({ etf: 'P', tail: [tp(101, 1, 'Leading')] })])[0].moved);
check('no tail field -> ok', buildLeaderboardRows([item({ etf: 'N', tail: undefined })])[0].spark === null);

// bad input
check('empty / null ok', buildLeaderboardRows([]).length === 0 && buildLeaderboardRows(null).length === 0);
const bad = buildLeaderboardRows([item({ etf: 'X', rsRatio: NaN }), item({ etf: 'Y', rsMomentum: null }), item({ etf: 'W', quadrant: undefined }), null, item({ etf: 'OK' })]);
check('rows with missing numbers or corner are dropped', bad.length === 1 && bad[0].etf === 'OK', bad.map((r) => r.etf));
const badTail = buildLeaderboardRows([item({ etf: 'T', tail: [tp(NaN, 1, 'Leading'), null, tp(101, 1, 'Leading')] })])[0];
check('bad tail points dropped', badTail.tail.length === 1 && badTail.spark === null, badTail.tail);

// spark
const sp = sparkPoints([98, 98.5, 99, 99.5, 100]);
check('spark has one point per value, inside the box', sp.length === 5 && sp.every(([x, y]) => x >= 4 && x <= 88 && y >= 4 && y <= 26), sp);
check('rising values go up (smaller y)', sp[4][1] < sp[0][1]);
const flat = sparkPoints([100, 100.1, 100, 100.05]);
check('flat line stays near the middle', flat.every(([, y]) => y > 8 && y < 22), flat);
check('under 2 values -> null', sparkPoints([1]) === null && sparkPoints([]) === null && sparkPoints(null) === null);
check('NaN values skipped', sparkPoints([1, NaN, 2]).length === 2);

console.log(fails + ' failed'); process.exit(fails ? 1 : 0);
