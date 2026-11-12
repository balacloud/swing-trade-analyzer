// getVixPositionMultiplier must equal the two inline App.jsx ladders it replaces
// (Analyze Redesign Step 8, Day 124). Only deliberate change: non-finite VIX
// (NaN) was 0.50x via fall-through, now 1.0x marked unknown.
//   cd frontend && node scripts/test_vix_multiplier.mjs
import { getVixPositionMultiplier, calculatePositionSize } from '../src/utils/positionSizing.js';

const oldLadder = (v) => (v == null ? 1.0 : v < 20 ? 1.0 : v <= 30 ? 0.75 : 0.50);
let fail = 0, pass = 0;
const expect = (c, m) => { if (c) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };

for (const v of [0, 15, 19.99, 20, 25, 30, 30.01, 45, 80]) {
  const r = getVixPositionMultiplier(v);
  expect(r.multiplier === oldLadder(v) && r.isDefault === false, `VIX ${v} -> ${r.multiplier} (old ${oldLadder(v)})`);
}
for (const v of [null, undefined]) {
  const r = getVixPositionMultiplier(v);
  expect(r.multiplier === 1.0 && r.isDefault === true, `VIX ${v} -> 1.0, isDefault`);
}
for (const v of [NaN, Infinity, '18']) {
  const r = getVixPositionMultiplier(v);
  expect(r.multiplier === 1.0 && r.isDefault === true, `VIX ${String(v)} (${typeof v}) -> 1.0, isDefault (deliberate)`);
}

// vixUnknown flows through calculatePositionSize so the calculator can show it.
const base = calculatePositionSize(100000, 1, 50, 48, { maxPositionPercent: 25, vixMultiplier: 1.0, vixUnknown: true });
expect(base.vixUnknown === true, 'calculatePositionSize returns vixUnknown: true when passed');
const known = calculatePositionSize(100000, 1, 50, 48, { maxPositionPercent: 25, vixMultiplier: 0.75 });
expect(known.vixUnknown === false, 'vixUnknown defaults to false');
expect(known.vixMultiplier === 0.75, 'vixMultiplier still returned');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
