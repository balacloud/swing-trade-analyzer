/**
 * Mean-Reversion Signal Card
 * Tier 3B (Day 70): Displays RSI(2) oversold signals as a SEPARATE card
 * below the momentum analysis. Does NOT modify any existing verdict logic.
 *
 * ONLY renders when signal is ACTIVE (RSI(2) < 10). Hidden otherwise.
 * Simplicity premium: don't clutter the UI with inactive signals.
 *
 * Source: Connors RSI(2) approach — "Short Term Trading Strategies That Work" (2009)
 */

import React from 'react';

export default function MRSignalCard({ mrData, loading }) {
  // Don't show anything while loading or when no data
  if (loading || !mrData || mrData.error) {
    return null;
  }

  const { signal, rsi2, sma200, current_price, conditions, stop, target,
          max_hold_days, exit_rule, adx, range_bound } = mrData;

  // Simplicity premium: only show card when signal is ACTIVE
  if (!signal) {
    return null;
  }

  const stopPct = ((1 - stop / current_price) * 100).toFixed(1);

  return (
    <div className="bg-purple-900/30 border border-purple-500/50 rounded-lg p-6 mt-4">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-semibold text-purple-400">
          Mean-Reversion Signal
        </h3>
        <span className="bg-purple-600 text-white text-xs font-bold px-3 py-1 rounded uppercase">
          Active
        </span>
      </div>

      {/* Key metrics */}
      <div className="grid grid-cols-3 gap-4 mb-4">
        <div>
          <div className="text-gray-400 text-xs uppercase">RSI(2)</div>
          <div className="text-red-400 text-xl font-bold">
            {rsi2} <span className="text-sm">(OVERSOLD)</span>
          </div>
        </div>
        <div>
          <div className="text-gray-400 text-xs uppercase">200 SMA</div>
          <div className="text-gray-200 text-xl font-bold">
            ${sma200} <span className="text-green-400 text-sm">&#10003;</span>
          </div>
        </div>
        {adx != null && (
          <div>
            <div className="text-gray-400 text-xs uppercase">ADX</div>
            <div className="text-gray-200 text-xl font-bold">
              {adx} <span className="text-gray-400 text-sm">{range_bound ? '(Range)' : '(Trend)'}</span>
            </div>
          </div>
        )}
      </div>

      {/* Conditions */}
      <div className="flex flex-wrap gap-2 mb-4">
        {conditions && Object.entries(conditions).map(([key, passed]) => (
          <span
            key={key}
            className={`text-xs px-2 py-1 rounded font-medium ${
              passed
                ? 'bg-green-900/40 text-green-400'
                : 'bg-red-900/40 text-red-400'
            }`}
          >
            {passed ? '\u2713' : '\u2717'} {formatConditionName(key)}
          </span>
        ))}
      </div>

      {/* Trade params */}
      <div className="border-t border-gray-600 pt-3">
        <div className="grid grid-cols-2 gap-4 text-sm text-gray-300">
          <div>
            Stop: <span className="text-white font-semibold">${stop}</span>
            <span className="text-gray-400 ml-1">({stopPct}%)</span>
          </div>
          <div>
            Target: <span className="text-white font-semibold">${target}</span>
          </div>
          <div>
            Max Hold: <span className="text-white font-semibold">{max_hold_days} days</span>
          </div>
          <div>
            Exit: <span className="text-white font-semibold">{exit_rule}</span>
          </div>
        </div>
        <div className="mt-3 bg-yellow-900/30 border border-yellow-600/30 rounded px-3 py-2 text-xs text-yellow-300">
          Different strategy than momentum — tighter stops, shorter hold period
        </div>
      </div>
    </div>
  );
}

function formatConditionName(key) {
  const names = {
    rsi2_oversold: 'RSI(2) < 10',
    above_200sma: 'Above 200 SMA',
    price_filter: 'Price > $5',
    volume_filter: 'Vol > 500K',
  };
  return names[key] || key;
}
