// RrgChart.jsx — Day 126. The standard Relative Rotation Graph: each sector is a
// dot, with a 5-week trail showing where it came from. Layout lives in
// utils/rrgChart.js (unit-tested); this file only draws it.
import React from 'react';
import { buildRrgModel, RRG_COLORS } from '../utils/rrgChart';

export default function RrgChart({ sectors }) {
  const m = buildRrgModel(sectors);
  if (m.points.length === 0) return null;
  const { plot } = m;

  return (
    <div className="bg-gray-800 border border-gray-700 rounded-lg p-3 mb-6" data-testid="rrg-chart">
      <svg viewBox={`0 0 ${m.w} ${m.h}`} className="w-full h-auto" role="img"
           aria-label="Sector rotation chart: strength against SPY on the horizontal axis, momentum on the vertical axis">
        {/* quadrant tints */}
        <rect x={m.cx} y={plot.t} width={plot.r - m.cx} height={m.cy - plot.t} fill="#22c55e" opacity="0.07" />
        <rect x={m.cx} y={m.cy} width={plot.r - m.cx} height={plot.b - m.cy} fill="#eab308" opacity="0.07" />
        <rect x={plot.l} y={m.cy} width={m.cx - plot.l} height={plot.b - m.cy} fill="#ef4444" opacity="0.07" />
        <rect x={plot.l} y={plot.t} width={m.cx - plot.l} height={m.cy - plot.t} fill="#3b82f6" opacity="0.07" />
        <line x1={m.cx} y1={plot.t} x2={m.cx} y2={plot.b} stroke="#6b7280" strokeDasharray="4 4" />
        <line x1={plot.l} y1={m.cy} x2={plot.r} y2={m.cy} stroke="#6b7280" strokeDasharray="4 4" />
        <rect x={plot.l} y={plot.t} width={plot.r - plot.l} height={plot.b - plot.t} fill="none" stroke="#374151" />

        {/* corner names */}
        <g fontSize="11" fontWeight="600" fontFamily="monospace">
          <text x={plot.r - 6} y={plot.t + 14} textAnchor="end" fill={RRG_COLORS.Leading} opacity="0.8">LEADING</text>
          <text x={plot.r - 6} y={plot.b - 6} textAnchor="end" fill={RRG_COLORS.Weakening} opacity="0.8">WEAKENING</text>
          <text x={plot.l + 6} y={plot.b - 6} fill={RRG_COLORS.Lagging} opacity="0.8">LAGGING</text>
          <text x={plot.l + 6} y={plot.t + 14} fill={RRG_COLORS.Improving} opacity="0.8">IMPROVING</text>
        </g>

        {/* axis titles */}
        <text x={(plot.l + plot.r) / 2} y={m.h - 8} textAnchor="middle" fontSize="11" fill="#9ca3af">
          Strength vs SPY (RS-Ratio) →
        </text>
        <text transform={`translate(12 ${(plot.t + plot.b) / 2}) rotate(-90)`} textAnchor="middle" fontSize="11" fill="#9ca3af">
          Momentum →
        </text>

        {/* trails, then heads */}
        {m.points.map((p) => {
          const color = RRG_COLORS[p.quadrant] || '#9ca3af';
          const trail = [...p.tail];
          return (
            <g key={`t-${p.etf}`}>
              {trail.length > 1 && (
                <polyline points={trail.map((t) => `${t.x},${t.y}`).join(' ')}
                          fill="none" stroke={color} strokeOpacity="0.45" strokeWidth="1.5" />
              )}
              {trail.slice(0, -1).map((t, i) => (
                <circle key={i} cx={t.x} cy={t.y} r="2" fill={color} opacity="0.5" />
              ))}
            </g>
          );
        })}
        {m.points.map((p) => {
          const color = RRG_COLORS[p.quadrant] || '#9ca3af';
          return (
            <g key={`h-${p.etf}`}>
              <circle cx={p.x} cy={p.y} r="6" fill={color} stroke="#111827" strokeWidth="1.5" />
              <text x={p.x + 9} y={p.labelY} fontSize="11" fontFamily="monospace" fontWeight="600" fill="#e5e7eb">{p.etf}</text>
            </g>
          );
        })}
      </svg>
      <p className="text-gray-500 text-xs mt-1">
        Trail = the last 5 weeks. Built like the Bloomberg / StockCharts rotation chart (weekly, centred on 100), as a close approximation of the standard.
      </p>
    </div>
  );
}
