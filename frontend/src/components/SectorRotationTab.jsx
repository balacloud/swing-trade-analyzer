// SectorRotationTab.jsx — Day 62, v4.24
// Sector Rotation Phase 2: Dedicated tab with 11 sector cards, quadrant colors, Scan for Rank 1

import React, { useMemo } from 'react';

// Quadrant display config
const QUADRANT_CONFIG = {
  Leading:   { color: 'text-green-400',  border: 'border-green-500',  bg: 'bg-green-500/10',  badge: 'bg-green-600/80 text-green-100',  icon: '🟢' },
  Improving: { color: 'text-blue-400',   border: 'border-blue-500',   bg: 'bg-blue-500/10',   badge: 'bg-blue-600/80 text-blue-100',    icon: '🔵' },
  Weakening: { color: 'text-yellow-400', border: 'border-yellow-500', bg: 'bg-yellow-500/10', badge: 'bg-yellow-600/80 text-yellow-100', icon: '🟡' },
  Lagging:   { color: 'text-red-400',    border: 'border-red-500',    bg: 'bg-red-500/10',    badge: 'bg-red-600/80 text-red-100',      icon: '🔴' },
};

// Rank badge color
function rankBadgeClass(rank) {
  if (rank <= 3) return 'bg-green-700 text-green-100';
  if (rank <= 7) return 'bg-yellow-700 text-yellow-100';
  return 'bg-red-800 text-red-200';
}

