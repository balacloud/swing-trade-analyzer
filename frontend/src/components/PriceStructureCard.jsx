/**
 * Price Structure Card
 * Day 72 — Phase 1
 *
 * Collapsible Tier 2 card showing structured price narrative:
 *   Section A: Structure state + trend context
 *   Section B: Key levels (nearest first, max 2R + 2S, touch counts, confluence)
 *   Section C: Watch items (up to 3 conditional observations)
 *
 * Placement: Between Trade Setup (Tier 1) and Pattern Detection (Tier 2).
 * Color: Teal-400 header — distinct from purple (Pattern) and blue (Assessment).
 *
 * Design spec: docs/claude/design/PRICE_STRUCTURE_CARD_SPEC.md (v2)
 */

import React from 'react';

const STATE_COLORS = {
  green:  { badge: 'bg-green-900/50 text-green-300 border border-green-600',  dot: 'bg-green-400' },
  yellow: { badge: 'bg-yellow-900/50 text-yellow-300 border border-yellow-600', dot: 'bg-yellow-400' },
  red:    { badge: 'bg-red-900/50 text-red-300 border border-red-600',        dot: 'bg-red-400' },
  gray:   { badge: 'bg-gray-700/50 text-gray-400 border border-gray-600',     dot: 'bg-gray-400' },
};

export default function PriceStructureCard({ srData, priceStructure, expanded, onToggle }) {
  if (!priceStructure) return null;

  const { structureState, stateColor, trendContext, keyLevels, watchItems, meta } = priceStructure;
  const colors = STATE_COLORS[stateColor] || STATE_COLORS.gray;
  const currentPrice = srData?.currentPrice;

  const resistance = keyLevels.filter(l => l.type === 'resistance');
  const support    = keyLevels.filter(l => l.type === 'support');

  return (
    <div className="bg-gray-800 rounded-lg">
      {/* Header — always visible */}
      <button
        onClick={onToggle}
        className="flex items-center gap-2 w-full px-6 py-4 text-left hover:bg-gray-700/30 transition-colors rounded-lg"
      >
        <span className="text-sm text-gray-500">{expanded ? '▼' : '▶'}</span>
        <span className="text-lg font-semibold text-teal-400">Price Structure</span>
        <span className={`ml-2 px-2 py-0.5 rounded-full text-xs font-medium ${colors.badge}`}>
          {structureState}
        </span>
      </button>

      {/* Expanded content */}
      {expanded && (
        <div className="px-6 pb-6 space-y-4">

          {/* Section A: Structure State */}
          <div className="p-3 rounded-lg bg-gray-700/40 border border-gray-600">
            <div className="flex items-center gap-2 mb-1">
              <span className={`w-2 h-2 rounded-full ${colors.dot}`} />
              <span className="text-gray-200 font-medium text-sm">
                {currentPrice != null ? `$${currentPrice.toFixed(2)}` : ''} — {structureState}
              </span>
            </div>
            {trendContext && (
              <div className="text-xs text-gray-400 ml-4">{trendContext}</div>
            )}
          </div>

          {/* Section B: Key Levels */}
          <div className="space-y-1">
            {/* Resistance levels */}
            {resistance.map((lv, i) => (
              <LevelRow key={`r${i}`} level={lv} label={`R${i + 1}`} />
            ))}

            {/* Current price divider */}
            <div className="flex items-center gap-2 py-1">
              <span className="text-gray-500 text-xs">━</span>
              <span className="text-gray-300 text-xs font-medium">
                Current {currentPrice != null ? `$${currentPrice.toFixed(2)}` : ''}
              </span>
            </div>

            {/* Support levels */}
            {support.map((lv, i) => (
              <LevelRow key={`s${i}`} level={lv} label={`S${i + 1}`} />
            ))}

            {keyLevels.length === 0 && (
              <div className="text-xs text-gray-500 italic">No levels within proximity window</div>
            )}
          </div>

          {/* Section C: Watch Items */}
          {watchItems.length > 0 && (
            <div className="space-y-2">
              <div className="text-xs text-gray-500 uppercase tracking-wide">What to watch</div>
              {watchItems.map((item, i) => (
                <div key={i} className="flex items-start gap-2 text-sm text-gray-300">
                  <span className="text-teal-400 mt-0.5 shrink-0">⚡</span>
                  <span>{item}</span>
                </div>
              ))}
            </div>
          )}

          {/* Footer: ATR context */}
          {meta.atr > 0 && (
            <div className="text-xs text-gray-600 border-t border-gray-700 pt-2">
              ATR {meta.atr.toFixed(2)} ({currentPrice ? ((meta.atr / currentPrice) * 100).toFixed(1) : '—'}% of price) · Proximity = 2× ATR
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function LevelRow({ level, label }) {
  const { type, price, touches, confluent, distancePct } = level;
  const isRes = type === 'resistance';

  return (
    <div className="flex items-center gap-2 text-xs py-0.5">
      <span className={`w-5 text-right font-mono font-bold ${isRes ? 'text-red-400' : 'text-green-400'}`}>
        {isRes ? '▲' : '▼'}
      </span>
      <span className={`font-medium ${isRes ? 'text-red-300' : 'text-green-300'} w-6`}>
        {label}
      </span>
      <span className="text-gray-200 font-mono">${price.toFixed(2)}</span>

      {touches != null && (
        <span className="text-gray-400">tested {touches}x</span>
      )}
      {confluent && (
        <span className="px-1 py-0.5 rounded bg-blue-900/40 text-blue-300 border border-blue-700 text-xs">
          D+W
        </span>
      )}
      <span className="ml-auto text-gray-500">{distancePct}%</span>
    </div>
  );
}
