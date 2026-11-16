// SectorLeaderboard.jsx — Day 126. One ranked list for sectors or themes:
// strength bar centred on 100, momentum arrow, 5-week line, corner pill, and a
// "Moved" note when the corner changed a week ago. Tap a row for the numbers.
// The RRG chart sits behind "Show chart". Row model: utils/leaderboardRows.js (tested).
import React, { useMemo, useState } from 'react';
import { buildLeaderboardRows } from '../utils/leaderboardRows';
import { RRG_COLORS } from '../utils/rrgChart';
import RrgChart from './RrgChart';

const num = (v, d = 2) => (typeof v === 'number' && Number.isFinite(v) ? v.toFixed(d) : '—');
const signed = (v, d = 2) => (typeof v === 'number' && Number.isFinite(v) ? `${v > 0 ? '+' : ''}${v.toFixed(d)}` : '—');
const COLS = 'md:grid md:grid-cols-[minmax(120px,1.3fr)_minmax(150px,2fr)_84px_96px_112px] md:gap-x-3';

function Spark({ points, color }) {
  if (!points) return <div className="h-[30px] w-[92px]" />;
  const last = points[points.length - 1];
  return (
    <svg viewBox="0 0 92 30" className="h-[30px] w-[92px]" aria-hidden="true">
      <polyline points={points.map((p) => p.join(',')).join(' ')} fill="none" stroke={color}
                strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" opacity="0.85" />
      <circle cx={last[0]} cy={last[1]} r="3" fill={color} />
    </svg>
  );
}

function Row({ r, showChanges }) {
  const [open, setOpen] = useState(false);
  const color = RRG_COLORS[r.quadrant] || '#9ca3af';
  const up = r.rsMomentum >= 0;
  const barStyle = r.bar.side === 'right'
    ? { left: '50%', width: `${r.bar.pct}%`, background: color }
    : { right: '50%', width: `${r.bar.pct}%`, background: color };

  return (
    <div className="border-b border-gray-700/60 last:border-0">
      <button type="button" aria-expanded={open} onClick={() => setOpen(o => !o)}
              className={`w-full text-left px-3 py-3 hover:bg-gray-700/30 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 ${COLS} flex flex-col gap-2 md:items-center`}>
        <div className="flex items-start justify-between gap-2 md:block">
          <div>
            <div className="text-white font-semibold text-sm">{r.name}</div>
            <div className="text-gray-500 text-xs font-mono">{r.etf}</div>
            {r.note && <div className="text-yellow-500/80 text-xs mt-0.5">{r.note}</div>}
          </div>
          <span className="md:hidden text-xs font-semibold px-2 py-0.5 rounded-full border whitespace-nowrap" style={{ color, borderColor: color }}>{r.quadrant}</span>
        </div>

        <div>
          <div className="relative h-2.5 rounded-full bg-gray-700">
            <i className="absolute top-0 bottom-0 rounded-full" style={barStyle} />
            <span className="absolute left-1/2 -top-[3px] -bottom-[3px] w-px bg-gray-400/70" />
          </div>
          <div className="text-white font-semibold text-xs mt-1 font-mono">{num(r.rsRatio)}</div>
        </div>

        <div className="flex items-center justify-between md:block">
          <div className="flex items-center gap-1.5 text-sm font-semibold font-mono">
            <span className={up ? 'text-green-400' : 'text-red-400'}>{up ? '▲' : '▼'}</span>
            <span className="text-white">{signed(r.rsMomentum)}</span>
          </div>
          <div className="md:hidden"><Spark points={r.spark} color={color} /></div>
        </div>

        <div className="hidden md:block"><Spark points={r.spark} color={color} /></div>

        <div className="hidden md:block text-right">
          <span className="inline-flex items-center gap-1.5 text-xs font-semibold px-2 py-0.5 rounded-full border whitespace-nowrap" style={{ color, borderColor: color }}>
            <span className="inline-block w-1.5 h-1.5 rounded-full" style={{ background: color }} />{r.quadrant}
          </span>
        </div>

        {r.moved && (
          <div className="text-xs text-gray-400 md:col-span-5 md:text-right">
            Moved: {r.prevCorner} → <b className="text-white">{r.quadrant}</b> this week
          </div>
        )}
      </button>

      {open && (
        <div className="px-3 pb-3 text-xs text-gray-400">
          {r.tail.length > 0 && (
            <div className="flex flex-wrap gap-2 my-2">
              {r.tail.map((t, k) => (
                <div key={k} className="border border-gray-700 rounded-lg px-2.5 py-1.5 text-gray-200 font-mono">
                  {num(t.rs_ratio)}
                  <div className="text-gray-500 text-[11px] font-sans">{k === r.tail.length - 1 ? 'now' : `${r.tail.length - 1 - k} wk ago`}</div>
                </div>
              ))}
            </div>
          )}
          {showChanges && r.weekChange != null && (
            <div>1 week {signed(r.weekChange, 1)}% · 1 month {signed(r.monthChange, 1)}%</div>
          )}
          {r.onScan && (
            <button type="button" onClick={r.onScan}
                    className="mt-2 text-blue-400 hover:text-blue-300 border border-gray-700 rounded-lg px-2.5 py-1.5">
              Scan stocks in {r.name} →
            </button>
          )}
        </div>
      )}
    </div>
  );
}

export default function SectorLeaderboard({ items, showChanges = false }) {
  const rows = useMemo(() => buildLeaderboardRows(items), [items]);
  const [chart, setChart] = useState(false);
  if (rows.length === 0) return null;

  return (
    <div className="mb-6" data-testid="rotation-table">
      <p className="text-xs text-gray-500 mb-2">
        Ranked by strength against SPY. Bar right of the line = stronger than its own recent level, left = weaker.
        Arrow = momentum rising or falling. Line = last 5 weeks. Tap a row for the numbers.
      </p>
      <div className="hidden md:grid grid-cols-[minmax(120px,1.3fr)_minmax(150px,2fr)_84px_96px_112px] gap-x-3 px-3 pb-1 text-[11px] uppercase tracking-wide text-gray-500">
        <span className="col-start-2">Strength</span><span>Momentum</span><span>5 weeks</span><span className="text-right">Corner</span>
      </div>
      <div className="bg-gray-800 border border-gray-700 rounded-lg overflow-hidden">
        {rows.map((r) => <Row key={r.key} r={r} showChanges={showChanges} />)}
      </div>
      <button type="button" onClick={() => setChart(c => !c)}
              className="mt-3 text-xs text-blue-400 hover:text-blue-300 border border-gray-700 rounded-lg px-3 py-1.5">
        {chart ? 'Hide chart' : 'Show chart'}
      </button>
      {chart && <div className="mt-3"><RrgChart sectors={rows} /></div>}
    </div>
  );
}