// RS ratio bar — normalized around 1.0, clamped to [0.5, 1.5]
function RsBar({ value, label }) {
  const clamped = Math.max(0.5, Math.min(1.5, value ?? 1.0));
  const pct = ((clamped - 0.5) / 1.0) * 100; // 0% = 0.5, 100% = 1.5, 50% = 1.0
  const barColor = value >= 1.0 ? 'bg-green-500' : 'bg-red-500';
  const arrow = value > 1.0 ? '↑' : value < 1.0 ? '↓' : '→';
  const textColor = value >= 1.0 ? 'text-green-400' : 'text-red-400';

  return (
    <div className="mt-1">
      <div className="flex items-center justify-between mb-0.5">
        <span className="text-gray-500 text-xs">{label}</span>
        <span className={`text-xs font-mono ${textColor}`}>
          {value != null ? value.toFixed(3) : 'N/A'} {arrow}
        </span>
      </div>
      <div className="w-full bg-gray-700 rounded-full h-1.5">
        <div
          className={`h-1.5 rounded-full ${barColor}`}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}

// Individual sector card
function SectorCard({ sector, onScanForSector }) {
  const qc = QUADRANT_CONFIG[sector.quadrant] || QUADRANT_CONFIG.Lagging;

  return (
    <div className={`rounded-lg border-l-4 ${qc.border} ${qc.bg} p-4 bg-gray-800`}>
      {/* Header row: rank badge + quadrant badge */}
      <div className="flex items-center justify-between mb-2">
        <span className={`text-xs font-bold px-2 py-0.5 rounded ${rankBadgeClass(sector.rank)}`}>
          #{sector.rank}
        </span>
        <span className={`text-xs font-medium px-2 py-0.5 rounded ${qc.badge}`}>
          {qc.icon} {sector.quadrant}
        </span>
      </div>

      {/* Sector name + ETF */}
      <div className="flex items-baseline justify-between mb-2">
        <span className="text-white font-semibold text-sm">{sector.name}</span>
        <span className="text-gray-400 text-xs font-mono">{sector.etf}</span>
      </div>

      {/* RS bars */}
      <RsBar value={sector.rsRatio} label="RS Ratio" />
      <RsBar value={sector.rsMomentum} label="RS Momentum" />

      {/* Scan button (only top-3 quadrants or rank 1-4) */}
      {sector.rank <= 4 && (
        <button
          onClick={() => onScanForSector(sector)}
          className="mt-3 w-full text-xs text-blue-400 hover:text-blue-300 hover:bg-blue-900/30 border border-blue-700/50 rounded px-2 py-1 transition-colors"
        >
          Scan stocks in this sector →
        </button>
      )}
    </div>
  );
}

export default function SectorRotationTab({ sectorRotation, onScanForSector }) {
  // Sort sectors by rank
  const sortedSectors = useMemo(() => {
    if (!sectorRotation?.sectors) return [];
    return [...sectorRotation.sectors].sort((a, b) => a.rank - b.rank);
  }, [sectorRotation]);

  // Quadrant summary counts
  const summary = useMemo(() => {
    const counts = { Leading: 0, Improving: 0, Weakening: 0, Lagging: 0 };
    sortedSectors.forEach(s => { if (counts[s.quadrant] != null) counts[s.quadrant]++; });
    return counts;
  }, [sortedSectors]);

  // Rank 1 sector
  const rank1 = sortedSectors[0];
  const rank1IsLeading = rank1?.quadrant === 'Leading';

  // Timestamp display
  const lastUpdated = useMemo(() => {
    if (!sectorRotation?.timestamp) return null;
    const ts = new Date(sectorRotation.timestamp);
    const now = new Date();
    const diffMin = Math.round((now - ts) / 60000);
    if (diffMin < 1) return 'just now';
    if (diffMin < 60) return `${diffMin}m ago`;
    const diffHr = Math.round(diffMin / 60);
    return `${diffHr}h ago`;
  }, [sectorRotation]);

  // Loading state
  if (!sectorRotation) {
    return (
      <div className="text-center py-20">
        <div className="text-4xl mb-4">📡</div>
        <p className="text-gray-400 text-lg">Loading sector rotation data…</p>
        <p className="text-gray-500 text-sm mt-2">Fetching RS ratios for 11 SPDR sector ETFs vs SPY</p>
      </div>
    );
  }

  return (
    <div>
      {/* Header */}
      <div className="bg-gray-800 rounded-lg p-5 mb-6">
        <div className="flex items-center justify-between flex-wrap gap-3">
          <div>
            <h2 className="text-xl font-bold text-white">📊 Sector Rotation Monitor</h2>
            <p className="text-gray-400 text-sm mt-0.5">
              Relative Strength vs SPY · RRG Quadrant Analysis · 11 SPDR ETFs
              {lastUpdated && (
                <span className="ml-2 text-gray-500">· Last refreshed {lastUpdated}</span>
              )}
            </p>
          </div>

          {/* Primary CTA — Scan for Rank 1 */}
          <button
            onClick={() => onScanForSector(rank1)}
            disabled={!rank1}
            className={`px-5 py-2.5 rounded-lg font-semibold text-sm transition-colors ${
              rank1IsLeading
                ? 'bg-green-600 hover:bg-green-500 text-white'
                : 'bg-blue-600 hover:bg-blue-500 text-white'
            } disabled:opacity-40 disabled:cursor-not-allowed`}
          >
            🔍 Scan for Rank #1: {rank1 ? `${rank1.name} (${rank1.etf})` : '…'}
          </button>
        </div>

        {/* Quadrant summary chips */}
        <div className="flex gap-3 mt-4 flex-wrap">
          {Object.entries(QUADRANT_CONFIG).map(([q, qc]) => (
            <div key={q} className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium ${qc.badge}`}>
              <span>{qc.icon}</span>
              <span>{q}: {summary[q]}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Explanation row */}
      <div className="bg-gray-800/50 border border-gray-700 rounded-lg p-4 mb-6 text-xs text-gray-400">
        <span className="font-semibold text-gray-300">How to read this:</span>
        &nbsp;
        <span className="text-green-400 font-medium">Leading</span> = RS Ratio &gt; 1.0 AND Momentum &gt; 1.0 (strong & improving) ·&nbsp;
        <span className="text-blue-400 font-medium">Improving</span> = RS below market but gaining ·&nbsp;
        <span className="text-yellow-400 font-medium">Weakening</span> = above market but fading ·&nbsp;
        <span className="text-red-400 font-medium">Lagging</span> = below market and falling.
        &nbsp;RS Ratio bar midpoint = 1.0 (market parity).
      </div>

      {/* 11 Sector Cards — responsive grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
        {sortedSectors.map(sector => (
          <SectorCard
            key={sector.etf}
            sector={sector}
            onScanForSector={onScanForSector}
          />
        ))}
      </div>

      {/* Footer note */}
      <div className="mt-6 text-center text-xs text-gray-600">
        Data from TwelveData · RS Ratio = ETF / SPY 12-week performance ratio · Cached per trading day
      </div>
    </div>
  );
}
