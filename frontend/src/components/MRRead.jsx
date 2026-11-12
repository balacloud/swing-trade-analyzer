/**
 * MRRead — Mean-Reversion Read card (Analyze Page Redesign Step 5, Day 123)
 *
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP5_PLAN_DAY123.md (Fable-reviewed).
 * Replaces MRSignalCard.jsx, which showed an ATR stop and an entry+2ATR
 * target that were never the tested rule, and rendered nothing on loading,
 * error or no signal. Every rule number comes from the API's `rules`
 * (mean_reversion.MR_RULES); ✓/✗ come only from the backend's `conditions`
 * (None = input missing, shown as "no data", never as a fail). The track
 * record is the forward test re-run at the next open
 * (backtest/mr_open_entry_retest.py), matching the plan's "buy at the open".
 */
import React from 'react';
import useMissingInputWarning from '../hooks/useMissingInputWarning';
import { mrEntryTiming } from '../utils/mrEntryTiming';

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);
const money = (v) => (isNum(v) ? `$${v.toFixed(2)}` : '—');
const bigMoney = (v) => (!isNum(v) ? '—'
  : v >= 1e9 ? `$${+(v / 1e9).toFixed(1)}B`
  : v >= 1e6 ? `$${+(v / 1e6).toFixed(1)}M`
  : `$${Math.round(v).toLocaleString()}`);

const Mark = ({ state }) => (
  <span className={`font-bold ${state === true ? 'text-green-400' : state === false ? 'text-red-400' : 'text-gray-500'}`}>
    {state === true ? '✓' : state === false ? '✗' : '–'}
  </span>
);

// Plain-English reason for the first failing rule, in rule order.
const FAIL_TEXT = {
  rsi2_oversold: "It hasn't dropped hard enough over the last 2 days.",
  above_200sma: "It's below its 200-day average, so a dip here isn't the tested setup (it could be a falling knife).",
  price_filter: 'The price is below the $10 floor the system uses.',
  volume_filter: "It doesn't trade enough dollars a day to get in and out cleanly.",
};

function Shell({ children }) {
  return (
    <div className="bg-gray-800 rounded-lg p-6">
      <div className="flex justify-between items-start gap-3 mb-1">
        <h3 className="text-lg font-semibold text-blue-400">🔄 Mean-Reversion Read</h3>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-gray-700 text-gray-300 shrink-0">⚙ FORWARD-TESTED</span>
      </div>
      <p className="text-sm text-gray-400 mb-3">A separate question: is this a short, sharp dip worth buying for a bounce?</p>
      {children}
    </div>
  );
}

function TrackRecord({ trackRecord }) {
  if (!trackRecord?.variants?.length) {
    return <div className="text-xs text-gray-500">Track record unavailable (see the server log).</div>;
  }
  const bt = trackRecord.backtest;
  return (
    <div className="text-xs text-gray-400 space-y-1.5">
      <div className="text-gray-300 font-semibold">
        Track record · forward test, {trackRecord.basis}
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
        {trackRecord.variants.map((v) => (
          <div key={v.variant} className="rounded bg-gray-700/40 border border-gray-700 px-2.5 py-1.5">
            <div className="text-gray-300">{v.label} <span className="text-gray-500">· {v.firstEntry} to {v.lastExit}</span></div>
            <div className="font-mono text-gray-200">
              {v.trades} trades · {v.winPct}% wins · PF {isNum(v.profitFactor) ? v.profitFactor.toFixed(2) : 'n/a (no losing trades)'}
            </div>
            <div className="text-gray-500">{v.avgPnlPct >= 0 ? '+' : ''}{v.avgPnlPct?.toFixed(2)}% average per trade</div>
          </div>
        ))}
      </div>
      {bt && (
        <div>2020–2025 backtest ({bt.universe}, buying at the {bt.entry}): PF {bt.profitFactor.toFixed(2)}, {bt.note}.</div>
      )}
      <div className="text-gray-500">
        Profit factor = dollars won ÷ dollars lost; 1.0 is break-even. These results are across many stocks, not this one,
        from about ten weeks of mostly rising markets.
      </div>
    </div>
  );
}

