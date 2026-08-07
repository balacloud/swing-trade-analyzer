// SectorRotationTab.jsx — Day 62, v4.24
// Sector Rotation Phase 2: Dedicated tab with 11 sector cards, quadrant colors, Scan for Rank 1

import React, { useMemo, useState } from 'react';
import { ALIGNMENT_STYLES, ALIGNMENT_ICONS } from '../utils/alignmentStyles';
import { fetchSubIndustryRotation, fetchSrpsPullbackScreen } from '../services/api';

// Quadrant display config. sectionHint is the beginner-facing "what do I do
// with this" translation shown once per group, not per card.
const QUADRANT_CONFIG = {
  Leading:   { color: 'text-green-400',  border: 'border-green-500',  bg: 'bg-green-500/10',  badge: 'bg-green-600/80 text-green-100',  icon: '🟢', sectionHint: 'Strong and gaining momentum — the most trade-ready group' },
  Improving: { color: 'text-blue-400',   border: 'border-blue-500',   bg: 'bg-blue-500/10',   badge: 'bg-blue-600/80 text-blue-100',    icon: '🔵', sectionHint: 'Still lagging SPY, but turning up — early, not yet confirmed' },
  Weakening: { color: 'text-yellow-400', border: 'border-yellow-500', bg: 'bg-yellow-500/10', badge: 'bg-yellow-600/80 text-yellow-100', icon: '🟡', sectionHint: 'Ahead of SPY but losing steam — existing positions, not new ones' },
  Lagging:   { color: 'text-red-400',    border: 'border-red-500',    bg: 'bg-red-500/10',    badge: 'bg-red-600/80 text-red-100',      icon: '🔴', sectionHint: 'Behind SPY and still falling — avoid for now' },
};
const QUADRANT_ORDER = ['Leading', 'Improving', 'Weakening', 'Lagging'];

// The single most-favorable sector to point a beginner at — NOT the highest
// RS Ratio (that's just magnitude of past outperformance, see Golden Rule-
// style finding: a #1-by-magnitude sector can be actively Weakening). Picks
// the top Leading sector by RS Ratio; falls back to top Improving if nothing
// is Leading; null if the market has no sector in either favorable quadrant.
function pickBestSector(sectorsByRsRatioDesc) {
  const leading = sectorsByRsRatioDesc.filter(s => s.quadrant === 'Leading');
  if (leading.length > 0) return { sector: leading[0], tier: 'Leading' };
  const improving = sectorsByRsRatioDesc.filter(s => s.quadrant === 'Improving');
  if (improving.length > 0) return { sector: improving[0], tier: 'Improving' };
  return { sector: null, tier: null };
}

