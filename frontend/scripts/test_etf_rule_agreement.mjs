// The tab's fund type comes from the backend (data_quality.classify_instrument); the Analyze page's ETF display uses
// detectEtf(quoteType). Both read the same Yahoo quote type, so they must agree. Real Yahoo names (checked Day 126).
// Intentional difference: a CDR is its own class in the tab, but detectEtf follows Yahoo's quote type (most CDRs say ETF).
// Run: cd frontend && node scripts/test_etf_rule_agreement.mjs
import { detectEtf } from '../src/utils/fundamentalsRead.js';

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };

// [quoteType, name, backend class (mirrors backend/data_quality.classify_instrument, tested in test_data_quality.py)]
const REAL = [
  ['EQUITY', 'Apple Inc.', 'Stock'], ['EQUITY', 'ROYAL BANK OF CANADA', 'Stock'],
  ['ETF', 'VanEck Semiconductor ETF', 'ETF'], ['ETF', 'ISHARES CORE EQUITY ETF', 'ETF'],
  ['ETF', 'BETAPRO 3X SEMICONDUCTOR DAILY ', 'Leveraged ETF'], ['ETF', 'BETAPRO CDN GOLD MINERS 2X DLY ', 'Leveraged ETF'],
  ['ETF', 'Defiance 2X Daily Long Pure Qua', 'Leveraged ETF'], ['ETF', 'Direxion Daily Semiconductor Bu', 'Leveraged ETF'],
  ['EQUITY', 'ADVANCED MICRO DEVICES CDR (CAD', 'CDR'], ['ETF', 'MICRON CDR (CAD HEDGED)', 'CDR'], ['ETF', 'SANDISK CDR (CAD HEDGED)', 'CDR'],
];
for (const [qt, name, cls] of REAL) {
  const fe = detectEtf({ quoteType: qt, name }).etf;
  if (cls === 'ETF' || cls === 'Leveraged ETF') ok(fe === true, `${cls}: frontend also says ETF  (${name.trim()})`);
  else if (cls === 'Stock') ok(fe === false, `Stock: frontend says not an ETF  (${name.trim()})`);
  else ok(fe === (qt === 'ETF'), `CDR: frontend follows Yahoo's quote type (${qt}); the tab labels it CDR  (${name.trim()})`);
}
console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
