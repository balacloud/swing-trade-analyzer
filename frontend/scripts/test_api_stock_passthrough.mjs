// fetchStockData rebuilds the stock object field by field (Golden Rule 30). priceFreshness must survive that, or the saved-prices line never reaches the page (Day 135).
//   cd frontend && node scripts/test_api_stock_passthrough.mjs
import { fetchStockData } from '../src/services/api.js';

let pass = 0, fail = 0;
const expect = (got, want, m) => { const g = JSON.stringify(got), w = JSON.stringify(want); if (g === w) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}: got ${g}, want ${w}`); } };

const pf = { newestDate: '2026-11-24', expectedDate: '2026-11-25', sessionsBehind: 1, behindLevel: 'PASS', servedFromStaleCache: true, maybePartial: true };
const body = { ticker: 'VFV.TO', name: 'x', currentPrice: 182.31, priceHistory: [{ date: '2026-11-24', close: 182.31 }], dataPoints: 1, oldestDate: '2026-11-24', newestDate: '2026-11-24', priceFreshness: pf, dataNotes: { integrity: { level: 'FAIL', note: 'n', bars: 5, since: '2024-11-25' }, tracking: null } };
globalThis.fetch = async () => ({ ok: true, status: 200, json: async () => body });
const out = await fetchStockData('vfv.to');
expect(out.priceFreshness, pf, 'priceFreshness reaches the page object unchanged');
expect(out.dataNotes, body.dataNotes, 'dataNotes reaches the page object unchanged');
expect(out.newestDate, '2026-11-24', 'existing fields still pass through');

const { priceFreshness, dataNotes, ...old } = body;                      // an older backend without the field
globalThis.fetch = async () => ({ ok: true, status: 200, json: async () => old });
const oldOut = await fetchStockData('AAPL');
expect(oldOut.priceFreshness, null, 'an answer without priceFreshness gives null, not undefined or a crash');
expect(oldOut.dataNotes, null, 'an answer without dataNotes gives null, not undefined or a crash');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
