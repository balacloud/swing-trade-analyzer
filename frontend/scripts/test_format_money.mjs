// One money format for the whole page (Day 126). Run: cd frontend && node scripts/test_format_money.mjs
import { register } from 'node:module';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { formatMoney } = await import('../src/utils/formatMoney.js');
let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };
ok(formatMoney(12.045) === '$12.05', "a half-cent price rounds up the same way everywhere ($12.045 -> $12.05, the header's rule)");
ok(formatMoney(1234.5) === '$1,234.50' && formatMoney(1234567.891) === '$1,234,567.89', 'thousands separators and two decimals');
ok(formatMoney(0) === '$0.00', 'zero');
ok(typeof formatMoney(-3.2) === 'string' && formatMoney(-3.2).includes('3.20'), 'a negative value does not throw');
ok(formatMoney(null) === '—' && formatMoney(undefined) === '—' && formatMoney(NaN) === '—' && formatMoney(Infinity) === '—' && formatMoney('5') === '—', 'missing or non-numeric -> the dash, never "NaN"');
ok(formatMoney(null, 'N/A') === 'N/A', 'the dash can be replaced (the header says N/A)');
console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
