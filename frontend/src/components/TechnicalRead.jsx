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
import { deriveTechnicalRead, deriveStrongCriteria, STRONG_RULE, ADX_NO_TREND_THRESHOLD } from '../utils/categoricalAssessment';
import {
  deriveTrendChecks, deriveEntryTiming, deriveEntryVolume, todayInNewYork,
  TREND_TEMPLATE_MIN_BARS,
} from '../utils/technicalReadChecks';
import {
  getVolumeConfirmationRead, getVolumeDirectionRead, getObvHorizonRead, getEffortVsResultRead,
} from '../utils/volumeThresholds';
import useMissingInputWarning from '../hooks/useMissingInputWarning';

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
    return <div className="text-sm text-gray-400">The three checks couldn't be read ({strong.reason}).</div>;
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
        <div className="text-xs text-gray-400 mt-1">rule of thumb: {STRONG_RULE.minTrendChecks}+ · the 4 below plus 4 more</div>
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
            ? `rule of thumb: ${STRONG_RULE.rsiMin}–${STRONG_RULE.rsiMax}`
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
          {rs.available ? 'rule of thumb: beat it · past year' : "relative strength didn't load"}
        </div>
      </div>
    </div>
  );
}

// Price against its moving averages, drawn as a ruler of REAL PRICES (Day 126). No verdict colours: the bar is one calm colour and only the
// stretch between the price and the 21-day average is filled. The dot carries the current price; the ticks are the 21, 50 and 200-day averages.
const ROW_GAP = 36;   // px between label rows when two averages sit close together

