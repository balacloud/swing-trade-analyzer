// describeDataNotes: the Analyze header's thin-data and leveraged-comparison lines (Day 135).
//   cd frontend && node scripts/test_data_notes.mjs
import { describeDataNotes } from '../src/utils/dataNotes.js';

let pass = 0, fail = 0;
const expect = (got, want, m) => { const g = JSON.stringify(got), w = JSON.stringify(want); if (g === w) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}: got ${g}, want ${w}`); } };
const has = (got, part, m) => { if (typeof got === 'string' && got.includes(part)) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}: ${JSON.stringify(got)} lacks ${JSON.stringify(part)}`); } };
const lacks = (got, part, m) => { if (typeof got === 'string' && !got.includes(part)) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}: ${JSON.stringify(got)}`); } };
const line = (dn, id) => (describeDataNotes(dn).find(x => x.id === id) || {}).text;

const NOTE = '82% of bars flat with zero volume; 0 malformed bars; zero volume on 3 of the last 5 days';
const integ = { level: 'FAIL', note: NOTE, bars: 502, since: '2024-11-25' };
const trk = { reference: 'NVDA', multiple: 2, basis: 'stock', twin: false, corr: 1.0, beta: 1.98, n: 503, date: '2026-11-24' };

// integrity: the tab's wording verbatim, plus what the percentage covers
has(line({ integrity: integ, tracking: null }, 'integrity'), `Price data: ${NOTE}`, 'integrity: the tab note is quoted verbatim');
has(line({ integrity: integ }, 'integrity'), '(of 502 saved bars since Nov 25, 2024)', 'integrity: says which bars the percentage covers');
expect(describeDataNotes({ integrity: { ...integ, level: 'PASS' } }), [], 'integrity PASS: nothing');
has(line({ integrity: { ...integ, level: 'WARN' } }, 'integrity'), 'Price data:', 'integrity WARN is shown');
lacks(line({ integrity: { level: 'FAIL', note: NOTE } }, 'integrity'), 'saved bars', 'integrity without bars/since: no coverage text, still shown');
expect(describeDataNotes({ integrity: { level: 'FAIL', note: '' } }), [], 'integrity with an empty note: nothing');

// tracking templates
const t1 = line({ tracking: trk }, 'tracking');
has(t1, 'Compared with NVDA (x2 stated): correlation 1.000, beta 1.98 over 503 trading days (audit, Nov 24).', 'stock basis: stated multiple, 3-decimal correlation (1.0 shows as 1.000)');
has(line({ tracking: { ...trk, reference: 'BRK-B', corr: 0.995, beta: 1.95, n: 489 } }, 'tracking'), 'correlation 0.995, beta 1.95', '0.995 is not rounded to 1.00');
has(line({ tracking: { ...trk, reference: 'BOTZ', basis: 'measured' } }, 'tracking'), 'BOTZ, the closest match by price (x2 stated)', 'measured basis: closest match by price, multiple stated');
has(line({ tracking: { ...trk, reference: 'GDX', multiple: null, basis: 'measured' } }, 'tracking'), 'GDX (multiple not known)', 'unknown multiple says so');
has(line({ tracking: { ...trk, reference: 'SOXL', multiple: 1, twin: true, basis: 'measured' } }, 'tracking'), 'SOXL, a fund with the same leverage (x1)', 'twin: not shown as an unleveraged x1');
lacks(t1, 'Follows', 'no "Follows" claim');
for (const w of ['Strong', 'Weak', 'Good', 'Bad', 'Reliable', 'matches', 'perfect']) lacks(t1 + line({ integrity: integ }, 'integrity'), w, `no verdict word "${w}"`);
// missing or bad numbers skip the line, never throw
for (const [name, t] of [['no reference', { ...trk, reference: '' }], ['NaN corr', { ...trk, corr: NaN }], ['string beta', { ...trk, beta: '1.9' }], ['no n', { ...trk, n: null }]]) expect(describeDataNotes({ tracking: t }), [], `tracking ${name}: skipped`);
has(line({ tracking: { ...trk, date: 'garbage' } }, 'tracking'), 'over 503 trading days.', 'bad audit date: line kept without the date');
// both lines, in order
expect(describeDataNotes({ integrity: integ, tracking: trk }).map(x => x.id), ['integrity', 'tracking'], 'both notes: integrity first');
// never throws
for (const bad of [null, undefined, 'x', 5, [], {}, { integrity: 'x', tracking: 'y' }]) expect(describeDataNotes(bad), [], `input ${JSON.stringify(bad)} -> no notes`);

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
