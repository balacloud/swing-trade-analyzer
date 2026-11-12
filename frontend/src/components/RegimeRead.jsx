/**
 * RegimeRead — market backdrop band at the top of the Analyze page
 * (Analyze Page Redesign Step 4, Day 123). Info only since the Day 110
 * reversal: it never gates anything and uses no imperative language.
 * Text comes from describeRegimeRead() (categoricalAssessment.js), which
 * describes assessRiskMacro()'s result.
 */
import React, { useMemo } from 'react';
import { describeRegimeRead } from '../utils/categoricalAssessment';
import useMissingInputWarning from '../hooks/useMissingInputWarning';

const STYLES = {
  green: { band: 'bg-green-900/20 border-green-700/60', text: 'text-green-300' },
  yellow: { band: 'bg-yellow-900/20 border-yellow-700/60', text: 'text-yellow-300' },
  red: { band: 'bg-red-900/20 border-red-700/60', text: 'text-red-300' },
  gray: { band: 'bg-gray-800 border-gray-600', text: 'text-gray-300' },
};

export default function RegimeRead({ riskMacro, ticker }) {
  const regime = useMemo(() => describeRegimeRead(riskMacro), [riskMacro]);
  const missing = [];
  if (regime.read === 'Unavailable') missing.push('market regime assessment missing');
  if (riskMacro?.data?.spyAvailable === false) missing.push('SPY 200-day data missing, engine assumed below');
  if (riskMacro?.data?.vixUnavailable) missing.push('VIX missing');
  useMissingInputWarning('Regime', ticker, missing);

  const s = STYLES[regime.color] || STYLES.gray;
  return (
    <div className={`rounded-lg border px-4 py-3 ${s.band}`}>
      <div className="flex justify-between items-start gap-3 flex-wrap">
        <div className="text-sm">
          <span className={`font-semibold ${s.text}`}>Market: {regime.read}</span>
          <span className="text-gray-400"> · {regime.detail}</span>
        </div>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-900/40 text-amber-300 shrink-0">
          ◇ INFO · NEVER GATES THIS PAGE
        </span>
      </div>
      <p className="text-sm text-gray-300 mt-1">{regime.plainEnglish}</p>
    </div>
  );
}
