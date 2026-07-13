/**
 * Pattern Mini Card
 * Day 83: shared renderer for the Pattern Detection Card's VCP / Cup & Handle /
 * Flat Base tiles — these were 3 copy-pasted ~45-line JSX blocks differing only
 * in title/tooltip/stat-rows/highlight-status/description. The stat rows still
 * differ per pattern type (contractions vs cup depth vs range), so callers pass
 * them in; everything else (badge, status row, pivot row, footer) is shared.
 *
 * Also fixes a Golden-Rule-4-class bug: the pivot price row used to be gated by
 * `pivotPrice && (...)`, which would hide the row if pivotPrice were ever 0
 * instead of only when it's genuinely missing. Now uses `!= null`.
 */
import React from 'react';

export default function PatternMiniCard({ title, tooltip, pattern, statRows, highlightStatus, description }) {
  const detected = pattern?.detected;
  const confidence = pattern?.confidence || 0;
  const status = pattern?.status;
  const pivotPrice = pattern?.pivot_price;

  return (
    <div className={`rounded-lg p-3 ${
      detected ? 'bg-green-900/30 border border-green-600' : 'bg-gray-700/30 border border-gray-600'
    }`}>
      <div className="flex justify-between items-center mb-2">
        <span className="font-medium text-gray-200 cursor-help" title={tooltip}>{title}</span>
        <span className={`text-xs px-2 py-0.5 rounded ${
          detected ? 'bg-green-600 text-white' : 'bg-gray-600 text-gray-300'
        }`}>
          {confidence}%
        </span>
      </div>
      <div className="text-xs space-y-1">
        {statRows.map((row, i) => (
          <div key={i} className="flex justify-between text-gray-400">
            <span>{row.label}</span>
            <span className={row.colorClass || 'text-gray-300'}>{row.value}</span>
          </div>
        ))}
        <div className="flex justify-between text-gray-400">
          <span>Status</span>
          <span className={
            status === highlightStatus ? 'text-yellow-400' :
            status === 'broken_out' ? 'text-green-400' :
            'text-gray-300'
          }>
            {status || 'N/A'}
          </span>
        </div>
        {pivotPrice != null && (
          <div className="flex justify-between text-gray-400">
            <span>Pivot</span>
            <span className="text-blue-400 font-mono">${pivotPrice.toFixed(2)}</span>
          </div>
        )}
        <div className="text-gray-500 italic mt-1.5 pt-1.5 border-t border-gray-600">
          {description}
        </div>
      </div>
    </div>
  );
}
