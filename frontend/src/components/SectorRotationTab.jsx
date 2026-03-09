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

// Rank badge — neutral, position only (quadrant badge + border carry color meaning)
function rankBadgeClass() {
  return 'bg-gray-600 text-gray-200';
}

// RS Ratio bar — 100-centered (backend returns RRG-style values, e.g. 95.88, 125.57)
// RS Momentum bar — 0-centered (delta values, e.g. -5.36, +4.95)
function RsBar({ value, label, isMomentum = false }) {
  let pct, barColor, arrow, textColor;

  if (isMomentum) {
    // Momentum: 0 = neutral, range [-12, +12]
    const clamped = Math.max(-12, Math.min(12, value ?? 0));
    pct = ((clamped + 12) / 24) * 100; // 50% = 0 (neutral)
    barColor  = value >= 0 ? 'bg-green-500' : 'bg-red-500';
    arrow     = value > 0  ? '↑' : value < 0 ? '↓' : '→';
    textColor = value >= 0 ? 'text-green-400' : 'text-red-400';
  } else {
    // RS Ratio: 100 = market parity, range [85, 130]
    const clamped = Math.max(85, Math.min(130, value ?? 100));
    pct = ((clamped - 85) / 45) * 100; // 33% = 100 (parity)
    barColor  = value >= 100 ? 'bg-green-500' : 'bg-red-500';
    arrow     = value > 100  ? '↑' : value < 100 ? '↓' : '→';
    textColor = value >= 100 ? 'text-green-400' : 'text-red-400';
  }

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

// Size rotation signal config
const SIZE_SIGNAL_CONFIG = {
  'Risk-On':  { color: 'text-green-400',  bg: 'bg-green-500/10',  border: 'border-green-600/40', icon: '🟢', label: 'RISK-ON'  },
  'Risk-Off': { color: 'text-red-400',    bg: 'bg-red-500/10',    border: 'border-red-600/40',   icon: '🔴', label: 'RISK-OFF' },
  'Neutral':  { color: 'text-gray-400',   bg: 'bg-gray-700/40',   border: 'border-gray-600/40',  icon: '⚪', label: 'NEUTRAL'  },
};

// Size ETF display order: large → mid → small
const SIZE_ORDER = ['QQQ', 'MDY', 'IWM'];

function SizeRotationStrip({ sizeRotation, sizeSignal, sizeSignalDetail }) {
  if (!sizeRotation || sizeRotation.length === 0) return null;

  const sc = SIZE_SIGNAL_CONFIG[sizeSignal] || SIZE_SIGNAL_CONFIG['Neutral'];
  const ordered = SIZE_ORDER.map(etf => sizeRotation.find(s => s.etf === etf)).filter(Boolean);

  return (
    <div className={`rounded-lg border ${sc.border} ${sc.bg} p-4 mb-6`}>
      {/* Header row */}
      <div className="flex items-center justify-between mb-3 flex-wrap gap-2">
        <div>
          <span className="text-gray-300 text-sm font-semibold">📐 Cap Size Rotation</span>
          <span className="text-gray-500 text-xs ml-2">Large → Mid → Small vs SPY</span>
        </div>
        <span className={`text-sm font-bold ${sc.color}`}>
          {sc.icon} {sc.label} · <span className="font-normal text-xs text-gray-400">{sizeSignalDetail}</span>
        </span>
      </div>

      {/* Three ETF tiles */}
      <div className="grid grid-cols-3 gap-3">
        {ordered.map(s => {
          const isOutperforming = s.rsRatio >= 100;
          const arrow = s.rsMomentum > 0 ? '↑' : s.rsMomentum < 0 ? '↓' : '→';
          const valColor = isOutperforming ? 'text-green-400' : 'text-red-400';
          // Bar: same scale as sector cards
          const clamped = Math.max(85, Math.min(130, s.rsRatio));
          const pct = ((clamped - 85) / 45) * 100;
          const barColor = isOutperforming ? 'bg-green-500' : 'bg-red-500';

          return (
            <div key={s.etf} className="bg-gray-800/60 rounded-lg p-3 text-center">
              <div className="text-gray-500 text-xs font-mono mb-0.5">{s.etf}</div>
              <div className="text-gray-300 text-xs mb-1 truncate">{s.name}</div>
              <div className={`text-sm font-mono font-semibold ${valColor}`}>
                {s.rsRatio.toFixed(1)} {arrow}
              </div>
              <div className="w-full bg-gray-700 rounded-full h-1 mt-1.5">
                <div className={`h-1 rounded-full ${barColor}`} style={{ width: `${pct}%` }} />
              </div>
            </div>
          );
        })}
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
      <RsBar value={sector.rsMomentum} label="RS Momentum" isMomentum />

      {/* Scan button — Leading (strong) or Improving (momentum turning up = best trade setup) */}
      {(sector.quadrant === 'Leading' || sector.quadrant === 'Improving') && (
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
  // Destructure size rotation fields (may be absent on old cached response)
  const sizeRotation = sectorRotation?.size_rotation;
  const sizeSignal = sectorRotation?.size_signal || 'Neutral';
  const sizeSignalDetail = sectorRotation?.size_signal_detail || '';

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

      {/* Size Rotation Strip */}
      <SizeRotationStrip
        sizeRotation={sizeRotation}
        sizeSignal={sizeSignal}
        sizeSignalDetail={sizeSignalDetail}
      />

      {/* Explanation row */}
      <div className="bg-gray-800/50 border border-gray-700 rounded-lg p-4 mb-6 text-xs text-gray-400">
        <span className="font-semibold text-gray-300">How to read this:</span>
        &nbsp;
        <span className="text-green-400 font-medium">Leading</span> = RS Ratio &gt; 100 AND Momentum &gt; 0 (strong & gaining) ·&nbsp;
        <span className="text-blue-400 font-medium">Improving</span> = RS below 100 but gaining momentum ·&nbsp;
        <span className="text-yellow-400 font-medium">Weakening</span> = RS above 100 but fading ·&nbsp;
        <span className="text-red-400 font-medium">Lagging</span> = RS below 100 and falling.
        &nbsp;Rank = RS Ratio magnitude · Quadrant = momentum direction · RS Ratio 100 = market parity (SPY).
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
        Data from TwelveData · RS Ratio: 100 = market parity, &gt;100 = outperforming SPY · Momentum: positive = gaining, negative = fading · Cached per trading day
      </div>
    </div>
  );
}
