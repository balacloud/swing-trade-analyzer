// RegimeBanner.jsx — Day 62, v4.24
// Full-width overall macro regime banner for Context Tab

const REGIME_STYLES = {
  FAVORABLE: {
    bg: 'bg-green-900/40 border-green-600',
    text: 'text-green-300',
    icon: '🟢',
    bar: 'bg-green-500',
  },
  NEUTRAL: {
    bg: 'bg-yellow-900/30 border-yellow-600',
    text: 'text-yellow-300',
    icon: '🟡',
    bar: 'bg-yellow-500',
  },
  ADVERSE: {
    bg: 'bg-red-900/40 border-red-700',
    text: 'text-red-300',
    icon: '🔴',
    bar: 'bg-red-500',
  },
};

export default function RegimeBanner({ overall_regime, favorable, neutral, adverse, total }) {
  const regime = overall_regime || 'NEUTRAL';
  const s = REGIME_STYLES[regime] || REGIME_STYLES.NEUTRAL;
  const pct = total > 0 ? Math.round((favorable / total) * 100) : 0;

  return (
    <div className={`rounded-lg border p-4 mb-6 ${s.bg}`}>
      <div className="flex items-center justify-between flex-wrap gap-2">
        <div>
          <div className={`text-lg font-bold ${s.text}`}>
            {s.icon} OVERALL MACRO REGIME: {regime}
          </div>
          <div className="text-gray-400 text-sm mt-0.5">
            {favorable ?? 0} of {total ?? 0} indicators supportive ·{' '}
            {neutral ?? 0} neutral · {adverse ?? 0} adverse
          </div>
        </div>
        <div className="text-xs text-gray-500">
          Sources: FRED · Calendar · Alpha Vantage
        </div>
      </div>
      {/* Progress bar */}
      <div className="mt-3 w-full bg-gray-700 rounded-full h-2">
        <div className={`h-2 rounded-full ${s.bar}`} style={{ width: `${pct}%` }} />
      </div>
    </div>
  );
}
