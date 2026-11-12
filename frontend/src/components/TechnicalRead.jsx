/**
 * TechnicalRead — "is this stock in a healthy uptrend?" card
 * (Analyze Page Redesign Step 4, Day 123; mockup v0.14).
 *
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP4_PLAN_DAY123.md (Fable-reviewed).
 * Every value comes from an engine function: the read from
 * deriveTechnicalRead(), the tiles from deriveStrongCriteria() (same
 * STRONG_RULE as assessTechnical), the 4 checks from check_trend_template(),
 * timing/volume from technicalReadChecks.js. Entry checks are Info only.
 * Missing inputs are shown as such on the card and logged once to the console.
 */
import React, { useMemo } from 'react';
import { deriveTechnicalRead, deriveStrongCriteria, STRONG_RULE } from '../utils/categoricalAssessment';
import {
  deriveTrendChecks, deriveEntryTiming, deriveEntryVolume, todayInNewYork,
  ENTRY_TIMING_CLOSE_ATR, ENTRY_TIMING_STRETCHED_ATR, TREND_TEMPLATE_MIN_BARS,
} from '../utils/technicalReadChecks';
import {
  getVolumeConfirmationRead, getVolumeDirectionRead, getObvHorizonRead, getEffortVsResultRead,
} from '../utils/volumeThresholds';
import useMissingInputWarning from '../hooks/useMissingInputWarning';

const READ_COLOR = { green: 'text-green-400', yellow: 'text-yellow-400', red: 'text-red-400', gray: 'text-gray-400' };
const money = (v) => (Number.isFinite(v) ? `$${v.toFixed(2)}` : '—');
const signed = (v, d = 1) => (Number.isFinite(v) ? `${v >= 0 ? '+' : '−'}${Math.abs(v).toFixed(d)}%` : '—');

const Mark = ({ pass, na }) => (
  <span className={`inline-block w-4 text-center font-bold ${na ? 'text-gray-500' : pass ? 'text-green-400' : 'text-red-400'}`}>
    {na ? '–' : pass ? '✓' : '✗'}
  </span>
);

const Info = ({ children }) => (
  <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-900/40 text-amber-300 shrink-0">{children}</span>
);

const Why = ({ children }) => (
  <details className="mt-1 text-xs text-gray-400">
    <summary className="cursor-pointer text-blue-400 w-fit">why? ⓘ</summary>
    <div className="mt-1">{children}</div>
  </details>
);

function StrongTiles({ strong }) {
  if (strong.state !== 'ok') {
    return <div className="text-sm text-gray-400">The three Strong checks couldn't be read ({strong.reason}).</div>;
  }
  const { trend, momentum, rs } = strong;
  const rsiPos = momentum.rsi != null ? Math.min(100, Math.max(0, momentum.rsi)) : null;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
      <div className="rounded-lg bg-gray-700/40 border border-gray-700 p-2.5">
        <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold"><Mark pass={trend.pass} na={!trend.available} /> Trend checks</div>
        <div className="font-mono text-gray-100 mt-0.5">{trend.available ? `${trend.count} / ${trend.total}` : 'no data'}</div>
        <div className="flex gap-0.5 mt-1.5">
          {Array.from({ length: trend.total }, (_, i) => (
            <span key={i} className={`h-1.5 flex-1 rounded-sm ${i < trend.count ? 'bg-green-500/70' : 'bg-gray-600'}`} />
          ))}
        </div>
        <div className="text-xs text-gray-400 mt-1">needs {STRONG_RULE.minTrendChecks}+ · the 4 above plus 4 more</div>
      </div>

      <div className="rounded-lg bg-gray-700/40 border border-gray-700 p-2.5">
        <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold"><Mark pass={momentum.pass} /> Momentum (RSI)</div>
        <div className="font-mono text-gray-100 mt-0.5">{momentum.rsiAvailable ? momentum.rsi?.toFixed(1) : 'n/a'}</div>
        <div className="relative h-1.5 mt-1.5 rounded-sm bg-gray-600">
          <span className="absolute inset-y-0 bg-green-500/40" style={{ left: `${STRONG_RULE.rsiMin}%`, width: `${STRONG_RULE.rsiMax - STRONG_RULE.rsiMin}%` }} />
          {momentum.rsiAvailable && rsiPos != null && (
            <span className="absolute -top-0.5 -bottom-0.5 w-0.5 bg-gray-100" style={{ left: `${rsiPos}%` }} />
          )}
        </div>
        <div className="text-xs text-gray-400 mt-1">
          {momentum.rsiAvailable
            ? `needs ${STRONG_RULE.rsiMin}–${STRONG_RULE.rsiMax}`
            : `RSI didn't load; the engine assumed ${momentum.rsi}, which counts as a pass`}
        </div>
      </div>

      <div className="rounded-lg bg-gray-700/40 border border-gray-700 p-2.5">
        <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold"><Mark pass={rs.pass} na={!rs.available} /> vs S&amp;P 500</div>
        <div className="font-mono text-gray-100 mt-0.5">
          {!rs.available ? 'no data'
            : rs.stockReturn != null && rs.spyReturn != null ? `${signed(rs.stockReturn)} vs ${signed(rs.spyReturn)}`
            : `${rs.ratio.toFixed(2)}×`}
        </div>
        <div className="text-xs text-gray-400 mt-1">
          {rs.available ? 'needs to beat it · past year' : "relative strength didn't load, so Strong isn't possible"}
        </div>
      </div>
    </div>
  );
}

