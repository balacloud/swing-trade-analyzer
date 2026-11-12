// describePriceAsOf: the header price's date label (Day 124, follow-up to Step 8).
//   cd frontend && node scripts/test_price_as_of.mjs
import { describePriceAsOf } from '../src/utils/priceAsOf.js';

let pass = 0, fail = 0;
const expect = (got, want, m) => { if (got === want) { pass++; console.log(`ok ${m}: "${got}"`); } else { fail++; console.log(`FAIL ${m}: got "${got}", want "${want}"`); } };
// Times are UTC; New York is UTC-5 in November.
const at = (iso) => new Date(iso);

expect(describePriceAsOf('2026-11-11', at('2026-11-12T15:38:00Z')), 'Nov 11 close', 'yesterday\'s bar during market hours');
expect(describePriceAsOf('2026-11-12', at('2026-11-12T15:38:00Z')), 'Nov 12 · intraday, not a close', 'today\'s bar at 10:38 ET');
expect(describePriceAsOf('2026-11-12', at('2026-11-12T21:29:00Z')), 'Nov 12 · intraday, not a close', 'today\'s bar at 16:29 ET (before the 16:30 cutoff)');
expect(describePriceAsOf('2026-11-12', at('2026-11-12T21:30:00Z')), 'Nov 12 close', 'today\'s bar at 16:30 ET');
expect(describePriceAsOf('2026-11-12', at('2026-11-13T03:00:00Z')), 'Nov 12 close', 'evening ET is still Nov 12 in New York (UTC already Nov 13)');
expect(describePriceAsOf('2026-11-06', at('2026-11-09T14:00:00Z')), 'Nov 6 close', 'Friday bar seen Monday morning');
expect(describePriceAsOf('2025-12-31', at('2026-01-02T15:00:00Z')), 'Dec 31, 2025 close', 'previous year shows the year');
expect(describePriceAsOf(null, at('2026-11-12T15:38:00Z')), null, 'missing date -> null (no label, no guess)');
expect(describePriceAsOf('garbage', at('2026-11-12T15:38:00Z')), null, 'bad date -> null');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
