// Mean-Reversion Read rows (Day 126). Run: cd frontend && node scripts/test_mr_read_rows.mjs
import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { buildMRRows, volumeIsMissing, bigMoney } = await import('../src/utils/mrReadRows.js');

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };
const rules = { rsi2_entry: 10, price_min: 10, dollar_volume_min: 25_000_000, stop_pct: 0.05, rsi2_exit: 70, max_hold_days: 10, cooldown_days: 5 };
const row = (r, k) => r.rows.find((x) => x.key === k);

// Real SOXL.NE response, 2026-11-13 (zero volume on every bar)
const soxl = { rsi2: 29.21, current_price: 14.69, pct_above_sma200: -52.46, avg_dollar_volume: 0, avg_volume: 0, rules,
  conditions: { rsi2_oversold: false, above_200sma: false, price_filter: true, volume_filter: false } };
const s = buildMRRows(soxl);
ok(volumeIsMissing(soxl), 'zero volume everywhere = missing');
ok(row(s, 'volume_filter').state === null && row(s, 'volume_filter').value === 'no volume data', 'volume row is "no volume data", not $0 and not a fail');
ok(!JSON.stringify(s).includes('$0'), 'no "$0" anywhere on the card');
ok(s.blockers.length === 2 && s.unchecked.join() === 'Trading volume', 'blocked by dip + trend; volume listed as not checked');
ok(row(s, 'rsi2_oversold').gauge.passSide === 'left' && Math.abs(row(s, 'rsi2_oversold').gauge.pos - 0.2921) < 1e-9, 'dip gauge: marker at 29.21 of 100, pass zone left');
ok(row(s, 'above_200sma').gauge.offScale === 'left' && row(s, 'above_200sma').gauge.pos === 0, '-52.5% is past the left edge, marker clamped');
ok(row(s, 'above_200sma').value === '52.5% below its 200-day average', 'uptrend wording says below');

// RIVN-like: real volume, rule fails
const rivn = { rsi2: 3.92, current_price: 12.18, pct_above_sma200: -20.55, avg_dollar_volume: 398385955, avg_volume: 31449520, rules,
  conditions: { rsi2_oversold: true, above_200sma: false, price_filter: true, volume_filter: true } };
const r = buildMRRows(rivn);
ok(row(r, 'volume_filter').state === true && row(r, 'volume_filter').value === '$398.4M traded on an average day', 'real volume still shows and passes');
ok(r.blockers.join() === 'it is below its 200-day average' && r.unchecked.length === 0, 'only the trend blocks');

// A real thin stock: tiny but non-zero volume is a real fail, not missing
const thin = { ...rivn, avg_dollar_volume: 900000, avg_volume: 70000, conditions: { ...rivn.conditions, volume_filter: false } };
ok(!volumeIsMissing(thin) && row(buildMRRows(thin), 'volume_filter').state === false, 'thin but real volume is still a fail');

// Missing inputs
const empty = buildMRRows({ rsi2: null, current_price: null, pct_above_sma200: null, avg_dollar_volume: null, rules, conditions: {} });
ok(empty.rows.every((x) => x.state === null) && row(empty, 'rsi2_oversold').gauge === null, 'all-null input: nothing fails, no gauge');
ok(volumeIsMissing(null) && volumeIsMissing({ avg_dollar_volume: NaN }), 'null / NaN volume = missing');

// Boundaries and a passing signal
const sig = { rsi2: 4, current_price: 50, pct_above_sma200: 8, avg_dollar_volume: 5e9, avg_volume: 1e8, rules,
  conditions: { rsi2_oversold: true, above_200sma: true, price_filter: true, volume_filter: true } };
const g = buildMRRows(sig);
ok(g.blockers.length === 0 && g.unchecked.length === 0 && g.rows.every((x) => x.state === true), 'signal: all four pass');
ok(row(g, 'above_200sma').gauge.pos > row(g, 'above_200sma').gauge.thresholdPos, 'above trend: dot right of the line');
ok(row(buildMRRows({ ...sig, pct_above_sma200: 0 }), 'above_200sma').value === 'right at its 200-day average', 'exactly 0% wording');
ok(row(buildMRRows({ ...sig, pct_above_sma200: 400 }), 'above_200sma').gauge.offScale === 'right', 'far above: clamped, off the right edge');
ok(bigMoney(25_000_000) === '$25M' && bigMoney(5e9) === '$5B' && bigMoney(null) === '—', 'money formatting');

// Pass 2: a response missing a rule number must not produce a NaN gauge
const noRule = buildMRRows({ ...rivn, rules: { ...rules, rsi2_entry: undefined } });
ok(row(noRule, 'rsi2_oversold').gauge === null, 'missing rsi2_entry: no gauge drawn');
const inf = buildMRRows({ ...rivn, pct_above_sma200: Infinity });
ok(row(inf, 'above_200sma').value === 'no data' && row(inf, 'above_200sma').state === null, 'Infinity trend value = no data, not a fail');

// Wording: the dip row must say RSI (low = sharp drop) and label both ends of the bar
const dip = row(buildMRRows(rivn), 'rsi2_oversold');
ok(dip.value === `2-day RSI ${rivn.rsi2.toFixed(1)}` && dip.ends.join() === 'sharp drop,sharp rise', 'dip row: "2-day RSI" to one decimal, ends labelled');
// Day 126 (Statement Audit): a 10.24 must not read "10 needs under 10"
const edgeRsi = row(buildMRRows({ ...rivn, rsi2: 10.24, conditions: { ...rivn.conditions, rsi2_oversold: false } }), 'rsi2_oversold');
ok(edgeRsi.value === '2-day RSI 10.2' && edgeRsi.state === false, 'RSI 10.24 reads "10.2" (not "10") next to "needs under 10"');
ok(/or higher/.test(edgeRsi.blocker) && !/drop is too small/.test(edgeRsi.blocker), 'the RSI blocker is true after a rise too ("2-day RSI is 10 or higher")');
ok(row(buildMRRows(rivn), 'above_200sma').ends.join() === 'below,above', 'trend row: ends labelled below / above');
ok(row(buildMRRows(rivn), 'price_filter').hint && row(buildMRRows(rivn), 'volume_filter').hint, 'price and volume rows explain why they exist');
ok(row(s, 'volume_filter').hint === null, 'no volume hint when volume is missing');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