export default function MRRead({ mrData, loading, ticker }) {
  const missing = [];
  if (!loading && (!mrData || mrData.error)) missing.push(`couldn't check: ${mrData?.reason || mrData?.error || 'no response'}`);
  if (!loading && mrData && !mrData.error) {
    if (mrData.missing?.length) missing.push(`inputs missing: ${mrData.missing.join(', ')}`);
    if (!mrData.trackRecord) missing.push('track record missing');
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

  const { signal, rsi2, current_price: price, pct_above_sma200: pctAbove, avg_dollar_volume: dollarVol,
    conditions = {}, rules, asOf, barDropped, trackRecord } = mrData;
  const order = ['rsi2_oversold', 'above_200sma', 'price_filter', 'volume_filter'];
  const passing = order.filter((k) => conditions[k] === true).length;
  const unchecked = order.filter((k) => conditions[k] == null).length;
  const firstFail = order.find((k) => conditions[k] === false);

  const tiles = [
    { key: 'rsi2_oversold', label: '2-day dip', value: isNum(rsi2) ? `RSI(2) ${rsi2.toFixed(1)}` : 'no data', needs: `needs below ${rules.rsi2_entry}` },
    { key: 'above_200sma', label: 'Uptrend', value: isNum(pctAbove) ? `${pctAbove >= 0 ? '+' : '−'}${Math.abs(pctAbove).toFixed(1)}% vs 200-day avg` : 'no data', needs: 'needs above it' },
    { key: 'price_filter', label: 'Price', value: money(price), needs: `needs above $${rules.price_min}` },
    { key: 'volume_filter', label: 'Trading volume', value: isNum(dollarVol) ? `${bigMoney(dollarVol)}/day` : 'no data', needs: `needs above ${bigMoney(rules.dollar_volume_min)}` },
  ];
  const stopEstimate = isNum(price) ? price * (1 - rules.stop_pct) : null;
  const entry = mrEntryTiming(asOf);

  return (
    <Shell>
      <div className={`text-xl font-bold ${signal ? 'text-green-400' : 'text-gray-200'}`}>{signal ? 'Buy the dip' : 'No signal'}</div>
      <p className="text-sm text-gray-300 mt-1">
        {signal ? 'A sharp 2-day drop inside an uptrend. All 4 rules pass.'
          : firstFail ? FAIL_TEXT[firstFail]
          : "Some inputs didn't load, so the rules couldn't all be checked."}
        {!signal && <>{' '}<span className="text-gray-400">{passing} of 4 rules pass{unchecked ? `, ${unchecked} not checked` : ''}.</span></>}
      </p>

      <div className="mt-4">
        <div className="text-sm font-semibold text-gray-200 mb-2">Buy the dip needs all four</div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
          {tiles.map((t) => (
            <div key={t.key} className={`rounded-lg p-2.5 ${conditions[t.key] == null ? 'border border-dashed border-gray-600' : 'bg-gray-700/40 border border-gray-700'}`}>
              <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold"><Mark state={conditions[t.key]} /> {t.label}</div>
              <div className="font-mono text-gray-100 mt-0.5">{t.value}</div>
              <div className="text-xs text-gray-400 mt-0.5">{conditions[t.key] == null ? 'not checked' : t.needs}</div>
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
            <li><b className="text-gray-100">3 · Sell</b> at the first close with RSI(2) above {rules.rsi2_exit} (the bounce is done).</li>
            <li><b className="text-gray-100">4 · Or sell</b> after {rules.max_hold_days} trading days if it never bounced.</li>
          </ol>
          <div className="text-xs text-gray-400 mt-2">
            No price target; the RSI(2) exit is the target. After selling, the system waited about {rules.cooldown_days} days before buying the same stock again.
            Changing any step means it's no longer the tested system.
          </div>
        </div>
      )}

      <div className="mt-4 pt-3 border-t border-gray-700">
        <TrackRecord trackRecord={trackRecord} />
      </div>

      <details className="mt-3 text-xs text-gray-400">
        <summary className="cursor-pointer text-blue-400">How this read was formed</summary>
        <div className="mt-2 space-y-2">
          <p><b className="text-gray-300">What it is:</b> Larry Connors' RSI(2) system ("Short Term Trading Strategies That Work").
            RSI(2) scores the last 2 days from 0 to 100; below {rules.rsi2_entry} means a sharp, short drop. It buys that drop only while the
            stock is above its 200-day average, so it doesn't buy a falling knife.</p>
          <p><b className="text-gray-300">The four rules:</b> RSI(2) below {rules.rsi2_entry}, close above the 200-day average, price above
            ${rules.price_min}, and average daily trading above {bigMoney(rules.dollar_volume_min)} (so you can get in and out cleanly). All four must pass.</p>
          <p><b className="text-gray-300">About the numbers:</b> the forward test was first scored as if each trade was bought at the
            entry day's close, which made it look better than it was. The track record above is the same trades re-run at the
            next open, which is what you can actually do.</p>
          <p><b className="text-gray-300">Independent of the Technical Read:</b> a stock can be Strong there and show No signal here,
            or the other way round. They answer different questions, and neither gates the other.</p>
        </div>
      </details>
    </Shell>
  );
}
