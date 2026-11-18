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
  deriveTrendChecks, deriveEntryTiming, deriveEntryVolume, todayInNewYork, gaugeX, pickVolumeBar,
  TREND_TEMPLATE_MIN_BARS,
} from '../utils/technicalReadChecks';
import {
  getVolumeConfirmationRead, getVolumeDirectionRead, getObvHorizonRead, getEffortVsResultRead,
} from '../utils/volumeThresholds';
import { basisLabel } from '../utils/liveQuote';
import { formatMoney, roundMoney } from '../utils/formatMoney';
import useMissingInputWarning from '../hooks/useMissingInputWarning';

const money = (v) => formatMoney(v);
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

function StrongTiles({ strong, historyBars = null, firstDate = null }) {
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
          {rs.available
            // Day 127 (universe run): with under a year of history the "year-ago" price is the first bar, so say the period it really covers
            ? `rule of thumb: beat it · ${Number.isFinite(historyBars) && historyBars < 252 && firstDate ? `since ${firstDate} (under a year of history)` : 'past year'}`
            : "relative strength didn't load"}
        </div>
      </div>
    </div>
  );
}

// Price against its moving averages (Day 126): a GAUGE on top and a LADDER under it. No good/bad colours: each colour only names a line.
// The gauge places the price and the 21, 50 and 200-day averages by how many normal day-moves they are from the 21-day average (the
// distances, not the prices); the ladder gives the real prices, highest first, and is the gauge's legend. Anything beyond the gauge's
// scale is pinned to its edge, marked with an arrow, and its real distance is written out.
const LINE_COLOR = {
  now:    { text: 'text-sky-400',    bg: 'bg-sky-400',    hex: '#38bdf8' },
  ema21:  { text: 'text-amber-400',  bg: 'bg-amber-400',  hex: '#fbbf24' },
  sma50:  { text: 'text-violet-400', bg: 'bg-violet-400', hex: '#a78bfa' },
  sma200: { text: 'text-pink-400',   bg: 'bg-pink-400',   hex: '#f472b6' },
};
const ROW_GAP = 18;          // px between rows of tick labels
const LABEL_MIN_GAP = 17;    // % of the gauge width two labels need between them to share a row
const dm = (u) => `${u >= 0 ? '+' : '−'}${Math.abs(u).toFixed(1)}`;
const upperFirst = (t) => (t ? t.charAt(0).toUpperCase() + t.slice(1) : t);

