// describeKeyLevels + zoneSpan + deriveStructureState (rebuilt Day 126 for the simple S&R engine).
//   cd frontend && node scripts/test_key_levels.mjs
import { describeKeyLevels, deriveStructureState, zoneSpan } from '../src/utils/keyLevels.js';

let pass = 0, fail = 0;
const ok = (cond, m) => { if (cond) { pass++; console.log(`ok ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };
const near = (a, b) => Math.abs(a - b) < 1e-9;

const zone = (o) => ({ low: 0, high: 0, mid: 0, swings: 1, side: 'support', insideZone: false, nearest: false, lastSwingDate: '2026-01-05', ...o });
const base = () => ({
  currentPrice: 100,
  support: [95.1, 90.25],                    // zone highs, nearest first (as the API sends it)
  resistance: [104.2, 110],
  meta: {
    zones: [
      zone({ low: 94.0, high: 95.1, swings: 3, side: 'support', nearest: true }),
      zone({ low: 89.9, high: 90.25, swings: 1, side: 'support' }),
      zone({ low: 104.2, high: 105.5, swings: 2, side: 'resistance', nearest: true }),
      zone({ low: 110, high: 110, swings: 1, side: 'resistance' }),
    ],
    nearHigh52w: false,
    proximityFilter: { supportPct: 0.2, resistancePct: 0.3 },
  },
});

// ---- nearest zone per side comes from the zones flagged nearest
let r = describeKeyLevels(base());
ok(r.ceiling.kind === 'level' && r.ceiling.low === 104.2 && r.ceiling.high === 105.5, 'ceiling = the nearest resistance zone');
ok(r.floor.kind === 'level' && r.floor.low === 94.0 && r.floor.high === 95.1, 'floor = the nearest support zone (not the deeper one)');
ok(r.ceiling.swings === 2 && r.floor.swings === 3, 'turn counts come from the zones');
ok(near(r.ceiling.pctAway, 4.2), 'resistance distance is to its LOW edge (the Target): 4.2%');
ok(near(r.floor.pctAway, 4.9), 'support distance is to its HIGH edge (the Buy): 4.9%');
ok(r.floor.edge === 95.1 && r.ceiling.edge === 104.2, 'edge = the price Buy/Target use (Golden Rule 63)');

// ---- a 1-turn zone is shown like any other, never hidden or ranked
const one = base(); one.meta.zones[0].swings = 1;
ok(describeKeyLevels(one).floor.swings === 1, '1-turn zone is shown with its count');
const noCount = base(); delete noCount.meta.zones[0].swings;
ok(describeKeyLevels(noCount).floor.swings === null, 'missing turn count -> null, never 0');

// ---- inside a zone
const ins = base(); ins.currentPrice = 94.6;
ins.meta.zones[0].insideZone = true;
r = describeKeyLevels(ins);
ok(r.floor.kind === 'inside' && r.floor.pctAway === 0 && r.insideSupport === true, 'price inside the support zone -> kind "inside", distance 0');
ok(describeKeyLevels(base()).insideSupport === false, 'not inside -> insideSupport false');

// ---- none on a side
const noRes = base(); noRes.resistance = []; noRes.meta.zones = noRes.meta.zones.filter((z) => z.side !== 'resistance'); noRes.meta.nearHigh52w = true;
r = describeKeyLevels(noRes);
ok(r.ceiling.kind === 'none' && r.ceiling.limitPct === 30 && r.nearHigh52w === true, 'no resistance zone -> none, within 30%, at-52-week-high flag carried');
const noSup = base(); noSup.support = []; noSup.meta.zones = noSup.meta.zones.filter((z) => z.side !== 'support');
ok(describeKeyLevels(noSup).floor.kind === 'none' && describeKeyLevels(noSup).floor.limitPct === 20, 'no support zone -> none, within 20%');

// ---- no zone flagged nearest on a side -> none (never guess one)
const noFlag = base(); noFlag.meta.zones.forEach((z) => { z.nearest = false; });
ok(describeKeyLevels(noFlag).ceiling.kind === 'none', 'no zone flagged nearest -> none, not a guess');

// ---- old-format response and bad input
const old = base(); delete old.meta.zones;
ok(describeKeyLevels(old).unavailable === true, 'srData without meta.zones -> {unavailable: true}');
ok(describeKeyLevels(null) === null, 'null srData -> null');
ok(describeKeyLevels({ currentPrice: null }) === null, 'no price -> null');
const noMeta = base(); delete noMeta.meta;
ok(describeKeyLevels(noMeta).unavailable === true, 'missing meta -> unavailable');
const junk = base(); junk.meta.zones[2] = zone({ low: NaN, high: 105, side: 'resistance', nearest: true });
ok(describeKeyLevels(junk).ceiling.kind === 'none', 'a zone with a non-number edge is ignored');

// ---- removed fields are not read
const legacyish = base(); legacyish.meta.resistanceProjected = true; legacyish.meta.levelScores = { '104.20': 9 };
r = describeKeyLevels(legacyish);
ok(r.ceiling.kind === 'level' && !('daysNear' in r.ceiling) && !('weekly' in r.ceiling) && !('projectedPrice' in r.ceiling), 'projected / levelScores / weekly are ignored (no such fields)');

// ---- zoneSpan: shading on the price bar
let s = zoneSpan({ low: 94, high: 96 }, 90, 110);
ok(s && near(s.left, 20) && near(s.width, 10), 'zone maps onto the bar scale: 94-96 on 90-110 -> left 20%, width 10%');
s = zoneSpan({ low: 85, high: 92 }, 90, 110);
ok(s && s.left === 0 && near(s.width, 10), 'zone partly below the bar is clipped at the left edge');
s = zoneSpan({ low: 108, high: 120 }, 90, 110);
ok(s && near(s.left, 90) && near(s.width, 10), 'zone partly above the bar is clipped at the right edge');
ok(zoneSpan({ low: 70, high: 80 }, 90, 110) === null, 'zone entirely below the bar -> null (not drawn)');
ok(zoneSpan({ low: 120, high: 130 }, 90, 110) === null, 'zone entirely above the bar -> null');
s = zoneSpan({ low: 100, high: 100 }, 90, 110);
ok(s && s.width >= 0.6, 'a one-price zone still gets a visible sliver');
ok(zoneSpan(null, 90, 110) === null && zoneSpan({ low: NaN, high: 1 }, 90, 110) === null, 'bad zone -> null');
ok(zoneSpan({ low: 94, high: 96 }, 110, 90) === null && zoneSpan({ low: 94, high: 96 }, 100, 100) === null, 'bad scale -> null');

// ---- deriveStructureState: nearest support even with ascending input (Fable #4)
// price 100, ATR 1 -> "near" = within $2. Nearest support 98.5 (near); deepest 80 (far).
let st = deriveStructureState(100, [120], [80, 90, 98.5], 7, { adx: 25 }, 1);
ok(st.state === 'Uptrend pulling back to support', `near nearest support -> pulling back (got "${st.state}")`);
st = deriveStructureState(100, [130, 101.5], [80], 7, { adx: 25 }, 1);
ok(st.state === 'Uptrend testing resistance', `nearest resistance from unsorted input (got "${st.state}")`);
st = deriveStructureState(100, [], [95], 7, { adx: 25 }, 1);
ok(st.state === 'No resistance within 30% above — strong trend', 'no real resistance + strong trend -> no ceiling within 30%');
st = deriveStructureState(100, [120], [], 7, { adx: 25 }, 1, { supportPct: 20 });
ok(st.state === 'No support within 20% below', 'no real support -> no floor within 20%');
ok(deriveStructureState(100, [120], [95], null, { adx: 25 }, 1) === null, 'missing trend data -> no line (not "Downtrend")');
ok(deriveStructureState(100, [120], [95], 2, null, 1) === null, 'weak trend + missing ADX -> no line');
st = deriveStructureState(100, [120], [90], 2, { adx: 30 }, 1);
ok(st.state === 'Downtrend', 'weak trend + ADX 30 -> Downtrend');
// Day 126: price inside the support zone (its high is ABOVE price, so it never passes the "below" filter)
st = deriveStructureState(100, [120], [100.5], 7, { adx: 25 }, 1, { insideSupport: true });
ok(st.state === 'Uptrend pulling back to support', `inside the support zone counts as near support (got "${st.state}")`);
st = deriveStructureState(100, [120], [100.5], 7, { adx: 25 }, 1);
ok(st.state === 'No support within 20% below', 'without the inside flag, an edge above price is not support (old behaviour kept)');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