function TimingStrip({ timing }) {
  // Strip spans −1.5 to +3.5 ATR around the 21-day EMA.
  const LO = -1.5, HI = 3.5;
  const at = (u) => ((Math.min(HI, Math.max(LO, u)) - LO) / (HI - LO)) * 100;
  const zones = [
    { from: LO, to: 0, cls: 'bg-gray-600/60', label: 'below' },
    { from: 0, to: ENTRY_TIMING_CLOSE_ATR, cls: 'bg-green-600/50', label: 'close' },
    { from: ENTRY_TIMING_CLOSE_ATR, to: ENTRY_TIMING_STRETCHED_ATR, cls: 'bg-green-800/50', label: 'extended' },
    { from: ENTRY_TIMING_STRETCHED_ATR, to: HI, cls: 'bg-amber-700/50', label: 'stretched' },
  ];
  return (
    <div className="mt-6 mb-1">
      <div className="relative h-2.5 rounded-full overflow-visible flex">
        {zones.map((z) => (
          <span key={z.label} className={`h-full ${z.cls} first:rounded-l-full last:rounded-r-full`} style={{ width: `${at(z.to) - at(z.from)}%` }} />
        ))}
        <span className="absolute -top-1.5 -bottom-1.5 w-0.5 bg-gray-300" style={{ left: `${at(0)}%` }} />
        <span className="absolute bottom-4 -translate-x-1/2 whitespace-nowrap text-[10px] text-gray-400" style={{ left: `${at(0)}%` }}>21-day avg</span>
        <span className="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 w-3.5 h-3.5 rounded-full bg-white border-2 border-gray-900" style={{ left: `${at(timing.atrUnits)}%` }} />
      </div>
      <div className="flex text-[10px] text-gray-500 mt-1">
        {zones.map((z) => (
          <span key={z.label} className="text-center" style={{ width: `${at(z.to) - at(z.from)}%` }}>{z.label}</span>
        ))}
      </div>
    </div>
  );
}

function VolumeBars({ volume }) {
  const { bars, avg50 } = volume;
  if (!bars || bars.length === 0) return <div className="text-xs text-gray-500 mt-2">No volume history.</div>;
  const max = Math.max(...bars.map((b) => b.volume), avg50 || 0) || 1;
  return (
    <div className="mt-2">
      <div className="relative h-14 flex items-end gap-[2px]">
        {bars.map((b) => (
          <span
            key={b.date}
            title={`${b.date}: ${b.volume.toLocaleString()}${b.state === 'partial' ? ' (still forming)' : b.state === 'unknown' ? ' (may be incomplete)' : ''}`}
            className={`flex-1 rounded-t-sm ${
              b.state === 'complete' ? (b.up ? 'bg-green-500/50' : 'bg-red-500/50') : 'border border-dashed border-gray-400 bg-transparent'
            }`}
            style={{ height: `${Math.max(2, (b.volume / max) * 100)}%` }}
          />
        ))}
        {avg50 != null && (
          <span className="absolute inset-x-0 border-t border-dashed border-gray-300/70" style={{ bottom: `${(avg50 / max) * 100}%` }} />
        )}
      </div>
      <div className="text-[10px] text-gray-500 mt-1">
        Last {bars.length} days · green up day, red down day · dashed line = 50-day average
        {bars[bars.length - 1]?.state === 'partial' && ' · outlined bar = today, still forming'}
        {bars[bars.length - 1]?.state === 'unknown' && ' · outlined bar = latest, may be incomplete'}
      </div>
    </div>
  );
}

