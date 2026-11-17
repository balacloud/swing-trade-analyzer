/**
 * MRRead — Mean-Reversion Read card (Analyze Page Redesign Step 5, Day 123)
 *
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP5_PLAN_DAY123.md (Fable-reviewed).
 * Replaces MRSignalCard.jsx, which showed an ATR stop and an entry+2ATR
 * target that were never the tested rule, and rendered nothing on loading,
 * error or no signal. Every rule number comes from the API's `rules`
 * (mean_reversion.MR_RULES); ✓/✗ come from the backend's `conditions`
 * (None = input missing, shown as "no data", never as a fail). Day 126: one row
 * + gauge per rule (utils/mrReadRows.js); a feed with zero volume on every bar
 * is shown as "no volume data", not a $0 fail. Day 125: the
 * track record box was removed at the user's direction (less to read); it
 * lives on the Forward Test tab. The API still returns `trackRecord`.
 */
import React from 'react';
import useMissingInputWarning from '../hooks/useMissingInputWarning';
import { mrEntryTiming } from '../utils/mrEntryTiming';
import { buildMRRows, money, bigMoney } from '../utils/mrReadRows';

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);

const Mark = ({ state }) => (
  <span className={`font-bold ${state === true ? 'text-green-400' : state === false ? 'text-red-400' : 'text-gray-500'}`}>
    {state === true ? '✓' : state === false ? '✗' : '–'}
  </span>
);

// A short bar: the line is where the rule is met, the dot is where the stock is.
function Gauge({ g, state }) {
  const passLeft = g.passSide === 'left';
  const dot = state === true ? 'bg-green-400' : state === false ? 'bg-red-400' : 'bg-gray-400';
  return (
    <div className="relative h-2 rounded-full bg-gray-700 mt-2" aria-hidden="true">
      <div
        className="absolute inset-y-0 rounded-full bg-green-500/25"
        style={passLeft ? { left: 0, width: `${g.thresholdPos * 100}%` } : { left: `${g.thresholdPos * 100}%`, right: 0 }}
      />
      <div className="absolute -top-1 -bottom-1 w-0.5 bg-gray-300" style={{ left: `${g.thresholdPos * 100}%` }} />
      <div className={`absolute top-1/2 w-3 h-3 rounded-full ring-2 ring-gray-800 ${dot}`}
        style={{ left: `${g.pos * 100}%`, transform: 'translate(-50%, -50%)' }} />
    </div>
  );
}

function Shell({ children }) {
  return (
    <div data-testid="card-mr-read" className="bg-gray-800 rounded-lg p-6">
      <div data-card-head className="flex justify-between items-start gap-3 mb-1">
        <h3 className="text-lg font-semibold text-blue-400">🔄 Mean-Reversion Read</h3>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-gray-700 text-gray-300 shrink-0">⚙ FORWARD-TESTED</span>
      </div>
      <p data-card-head className="text-sm text-gray-400 mb-3">A separate question: is this a short, sharp dip worth buying for a bounce?</p>
      {children}
    </div>
  );
}

