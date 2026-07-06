/**
 * JS-side runner for the verdict parity grid test — Day 78 (Fable
 * Remediation Task 2.4). Invoked by backend/backtest/test_verdict_parity.py,
 * not meant to be run standalone (though it can be: node verdict_grid.mjs
 * <inputs.json> <output.json>).
 *
 * Reads a grid of scalar inputs, runs each row through the SAME granular
 * functions categoricalAssessment.js exports (assessTechnical,
 * assessFundamental, assessRiskMacro, determineVerdict) — the live-truth
 * verdict logic that ships to users — and writes results in the same shape
 * as the Python side for comparison.
 *
 * sentiment is hardcoded to 'Neutral' throughout, matching how the backtest
 * (categorical_engine.py) always runs it — sentiment is informational only
 * and does not affect strongCount / the verdict (Day 70 removal), so this
 * is a like-for-like comparison of what's actually validated.
 */

import { readFileSync, writeFileSync } from 'fs';
import {
  assessTechnical,
  assessFundamental,
  assessRiskMacro,
  determineVerdict,
} from '../src/utils/categoricalAssessment.js';

const [, , inputsPath, outputPath] = process.argv;

if (!inputsPath || !outputPath) {
  console.error('Usage: node verdict_grid.mjs <inputs.json> <output.json>');
  process.exit(1);
}

const grid = JSON.parse(readFileSync(inputsPath, 'utf-8'));

const results = grid.map((row) => {
  // --- assessTechnical(technicalData, trendTemplate, rsi) ---
  const trendTemplate = { criteria_met: row.tt, total_criteria: 8 };
  const technicalData = { rsData: { rs52Week: row.rs } };
  const technical = assessTechnical(technicalData, trendTemplate, row.rsi);

  // --- assessFundamental(fundamentals, ticker) ---
  const fundamentals = {
    roe: row.roe,
    revenueGrowth: row.revenue_growth,
    debtToEquity: row.debt_equity,
    epsGrowth: null,
  };
  const fundamental = assessFundamental(fundamentals, 'TEST');

  // --- assessRiskMacro(vixData, spyData) ---
  const vixData = { current: row.vix === null ? null : row.vix };
  const spyData = { aboveSma200: row.spy_above, sma50Declining: row.spy_declining };
  const riskMacro = assessRiskMacro(vixData, spyData);

  // --- determineVerdict(technical, fundamental, sentiment, riskMacro, adxData, holdingPeriod) ---
  const adxData = { adx: row.adx };
  const verdict = determineVerdict(
    technical.assessment,
    fundamental.assessment,
    'Neutral', // sentiment — hardcoded, matches categorical_engine.py backtest convention
    riskMacro.assessment,
    adxData,
    row.holding_period
  );

  return {
    technical: technical.assessment,
    fundamental: fundamental.assessment,
    risk_macro: riskMacro.assessment,
    verdict: verdict.verdict,
  };
});

writeFileSync(outputPath, JSON.stringify(results));
console.log(`Processed ${results.length} rows -> ${outputPath}`);
