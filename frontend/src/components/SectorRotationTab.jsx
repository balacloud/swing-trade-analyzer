// SectorRotationTab.jsx — Day 62, v4.24; trimmed to facts Day 126
// RRG chart + one compact table per level (11 sectors, then sub-industry proxies). No verdict wording:
// the corner names and numbers are shown, the user decides.

import React, { useEffect, useMemo, useState } from 'react';
import RrgChart from './RrgChart';
import { fetchSubIndustryRotation, fetchSrpsPullbackScreen, fetchSubIndustryPullbackScreen } from '../services/api';

// Quadrant display: colour + icon only (Day 126: the "most trade-ready / avoid" hints were verdicts).
const QUADRANT_CONFIG = {
  Leading:   { color: 'text-green-400',  icon: '🟢' },
  Improving: { color: 'text-blue-400',   icon: '🔵' },
  Weakening: { color: 'text-yellow-400', icon: '🟡' },
  Lagging:   { color: 'text-red-400',    icon: '🔴' },
};
const QUADRANT_ORDER = ['Leading', 'Improving', 'Weakening', 'Lagging'];

// Size ETF display order: large → mid → small
const SIZE_ORDER = ['QQQ', 'MDY', 'IWM'];

const num = (v, d = 2) => (typeof v === 'number' && Number.isFinite(v) ? v.toFixed(d) : '—');
const signed = (v, d = 2) => (typeof v === 'number' && Number.isFinite(v) ? `${v > 0 ? '+' : ''}${v.toFixed(d)}` : '—');
const arrow = (v) => (typeof v === 'number' && v > 0 ? '↑' : typeof v === 'number' && v < 0 ? '↓' : '→');

