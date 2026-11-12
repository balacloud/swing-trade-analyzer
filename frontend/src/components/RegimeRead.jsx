/**
 * RegimeRead — Market backdrop band at the top of the Analyze page.
 * Step 4 (Day 123) built it from the engine's Favorable/Neutral/Unfavorable
 * call; Step 7 (Day 124, user decision) replaced that with facts only:
 * long-term (200-day) and short-term (50-day) trend for the S&P 500 and the
 * Nasdaq-100, the biggest one-day drop in the last 10 sessions, and VIX.
 * No verdict label, no band colour: the user makes the call.
 * Facts come from describeMarketBackdrop() (utils/marketBackdrop.js).
 */
import React, { useMemo } from 'react';
import { describeMarketBackdrop } from '../utils/marketBackdrop';
import useMissingInputWarning from '../hooks/useMissingInputWarning';

const fmtDate = (iso, withYear = false) => {
  if (!iso) return '';
  const d = new Date(`${iso}T12:00:00`);
  return d.toLocaleDateString('en-US', withYear
    ? { month: 'short', day: 'numeric', year: 'numeric' }
    : { month: 'short', day: 'numeric' });
};
const fmtPct = (v) => `${v > 0 ? '+' : ''}${v.toFixed(1)}%`;

function TrendCell({ line }) {
  if (line.state !== 'ok') return <span className="text-gray-500 italic">not enough history</span>;
  return (
    <span className={line.above ? 'text-green-400' : 'text-red-400'}>
      {line.above ? '↑ above' : '↓ below'} <span className="tabular-nums">{fmtPct(line.pct)}</span>
    </span>
  );
}

function DropCell({ drop }) {
  if (drop.state === 'no_down_day') return <span className="text-gray-300">no down day in the last 10 sessions</span>;
  if (drop.state !== 'drop') return <span className="text-gray-500 italic">not enough history</span>;
  return (
    <span className="text-gray-200">
      <span className="tabular-nums text-red-400">{drop.pct.toFixed(1)}%</span> on {fmtDate(drop.date)}
      <span className="text-gray-400">
        {drop.since
          ? ` (largest since ${fmtDate(drop.since, true)})`
          : drop.searchedFrom
            ? ` (largest in data back to ${fmtDate(drop.searchedFrom, true)})`
            : ''}
      </span>
    </span>
  );
}

const COLS = 'sm:grid sm:grid-cols-[8.5rem_1fr_1fr_2fr] sm:gap-x-3';
const MobileLabel = ({ children }) => <span className="sm:hidden text-gray-500 text-xs mr-2">{children}</span>;

export default function RegimeRead({ spy, qqq, vix, ticker, onOpenContext }) {
  const b = useMemo(() => describeMarketBackdrop({ spy, qqq, vix }), [spy, qqq, vix]);
  const warnings = b.missing.map(m => `${m} market data missing`);
  useMissingInputWarning('Market', ticker, warnings);

  return (
    <div className="rounded-lg border px-4 py-3 bg-gray-800 border-gray-600">
      <div className="flex justify-between items-start gap-3 flex-wrap">
        <span className="text-sm font-semibold text-gray-200">Market backdrop</span>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-900/40 text-amber-300 shrink-0">
          ◇ INFO · NEVER GATES THIS PAGE
        </span>
      </div>

      {b.allUnavailable ? (
        <p className="text-sm text-gray-400 mt-2 border border-dashed border-gray-600 rounded px-3 py-2">
          Couldn't load market data right now.
        </p>
      ) : (
        <div className="mt-2 text-sm">
          <div className={`hidden ${COLS} text-xs text-gray-500 pb-1 border-b border-gray-700`}>
            <span />
            <span>Long-term (200-day)</span>
            <span>Short-term (50-day)</span>
            <span>Biggest 1-day drop, last 10 sessions</span>
          </div>
          {b.rows.map(row => (
            <div key={row.label} className={`${COLS} py-1.5 border-b border-gray-700/60 last:border-b-0`}>
              <div className="font-medium text-gray-200">
                {row.label}
                {row.state === 'ok' && !b.asOfDate && row.asOfDate && (
                  <span className="text-xs text-gray-500 font-normal"> · {fmtDate(row.asOfDate)} close</span>
                )}
              </div>
              {row.state !== 'ok' ? (
                <div className="sm:col-span-3 text-gray-400 italic border border-dashed border-gray-600 rounded px-2 mt-1 sm:mt-0">
                  couldn't load{row.reason ? ` (${row.reason})` : ''}
                </div>
              ) : (
                <>
                  <div><MobileLabel>Long-term (200-day)</MobileLabel><TrendCell line={row.longTerm} /></div>
                  <div><MobileLabel>Short-term (50-day)</MobileLabel><TrendCell line={row.shortTerm} /></div>
                  <div><MobileLabel>Biggest 1-day drop, last 10 sessions</MobileLabel><DropCell drop={row.drop} /></div>
                </>
              )}
            </div>
          ))}
          <div className="flex justify-between gap-3 flex-wrap text-xs mt-2">
            <span className="text-gray-300">
              {b.vix.state === 'ok'
                ? <>VIX <span className="tabular-nums">{b.vix.value.toFixed(1)}</span>{b.vix.label ? ` · ${b.vix.label}` : ''} <span className="text-gray-500">(latest quote)</span></>
                : <span className="text-gray-400 italic">VIX: couldn't load</span>}
            </span>
            {b.asOfDate && <span className="text-gray-500">Index figures as of {fmtDate(b.asOfDate)} close</span>}
          </div>
          {onOpenContext && (
            <button onClick={onOpenContext} className="mt-1 text-xs text-blue-400 hover:text-blue-300">
              More market context (breadth, sectors, economy) →
            </button>
          )}
        </div>
      )}
    </div>
  );
}
