/**
 * Nearest support and resistance + one-line price state (Day 125, Analyze cleanup).
 * Replaces the S1..Sn / R1..Rn lists, the MTF Confluence badge, the Weekly
 * Levels dropdown and the Price Structure card. Data: utils/keyLevels.js.
 */
import React from 'react';
import { describeKeyLevels, deriveStructureState, ZONE_PCT } from '../utils/keyLevels';

const money = (x) => `$${x.toFixed(2)}`;
const STATE_TEXT = { green: 'text-green-300', yellow: 'text-yellow-300', red: 'text-red-300', gray: 'text-gray-400' };

function Row({ label, side, isCeiling }) {
  const color = isCeiling ? 'text-red-300' : 'text-green-300';
  const where = isCeiling ? 'above' : 'below';
  let body;
  if (side.kind === 'level') {
    body = (
      <>
        <span className={`font-mono ${color}`}>{money(side.low)} – {money(side.high)}</span>
        <span className="text-gray-400"> · {side.pctAway.toFixed(1)}% {where}</span>
        {side.daysNear != null && <span className="text-gray-400"> · near it on {side.daysNear} days</span>}
        {side.weekly && (
          <span className="text-yellow-400" title={side.weeklyStrength ? `A weekly-chart level is within 1.5% (${side.weeklyStrength})` : 'A weekly-chart level is within 1.5%'}> ★ weekly</span>
        )}
      </>
    );
  } else if (side.kind === 'projected') {
    body = (
      <span className="text-gray-400">
        No real {label.toLowerCase()} within {side.limitPct}% {where}.
        {side.projectedPrice != null && ` ${money(side.projectedPrice)} is a projected level (ATR/Fibonacci), not a real one.`}
      </span>
    );
  } else {
    body = <span className="text-gray-400">None within {side.limitPct}% {where}.</span>;
  }
  return (
    <div className="flex gap-3">
      <span className="w-20 shrink-0 text-gray-500">{label}</span>
      <span>{body}</span>
    </div>
  );
}

export default function KeyLevels({ srData, trendTemplate }) {
  const levels = describeKeyLevels(srData);
  if (!levels) return null;
  const state = deriveStructureState(
    srData.currentPrice, levels.realResistance, levels.realSupport,
    trendTemplate?.criteria_met, srData.meta?.adx, srData.meta?.atr,
    { resistancePct: levels.ceiling.limitPct, supportPct: levels.floor.limitPct },
  );
  return (
    <div data-testid="key-levels" className="mt-4 pt-3 border-t border-gray-700 space-y-1.5 text-sm">
      {state && (
        <div className="flex gap-3">
          <span className="w-20 shrink-0 text-gray-500">Price is</span>
          <span className={STATE_TEXT[state.color] || 'text-gray-300'}>{state.state}</span>
        </div>
      )}
      <Row label="Resistance" side={levels.ceiling} isCeiling />
      <Row label="Support" side={levels.floor} isCeiling={false} />
      <p className="text-xs text-gray-500 pt-1">
        Levels are zones (±{ZONE_PCT}%) where price turned before. "Near it" counts days the high or low came
        within {ZONE_PCT}% (about the last year). Common trader rules, not tested.
      </p>
    </div>
  );
}