// Cap-size strip: three funds against SPY, numbers and corner only.
function SizeRotationStrip({ sizeRotation }) {
  if (!sizeRotation || sizeRotation.length === 0) return null;
  const ordered = SIZE_ORDER.map(etf => sizeRotation.find(s => s.etf === etf)).filter(Boolean);

  return (
    <div className="rounded-lg border border-gray-700 bg-gray-800/50 p-4 mb-6">
      <div className="mb-2">
        <span className="text-gray-300 text-sm font-semibold">📐 Cap Size</span>
        <span className="text-gray-500 text-xs ml-2">Large, mid and small caps against SPY</span>
      </div>
      <div className="grid grid-cols-3 gap-3">
        {ordered.map(s => {
          const q = s.quadrant;
          const qc = QUADRANT_CONFIG[q] || QUADRANT_CONFIG.Lagging;
          return (
            <div key={s.etf} className="bg-gray-800/60 rounded-lg p-3 text-center">
              <div className="text-gray-500 text-xs font-mono">{s.etf}</div>
              <div className="text-gray-300 text-xs mb-1 truncate">{s.name}</div>
              <div className="text-sm font-mono font-semibold text-white">{num(s.rsRatio)}</div>
              <div className="text-xs font-mono text-gray-400">mom {signed(s.rsMomentum)} {arrow(s.rsMomentum)}</div>
              <div className={`text-xs font-medium mt-1 ${qc.color}`}>{qc.icon} {q}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

// One compact table for both levels. rows: {key, name, etf, quadrant, rsRatio, rsMomentum,
// weekChange?, monthChange?, note?, onScan?}. Sorted corner by corner, strongest ratio first.
function RotationTable({ rows, showChanges = false }) {
  const sorted = useMemo(() => [...rows].sort((a, b) => {
    const d = QUADRANT_ORDER.indexOf(a.quadrant) - QUADRANT_ORDER.indexOf(b.quadrant);
    return d !== 0 ? d : (b.rsRatio ?? 0) - (a.rsRatio ?? 0);
  }), [rows]);

  return (
    <div className="bg-gray-800 border border-gray-700 rounded-lg mb-6 overflow-x-auto" data-testid="rotation-table">
      <table className="w-full text-xs sm:text-sm">
        <thead>
          <tr className="text-gray-500 text-xs border-b border-gray-700">
            <th className="text-left font-medium p-2 sm:p-3">Name</th>
            <th className="text-left font-medium p-2 sm:p-3">Corner</th>
            <th className="text-right font-medium p-2 sm:p-3">RS Ratio</th>
            <th className="text-right font-medium p-2 sm:p-3">Momentum</th>
            {showChanges && <th className="hidden sm:table-cell text-right font-medium p-3">1 wk</th>}
            {showChanges && <th className="hidden sm:table-cell text-right font-medium p-3">1 mo</th>}
            <th className="hidden sm:table-cell p-3" />
          </tr>
        </thead>
        <tbody>
          {sorted.map(r => {
            const qc = QUADRANT_CONFIG[r.quadrant] || QUADRANT_CONFIG.Lagging;
            return (
              <tr key={r.key} className="border-b border-gray-700/50 last:border-0">
                <td className="p-2 sm:p-3">
                  <span className="text-white">{r.name}</span>
                  <span className="text-gray-500 text-xs font-mono ml-2">{r.etf}</span>
                  {r.note && <div className="text-yellow-500/80 text-xs">{r.note}</div>}
                  {r.onScan && (
                    <button onClick={r.onScan} className="sm:hidden block text-xs text-blue-400">Scan →</button>
                  )}
                </td>
                <td className={`p-2 sm:p-3 whitespace-nowrap ${qc.color}`}><span className="hidden sm:inline">{qc.icon} </span>{r.quadrant}</td>
                <td className="p-2 sm:p-3 text-right font-mono text-white">{num(r.rsRatio)}</td>
                <td className="p-2 sm:p-3 text-right font-mono text-gray-300">{signed(r.rsMomentum)} {arrow(r.rsMomentum)}</td>
                {showChanges && <td className="hidden sm:table-cell p-3 text-right font-mono text-gray-400">{signed(r.weekChange, 1)}%</td>}
                {showChanges && <td className="hidden sm:table-cell p-3 text-right font-mono text-gray-400">{signed(r.monthChange, 1)}%</td>}
                <td className="hidden sm:table-cell p-3 text-right">
                  {r.onScan && (
                    <button onClick={r.onScan} className="text-xs text-blue-400 hover:text-blue-300 whitespace-nowrap">
                      Scan →
                    </button>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

// Pullback screeners are hidden (Day 126, same pattern as the hidden Forward Test tab):
// they sit on the older sector gates and recommend names. Components stay for a later decision.
const SHOW_PULLBACK_SCREENERS = false;

// Collapsible Tier-2 section, lazy-loaded on first expand (own ~22-ticker
// fetch, slower than the eager-loaded 11 broad sectors above — most sessions
// won't need this every time, so it shouldn't tax every page load, same
// reasoning as Golden Rule 25). State is local to this component since
// nothing else in the app consumes sub-industry data.
function SubIndustryWatchSection({ refreshTrigger }) {
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

  // This component unmounts (and so naturally refetches) whenever the user
  // navigates away from the Sectors tab and back — but while they stay on
  // the tab, `data` is local state that never refetches once loaded (only
  // its own error-state Retry button re-triggers `load()`). So clicking
  // "Refresh Session" or the tab's own new Refresh button while this
  // section is already expanded silently left it showing pre-refresh data,
  // no error, nothing to indicate it hadn't updated — the "not failing
  // loud" version of Golden Rule 31. Discard the stale data on every
  // refresh signal; only re-fetch immediately if the section is currently
  // open, otherwise the next expand's existing `!data` check does it.
  useEffect(() => {
    if (refreshTrigger == null) return;
    setData(null);
    setError(null);
    if (expanded) load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [refreshTrigger]);

  // Resolved clusters as rows (errored ones render in their own strip below).
  // The chart labels each dot with its proxy ETF ticker.
  const resolvedRows = useMemo(() => (data?.clusters || []).filter(c => !c.error && !c.coveredBySector).map(c => ({
    key: c.cluster, name: c.cluster, etf: c.proxy, quadrant: c.quadrant,
    rsRatio: c.rsRatio, rsMomentum: c.rsMomentum, tail: c.tail,
    note: c.shortHistory ? `Short history (${c.weeks ?? '?'} weeks): shorter windows than standard` : null,
  })), [data]);

  const erroredClusters = useMemo(
    () => (data?.clusters || []).filter(c => c.error && !c.coveredBySector),
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
            Each theme is measured by one proxy ETF — one level below the 11 broad sectors above
          </span>
        </div>
        <span className="text-gray-400 text-sm">{expanded ? '▲' : '▼'}</span>
      </button>

      {expanded && (
        <div className="px-4 pb-4">
          {loading && (
            <div className="text-center py-10">
              <div className="text-3xl mb-2">📡</div>
              <p className="text-gray-400 text-sm">Loading sub-industry data — proxy ETFs vs SPY…</p>
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
              <RrgChart sectors={resolvedRows} />
              <RotationTable rows={resolvedRows} />

              {erroredClusters.length > 0 && (
                <div className="mb-5">
                  <div className="text-gray-500 text-xs mb-2">Unavailable this run ({erroredClusters.length}):</div>
                  <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                    {erroredClusters.map(cluster => (
                      <div key={cluster.cluster} className="rounded-lg border-l-4 border-gray-600 bg-gray-800/60 p-3">
                        <span className="text-white text-sm">{cluster.cluster}</span>
                        <span className="text-gray-400 text-xs font-mono ml-2">{cluster.proxy}</span>
                        <p className="text-gray-500 text-xs">Unavailable — {cluster.error}</p>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {data.coveredBySectors && data.coveredBySectors.length > 0 && (
                <div className="text-gray-600 text-xs mb-2">
                  Same fund as a sector row above (not repeated): {data.coveredBySectors.map(c => `${c.cluster} (${c.etf})`).join('; ')}
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
function SrpsPullbackScreenSection({ refreshTrigger }) {
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

  // Same staleness fix as SubIndustryWatchSection above — see its comment.
  useEffect(() => {
    if (refreshTrigger == null) return;
    setData(null);
    setError(null);
    if (expanded) load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [refreshTrigger]);

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

              {data.sectorsCappedFrom && (
                <p className="text-gray-500 text-xs mb-4">
                  {data.sectorsCappedFrom} sectors were Improving today — showing the top {data.improvingSectorCount} by RS Ratio.
                </p>
              )}

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

// Same screener as SrpsPullbackScreenSection above, applied to the 21
// Sub-Industry Watch clusters instead of the 11 broad GICS sectors
// (user-requested extension). One honest difference: the sector-level
// version at least ran through a real, failed, pre-registered backtest
// before shipping as a screener — this sub-industry version has NOT been
// separately backtested at all, it's the already-failed rule set applied
// to a finer, entirely untested universe. The backend's own `disclaimer`
// field says this explicitly; don't soften it here.
function SubIndustryPullbackScreenSection({ refreshTrigger }) {
  const [expanded, setExpanded] = useState(false);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const load = () => {
    setLoading(true);
    setError(null);
    fetchSubIndustryPullbackScreen()
      .then(res => {
        setData(res);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load sub-industry pullback screen:', err);
        setError(err.message || 'Failed to fetch sub-industry pullback screen');
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

  // Same staleness fix as SubIndustryWatchSection/SrpsPullbackScreenSection above.
  useEffect(() => {
    if (refreshTrigger == null) return;
    setData(null);
    setError(null);
    if (expanded) load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [refreshTrigger]);

  return (
    <div className="bg-gray-800/50 border border-gray-700 rounded-lg mb-6">
      <button
        onClick={handleToggle}
        className="w-full flex items-center justify-between p-4 text-left"
      >
        <div>
          <span className="text-white font-semibold text-sm">🔭 Sub-Sector Pullback Screener</span>
          <span className="text-gray-500 text-xs ml-2">
            Discretionary screen, not a signal — same pullback rules as the Sector Pullback Screener above, applied to the 21 Sub-Industry Watch clusters
          </span>
        </div>
        <span className="text-gray-400 text-sm">{expanded ? '▲' : '▼'}</span>
      </button>

      {expanded && (
        <div className="px-4 pb-4">
          {loading && (
            <div className="text-center py-10">
              <div className="text-3xl mb-2">📡</div>
              <p className="text-gray-400 text-sm">Screening sub-industry-improving candidates…</p>
            </div>
          )}

          {!loading && error && (
            <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 text-red-200">
              <p className="font-semibold">⚠️ Failed to load sub-industry pullback screen</p>
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

              {data.clustersCappedFrom && (
                <p className="text-gray-500 text-xs mb-4">
                  {data.clustersCappedFrom} clusters were Improving today — showing the top {data.improvingClusterCount} by RS Ratio.
                </p>
              )}

              {data.improvingClusterCount === 0 && (
                <p className="text-gray-500 text-sm">No sub-industry clusters in the Improving quadrant today — this screen has nothing to show until at least one cluster qualifies.</p>
              )}

              {data.clusters.map(c => (
                <div key={c.cluster} className="mb-5">
                  <div className="flex items-baseline gap-2 mb-2">
                    <span className="text-sm font-semibold text-blue-400">🔵 {c.cluster}</span>
                    <span className="text-gray-500 text-xs font-mono">{c.proxy}</span>
                  </div>
                  {c.error && <p className="text-gray-500 text-xs">Unavailable — {c.error}</p>}
                  {!c.error && c.candidates.length === 0 && (
                    <p className="text-gray-600 text-xs">Top RS names in this cluster aren't in a pullback zone today.</p>
                  )}
                  {!c.error && c.candidates.map(cand => (
                    <SrpsCandidateRow key={cand.ticker} c={cand} />
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

export default function SectorRotationTab({ sectorRotation, sectorRotationError, onRetry, onScanForSector, refreshTrigger, onRefresh, refreshing }) {
  const sizeRotation = sectorRotation?.size_rotation;

  const sortedSectors = useMemo(() => {
    if (!sectorRotation?.sectors) return [];
    return [...sectorRotation.sectors].sort((a, b) => a.rank - b.rank);
  }, [sectorRotation]);

  // Sector rows for the table; "Scan stocks" hands the whole sector object to the Scan tab
  const sectorRows = useMemo(() => sortedSectors.map(sec => ({
    key: sec.etf, name: sec.name, etf: sec.etf, quadrant: sec.quadrant,
    rsRatio: sec.rsRatio, rsMomentum: sec.rsMomentum,
    weekChange: sec.weekChange, monthChange: sec.monthChange,
    note: sec.thinHistory ? 'Short history: shorter windows than standard' : null,
    onScan: () => onScanForSector(sec),
  })), [sortedSectors, onScanForSector]);

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
              Relative strength vs SPY · RRG corners · 11 SPDR sector ETFs
              {lastUpdated && (
                <span className="ml-2 text-gray-500">· Last refreshed {lastUpdated}</span>
              )}
              {onRefresh && (
                <button
                  onClick={onRefresh}
                  disabled={refreshing}
                  title="Force a fresh sector pull — bypasses today's cache, also refreshes Sub-Industry Watch"
                  className="ml-2 text-gray-500 hover:text-gray-300 disabled:opacity-50 disabled:cursor-wait"
                >
                  {refreshing ? '🔄 Refreshing…' : '🔄 Refresh'}
                </button>
              )}
            </p>
          </div>

        </div>
      </div>

      {/* Standard RRG chart with 5-week trails (Day 126) */}
      <RrgChart sectors={sortedSectors} />

      {/* Size Rotation Strip */}
      <SizeRotationStrip sizeRotation={sizeRotation} />

      {/* How to read — one line */}
      <p className="text-xs text-gray-500 mb-3">
        RS Ratio above 100 = stronger than its own 26-week average against SPY. Momentum above 0 = the ratio is rising.
        Corners: Leading (both above), Weakening (ratio above, momentum below), Lagging (both below), Improving (ratio below, momentum above).
      </p>

      <RotationTable rows={sectorRows} showChanges />

      {/* Sub-Industry Watch — Tier 2, collapsed by default, lazy-loaded */}
      <SubIndustryWatchSection refreshTrigger={refreshTrigger} />

      {SHOW_PULLBACK_SCREENERS && <SrpsPullbackScreenSection refreshTrigger={refreshTrigger} />}
      {SHOW_PULLBACK_SCREENERS && <SubIndustryPullbackScreenSection refreshTrigger={refreshTrigger} />}

      {/* Footer note */}
      <div className="mt-6 text-center text-xs text-gray-600">
        Data from yfinance · weekly closes vs SPY · cached per trading day
      </div>
    </div>
  );
}
