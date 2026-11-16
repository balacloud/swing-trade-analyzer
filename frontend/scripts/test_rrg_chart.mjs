import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { buildRrgModel } = await import('../src/utils/rrgChart.js');

let fails = 0;
const check = (n, c, d) => { console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : '  ' + JSON.stringify(d))); if (!c) fails++; };

const tail = (r, m) => [0, 1, 2, 3, 4].map((i) => ({ rs_ratio: r - (4 - i) * 0.2, rs_momentum: m - (4 - i) * 0.1 }));
const sectors = [
  { etf: 'XLK', quadrant: 'Lagging', rsRatio: 97.86, rsMomentum: -1.1, tail: tail(97.86, -1.1) },
  { etf: 'XLP', quadrant: 'Leading', rsRatio: 102.38, rsMomentum: 0.95, tail: tail(102.38, 0.95) },
  { etf: 'XLV', quadrant: 'Leading', rsRatio: 102.17, rsMomentum: 0.75, tail: tail(102.17, 0.75) },
  { etf: 'XLU', quadrant: 'Leading', rsRatio: 100.61, rsMomentum: 1.32, tail: tail(100.61, 1.32) },
  { etf: 'XLRE', quadrant: 'Leading', rsRatio: 100.69, rsMomentum: 1.27, tail: tail(100.69, 1.27) },
];
const m = buildRrgModel(sectors);
const inPlot = (p) => p.x >= m.plot.l && p.x <= m.plot.r && p.y >= m.plot.t && p.y <= m.plot.b;

check('5 points', m.points.length === 5, m.points.length);
check('all heads and tails inside the plot', m.points.every((p) => inPlot(p) && p.tail.every(inPlot)));
check('cross is the exact middle', Math.abs(m.cx - (m.plot.l + m.plot.r) / 2) < 1e-9 && Math.abs(m.cy - (m.plot.t + m.plot.b) / 2) < 1e-9);
const xlk = m.points.find((p) => p.etf === 'XLK'); const xlp = m.points.find((p) => p.etf === 'XLP');
check('Lagging dot is left of and below the cross', xlk.x < m.cx && xlk.y > m.cy);
check('Leading dot is right of and above the cross', xlp.x > m.cx && xlp.y < m.cy);
check('tail kept (5 points)', xlp.tail.length === 5);
const close = m.points.filter((p) => ['XLU', 'XLRE'].includes(p.etf));
check('close labels do not overlap', Math.abs(close[0].labelY - close[1].labelY) >= 12, close.map((p) => p.labelY));

check('empty list ok', buildRrgModel([]).points.length === 0 && buildRrgModel(null).points.length === 0);
const bad = buildRrgModel([{ etf: 'A', quadrant: 'Leading', rsRatio: NaN, rsMomentum: 1 }, { etf: 'B', quadrant: 'Leading', rsRatio: 101, rsMomentum: null }, { etf: 'C', quadrant: 'Leading', rsRatio: 101, rsMomentum: 1, tail: [{ rs_ratio: NaN, rs_momentum: 1 }, null] }]);
check('NaN / null rows dropped, bad tail points dropped', bad.points.length === 1 && bad.points[0].tail.length === 0, bad.points);
const none = buildRrgModel([{ etf: 'C', quadrant: 'Leading', rsRatio: 101, rsMomentum: 1 }]);
check('no tail field ok', none.points[0].tail.length === 0 && inPlot(none.points[0]));
const flat = buildRrgModel([{ etf: 'F', quadrant: 'Leading', rsRatio: 100, rsMomentum: 0 }]);
check('single flat sector sits on the cross', Math.abs(flat.points[0].x - flat.cx) < 1e-9 && Math.abs(flat.points[0].y - flat.cy) < 1e-9);
const big = buildRrgModel([{ etf: 'B', quadrant: 'Leading', rsRatio: 140, rsMomentum: 30 }]);
check('large values still fit', inPlot(big.points[0]));
console.log(fails + ' failed'); process.exit(fails ? 1 : 0);
