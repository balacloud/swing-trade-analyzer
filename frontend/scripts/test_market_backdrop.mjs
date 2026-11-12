/**
 * Checks for utils/marketBackdrop.js (Day 124, redesign Step 7 — Market backdrop card).
 * Run: cd frontend && node scripts/test_market_backdrop.mjs
 */
import assert from 'assert';
import { describeMarketBackdrop } from '../src/utils/marketBackdrop.js';

let passed = 0;
const check = (name, cond) => { assert.ok(cond, name); passed += 1; console.log('ok', name); };

const spyTrend = {
  asOfDate: '2026-11-11', close: 759.79,
  sma50: 764.96, aboveSma50: false, pctVsSma50: -0.7,
  sma200: 731.31, aboveSma200: true, pctVsSma200: 3.9,
  biggestDrop10d: { date: '2026-11-05', pct: -4.41 }, biggestDrop10dSince: '2025-04-04',
};
const qqqTrend = {
  ...spyTrend, close: 690.38, pctVsSma50: -4.0, pctVsSma200: 1.3,
  biggestDrop10d: { date: '2026-11-05', pct: -6.49 }, biggestDrop10dSince: null, searchedFrom: '2024-11-13',
};
const spy = { aboveSma200: true, trend: spyTrend };
const qqq = { ticker: 'QQQ', trend: qqqTrend };
const vix = { current: 18.2, regime: 'normal' };

// --- full data ------------------------------------------------------------------
let b = describeMarketBackdrop({ spy, qqq, vix });
check('two rows, S&P first', b.rows.length === 2 && b.rows[0].label === 'S&P 500' && b.rows[1].label === 'Nasdaq-100 (QQQ)');
check('long-term above with pct', b.rows[0].longTerm.state === 'ok' && b.rows[0].longTerm.above === true && b.rows[0].longTerm.pct === 3.9);
check('short-term below with pct', b.rows[0].shortTerm.state === 'ok' && b.rows[0].shortTerm.above === false && b.rows[0].shortTerm.pct === -0.7);
check('drop with since', b.rows[0].drop.state === 'drop' && b.rows[0].drop.pct === -4.41 && b.rows[0].drop.since === '2025-04-04');
check('drop without since -> searchedFrom from the backend, not an assumed "2 years"',
  b.rows[1].drop.state === 'drop' && b.rows[1].drop.since === null && b.rows[1].drop.searchedFrom === '2024-11-13');
check('no largestIn2y claim left', !('largestIn2y' in b.rows[1].drop));
check('vix ok, normal range', b.vix.state === 'ok' && b.vix.value === 18.2 && b.vix.label === 'normal range');
check('shared as-of', b.asOfDate === '2026-11-11');
check('nothing missing', b.missing.length === 0 && b.allUnavailable === false);
check('no verdict words anywhere', !/favorable|unfavorable|neutral|healthy|calm/i.test(JSON.stringify(b)));

// --- vix buckets (backend's own) and fallback ------------------------------------
const label = (regime) => describeMarketBackdrop({ spy, qqq, vix: { current: 25, regime } }).vix.label;
check('vix buckets', label('low_volatility') === 'low' && label('elevated') === 'elevated' && label('high') === 'high' && label('extreme') === 'extreme');
b = describeMarketBackdrop({ spy, qqq, vix: { current: 25, regime: 'weird' } });
check('unknown bucket with a value: value shown, no label, never "undefined"', b.vix.state === 'ok' && b.vix.label === null);
b = describeMarketBackdrop({ spy, qqq, vix: { current: null, regime: 'unknown', fallback: true } });
check('vix null -> unavailable + missing', b.vix.state === 'unavailable' && b.missing.includes('VIX'));
b = describeMarketBackdrop({ spy, qqq, vix: undefined });
check('vix undefined -> unavailable', b.vix.state === 'unavailable');

// --- QQQ failure isolated to its row -----------------------------------------------
b = describeMarketBackdrop({ spy, qqq: { error: 'HTTP 500' }, vix });
check('qqq error -> row unavailable with reason', b.rows[1].state === 'unavailable' && b.rows[1].reason === 'HTTP 500');
check('qqq error -> spy row intact', b.rows[0].state === 'ok');
check('qqq error -> missing names it', b.missing.includes('Nasdaq-100 (QQQ)'));

// --- SPY trend null (backend isolated a failure) -----------------------------------
b = describeMarketBackdrop({ spy: { aboveSma200: true, trend: null }, qqq, vix });
check('spy trend null -> row unavailable', b.rows[0].state === 'unavailable' && b.missing.includes('S&P 500'));

// --- short history ------------------------------------------------------------------
b = describeMarketBackdrop({ spy: { trend: { ...spyTrend, sma50: null, aboveSma50: null, pctVsSma50: null, sma200: null, aboveSma200: null, pctVsSma200: null, biggestDrop10d: null } }, qqq, vix });
check('short history -> no_history states, not fake numbers',
  b.rows[0].longTerm.state === 'no_history' && b.rows[0].shortTerm.state === 'no_history' && b.rows[0].drop.state === 'no_history');

// --- no down day ---------------------------------------------------------------------
b = describeMarketBackdrop({ spy: { trend: { ...spyTrend, biggestDrop10d: { noDownDay: true }, biggestDrop10dSince: null } }, qqq, vix });
check('no down day state', b.rows[0].drop.state === 'no_down_day');

// --- different as-of dates are not blended --------------------------------------------
b = describeMarketBackdrop({ spy, qqq: { trend: { ...qqqTrend, asOfDate: '2026-11-10' } }, vix });
check('as-of mismatch -> null shared as-of, per-row dates kept', b.asOfDate === null && b.rows[1].asOfDate === '2026-11-10');

// --- everything missing -----------------------------------------------------------------
b = describeMarketBackdrop({ spy: undefined, qqq: undefined, vix: undefined });
check('all missing -> allUnavailable', b.allUnavailable === true && b.missing.length === 3);

console.log(`\n${passed} checks passed`);
