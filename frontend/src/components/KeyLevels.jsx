/**
 * Nearest support and resistance + one-line price state (Day 125 cleanup, rebuilt Day 126
 * on the simple S&R engine). Data: utils/keyLevels.js (reads /api/sr meta.zones).
 */
import React, { useEffect } from 'react';
import { describeKeyLevels, deriveStructureState, formatZoneRange } from '../utils/keyLevels';

const STATE_TEXT = { green: 'text-green-300', yellow: 'text-yellow-300', red: 'text-red-300', gray: 'text-gray-400' };

function Row({ label, side, isCeiling, nearHigh52w }) {
  const color = isCeiling ? 'text-red-300' : 'text-green-300';
  const where = isCeiling ? 'above' : 'below';
  let body;
  if (side.kind === 'level' || side.kind === 'inside') {
    body = (
      <>
        <span className={`font-mono ${color}`}>{formatZoneRange(side.low, side.high)}</span>
        {side.kind === 'inside'
          ? <span className="text-gray-400"> · price is inside this zone</span>
          : <span className="text-gray-400"> · {side.pctAway.toFixed(1)}% {where}</span>}
        {side.swings != null && <span className="text-gray-400"> · turned here {side.swings}×</span>}
      </>
    );
  } else {
    body = (
      <span className="text-gray-400">
        None within {side.limitPct}% {where}.
        {isCeiling && nearHigh52w && ' The stock is at its 52-week high.'}
      </span>
    );
  }
  return (
    <div className="flex gap-3" data-testid={`key-level-${label.toLowerCase()}`}>
      <span className="w-20 shrink-0 text-gray-500">{label}</span>
      <span>{body}</span>
    </div>
  );
}

export default function KeyLevels({ srData, trendTemplate }) {
  const levels = describeKeyLevels(srData);
  const unavailable = !!levels && levels.unavailable === true;
  // No silent failure: an old-format /api/sr response (no meta.zones) is logged and shown.
  useEffect(() => {
    if (unavailable) console.warn('[STA][KeyLevels] /api/sr response has no meta.zones; support/resistance not shown', srData?.ticker);
  }, [unavailable, srData?.ticker]);
  if (!levels) return null;
  if (unavailable) {
    return (
      <div data-testid="key-levels" className="mt-4 pt-3 border-t border-gray-700 text-sm text-gray-400">
        Support and resistance came back in an unexpected format, so they aren't shown. The plan above is unaffected.
      </div>
    );
  }
  const state = deriveStructureState(
    srData.currentPrice, levels.realResistance, levels.realSupport,
    trendTemplate?.criteria_met, srData.meta?.adx, srData.meta?.atr,
    { resistancePct: levels.ceiling.limitPct, supportPct: levels.floor.limitPct, insideSupport: levels.insideSupport },
  );
  return (
    <div data-testid="key-levels" className="mt-4 pt-3 border-t border-gray-700 space-y-1.5 text-sm">
      {state && (
        <div className="flex gap-3">
          <span className="w-20 shrink-0 text-gray-500">Price is</span>
          <span className={STATE_TEXT[state.color] || 'text-gray-300'}>{state.state}</span>
        </div>
      )}
      <Row label="Resistance" side={levels.ceiling} isCeiling nearHigh52w={levels.nearHigh52w} />
      <Row label="Support" side={levels.floor} isCeiling={false} />
      <p className="text-xs text-gray-500 pt-1">
        Zones are where price turned before (swing highs and lows over the last year). "Turned here N×" is how many
        times. The last 5 trading days can't be confirmed yet. Common trader rules, not tested.
      </p>
    </div>
  );
}
