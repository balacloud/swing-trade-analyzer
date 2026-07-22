// alignmentStyles.js — Day 92
// Shared color/icon vocabulary for "do these two signals agree" banners.
// Extracted after SectorRotationTab.jsx's macro_alignment banner and
// ContextTab.jsx's Market-Phase-vs-Macro-Regime reconciliation independently
// defined byte-identical ALIGNMENT_STYLES/ALIGNMENT_ICONS maps (Golden Rule 21 —
// DRY the shared logic, don't wait to find a drift bug first). Both consumers
// compute their own status ('aligned' | 'cross_current' | 'neutral') from
// different inputs; only the visual vocabulary for that shared 3-state enum
// lives here.

export const ALIGNMENT_STYLES = {
  aligned: 'text-green-400',
  cross_current: 'text-orange-400',
  neutral: 'text-gray-400',
};

export const ALIGNMENT_ICONS = {
  aligned: '✅',
  cross_current: '⚠️',
  neutral: 'ℹ️',
};