function TimingRuler({ timing }) {
  const span = timing.hi - timing.lo;
  const at = (v) => ((v - timing.lo) / span) * 100;
  const x = at(timing.price);
  const e = at(timing.ema21);
  // keep the price bubble inside the card at the two ends
  const bubbleShift = x < 12 ? 'translate-x-0' : x > 88 ? '-translate-x-full' : '-translate-x-1/2';
  const bubbleLeft = x < 12 ? '0%' : x > 88 ? '100%' : `${x}%`;
  // labels that would overlap drop to a lower row (a label is about a quarter of a phone-width card)
  const lastX = [];
  const ticks = timing.marks.map((k) => {
    const px = at(k.price);
    let row = lastX.findIndex((lx) => px - lx >= 26);
    if (row < 0) row = lastX.length < 3 ? lastX.length : 0;
    lastX[row] = px;
    return { ...k, px, row };
  });
  const rows = Math.max(...ticks.map((k) => k.row)) + 1;
  return (
    <div className="mt-2 mb-1" data-testid="timing-ruler">
      <div className="relative h-9">
        <span className={`absolute top-0 ${bubbleShift} px-2 py-0.5 rounded-md bg-white text-gray-900 text-xs font-bold whitespace-nowrap shadow`}
          style={{ left: bubbleLeft }} data-testid="timing-price">{money(timing.price)}</span>
        <span className="absolute bottom-0 -translate-x-1/2 border-x-[5px] border-x-transparent border-t-[6px] border-t-white" style={{ left: `${x}%` }} />
      </div>
      <div className="relative h-3 rounded-full overflow-hidden bg-gray-700/50">
        <span className="absolute inset-y-0 bg-sky-800/70" style={{ left: `${Math.min(x, e)}%`, width: `${Math.abs(x - e)}%` }} />
      </div>
      <div className="relative mt-0" style={{ height: 6 + (rows - 1) * ROW_GAP + 34 }}>
        {ticks.map((k) => (
          <div key={k.key} data-testid="timing-tick" data-key={k.key} data-price={k.price.toFixed(2)}>
            <span className="absolute top-0 w-px bg-gray-400" style={{ left: `${k.px}%`, height: 6 + k.row * ROW_GAP }} />
            {/* the label is kept inside the card; the tick above it stays at the true price */}
            <div className="absolute -translate-x-1/2 text-center leading-tight"
              style={{ top: 6 + k.row * ROW_GAP, left: `min(max(${k.px}%, 46px), calc(100% - 46px))` }}>
              <div className={`text-[11px] sm:text-xs font-mono ${k.key === 'ema21' ? 'text-gray-100 font-semibold' : 'text-gray-300'}`}>{money(k.price)}</div>
              <div className="text-[11px] text-gray-500 whitespace-nowrap">{k.caption}</div>
            </div>
          </div>
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

export default function TechnicalRead({ ticker, technical, adxData, rsData, patternsData, price, ema21, sma50, sma200, priceHistory, srData }) {
  const read = useMemo(() => deriveTechnicalRead(technical, adxData), [technical, adxData]);
  const strong = useMemo(() => deriveStrongCriteria(technical, rsData), [technical, rsData]);
  const trendChecks = useMemo(() => deriveTrendChecks(patternsData, priceHistory?.length ?? null), [patternsData, priceHistory]);
  const timing = useMemo(
    () => deriveEntryTiming({ price, ema21, sma50, sma200, atr: srData?.meta?.atr }),
    [price, ema21, sma50, sma200, srData]
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
    <div data-testid="card-technical-read" className="bg-gray-800 rounded-lg p-6">
      <div data-card-head className="flex justify-between items-start gap-3 mb-1">
        <h3 className="text-lg font-semibold text-blue-400">📈 Technical Read</h3>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-gray-700 text-gray-300 shrink-0">⚙ ENGINE</span>
      </div>
      <p data-card-head className="text-sm text-gray-400 mb-3">About this stock only. The market's mood is in the band above.</p>

      <div data-testid="technical-facts">
        <div className="text-sm font-semibold text-gray-200 mb-2">Trend, momentum and strength against the market
          <span className="font-normal text-gray-500"> · common rules of thumb, not tested by STA</span></div>
        {(read.read === 'Unavailable' || trendChecks.state !== 'ok') && <p className="text-sm text-gray-400 mb-2" data-testid="technical-unavailable">{unavailableText}</p>}
        <StrongTiles strong={strong} />
        <div className="text-xs text-gray-400 mt-2" data-testid="technical-adx">
          Trend strength (ADX): {Number.isFinite(read.adx) ? <span className="font-mono text-gray-200">{read.adx.toFixed(1)}</span> : 'not available'}
          {Number.isFinite(read.adx) && ` · ${read.adx < ADX_NO_TREND_THRESHOLD ? 'below 20 usually means it is moving sideways right now' : '20 or more usually means the price is pushing in one direction'}`}
        </div>
      </div>

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

      <div className="mt-5 pt-4 border-t border-gray-700">
        <div className="flex justify-between items-center gap-3 mb-2">
          <span className="text-sm font-semibold text-gray-200">Entry checks</span>
          <Info>◇ INFO ONLY</Info>
        </div>

        <div className="mb-4">
          <div className="text-sm text-gray-400">Price vs its 21-day average</div>
          {timing.state === 'ok' ? (
            <>
              <div className="font-semibold text-gray-100" data-testid="timing-sentence">
                {timing.side === 'at'
                  ? <>{money(timing.price)} is right at its 21-day average ({money(timing.ema21)})</>
                  : <>{money(timing.price)} is {Math.abs(timing.pctFromEma).toFixed(1)}% {timing.side} its 21-day average ({money(timing.ema21)})</>}
              </div>
              <div className="text-xs text-gray-400" data-testid="timing-sub">
                That is {Math.abs(timing.atrUnits).toFixed(1)} of a normal day's move{timing.side === 'at' ? '' : ` ${timing.side} it`}. A normal day's move here is {money(timing.atr)}.
              </div>
              <TimingRuler timing={timing} />
              <Why>
                The 21-day average is the line the stock has hovered around for about a month. A "day's move" is the stock's ATR
                ({money(timing.atr)} here), how far it normally travels in a day, and it is the same number your stop on the Trade Setup
                card uses. The ruler marks the 21, 50 and 200-day averages at their real prices, so you can see how far the price sits from
                each. Closer to the 21-day line usually means a closer stop; well above it means buying after a run. The marks are a
                measuring stick for your own judgment, not signals, and STA has not tested them.
              </Why>
            </>
          ) : (
            <div className="text-gray-400" data-testid="timing-unavailable">Can't tell: {timing.reason}.</div>
          )}
        </div>

        <div>
          <div className="text-sm text-gray-400">Volume behind the move</div>
          {volume.state === 'ok' ? (
            <>
              <div className="font-semibold text-gray-100" data-testid="volume-tally">
                {volume.voted} volume signal{volume.voted === 1 ? '' : 's'}: {[
                  volume.tally.up > 0 && `${volume.tally.up} up`,
                  volume.tally.down > 0 && `${volume.tally.down} down`,
                  volume.tally.flat > 0 && `${volume.tally.flat} flat`,
                ].filter(Boolean).join(', ')}
              </div>
              <div className="flex flex-wrap gap-1.5 mt-1.5">
                {volume.signals.map((s) => (
                  <span key={s.signal} className={`px-2 py-0.5 rounded text-xs ${s.vote > 0 ? 'bg-green-900/40 text-green-300' : s.vote < 0 ? 'bg-red-900/40 text-red-300' : 'bg-gray-700 text-gray-300'}`}>
                    {s.vote > 0 ? '▲' : s.vote < 0 ? '▼' : '•'} {s.text}
                  </span>
                ))}
              </div>
              <div className="text-xs text-gray-400 mt-1">
                {volume.rvol != null ? `${volume.rvol.toFixed(1)}× normal volume` : 'relative volume unavailable'}
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
        <summary className="cursor-pointer text-blue-400">What these numbers are</summary>
        <div className="mt-2 space-y-2">
          <p>The three tiles are common rules of thumb: at least {STRONG_RULE.minTrendChecks} of 8 trend checks pass, RSI is between {STRONG_RULE.rsiMin} and {STRONG_RULE.rsiMax}{' '}
            (rising but not overheated), and the stock has done better than the S&amp;P 500 over the past year. STA has not tested them, and they do not
            predict what happens next. They describe the stock; the decision is yours.</p>
          <p><b className="text-gray-300">Why only 4 checks are listed:</b> the full score uses 8 checks from Mark Minervini's Trend Template. The 4 listed
            are the ones most traders lean on; the other 4 mostly repeat them.</p>
          <p><b className="text-gray-300">Trend strength (ADX):</b> ADX measures how hard the price is pushing in one direction. Below 20 means it's
            moving sideways right now. In an uptrend that usually means resting, not a broken trend.</p>
          <p><b className="text-gray-300">Slow vs fast averages:</b> the trend checks use simple averages, which don't flip on a few noisy days. The price
            ruler uses a fast (exponential) 21-day average. Stops use neither; they're based on ATR.</p>
          <p><b className="text-gray-300">The price ruler</b> shows where the price sits against its 21, 50 and 200-day averages, in real dollars. It follows an old
            trading idea: buying far above the 21-day average means a farther stop (Livermore's pivotal points, O'Neil's "don't buy extended"). It shows for every
            stock and only measures; when to buy is your call.</p>
        </div>
      </details>
    </div>
  );
}