// One-sentence, plain-English takeaway — the "so what" a beginner needs
// before the grid, not after it.
function buildTakeaway(sortedSectors, summary) {
  const leadingNames = sortedSectors.filter(s => s.quadrant === 'Leading').map(s => s.name);
  const improvingNames = sortedSectors.filter(s => s.quadrant === 'Improving').map(s => s.name);

  if (leadingNames.length > 0) {
    const shown = leadingNames.slice(0, 3).join(', ');
    return `${summary.Leading} sector${summary.Leading > 1 ? 's' : ''} leading right now — strongest setups in ${shown}.`;
  }
  if (improvingNames.length > 0) {
    const shown = improvingNames.slice(0, 3).join(', ');
    return `No sector is leading yet — ${summary.Improving} improving (early-stage): ${shown}. Worth watching, not yet confirmed.`;
  }
  return 'No sector currently shows both strength and momentum — market breadth is weak, stay cautious.';
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
    // RS Ratio: 100 = flat vs SPY at the lookback's static midpoint anchor
    // (not real-time RRG normalization — see backend.py's own comment on
    // this endpoint), range [85, 130]
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

// Per-tile interpretation: color + momentum → quadrant label + hint
// barColor intentionally matches `color` (quadrant, not raw RS Ratio sign) —
// a prior version colored the bar/number by RS Ratio alone while this label
// used the quadrant color, so a Weakening tile (RS>=100) could show a green
// bar right next to yellow "Weakening" text, and an Improving tile (RS<100)
// could show a red bar next to blue "Improving" text.
function tileInterpretation(rsRatio, rsMomentum) {
  const out = rsRatio >= 100;
  const up  = rsMomentum > 0;
  if (out && up)   return { label: 'Leading · gaining',      color: 'text-green-400',  barColor: 'bg-green-500',  hint: 'Outperforming SPY & strengthening' };
  if (out && !up)  return { label: 'Weakening · fading',     color: 'text-yellow-400', barColor: 'bg-yellow-500', hint: 'Outperforming SPY but losing steam' };
  if (!out && up)  return { label: 'Improving · recovering', color: 'text-blue-400',   barColor: 'bg-blue-500',   hint: 'Lagging SPY but gaining momentum' };
  return             { label: 'Lagging · falling',      color: 'text-red-400',    barColor: 'bg-red-500',    hint: 'Underperforming SPY & weakening' };
}

// Momentum-aware sub-note for the headline — considers all 3 tiers (large/mid/small),
// not just QQQ/IWM. A prior version ignored MDY entirely, so it could claim
// "fading across all cap sizes" while MDY's own tile showed rising momentum.
function momentumNote(sizeRotation) {
  const qqq = sizeRotation.find(s => s.etf === 'QQQ');
  const mdy = sizeRotation.find(s => s.etf === 'MDY');
  const iwm = sizeRotation.find(s => s.etf === 'IWM');
  if (!qqq || !mdy || !iwm) return null;

  const qqqUp = qqq.rsMomentum > 0;
  const mdyUp = mdy.rsMomentum > 0;
  const iwmUp = iwm.rsMomentum > 0;
  const upCount = [qqqUp, mdyUp, iwmUp].filter(Boolean).length;

  if (upCount === 3) return '✅ Broad risk appetite — all sizes gaining vs SPY';
  if (upCount === 0) return '⚠️ Risk appetite fading across all cap sizes';

  const up = [];
  const down = [];
  if (qqqUp) up.push('large'); else down.push('large');
  if (mdyUp) up.push('mid');   else down.push('mid');
  if (iwmUp) up.push('small'); else down.push('small');
  const upWord = up.length > 1 ? 'caps' : 'cap';
  const downWord = down.length > 1 ? 'caps' : 'cap';
  return `⚠️ Mixed: ${up.join('/')} ${upWord} gaining, ${down.join('/')} ${downWord} fading`;
}

function SizeRotationStrip({ sizeRotation, sizeSignal, sizeSignalDetail }) {
  if (!sizeRotation || sizeRotation.length === 0) return null;

  const sc      = SIZE_SIGNAL_CONFIG[sizeSignal] || SIZE_SIGNAL_CONFIG['Neutral'];
  const ordered = SIZE_ORDER.map(etf => sizeRotation.find(s => s.etf === etf)).filter(Boolean);
  const note    = momentumNote(sizeRotation);

  return (
    <div className={`rounded-lg border ${sc.border} ${sc.bg} p-4 mb-6`}>
      {/* Header row */}
      <div className="flex items-center justify-between mb-1 flex-wrap gap-2">
        <div>
          <span className="text-gray-300 text-sm font-semibold">📐 Cap Size Rotation</span>
          <span className="text-gray-500 text-xs ml-2">Large → Mid → Small vs SPY</span>
        </div>
        <span className={`text-sm font-bold ${sc.color}`}>
          {sc.icon} {sc.label} · <span className="font-normal text-xs text-gray-400">{sizeSignalDetail}</span>
        </span>
      </div>
      <div className="text-gray-500 text-xs mb-2">Is money moving into risk (small caps) or safety (large caps)?</div>

      {/* Momentum context note */}
      {note && (
        <div className="text-xs text-gray-400 mb-3 pl-0.5">{note}</div>
      )}

      {/* Three ETF tiles */}
      <div className="grid grid-cols-3 gap-3">
        {ordered.map(s => {
          const interp  = tileInterpretation(s.rsRatio, s.rsMomentum);
          const arrow   = s.rsMomentum > 0 ? '↑' : s.rsMomentum < 0 ? '↓' : '→';
          const clamped  = Math.max(85, Math.min(130, s.rsRatio));
          const pct      = ((clamped - 85) / 45) * 100;

          return (
            <div key={s.etf} className="bg-gray-800/60 rounded-lg p-3 text-center">
              <div className="text-gray-500 text-xs font-mono mb-0.5">{s.etf}</div>
              <div className="text-gray-300 text-xs mb-1 truncate">{s.name}</div>
              <div className={`text-sm font-mono font-semibold ${interp.color}`}>
                {s.rsRatio.toFixed(1)} {arrow}
              </div>
              <div className="w-full bg-gray-700 rounded-full h-1 mt-1.5 mb-1.5">
                <div className={`h-1 rounded-full ${interp.barColor}`} style={{ width: `${pct}%` }} />
              </div>
              <div className={`text-xs font-medium ${interp.color}`}>{interp.label}</div>
              <div className="text-gray-600 text-xs mt-0.5">{interp.hint}</div>
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
      {/* Header row: quadrant badge only. A numbered "rank" badge used to sit
          here too, but any "#N" reads as "the winner" in English regardless
          of what qualifier is stuck in front of it — a #1 badge next to a
          "Weakening" label is a contradiction no amount of relabeling fixes.
          The RS Ratio value itself (magnitude info) is still shown below,
          just not framed as a competitive ranking. */}
      <div className="flex items-center justify-end mb-2">
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

// Sub-industry cluster card — same quadrant styling as SectorCard, one level
// below the 11 broad GICS sectors (Day 100+, "Sub-Industry Watch"). No "Scan
// stocks" CTA in this first pass — that action maps a sector ETF to a GICS
// scan filter STA already has; a sub-industry cluster's tickers are a curated
// theme list, not a scan-able GICS category, so it's a different feature not
// scoped here.
function SubIndustryCard({ cluster }) {
  if (cluster.error) {
    return (
      <div className="rounded-lg border-l-4 border-gray-600 bg-gray-800/60 p-4">
        <div className="flex items-baseline justify-between mb-1">
          <span className="text-white font-semibold text-sm">{cluster.cluster}</span>
          <span className="text-gray-400 text-xs font-mono">{cluster.proxy}</span>
        </div>
        <p className="text-gray-500 text-xs">Unavailable — {cluster.error}</p>
      </div>
    );
  }

  const qc = QUADRANT_CONFIG[cluster.quadrant] || QUADRANT_CONFIG.Lagging;

  return (
    <div className={`rounded-lg border-l-4 ${qc.border} ${qc.bg} p-4 bg-gray-800`}>
      <div className="flex items-center justify-end mb-2">
        <span className={`text-xs font-medium px-2 py-0.5 rounded ${qc.badge}`}>
          {qc.icon} {cluster.quadrant}
        </span>
      </div>
      <div className="flex items-baseline justify-between mb-2">
        <span className="text-white font-semibold text-sm">{cluster.cluster}</span>
        <span className="text-gray-400 text-xs font-mono">{cluster.proxy}</span>
      </div>
      <RsBar value={cluster.rsRatio} label="RS Ratio" />
      <RsBar value={cluster.rsMomentum} label="RS Momentum" isMomentum />
      {cluster.shortHistory && (
        <p className="text-yellow-500/80 text-xs mt-2">
          Short history ({cluster.usableDays}d) — read is thinner than the full ~6mo window.
        </p>
      )}
    </div>
  );
}

// Collapsible Tier-2 section, lazy-loaded on first expand (own ~22-ticker
// fetch, slower than the eager-loaded 11 broad sectors above — most sessions
// won't need this every time, so it shouldn't tax every page load, same
// reasoning as Golden Rule 25). State is local to this component since
// nothing else in the app consumes sub-industry data.
function SubIndustryWatchSection() {
  const [expanded, setExpanded] = useState(false);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const load = () => {
    setLoading(true);
    setError(null);
    fetchSubIndustryRotation()
      .then(res => {
        setData(res);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load sub-industry rotation:', err);
        setError(err.message || 'Failed to fetch sub-industry rotation data');
        setLoading(false);
      });
  };

  const handleToggle = () => {
    const next = !expanded;
    setExpanded(next);
    if (next && !data && !loading) {
      load();
    }
  };

  const grouped = useMemo(() => {
    if (!data?.clusters) return {};
    const out = { Leading: [], Improving: [], Weakening: [], Lagging: [] };
    data.clusters.forEach(c => {
      if (c.error) return; // errored clusters render in their own strip below, not grouped
      if (out[c.quadrant]) out[c.quadrant].push(c);
    });
    return out;
  }, [data]);

  const erroredClusters = useMemo(
    () => (data?.clusters || []).filter(c => c.error),
    [data]
  );

  return (
    <div className="bg-gray-800/50 border border-gray-700 rounded-lg mb-6">
      <button
        onClick={handleToggle}
        className="w-full flex items-center justify-between p-4 text-left"
      >
        <div>
          <span className="text-white font-semibold text-sm">🔬 Sub-Industry Watch</span>
          <span className="text-gray-500 text-xs ml-2">
            Semis / memory / nuclear / materials / gold / biotech / financials & more — one level below the 11 broad sectors above
          </span>
        </div>
        <span className="text-gray-400 text-sm">{expanded ? '▲' : '▼'}</span>
      </button>

      {expanded && (
        <div className="px-4 pb-4">
          {loading && (
            <div className="text-center py-10">
              <div className="text-3xl mb-2">📡</div>
              <p className="text-gray-400 text-sm">Loading sub-industry data — 21 proxy ETFs vs SPY…</p>
            </div>
          )}

          {!loading && error && (
            <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 text-red-200">
              <p className="font-semibold">⚠️ Failed to load sub-industry data</p>
              <p className="text-sm mt-1 text-red-300">{error}</p>
              <button
                onClick={load}
                className="mt-3 px-3 py-1.5 bg-red-700 hover:bg-red-600 rounded text-sm"
              >
                Retry
              </button>
            </div>
          )}

          {!loading && !error && data && (
            <>
              {QUADRANT_ORDER.map(q => {
                const list = grouped[q] || [];
                if (list.length === 0) return null;
                const qc = QUADRANT_CONFIG[q];
                return (
                  <div key={q} className="mb-5">
                    <div className="flex items-baseline gap-2 mb-3">
                      <span className={`text-sm font-semibold ${qc.color}`}>{qc.icon} {q}</span>
                      <span className="text-gray-500 text-xs">({list.length})</span>
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                      {list.map(cluster => (
                        <SubIndustryCard key={cluster.cluster} cluster={cluster} />
                      ))}
                    </div>
                  </div>
                );
              })}

              {erroredClusters.length > 0 && (
                <div className="mb-5">
                  <div className="text-gray-500 text-xs mb-2">Unavailable this run ({erroredClusters.length}):</div>
                  <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                    {erroredClusters.map(cluster => (
                      <SubIndustryCard key={cluster.cluster} cluster={cluster} />
                    ))}
                  </div>
                </div>
              )}

              {data.noProxyClusters && data.noProxyClusters.length > 0 && (
                <div className="text-gray-600 text-xs">
                  No thematic proxy fits: {data.noProxyClusters.map(c => `${c.cluster} (${c.tickers.join(', ')})`).join('; ')}
                </div>
              )}
            </>
          )}
        </div>
      )}
    </div>
  );
}

// Candidate row for the SRPS pullback screener — informational only, not a
// signal. Shows what the mechanical criteria found so a human can apply
// their own regime/news/catalyst judgment before acting on anything.
function SrpsCandidateRow({ c }) {
  return (
    <div className="flex items-center justify-between bg-gray-900/40 rounded px-3 py-2 mb-2 text-sm">
      <div className="flex items-baseline gap-3">
        <span className="text-white font-semibold">{c.ticker}</span>
        <span className="text-gray-400 text-xs">RS {c.rsRatio}</span>
        <span className="text-gray-400 text-xs">Vol {c.volumeVsAvg20d}x avg</span>
      </div>
      <div className="flex items-baseline gap-4 text-xs">
        <span className="text-gray-300">Price ${c.price}</span>
        <span className="text-red-400">Stop ${c.stopPrice} (-{c.riskPct}%)</span>
        <span className="text-green-400">Target ${c.targetPrice}</span>
      </div>
      {c.earningsWarning && (
        <span className="ml-3 text-yellow-500 text-xs whitespace-nowrap">⚠️ {c.earningsWarning}</span>
      )}
    </div>
  );
}

// Collapsible section, lazy-loaded on first expand — same pattern as
// SubIndustryWatchSection above. NOT a forward-test track: SRPS's
// mechanical rule set failed its own pre-registered backtest bar (34.1%
// win rate vs. required >45%, PF 1.177 vs. required >1.2), so it was
// never built as an automated paper-trading track. This repurposes the
// same rule logic as a pure discretionary screen — surfaces candidates
// matching the mechanical criteria, the user applies their own judgment
// (regime read, news, catalysts) before deciding anything. No ledger, no
// automated entry/exit.
function SrpsPullbackScreenSection() {
  const [expanded, setExpanded] = useState(false);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const load = () => {
    setLoading(true);
    setError(null);
    fetchSrpsPullbackScreen()
      .then(res => {
        setData(res);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load SRPS pullback screen:', err);
        setError(err.message || 'Failed to fetch SRPS pullback screen');
        setLoading(false);
      });
  };

  const handleToggle = () => {
    const next = !expanded;
    setExpanded(next);
    if (next && !data && !loading) {
      load();
    }
  };

  return (
    <div className="bg-gray-800/50 border border-gray-700 rounded-lg mb-6">
      <button
        onClick={handleToggle}
        className="w-full flex items-center justify-between p-4 text-left"
      >
        <div>
          <span className="text-white font-semibold text-sm">🎯 Sector Pullback Screener</span>
          <span className="text-gray-500 text-xs ml-2">
            Discretionary screen, not a signal — strong names in recovering sectors pulling back to their 21-EMA
          </span>
        </div>
        <span className="text-gray-400 text-sm">{expanded ? '▲' : '▼'}</span>
      </button>

      {expanded && (
        <div className="px-4 pb-4">
          {loading && (
            <div className="text-center py-10">
              <div className="text-3xl mb-2">📡</div>
              <p className="text-gray-400 text-sm">Screening sector-improving candidates…</p>
            </div>
          )}

          {!loading && error && (
            <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 text-red-200">
              <p className="font-semibold">⚠️ Failed to load pullback screen</p>
              <p className="text-sm mt-1 text-red-300">{error}</p>
              <button
                onClick={load}
                className="mt-3 px-3 py-1.5 bg-red-700 hover:bg-red-600 rounded text-sm"
              >
                Retry
              </button>
            </div>
          )}

          {!loading && !error && data && (
            <>
              <div className="bg-amber-900/30 border border-amber-600/50 rounded-lg p-3 mb-4 text-amber-200 text-xs">
                {data.disclaimer}
              </div>

              <div className={`rounded-lg p-3 mb-4 text-xs ${data.regimeOk ? 'bg-green-900/30 border border-green-600/50 text-green-200' : 'bg-red-900/30 border border-red-600/50 text-red-200'}`}>
                {data.regimeOk ? '🟢' : '🔴'} {data.regimeMessage}
                <span className="text-gray-400 ml-2">(SPY ${data.spyClose} vs 200-SMA ${data.spySma200})</span>
              </div>

              {data.improvingSectorCount === 0 && (
                <p className="text-gray-500 text-sm">No sectors in the Improving quadrant today — this screen has nothing to show until at least one sector qualifies.</p>
              )}

              {data.sectors.map(s => (
                <div key={s.etf} className="mb-5">
                  <div className="flex items-baseline gap-2 mb-2">
                    <span className="text-sm font-semibold text-blue-400">🔵 {s.sector}</span>
                    <span className="text-gray-500 text-xs font-mono">{s.etf}</span>
                  </div>
                  {s.error && <p className="text-gray-500 text-xs">Unavailable — {s.error}</p>}
                  {!s.error && s.candidates.length === 0 && (
                    <p className="text-gray-600 text-xs">Top RS names in this sector aren't in a pullback zone today.</p>
                  )}
                  {!s.error && s.candidates.map(c => (
                    <SrpsCandidateRow key={c.ticker} c={c} />
                  ))}
                </div>
              ))}
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default function SectorRotationTab({ sectorRotation, sectorRotationError, onRetry, onScanForSector }) {
  // Destructure size rotation fields (may be absent on old cached response)
  const sizeRotation = sectorRotation?.size_rotation;
  const sizeSignal = sectorRotation?.size_signal || 'Neutral';
  const sizeSignalDetail = sectorRotation?.size_signal_detail || '';
  const macroAlignment = sectorRotation?.macro_alignment || null;
  const macroAlignmentStatus = sectorRotation?.macro_alignment_status || null;

  // Sort sectors by RS Ratio magnitude (rank). This ordering still drives the
  // "RS Rank" badge and picking the strongest sector within a quadrant, but no
  // longer drives which sector is called out as "best" or which position a
  // card renders in — see pickBestSector() and the quadrant-grouped grid below.
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

  // Best actionable sector — Leading first, Improving as fallback. Replaces
  // the old "highest RS Ratio regardless of quadrant" pick, which could (and
  // did) surface a Weakening sector as the top CTA.
  const { sector: bestSector, tier: bestTier } = useMemo(
    () => pickBestSector(sortedSectors),
    [sortedSectors]
  );

  // One-line plain-English summary shown above the grid.
  const takeaway = useMemo(() => buildTakeaway(sortedSectors, summary), [sortedSectors, summary]);

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

  // Error state — data fetch failed (e.g. yfinance down). Shown instead of a
  // silent/stuck loading spinner, per Golden Rule "silent fallbacks are invisible lies".
  if (sectorRotationError) {
    return (
      <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6 text-red-200">
        <p className="font-semibold">⚠️ Failed to load sector rotation data</p>
        <p className="text-sm mt-1 text-red-300">{sectorRotationError}</p>
        {onRetry && (
          <button
            onClick={onRetry}
            className="mt-3 px-3 py-1.5 bg-red-700 hover:bg-red-600 rounded text-sm"
          >
            Retry
          </button>
        )}
      </div>
    );
  }

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

          {/* Primary CTA — the actually-favorable sector (Leading, or Improving as
              fallback), not just whichever sector has the highest RS Ratio number */}
          <button
            onClick={() => bestSector && onScanForSector(bestSector)}
            disabled={!bestSector}
            className={`px-5 py-2.5 rounded-lg font-semibold text-sm transition-colors ${
              bestTier === 'Leading'
                ? 'bg-green-600 hover:bg-green-500 text-white'
                : 'bg-blue-600 hover:bg-blue-500 text-white'
            } disabled:opacity-40 disabled:cursor-not-allowed`}
          >
            {bestSector
              ? `🔍 Scan Top Sector: ${bestSector.name} (${bestTier})`
              : '🔍 No leading sector right now'}
          </button>
        </div>

        {/* Plain-English takeaway — the "so what," stated before the grid */}
        <p className="text-gray-300 text-sm mt-3">{takeaway}</p>

        {/* Macro alignment — connects this tab to the Context tab's macro
            regime read, so "does the macro backdrop support this rotation?"
            is answered here instead of requiring a manual cross-check
            against a separate tab. Absent on old cached responses (backend
            added the field later) — render nothing rather than a stale/empty
            line, same defensive pattern as size_rotation below. */}
        {macroAlignment && (
          <p className={`text-sm mt-2 ${ALIGNMENT_STYLES[macroAlignmentStatus] || ALIGNMENT_STYLES.neutral}`}>
            {ALIGNMENT_ICONS[macroAlignmentStatus] || 'ℹ️'} {macroAlignment}
          </p>
        )}

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
        &nbsp;Sectors below are grouped by quadrant (most tradeable first) — the "RS Ratio" number on each card is how far above/below SPY it's run over the lookback; it's a separate, secondary stat, not a ranking, so a high value doesn't override the quadrant call.
      </div>

      {/* Sector cards grouped by quadrant — Leading first (most tradeable),
          Lagging last. Replaces the old flat RS-Ratio-rank order, which put
          the highest-magnitude sector first regardless of whether it was
          actually favorable. */}
      {QUADRANT_ORDER.map(q => {
        const list = sortedSectors.filter(s => s.quadrant === q);
        if (list.length === 0) return null;
        const qc = QUADRANT_CONFIG[q];
        return (
          <div key={q} className="mb-6">
            <div className="flex items-baseline gap-2 mb-3">
              <span className={`text-sm font-semibold ${qc.color}`}>{qc.icon} {q}</span>
              <span className="text-gray-500 text-xs">({list.length}) — {qc.sectionHint}</span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
              {list.map(sector => (
                <SectorCard
                  key={sector.etf}
                  sector={sector}
                  onScanForSector={onScanForSector}
                />
              ))}
            </div>
          </div>
        );
      })}

      {/* Sub-Industry Watch — Tier 2, collapsed by default, lazy-loaded */}
      <SubIndustryWatchSection />

      {/* SRPS Pullback Screener — discretionary screen, not a forward-test track (Day 102) */}
      <SrpsPullbackScreenSection />

      {/* Footer note */}
      <div className="mt-6 text-center text-xs text-gray-600">
        Data from yfinance · RS Ratio: 100 = flat vs SPY over the lookback, &gt;100 = outperformed since then · Momentum: positive = gaining, negative = fading · Cached per trading day
      </div>
    </div>
  );
}
