// Runs the REAL frontend indicator code on bars read from stdin and prints the results as JSON (Day 126).
// Used by backend/backtest/test_indicators.py (JS <-> Python parity) and indicator_golden.py (before/after snapshot).
// stdin:  {"cases":[{"id":"X","high":[...],"low":[...],"close":[...],"volume":[...]}]}
// stdout: {"X":{"sma50":..,"sma200":..,"ema8":..,"ema21":..,"atr14":..,"rsi14":..,"avgVolume50":..}}  (null where the code returns null)
// getIndicators() is the function the Analyze page calls; calculateSMA/EMA/ATR/RSI are its building blocks.
import { register } from 'node:module';
import { fileURLToPath } from 'node:url';
register('./lib/js-ext-loader.mjs', import.meta.url);
const { getIndicators } = await import('../src/utils/scoringEngine.js');
const { calculateSMA, calculateEMA, calculateATR, calculateRSI } = await import('../src/utils/technicalIndicators.js');

let raw = '';
for await (const chunk of process.stdin) raw += chunk;
const { cases } = JSON.parse(raw);
const out = {};
for (const c of cases) {
  const gi = getIndicators(c.close, c.volume, c.high, c.low);          // null under 50 bars
  out[c.id] = {
    sma50: calculateSMA(c.close, 50), sma200: calculateSMA(c.close, 200),
    ema8: calculateEMA(c.close, 8), ema21: calculateEMA(c.close, 21),
    atr14: calculateATR(c.high, c.low, c.close, 14), rsi14: calculateRSI(c.close, 14),
    avgVolume50: gi ? gi.avgVolume50 : null,
    getIndicators: gi,                                                   // the full object the page uses
  };
}
process.stdout.write(JSON.stringify(out));
