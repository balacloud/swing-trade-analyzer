// AutomatedPaperTradingPanel.jsx — Day 87
// Read-only status + manual trigger for the automated paper-trading engine
// (backend/paper_trading/, built Day 81 — runs unattended daily via launchd).
// Deliberately separate from the manual Forward Test journal above it on
// this tab: that one is a user-entered localStorage log; this one is the
// zero-human-filtering engine that's the real gate on capital allocation.

import { useState, useEffect, useCallback } from 'react';
import { fetchPaperTradingStatus, triggerPaperTradingRun } from '../services/api';

const STALE_DAYS = 3;

function daysSince(dateStr) {
  if (!dateStr) return null;
  const then = new Date(dateStr + 'T00:00:00');
  const now = new Date();
  return Math.floor((now - then) / (1000 * 60 * 60 * 24));
}

function fmtPrice(p) {
  return p != null ? `$${Number(p).toFixed(2)}` : '—';
}

function fmtPct(p) {
  return p != null ? `${p > 0 ? '+' : ''}${Number(p).toFixed(2)}%` : '—';
}

// Day 92: per-position detail table — ticker/entry/exit, so "what actually
// happened" is visible without querying the DB directly. Same status/
// entry/exit columns regardless of lifecycle stage; blank cells for
// fields that don't apply yet (pending has no entry, open has no exit).
function PositionsTable({ positions }) {
  const rows = [
    ...positions.open.map(p => ({ ...p, _bucket: 'open' })),
    ...positions.pending.map(p => ({ ...p, _bucket: 'pending' })),
    ...positions.closed.map(p => ({ ...p, _bucket: 'closed' })),
  ];
  if (rows.length === 0) {
    return <div className="text-xs text-gray-500 py-2">No positions yet.</div>;
  }
  return (
    <div className="overflow-x-auto mt-2">
      <table className="w-full text-xs">
        <thead>
          <tr className="text-gray-500 text-left border-b border-gray-700">
            <th className="py-1 pr-3">Ticker</th>
            <th className="py-1 pr-3">Status</th>
            <th className="py-1 pr-3">Entry</th>
            <th className="py-1 pr-3">Exit</th>
            <th className="py-1 pr-3">Result</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((p, i) => (
            <tr key={`${p.ticker}-${p._bucket}-${i}`} className="border-b border-gray-800">
              <td className="py-1 pr-3 text-white font-medium">{p.ticker}</td>
              <td className="py-1 pr-3">
                <span className={
                  p._bucket === 'open' ? 'text-blue-400' :
                  p._bucket === 'pending' ? 'text-gray-400' :
                  p.result === 'win' ? 'text-green-400' : p.result === 'loss' ? 'text-red-400' : 'text-gray-400'
                }>
                  {p._bucket === 'pending' ? 'pending' : p._bucket === 'open' ? 'open' : (p.result || 'closed')}
                </span>
              </td>
              <td className="py-1 pr-3 text-gray-300">
                {p.entryDate ? `${p.entryDate} @ ${fmtPrice(p.entryPrice)}` : `signal @ ${fmtPrice(p.signalPrice)}`}
              </td>
              <td className="py-1 pr-3 text-gray-300">
                {p.exitDate ? `${p.exitDate} @ ${fmtPrice(p.exitPrice)}` : '—'}
              </td>
              <td className="py-1 pr-3">
                {p.pnlPct != null ? (
                  <span className={p.pnlPct >= 0 ? 'text-green-400' : 'text-red-400'}>{fmtPct(p.pnlPct)}</span>
                ) : '—'}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function SystemCard({ name, label, data }) {
  const [expanded, setExpanded] = useState(false);
  if (!data) return null;
  const stats = data.stats;
  const totalPositions = (data.positions?.open?.length || 0)
    + (data.positions?.pending?.length || 0)
    + (data.positions?.closed?.length || 0);
  return (
    <div className="bg-gray-700/40 rounded-lg p-4">
      <div className="text-sm font-semibold text-gray-300 mb-2">{label}</div>
      <div className="flex gap-6 text-xs">
        <div>
          <div className="text-gray-500">Open</div>
          <div className="text-lg font-bold text-blue-400">{data.openPositions}</div>
        </div>
        <div>
          <div className="text-gray-500">Closed</div>
          <div className="text-lg font-bold text-white">{data.closedTrades}</div>
        </div>
        {stats && (
          <>
            <div>
              <div className="text-gray-500">Win Rate</div>
              <div className={`text-lg font-bold ${stats.win_rate >= 50 ? 'text-green-400' : 'text-yellow-400'}`}>
                {stats.win_rate}%
              </div>
            </div>
            <div>
              <div className="text-gray-500">Profit Factor</div>
              <div className={`text-lg font-bold ${stats.profit_factor >= 1 ? 'text-green-400' : 'text-red-400'}`}>
                {stats.profit_factor}
              </div>
            </div>
            <div>
              <div className="text-gray-500">Expectancy</div>
              <div className={`text-lg font-bold ${stats.expectancy_pct >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                {stats.expectancy_pct > 0 ? '+' : ''}{stats.expectancy_pct}%
              </div>
            </div>
          </>
        )}
      </div>
      {stats?.warnings?.length > 0 && (
        <div className="mt-2 text-xs text-yellow-500">{stats.warnings[0]}</div>
      )}
      {data.closedTrades === 0 && data.openPositions === 0 && (
        <div className="mt-2 text-xs text-gray-500">No closed trades yet</div>
      )}
      {data.positions && totalPositions > 0 && (
        <>
          <button
            onClick={() => setExpanded(e => !e)}
            className="mt-3 text-xs text-purple-400 hover:text-purple-300"
          >
            {expanded ? '▾ Hide tickers' : `▸ Show tickers (${totalPositions})`}
          </button>
          {expanded && <PositionsTable positions={data.positions} />}
        </>
      )}
    </div>
  );
}

export default function AutomatedPaperTradingPanel() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);
  const [triggering, setTriggering] = useState(false);
  const [triggerResult, setTriggerResult] = useState(null);
  const [error, setError] = useState(null);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchPaperTradingStatus();
      if (!data || data.error) throw new Error(data?.error || 'Failed to load status');
      setStatus(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { load(); }, [load]);

  const handleTrigger = async () => {
    setTriggering(true);
    setTriggerResult(null);
    setError(null);
    try {
      const { summary } = await triggerPaperTradingRun();
      setTriggerResult(summary);
      await load();
    } catch (e) {
      setError(e.message);
    } finally {
      setTriggering(false);
    }
  };

  const staleDays = daysSince(status?.lastRunDate);
  const isStale = staleDays != null && staleDays > STALE_DAYS;

  return (
    <div className="bg-gray-800 rounded-lg p-6 mb-6 border border-gray-700">
      <div className="flex justify-between items-center mb-1">
        <h3 className="text-lg font-semibold text-purple-400">🤖 Automated Paper Trading Engine</h3>
        <button
          onClick={handleTrigger}
          disabled={triggering}
          className="px-4 py-2 bg-purple-600 hover:bg-purple-700 disabled:bg-gray-600 disabled:cursor-not-allowed rounded-lg text-white text-sm font-medium transition-colors"
        >
          {triggering ? 'Running… (10-30s)' : 'Force Run Now'}
        </button>
      </div>
      <p className="text-xs text-gray-500 mb-4">
        Runs automatically every weekday at 16:30 CT — zero human filtering, this is the real gate on capital allocation.
        Use "Force Run" if a scheduled run was missed (e.g. laptop asleep). Catches up open positions; can't
        retroactively recover a missed day's entry signals (TradingView has no point-in-time query).
      </p>

      {loading && !status ? (
        <div className="text-gray-500 text-sm py-4 text-center">Loading…</div>
      ) : error ? (
        <div className="text-red-400 text-sm bg-red-900/20 border border-red-700 rounded px-3 py-2">
          ⚠️ {error}
        </div>
      ) : status ? (
        <>
          <div className={`text-xs mb-3 ${isStale ? 'text-red-400' : 'text-gray-500'}`}>
            Last run: {status.lastRunDate || 'never'}
            {isStale && ` — ⚠️ ${staleDays} days ago, likely missed a scheduled run`}
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <SystemCard label="Momentum" data={status.systems?.momentum} />
            <SystemCard label="Mean-Reversion" data={status.systems?.mr} />
          </div>
          {triggerResult && (
            <div className="mt-3 text-xs text-gray-400 bg-gray-700/30 rounded px-3 py-2">
              Run complete: activated {triggerResult.activated}, closed {triggerResult.closed},
              still open {triggerResult.still_open}, queued {triggerResult.queued_momentum} momentum
              + {triggerResult.queued_mr} MR signals.
            </div>
          )}
        </>
      ) : null}
    </div>
  );
}
