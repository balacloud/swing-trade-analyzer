/**
 * Day 131: JS side of the missing-input tests (run by
 * backend/backtest/test_engine_missing_inputs.py). Prints one JSON object.
 * NaN cannot go through the parity grid (Python writes NaN into the JSON and
 * Node rejects it), so NaN, 0 and null are checked here.
 */
import { assessTechnical, assessRiskMacro } from '../src/utils/categoricalAssessment.js';

const tt = { criteria_met: 8, total_criteria: 8 };
const td = { rsData: { rs52Week: 1.2 } };
const tech = (rsi, tdata = td) => {
  const r = assessTechnical(tdata, tt, rsi);
  return { a: r.assessment, rsi: r.data.rsi, avail: r.data.rsiAvailable, reasons: r.reasons.join(' | ') };
};
const risk = (vix, spy) => {
  const r = assessRiskMacro({ current: vix }, spy);
  return { a: r.assessment, spyAbove: r.data.spyAbove200EMA, spyAvail: r.data.spyAvailable, reasons: r.reasons.join(' | ') };
};
const out = {
  rsiNull: tech(null),
  rsiUndefined: tech(undefined),
  rsiNaN: tech(NaN),
  rsiZero: tech(0),
  rsi60: tech(60),
  rsiFallback: tech(null, { rsData: { rs52Week: 1.2 }, indicators: { rsi: 60 } }),
  spyNull_vix15: risk(15, { aboveSma200: null, sma50Declining: false }),
  spyMissing_vix35: risk(35, undefined),
  spyNull_vixNull: risk(null, { aboveSma200: undefined }),
  spyTrue_vix15: risk(15, { aboveSma200: true, sma50Declining: false }),
  spyFalse_vix15: risk(15, { aboveSma200: false, sma50Declining: false }),
};
console.log(JSON.stringify(out));
