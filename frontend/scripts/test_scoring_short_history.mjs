// Regression (Day 126): calculateScore() must not throw for a fund with 50-199 days of history.
// It used to crash the whole Analyze page ("Cannot read properties of null (reading 'sma50')")
// on DRAL (100 days), SPCL (154) and COPZ (188). Run: cd frontend && node scripts/test_scoring_short_history.mjs
import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { calculateScore } = await import('../src/utils/scoringEngine.js');

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };

const bars = (n) => Array.from({ length: n }, (_, i) => {
  const c = 20 + i * 0.05 + Math.sin(i / 5);
  return { date: `d${i}`, open: c, high: c + 0.5, low: c - 0.5, close: c, volume: 100000 + i };
});
const stock = (n) => ({ ticker: 'TEST', currentPrice: 22, priceHistory: bars(n), fundamentals: null, quoteType: 'ETF' });
const spy = { currentPrice: 700, priceHistory: bars(300), sma200: 650 };
const vix = { current: 18 };

for (const n of [49, 50, 100, 154, 188, 199, 200, 260]) {
  let res = null, err = null;
  try { res = calculateScore(stock(n), spy, vix); } catch (e) { err = e; }
  ok(err === null, `${n} bars: does not throw${err ? ` (${err.message})` : ''}`);
  if (res) ok(Number.isFinite(res.totalScore ?? res.score ?? 0), `${n} bars: returns a numeric score`);
}

// With 100 bars there is no 200-day average, and nothing pretends there is one.
const r100 = calculateScore(stock(100), spy, vix);
const ind = r100.indicators || r100.breakdown?.technical?.indicators;
ok(ind == null || ind.sma200 == null, '100 bars: sma200 is null, never a made-up number');
ok(ind == null || Number.isFinite(ind.sma50), '100 bars: sma50 is still computed');
const trend = r100.breakdown?.technical?.details?.trendStructure;
ok(!trend || trend.score === 0, '100 bars: trend structure is unscored (0), not scored from a missing average');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
