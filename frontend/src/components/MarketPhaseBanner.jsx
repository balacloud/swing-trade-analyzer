// MarketPhaseBanner.jsx — N4 Market Phase Synthesis (Day 76 research, Day 87 build)
// Context Tab banner: SPY trend + VIX level -> one of 5 phases, with
// breadth/sector leadership shown as supporting evidence, not a gate.
// Purely informational — zero impact on verdicts.

const PHASE_STYLES = {
  'Bull Rally': {
    bg: 'bg-green-900/40 border-green-600',
    text: 'text-green-300',
    icon: '🟢',
  },
  'Late Bull': {
    bg: 'bg-lime-900/30 border-lime-600',
    text: 'text-lime-300',
    icon: '🟡',
  },
  'Distribution': {
    bg: 'bg-orange-900/30 border-orange-600',
    text: 'text-orange-300',
    icon: '🟠',
  },
  'Correction': {
    bg: 'bg-red-900/40 border-red-700',
    text: 'text-red-300',
    icon: '🔴',
  },
  'Recovery': {
    bg: 'bg-blue-900/30 border-blue-600',
    text: 'text-blue-300',
    icon: '🔵',
  },
};

function fmtPct(v) {
  if (v == null) return 'N/A';
  return `${v > 0 ? '+' : ''}${v}%`;
}

export default function MarketPhaseBanner({ data, loading, error }) {
  if (loading) {
    return (
      <div className="rounded-lg border border-gray-700 bg-gray-800/50 p-4 mb-4 text-sm text-gray-500">
        ⏳ Loading market phase…
      </div>
    );
  }

  if (error || !data || data.error) {
    return null; // Informational-only feature — fail silent, don't block the tab
  }

  const { phase, description, signals } = data;
  const s = PHASE_STYLES[phase] || PHASE_STYLES['Late Bull'];

  return (
    <div className={`rounded-lg border p-4 mb-4 ${s.bg}`}>
      <div className="flex items-center justify-between flex-wrap gap-2">
        <div>
          <div className={`text-lg font-bold ${s.text}`}>
            {s.icon} MARKET PHASE: {phase.toUpperCase()}
          </div>
          <div className="text-gray-400 text-sm mt-0.5">{description}</div>
        </div>
        <div className="text-xs text-gray-500">
          {data.cached ? 'cached' : 'live'} · as of {data.asOf}
        </div>
      </div>

      {signals && (
        <div className="mt-3 grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
          <div className="bg-gray-800/50 rounded px-2 py-1.5">
            <div className="text-gray-500">SPY vs 200SMA</div>
            <div className="text-gray-200 font-mono">
              {signals.spy.aboveSma200 ? 'Above' : 'Below'} · {fmtPct(signals.spy.pctChange20d)} (20d)
            </div>
          </div>
          <div className="bg-gray-800/50 rounded px-2 py-1.5">
            <div className="text-gray-500">VIX</div>
            <div className="text-gray-200 font-mono">
              {signals.vix.current} ({signals.vix.levelBucket.toLowerCase()}) · {fmtPct(signals.vix.pctChange10d)} (10d)
            </div>
          </div>
          <div className="bg-gray-800/50 rounded px-2 py-1.5">
            <div className="text-gray-500">Breadth (RSP/SPY)</div>
            <div className="text-gray-200 font-mono">{signals.breadth.label}</div>
          </div>
          <div className="bg-gray-800/50 rounded px-2 py-1.5">
            <div className="text-gray-500">Sector Leadership</div>
            <div className="text-gray-200 font-mono">{signals.sectors.label}</div>
          </div>
        </div>
      )}
    </div>
  );
}