function TimingGauge({ timing, nowName }) {
  const x = gaugeX(timing.atrUnits);
  const e = gaugeX(0);
  // the price label (above the bar) stays inside the card: left-aligned near the left end, right-aligned near the right end
  const lab = x < 28 ? { cls: 'translate-x-0', left: `${Math.max(0, x - 4)}%` } : x > 72 ? { cls: '-translate-x-full', left: `${Math.min(100, x + 4)}%` } : { cls: '-translate-x-1/2', left: `${x}%` };
  // tick labels that would overlap drop to a lower row; items pinned to the same edge stack on separate rows
  const lastX = [];
  const ticks = timing.marks.map((k) => {
    const px = gaugeX(k.units);
    let row = lastX.findIndex((lx) => px - lx >= LABEL_MIN_GAP);
    if (row < 0) row = lastX.length < 3 ? lastX.length : 0;
    lastX[row] = px;
    return { ...k, px, row };
  });
  const rows = Math.max(0, ...ticks.map((k) => k.row)) + 1;
  const unitTicks = [];
  for (let u = timing.unitsMin; u <= timing.unitsMax; u++) unitTicks.push(u);
  const dir = x <= e ? 'to right' : 'to left';
  const gradient = `linear-gradient(${dir}, ${LINE_COLOR.now.hex}, ${LINE_COLOR.ema21.hex})`;
  const offFacts = [
    timing.priceOff && `the price is beyond the scale (${dm(timing.atrUnits)} day-moves from the 21-day average)`,
    ...timing.marks.filter((k) => k.off).map((k) => `the ${k.name} is beyond the scale (${dm(k.units)} day-moves)`),
  ].filter(Boolean);
  const aria = `Gauge: price ${money(timing.price)} is ${Math.abs(timing.atrUnits).toFixed(1)} day-moves ${timing.side === 'at' ? 'at' : timing.side} the 21-day average.${offFacts.length ? ` Note: ${offFacts.join('; ')}.` : ''}`;
  return (
    <div className="mt-3" data-testid="timing-ruler">
      <div className="px-3" role="img" aria-label={aria}>
        <div className="relative h-7" aria-hidden="true">
          <div className={`absolute top-0 ${lab.cls} whitespace-nowrap text-xs`} style={{ left: lab.left }}>
            <span className="font-bold font-mono text-sky-300" data-testid="timing-price">{money(timing.price)}</span>
            <span className="text-sky-400/80" data-testid="timing-dot-note">{timing.priceOff ? ` ${timing.priceOff === 'low' ? '◂' : '▸'}` : ''} · {Math.abs(timing.atrUnits).toFixed(1)} day-moves {timing.side === 'at' ? 'from it' : timing.side}</span>
          </div>
        </div>
        <div className="relative h-4" aria-hidden="true">
          <div className="absolute inset-x-0 top-[5px] h-[6px] rounded-full bg-gray-700/70" />
          <div className="absolute top-[5px] h-[6px] rounded-full" style={{ left: `${Math.min(x, e)}%`, width: `${Math.abs(x - e)}%`, background: gradient, opacity: 0.85 }} />
          {unitTicks.map((u) => <span key={u} className="absolute top-[3px] h-[10px] w-px bg-gray-500/70" style={{ left: `${gaugeX(u)}%` }} />)}
          {timing.marks.map((k) => (
            <span key={k.key} data-testid="timing-tick" data-key={k.key} data-price={roundMoney(k.price)} data-off={k.off || ''}
              className={`absolute top-0 h-4 w-[3px] -ml-[1.5px] rounded-sm ${LINE_COLOR[k.key].bg}`} style={{ left: `${gaugeX(k.units)}%` }} />
          ))}
          <span className="absolute top-[0px] h-4 w-4 -ml-2 rounded-full bg-sky-400 border-[3px] border-gray-800 shadow-[0_0_0_2px_#38bdf8,0_0_10px_2px_rgba(56,189,248,0.55)]" style={{ left: `${x}%` }} />
        </div>
        <div className="relative" style={{ height: 6 + (rows - 1) * ROW_GAP + 16 }} aria-hidden="true">
          {ticks.map((k) => (
            <div key={k.key} className={`absolute -translate-x-1/2 text-[11px] leading-none whitespace-nowrap font-semibold ${LINE_COLOR[k.key].text}`}
              style={{ top: 6 + k.row * ROW_GAP, left: `min(max(${k.px}%, 30px), calc(100% - 30px))` }}>
              {k.off === 'low' ? '◂ ' : ''}{k.short}{k.off === 'high' ? ' ▸' : ''}{k.off ? <span className="font-normal text-gray-400"> {dm(k.units)}</span> : null}
            </div>
          ))}
        </div>
      </div>
      <div className="text-[11px] text-gray-500 mb-2">Each small tick is one normal day's move. The gauge shows distances; the ladder below has the prices.</div>
      <table className="w-full text-sm border border-gray-700 rounded-md border-separate border-spacing-0 overflow-hidden" data-testid="timing-ladder">
        <thead className="sr-only"><tr><th scope="col">Line</th><th scope="col">Price</th><th scope="col">Price against it</th></tr></thead>
        <tbody>
          {timing.ladder.map((r) => {
            const c = LINE_COLOR[r.key];
            const gap = r.isNow ? '' : Math.abs(r.gapPct ?? 0) < 0.05 ? 'at it' : `${Math.abs(r.gapPct).toFixed(1)}% ${r.gapPct > 0 ? 'above' : 'below'}`;
            return (
              <tr key={r.key} className={r.isNow ? 'bg-sky-500/15' : ''} data-testid={r.isNow ? 'timing-now-row' : 'timing-ladder-row'}
                data-key={r.key} data-price={roundMoney(r.price)} data-gap={r.isNow || r.gapPct == null ? '' : r.gapPct.toFixed(1)}>
                <th scope="row" className={`text-left font-normal py-1.5 pl-2 pr-1 border-t border-gray-700/70 ${r.isNow ? 'font-bold ' + c.text : 'text-gray-300'}`}>
                  <span className={`inline-block align-middle mr-2 ${r.isNow ? 'h-2.5 w-2.5 rounded-full' : 'h-3 w-[3px] rounded-sm'} ${c.bg}`} aria-hidden="true" />
                  <span data-testid={r.isNow ? 'timing-now-name' : undefined}>{r.isNow ? nowName : r.name}</span>
                </th>
                <td className={`py-1.5 pr-2 border-t border-gray-700/70 text-right font-mono tabular-nums ${r.isNow ? 'font-bold text-gray-100' : 'text-gray-200'}`}>{money(r.price)}</td>
                <td className="py-1.5 pr-2 border-t border-gray-700/70 text-right text-xs text-gray-400 tabular-nums whitespace-nowrap">{gap}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
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
  if (!meta || meta.volume?.available === false || (meta.rvol == null && meta.prevBar?.rvol == null)) return null;
  const barComplete = meta.candle?.barComplete !== false;
  const prevBar = meta.prevBar;
  // Day 126: one helper decides which bar's numbers are read; a missing prior-bar number is NOT replaced by today's partial one
  const { rvol: effRvol, changePct: effChangePct, closeLocation: effCloseLocation } = pickVolumeBar(srData);

  const vol = getVolumeConfirmationRead(effRvol);
  if (!vol) return null;
  const dir = getVolumeDirectionRead({ changePct: effChangePct, closeLocation: effCloseLocation, obvTrend: meta.obv?.trend });
  const obvRead = getObvHorizonRead(meta.obv);
  // Day 126: ATR % is measured against the close of the SAME bar the numbers describe (the last complete one while today's forming),
  // not today's live price (SMCI read 0.63x instead of 0.66x of its ATR)
  const atrBasePrice = barComplete ? srData.currentPrice : (prevBar?.close ?? null);
  const atrPct = meta.atr && atrBasePrice ? (meta.atr / atrBasePrice) * 100 : null;
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

export default function TechnicalRead({ ticker, technical, adxData, rsData, patternsData, price, ema21, sma50, sma200, priceHistory, srData, live = null }) {
  const livePrice = live && Number.isFinite(live.price) ? live.price : null;
  const read = useMemo(() => deriveTechnicalRead(technical, adxData), [technical, adxData]);
  const strong = useMemo(() => deriveStrongCriteria(technical, rsData), [technical, rsData]);
  const trendChecks = useMemo(() => deriveTrendChecks(patternsData, priceHistory?.length ?? null), [patternsData, priceHistory]);
  const timing = useMemo(
    () => deriveEntryTiming({ price, ema21, sma50, sma200, atr: srData?.meta?.atr, livePrice }),
    [price, ema21, sma50, sma200, srData, livePrice]
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
        <StrongTiles strong={strong} historyBars={priceHistory?.length ?? null} firstDate={priceHistory?.[0]?.date ?? null} />
        <div className="text-xs text-gray-400 mt-2" data-testid="technical-adx">
          Trend strength (ADX): {Number.isFinite(read.adx) ? <span className="font-mono text-gray-200">{read.adx.toFixed(1)}</span> : 'not available'}
          {Number.isFinite(read.adx) && ` · ${read.adx < ADX_NO_TREND_THRESHOLD ? 'below 20 usually means it is moving sideways right now' : '20 or more usually means the price is pushing in one direction'}`}
        </div>
      </div>

      {trendChecks.state === 'ok' && (
        <div className="mt-4">
          <div className="text-sm font-semibold text-gray-200 mb-1">Is it in an uptrend? <span className="font-normal text-gray-500">· simple averages{livePrice != null && live?.lastClose ? ` · counted at the last close (${money(live.lastClose.price)}${live.lastClose.dateLabel ? `, ${live.lastClose.dateLabel}` : ''})` : ''}</span></div>
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
                {money(timing.price)} <span className="font-normal text-gray-400" data-testid="timing-basis">({timing.basis === 'live' ? basisLabel(live) : 'last close'})</span>
                {timing.side === 'at'
                  ? <> is right at its 21-day average ({money(timing.ema21)})</>
                  : <> is {Math.abs(timing.pctFromEma).toFixed(1)}% {timing.side} its 21-day average ({money(timing.ema21)})</>}
              </div>
              <div className="text-xs text-gray-400" data-testid="timing-sub">
                That is {Math.abs(timing.atrUnits).toFixed(1)} of a normal day's move{timing.side === 'at' ? '' : ` ${timing.side} it`}. A normal day's move here is {money(timing.atr)}.
              </div>
              <TimingGauge timing={timing} nowName={upperFirst(timing.basis === 'live' ? basisLabel(live) : 'last close')} />
              {timing.basis === 'live' && live?.lastClose && (
                <div className="text-xs text-gray-500" data-testid="timing-close-note">
                  Last close {money(live.lastClose.price)}{live.lastClose.dateLabel ? ` · ${live.lastClose.dateLabel}` : ''}
                </div>
              )}
              <Why>
                The 21-day average is the line the stock has hovered around for about a month. A "day's move" is the stock's ATR
                ({money(timing.atr)} here), how far it normally travels in a day, and it is the same number your stop on the Trade Setup
                card uses. The gauge places the price and the 21, 50 and 200-day averages by how many day-moves they sit from the 21-day average,
                and the ladder under it gives their real prices. Closer to the 21-day line usually means a closer stop; well above it means buying after a run. The marks are a
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
          ) : volume.noVolume ? (
            <div className="text-gray-400" data-testid="volume-unavailable">{volume.text}</div>
          ) : (
            <div className="text-gray-400">Can't tell: {volume.reason}.</div>
          )}
          {!volume.noVolume && <VolumeBars volume={volume} />}
          {!volume.noVolume && <Why>
            Heavy volume on an up day that closes near its high is what buyer demand looks like (Wyckoff, O'Neil). The three signals are
            the day's change, where it closed in the day's range, and the 20-day On-Balance Volume trend.
          </Why>}
          {!volume.noVolume && <VolumeDetail srData={srData} />}
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
          <p><b className="text-gray-300">Prices are adjusted for dividends:</b> older prices (and so highs and averages) are lowered for dividends paid, so for a dividend payer they can sit a little below what the chart showed on the day. The 1-year high here and on the Price Data card are the same number.</p>
          <p><b className="text-gray-300">Slow vs fast averages:</b> the trend checks use simple averages, which don't flip on a few noisy days. The price
            gauge uses a fast (exponential) 21-day average. Stops use neither; they're based on ATR.</p>
          <p><b className="text-gray-300">The price gauge and ladder</b> show where the price sits against its 21, 50 and 200-day averages: the gauge in day-moves, the ladder in real dollars. It follows an old
            trading idea: buying far above the 21-day average means a farther stop (Livermore's pivotal points, O'Neil's "don't buy extended"). It shows for every
            stock and only measures; when to buy is your call.</p>
        </div>
      </details>
    </div>
  );
}