export default function MRRead({ mrData, loading, ticker }) {
  const missing = [];
  if (!loading && (!mrData || mrData.error)) missing.push(`couldn't check: ${mrData?.reason || mrData?.error || 'no response'}`);
  if (!loading && mrData && !mrData.error) {
    if (mrData.missing?.length) missing.push(`inputs missing: ${mrData.missing.join(', ')}`);
    if (!mrData.rules) missing.push('rules missing from response');
  }
  useMissingInputWarning('MRRead', ticker, missing);

  if (loading) {
    return <Shell><div className="text-sm text-gray-500 animate-pulse">Checking the dip rules…</div></Shell>;
  }
  if (!mrData || mrData.error || !mrData.rules) {
    const why = !mrData ? 'no response from the server'
      : mrData.error ? (mrData.reason || mrData.error)
      : 'the server response had no rules (see the console)';
    return (
      <Shell>
        <div className="p-3 rounded-lg text-sm bg-gray-700/30 border border-gray-600 text-gray-400">
          Couldn't check the dip rules: {why}.
        </div>
      </Shell>
    );
  }

  const { signal, current_price: price, rules, asOf, barDropped } = mrData;
  const { rows, blockers, unchecked } = buildMRRows(mrData);
  const stopEstimate = isNum(price) ? price * (1 - rules.stop_pct) : null;
  const entry = mrEntryTiming(asOf);

  return (
    <Shell>
      <div className={`text-xl font-bold ${signal ? 'text-green-400' : 'text-gray-200'}`}>{signal ? 'Signal: all 4 rules pass' : 'No signal'}</div>
      <p className="text-sm text-gray-300 mt-1">
        {signal ? 'A sharp 2-day drop inside an uptrend.'
          : blockers.length ? <>Blocked by: {blockers.join('; ')}.</>
          : "Some inputs didn't load, so the rules couldn't all be checked."}
        {!signal && unchecked.length > 0 && <span className="text-gray-400"> Couldn't check: {unchecked.join(', ').toLowerCase()}.</span>}
      </p>

      <div className="mt-4">
        <div className="text-sm font-semibold text-gray-200 mb-2">Buying the dip needs all four to pass</div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
          {rows.map((r) => (
            <div key={r.key} data-testid={`mr-row-${r.key}`}
              className={`rounded-lg p-3 ${r.state == null ? 'border border-dashed border-gray-600' : 'bg-gray-700/40 border border-gray-700'}`}>
              <div className="flex items-baseline justify-between gap-2">
                <div className="text-xs text-gray-400">{r.question}</div>
                <Mark state={r.state} />
              </div>
              <div className="font-semibold text-gray-100 mt-1">{r.value}</div>
              <div className="text-xs text-gray-400">{r.needs}</div>
              {r.gauge && <Gauge g={r.gauge} state={r.state} />}
              {r.gauge && r.ends && (
                <div className="flex justify-between text-[10px] text-gray-500 mt-1">
                  <span>{r.ends[0]}</span>
                  {r.gauge.offScale && <span>(past the edge of the bar)</span>}
                  <span>{r.ends[1]}</span>
                </div>
              )}
              {r.hint && <div className="text-[10px] text-gray-500 mt-1">{r.hint}</div>}
            </div>
          ))}
        </div>
        <div className="text-xs text-gray-500 mt-1.5">
          Checked on the {asOf || 'latest'} close
          {barDropped ? "; today's bar is still forming, and the system only decides on completed days." : '.'}
        </div>
      </div>

      {signal && (
        <div className="mt-4 rounded-lg border border-gray-600 p-3">
          <div className="text-sm font-semibold text-gray-200 mb-2">The plan, as tested</div>
          <ol className="text-sm text-gray-300 space-y-1.5">
            <li><b className="text-gray-100">1 · Buy</b> {entry.text}.</li>
            <li>
              <b className="text-gray-100">2 · Stop</b> {Math.round(rules.stop_pct * 100)}% below your fill. If it opens below the stop, you're out at the open.
              {stopEstimate != null && <span className="text-gray-400"> About {money(stopEstimate)} if you fill near the {asOf ? `${asOf} ` : ''}close of {money(price)}.</span>}
            </li>
            <li><b className="text-gray-100">3 · Sell</b> at the first close with the 2-day RSI above {rules.rsi2_exit} (the bounce is done).</li>
            <li><b className="text-gray-100">4 · Or sell</b> after {rules.max_hold_days} trading days if it never bounced.</li>
          </ol>
          <div className="text-xs text-gray-400 mt-2">
            No price target; the RSI(2) exit is the target. After selling, the system waited about {rules.cooldown_days} days before buying the same stock again.
            Changing any step means it's no longer the tested system.
          </div>
        </div>
      )}

      <details className="mt-3 text-xs text-gray-400">
        <summary className="cursor-pointer text-blue-400">How this read was formed</summary>
        <div className="mt-2 space-y-2">
          <p><b className="text-gray-300">What it is:</b> Larry Connors' RSI(2) system ("Short Term Trading Strategies That Work").
            RSI(2) scores recent momentum from 0 to 100, weighted mostly to the last 2 days; below {rules.rsi2_entry} means a sharp, short drop. It buys that drop only while the
            stock is above its 200-day average, so it doesn't buy a falling knife.</p>
          <p><b className="text-gray-300">The four rules:</b> the 2-day RSI below {rules.rsi2_entry}, close above the 200-day average, price above
            ${rules.price_min}, and average daily trading above {bigMoney(rules.dollar_volume_min)} (so you can get in and out cleanly). All four must pass.</p>
          <p><b className="text-gray-300">Track record:</b> the rules were tested across many stocks with fills at the next open (what you can actually do).
            That record is about the system, not this stock.</p>
          <p><b className="text-gray-300">Independent of the Technical Read:</b> a stock can pass most trend checks there and show No signal here,
            or the other way round. They answer different questions, and neither gates the other.</p>
        </div>
      </details>
    </Shell>
  );
}