/**
 * The Day 111/112/116 volume read, moved here from the Trade Setup card with
 * its logic unchanged (same helpers, same last-complete-bar guard).
 */
function VolumeDetail({ srData }) {
  const meta = srData?.meta;
  if (!meta || (meta.rvol == null && meta.prevBar?.rvol == null)) return null;
  const barComplete = meta.candle?.barComplete !== false;
  const prevBar = meta.prevBar;
  const effRvol = barComplete ? meta.rvol : (prevBar?.rvol ?? meta.rvol);
  const effChangePct = barComplete ? srData.change : (prevBar?.changePct ?? srData.change);
  const effCloseLocation = barComplete ? meta.candle?.closeLocation : (prevBar?.closeLocation ?? meta.candle?.closeLocation);

  const vol = getVolumeConfirmationRead(effRvol);
  if (!vol) return null;
  const dir = getVolumeDirectionRead({ changePct: effChangePct, closeLocation: effCloseLocation, obvTrend: meta.obv?.trend });
  const obvRead = getObvHorizonRead(meta.obv);
  const atrPct = meta.atr && srData.currentPrice ? (meta.atr / srData.currentPrice) * 100 : null;
  const evr = getEffortVsResultRead({
    rvol: effRvol, changePct: effChangePct, atrPct, closeLocation: effCloseLocation, barComplete, asOf: prevBar?.date,
  });
  // Day 123: a complete last bar is only "Today" if it is dated today (pre-market
  // and weekends it is a past session).
  const lastDate = meta.candle?.date;
  const dayLabel = !barComplete ? `Last session (${prevBar?.date || 'prior day'})`
    : lastDate && lastDate !== todayInNewYork() ? `Last session (${lastDate})`
    : 'Today';

  return (
    <details className="mt-2 text-xs text-gray-400">
      <summary className="cursor-pointer text-blue-400 w-fit">Volume detail</summary>
      <div className="mt-1 space-y-1 text-gray-300">
        <div><span className="font-semibold">{dayLabel}:</span> {vol.text}</div>
        {dir && <div>Lean: {dir.text}</div>}
        {evr && <div>Effort vs. result: {evr.text}</div>}
        {obvRead && <div>Last 20 days: {obvRead.text}</div>}
        <div className="text-gray-500">
          Direction comes from daily bars (day change, where it closed in the day's range, OBV). Daily bars can't show actual
          buy or sell orders, so this is a lean, not a verdict. The effort-vs-result thresholds are first-principles, not backtested.
        </div>
      </div>
    </details>
  );
}

export default function TechnicalRead({ ticker, technical, adxData, rsData, patternsData, price, ema21, priceHistory, srData }) {
  const read = useMemo(() => deriveTechnicalRead(technical, adxData), [technical, adxData]);
  const strong = useMemo(() => deriveStrongCriteria(technical, rsData), [technical, rsData]);
  const trendChecks = useMemo(() => deriveTrendChecks(patternsData, priceHistory?.length ?? null), [patternsData, priceHistory]);
  const timing = useMemo(
    () => deriveEntryTiming({ read: read.read, price, ema21, atr: srData?.meta?.atr }),
    [read.read, price, ema21, srData]
  );
  const volume = useMemo(() => deriveEntryVolume({ priceHistory, srData }), [priceHistory, srData]);

  const missing = [];
  if (trendChecks.state !== 'ok') missing.push(trendChecks.reason === 'short_history' ? `trend template not computed (${trendChecks.bars ?? '?'} bars)` : '/api/patterns returned nothing');
  if (strong.state === 'ok' && !strong.momentum.rsiAvailable) missing.push('RSI missing, engine assumed 50');
  if (strong.state === 'ok' && !strong.consistent) missing.push(`tiles (allPass=${strong.allPass}) disagree with engine read (${technical?.assessment})`);
  if (timing.state === 'unavailable') missing.push(`timing: ${timing.reason}`);
  if (volume.state !== 'ok') missing.push(`volume: ${volume.reason}`);
  if (volume.warnings?.length) missing.push(...volume.warnings);
  useMissingInputWarning('TechnicalRead', ticker, missing);

  const unavailableText = trendChecks.state === 'ok' ? read.plainEnglish
    : trendChecks.reason === 'short_history'
      ? `This stock has under a year of trading history${trendChecks.bars ? ` (${trendChecks.bars} days)` : ''}; the trend checks need ${TREND_TEMPLATE_MIN_BARS}.`
      : "Pattern detection didn't return for this ticker, so the trend checks couldn't run. Try again in a moment.";

  return (
    <div className="bg-gray-800 rounded-lg p-6">
      <div className="flex justify-between items-start gap-3 mb-1">
        <h3 className="text-lg font-semibold text-blue-400">📈 Technical Read</h3>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-gray-700 text-gray-300 shrink-0">⚙ ENGINE</span>
      </div>
      <p className="text-sm text-gray-400 mb-3">About this stock only. The market's mood is in the band above.</p>

      <div className="text-xl font-bold">
        <span className={READ_COLOR[read.color]}>{read.read}</span>
        {read.adxModifier && <span className="text-sm font-normal text-gray-400"> · {read.adxModifier}</span>}
      </div>
      <p className="text-sm text-gray-300 mt-1">{read.read === 'Unavailable' ? unavailableText : read.plainEnglish}</p>

      {strong.state === 'ok' && !strong.consistent && (
        <div className="mt-3 p-2 rounded text-xs bg-amber-900/30 border border-amber-700/50 text-amber-300">
          The three checks below don't match the engine's read. This is a bug; the read above is the engine's answer.
        </div>
      )}

      {trendChecks.state === 'ok' && (
        <div className="mt-4">
          <div className="text-sm font-semibold text-gray-200 mb-1">Is it in an uptrend? <span className="font-normal text-gray-500">· simple averages</span></div>
          <div className="divide-y divide-gray-700/60">
            {trendChecks.checks.map((c) => (
              <div key={c.key} className="py-1.5 flex flex-col sm:flex-row sm:justify-between gap-0.5 sm:gap-3 text-sm">
                <div>
                  <Mark pass={c.pass} /> <span className="text-gray-200">{c.label}</span>
                  <div className="text-xs text-gray-500 ml-5">{c.why}</div>
                </div>
                <div className="text-xs font-mono text-gray-400 ml-5 sm:ml-0 sm:text-right sm:shrink-0">{c.detail}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="mt-4">
        <div className="text-sm font-semibold text-gray-200 mb-2">Strong needs all three</div>
        <StrongTiles strong={strong} />
      </div>

      <div className="mt-5 pt-4 border-t border-gray-700">
        <div className="flex justify-between items-center gap-3 mb-2">
          <span className="text-sm font-semibold text-gray-200">Entry checks</span>
          <Info>◇ INFO ONLY · DOESN'T CHANGE THE READ</Info>
        </div>

        <div className="mb-4">
          <div className="text-sm text-gray-400">Is now a good moment to get in?</div>
          {timing.state === 'ok' ? (
            <>
              <div className={`font-semibold ${timing.good ? 'text-gray-100' : 'text-amber-300'}`}>{timing.answer}</div>
              <TimingStrip timing={timing} />
              <div className="text-xs font-mono text-gray-400">
                {money(timing.price)} vs {money(timing.ema21)} · {signed(timing.pctFromEma)} · {Math.abs(timing.atrUnits).toFixed(1)} ATR {timing.atrUnits >= 0 ? 'above' : 'below'}
              </div>
              <Why>
                {timing.why} Distance is measured in ATR (how much the stock normally moves in a day): within {ENTRY_TIMING_CLOSE_ATR} ATR
                above the line is close, {ENTRY_TIMING_CLOSE_ATR}–{ENTRY_TIMING_STRETCHED_ATR} is a bit extended, more than {ENTRY_TIMING_STRETCHED_ATR} is
                stretched (the edge of a standard Keltner Channel). These cutoffs are common rules of thumb, not tested by STA.
              </Why>
            </>
          ) : timing.state === 'not_shown' ? (
            <div className="text-gray-400">{timing.answer}</div>
          ) : (
            <div className="text-gray-400">Can't tell: {timing.reason}.</div>
          )}
        </div>

        <div>
          <div className="text-sm text-gray-400">Are buyers behind the move?</div>
          {volume.state === 'ok' ? (
            <>
              <div className={`font-semibold ${volume.lean === 'buying' ? 'text-gray-100' : 'text-amber-300'}`}>{volume.answer}</div>
              <div className="flex flex-wrap gap-1.5 mt-1.5">
                {volume.signals.map((s) => (
                  <span key={s.signal} className={`px-2 py-0.5 rounded text-xs ${s.vote > 0 ? 'bg-green-900/40 text-green-300' : s.vote < 0 ? 'bg-red-900/40 text-red-300' : 'bg-gray-700 text-gray-300'}`}>
                    {s.vote > 0 ? '▲' : s.vote < 0 ? '▼' : '•'} {s.text}
                  </span>
                ))}
              </div>
              <div className="text-xs text-gray-400 mt-1">
                {volume.rvol != null ? `${volume.rvol.toFixed(1)}× normal volume` : 'relative volume unavailable'}
                {' · '}
                {volume.lean === 'mixed' ? 'signals disagree' : volume.lean === 'none' ? 'no clear lean' : `${volume.agreeing} of ${volume.voted} agree`}
                {volume.asOf && (volume.lastBar === 'partial' ? ` · from ${volume.asOf}, today's bar is still forming` : ` · from the ${volume.asOf} session`)}
              </div>
              {volume.distribution && (
                <div className="mt-2 p-2 rounded text-xs bg-orange-900/30 border border-orange-700/50 text-orange-300">
                  ⚠️ Heavy volume while On-Balance Volume is falling: big holders may be selling. Not a sell signal, a reason for caution.
                </div>
              )}
            </>
          ) : (
            <div className="text-gray-400">Can't tell: {volume.reason}.</div>
          )}
          <VolumeBars volume={volume} />
          <Why>
            Heavy volume on an up day that closes near its high is what buyer demand looks like (Wyckoff, O'Neil). The three signals are
            the day's change, where it closed in the day's range, and the 20-day On-Balance Volume trend.
          </Why>
          <VolumeDetail srData={srData} />
        </div>
      </div>

      <details className="mt-4 text-xs text-gray-400">
        <summary className="cursor-pointer text-blue-400">How this read was formed</summary>
        <div className="mt-2 space-y-2">
          <p>The read needs three things: the stock passes at least {STRONG_RULE.minTrendChecks} of 8 trend checks, its momentum score (RSI) is
            between {STRONG_RULE.rsiMin} and {STRONG_RULE.rsiMax} (rising but not overheated), and it has done better than the S&amp;P 500 over the past year.</p>
          <p><b className="text-gray-300">Why only 4 checks are shown:</b> the full score uses 8 checks from Mark Minervini's Trend Template. The 4 shown
            are the ones most traders lean on; the other 4 mostly repeat them. If all 4 pass but the read isn't Strong, the tiles show why.</p>
          <p><b className="text-gray-300">"Taking a breather":</b> ADX measures how hard the price is pushing in one direction. Below 20 means it's
            moving sideways right now. In an uptrend that usually means resting, not a broken trend.</p>
          <p><b className="text-gray-300">Slow vs fast averages:</b> the trend checks use simple averages, which don't flip on a few noisy days. The timing
            line uses a fast (exponential) 21-day average. Stops use neither; they're based on ATR.</p>
          <p><b className="text-gray-300">Timing</b> follows the oldest rule in trading: don't chase, buy close to where you'd be proven wrong (Livermore's
            pivotal points, O'Neil's "don't buy extended"). It only shows once the read is Strong or Developing.</p>
        </div>
      </details>
    </div>
  );
}
