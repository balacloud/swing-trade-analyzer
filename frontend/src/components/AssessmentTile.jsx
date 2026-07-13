/**
 * Assessment Tile
 * Day 83: shared renderer for the Categorical Assessment section's 4 tiles
 * (Technical/Fundamental/Sentiment/Risk-Macro) — these were 4 copy-pasted
 * blocks differing only in label, assessment value, and color vocabulary.
 *
 * Each category has a genuinely different, INTENTIONAL color vocabulary —
 * Sentiment's "Neutral" is deliberately gray (de-emphasized, informational-only
 * per Day 70), while Risk/Macro's "Neutral" is yellow (an actual caution
 * signal). Unifying those would erase a real design decision, so `variant`
 * selects the right vocabulary rather than forcing one scheme on all 4.
 *
 * What WAS a genuine inconsistency (not intentional): Technical's tile had no
 * 'N/A'/'Unknown' branch at all (anything non-Strong/Decent fell through to
 * red, including missing data), while Fundamental's did. All 3 non-sentiment
 * variants below now handle N/A/Unknown/null the same way (gray), closing
 * that gap.
 */
import React from 'react';

const COLOR_MAPS = {
  standard: (a) =>
    a === 'Strong' ? 'text-green-400' :
    a === 'Decent' ? 'text-yellow-400' :
    (a === 'N/A' || a === 'Unknown' || a == null) ? 'text-gray-400' :
    'text-red-400',
  sentiment: (a) =>
    a === 'Strong' ? 'text-green-400' :
    a === 'Neutral' ? 'text-gray-300' :
    (a === 'N/A' || a === 'Unknown' || a == null) ? 'text-gray-400' :
    'text-red-400',
  riskMacro: (a) =>
    a === 'Favorable' ? 'text-green-400' :
    a === 'Neutral' ? 'text-yellow-400' :
    (a === 'N/A' || a === 'Unknown' || a == null) ? 'text-gray-400' :
    'text-red-400',
};

export function getAssessmentColor(assessment, variant = 'standard') {
  return (COLOR_MAPS[variant] || COLOR_MAPS.standard)(assessment);
}

export default function AssessmentTile({ label, infoLabel, assessment, variant = 'standard', expanded, onClick, extra, opacityMuted }) {
  return (
    <div
      className={`bg-gray-700/50 rounded-lg p-4 cursor-pointer transition-all hover:bg-gray-700 ${opacityMuted ? 'opacity-75' : ''} ${expanded ? 'ring-2 ring-blue-500' : ''}`}
      onClick={onClick}
    >
      <div className="flex justify-between items-center">
        <div className="text-gray-400 text-sm">
          {label} {infoLabel && <span className="text-gray-600 text-xs">{infoLabel}</span>}
        </div>
        <span className="text-gray-500 text-xs">{expanded ? '▼' : '▶'}</span>
      </div>
      <div className={`text-xl font-bold ${getAssessmentColor(assessment, variant)}`}>
        {assessment}
      </div>
      {extra}
    </div>
  );
}
