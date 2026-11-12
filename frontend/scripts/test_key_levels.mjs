// describeKeyLevels + deriveStructureState (Day 125, Analyze cleanup).
//   cd frontend && node scripts/test_key_levels.mjs
import { describeKeyLevels, deriveStructureState } from '../src/utils/keyLevels.js';

let pass = 0, fail = 0;
const ok = (cond, m) => { if (cond) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };
const near = (a, b) => Math.abs(a - b) < 1e-9;

const base = () => ({
  currentPrice: 100,
  support: [80.5, 90.25, 95.1],            // ascending, as the API sends it
  resistance: [104.2, 110, 125.3],
  meta: {
    levelScores: { '95.10': 7, '104.20': 3, '80.50': 2 },
    mtf: { confluence_map: { '104.20': { confluent: true, strength_label: 'Strong' }, '95.10': { confluent: false } } },
    resistanceProjected: false,
    supportProjected: false,
    proximityFilter: { supportPct: 0.2, resistancePct: 0.3 },
  },
});

// nearest pick
let r = describeKeyLevels(base());
ok(r.ceiling.kind === 'level' && r.ceiling.price === 104.2, 'ceiling = nearest resistance (min above)');
ok(r.floor.kind === 'level' && r.floor.price === 95.1, 'floor = nearest support (max below), not support[0] (BUG-B)');

// zone = ±0.5%
ok(near(r.ceiling.low, 104.2 * 0.995) && near(r.ceiling.high, 104.2 * 1.005), 'ceiling zone ±0.5%');
ok(near(r.floor.low, 95.1 * 0.995) && near(r.floor.high, 95.1 * 1.005), 'floor zone ±0.5%');

// distance
ok(near(r.ceiling.pctAway, 4.2), 'ceiling 4.2% above');
ok(near(r.floor.pctAway, 4.9), 'floor 4.9% below');

// days near (camelCase levelScores, exact 2dp key — Fable #1, Day 112 BUG-A)
ok(r.ceiling.daysNear === 3, 'ceiling daysNear from meta.levelScores');
ok(r.floor.daysNear === 7, 'floor daysNear from meta.levelScores');
const noScore = base(); delete noScore.meta.levelScores['104.20'];
ok(describeKeyLevels(noScore).ceiling.daysNear === null, 'missing score key -> null, never 0');
const snake = base(); snake.meta.level_scores = snake.meta.levelScores; delete snake.meta.levelScores;
ok(describeKeyLevels(snake).ceiling.daysNear === null, 'snake_case level_scores is not read');
const zeroPad = base(); zeroPad.resistance = [104.2, 110]; zeroPad.meta.levelScores = { '104.2': 9 };
ok(describeKeyLevels(zeroPad).ceiling.daysNear === null, 'key must be 2dp ("104.20"), no fuzzy match');

// weekly star
ok(r.ceiling.weekly === true && r.ceiling.weeklyStrength === 'Strong', 'ceiling weekly ★ with strength');
ok(r.floor.weekly === false && r.floor.weeklyStrength === null, 'floor no ★');

// none on a side (Fable #3)
const noRes = base(); noRes.resistance = [];
r = describeKeyLevels(noRes);
ok(r.ceiling.kind === 'none' && r.ceiling.limitPct === 30, 'no resistance -> none, within 30%');
const noSup = base(); noSup.support = [];
ok(describeKeyLevels(noSup).floor.kind === 'none' && describeKeyLevels(noSup).floor.limitPct === 20, 'no support -> none, within 20%');

// projected levels are never shown as real
const proj = base(); proj.meta.resistanceProjected = true; proj.resistance = [108.7, 117.4];
r = describeKeyLevels(proj);
ok(r.ceiling.kind === 'projected' && r.ceiling.projectedPrice === 108.7, 'projected ceiling flagged with its price');
ok(r.realResistance.length === 0, 'projected resistance excluded from real levels');
const projS = base(); projS.meta.supportProjected = true;
ok(describeKeyLevels(projS).floor.kind === 'projected', 'projected support flagged');

// wrong-side and junk values ignored
const junk = base(); junk.resistance = [99, null, NaN, 103];
ok(describeKeyLevels(junk).ceiling.price === 103, 'levels below price and non-numbers ignored for the ceiling');

// bad input
ok(describeKeyLevels(null) === null, 'null srData -> null');
ok(describeKeyLevels({ currentPrice: null }) === null, 'no price -> null');
const noMeta = base(); delete noMeta.meta;
r = describeKeyLevels(noMeta);
ok(r.ceiling.kind === 'level' && r.ceiling.daysNear === null && r.ceiling.limitPct === 30, 'missing meta -> levels still shown, no counts');

// deriveStructureState: nearest support even with ascending input (Fable #4)
// price 100, ATR 1 -> "near" = within $2. Nearest support 98.5 (near); deepest 80 (far).
let s = deriveStructureState(100, [120], [80, 90, 98.5], 7, { adx: 25 }, 1);
ok(s.state === 'Uptrend pulling back to support', `near nearest support -> pulling back (got "${s.state}")`);
s = deriveStructureState(100, [130, 101.5], [80], 7, { adx: 25 }, 1);
ok(s.state === 'Uptrend testing resistance', `nearest resistance from unsorted input (got "${s.state}")`);
s = deriveStructureState(100, [], [95], 7, { adx: 25 }, 1);
ok(s.state === 'No resistance within 30% above — strong trend', 'no real resistance + strong trend -> no ceiling within 30% (not "breakout")');
s = deriveStructureState(100, [120], [], 7, { adx: 25 }, 1, { supportPct: 20 });
ok(s.state === 'No support within 20% below', 'no real support -> no floor within 20% (not "below all support")');
ok(deriveStructureState(100, [120], [95], null, { adx: 25 }, 1) === null, 'missing trend data -> no line (not "Downtrend")');
ok(deriveStructureState(100, [120], [95], 2, null, 1) === null, 'weak trend + missing ADX -> no line');
s = deriveStructureState(100, [120], [90], 2, { adx: 30 }, 1);
ok(s.state === 'Downtrend', 'weak trend + ADX 30 -> Downtrend');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
