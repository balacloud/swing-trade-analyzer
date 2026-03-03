// ConflictCheck.jsx — Day 62, v4.24
// Cycle vs. news conflict/alignment banner for Context Tab

import { useMemo } from 'react';

export default function ConflictCheck({ cyclesRegime, newsLabel, hasOptionsBlock }) {
  const { type, icon, message, style } = useMemo(() => {
    if (cyclesRegime === 'FAVORABLE' && newsLabel === 'BULLISH' && !hasOptionsBlock) {
      return {
        type: 'ALIGNED',
        icon: '✅',
        message: `No Conflicts — Cycles FAVORABLE · News BULLISH`,
        style: 'bg-green-900/30 border-green-600 text-green-300',
      };
    }
    if (cyclesRegime === 'ADVERSE' && newsLabel === 'BEARISH') {
      return {
        type: 'CONFLICT',
        icon: '⚠️',
        message: `CONFLICT — Adverse cycles + Bearish news · Reduce size`,
        style: 'bg-red-900/30 border-red-700 text-red-300',
      };
    }
    if (hasOptionsBlock) {
      return {
        type: 'PARTIAL',
        icon: '🟠',
        message: `Options Block Active — FOMC or Quad Witching nearby · Caution`,
        style: 'bg-orange-900/30 border-orange-600 text-orange-300',
      };
    }
    return {
      type: 'PARTIAL',
      icon: '🟠',
      message: `Mixed Signals — Proceed cautiously · Confirm with other tabs`,
      style: 'bg-orange-900/30 border-orange-600 text-orange-300',
    };
  }, [cyclesRegime, newsLabel, hasOptionsBlock]);

  return (
    <div className={`rounded border px-3 py-2 text-sm mt-3 ${style}`}>
      <span className="font-semibold">{icon} {type}:</span>{' '}
      <span>{message}</span>
    </div>
  );
}
