// CycleCard.jsx — Day 62, v4.24
// Single cycle/econ indicator card for Context Tab Columns A and B

const REGIME_STYLES = {
  FAVORABLE: {
    border: 'border-green-500',
    bg: 'bg-green-500/10',
    badge: 'bg-green-700/70 text-green-200',
  },
  NEUTRAL: {
    border: 'border-yellow-500',
    bg: 'bg-yellow-500/10',
    badge: 'bg-yellow-700/70 text-yellow-200',
  },
  ADVERSE: {
    border: 'border-red-600',
    bg: 'bg-red-600/10',
    badge: 'bg-red-800/70 text-red-200',
  },
};

export default function CycleCard({ name, icon, value, phase, source, history, regime }) {
  const s = REGIME_STYLES[regime] || REGIME_STYLES.NEUTRAL;

  return (
    <div className={`rounded-lg border-l-4 ${s.border} ${s.bg} bg-gray-800 p-3`}>
      <div className="flex items-center justify-between mb-1">
        <span className="text-white text-sm font-semibold">
          {icon} {name}
        </span>
        <span className={`text-xs font-bold px-2 py-0.5 rounded ${s.badge}`}>
          {regime}
        </span>
      </div>
      <div className="text-gray-200 text-sm font-mono mb-1">{value || 'N/A'}</div>
      {phase && <div className="text-gray-400 text-xs mb-1">{phase}</div>}
      {history && (
        <div className="text-gray-500 text-xs border-t border-gray-700 pt-1 mt-1">
          📊 {history}
        </div>
      )}
      {source && (
        <div className="text-gray-600 text-xs mt-0.5">{source}</div>
      )}
    </div>
  );
}
