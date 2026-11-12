/**
 * FundamentalsRead — "is the business behind the stock in trouble?"
 * (Analyze Page Redesign Step 6, Day 123; mockup v0.14).
 *
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP6_PLAN_DAY123.md (Fable-reviewed).
 * Facts, not a score: three red-flag checks from screenFundamentalRedFlags()
 * (thresholds from RED_FLAG_THRESHOLDS), a P/E guide that is never a flag,
 * and the next earnings date. Info only; gates nothing. A failed feed reads
 * "Can't check", never "No red flags".
 */
import React, { useMemo } from 'react';
import { screenFundamentalRedFlags, RED_FLAG_THRESHOLDS } from '../utils/categoricalAssessment';
import { describePE, describeEarnings, detectEtf, revenueBasis, describeSources, PE_GUIDE_BANDS, PE_EXTREME } from '../utils/fundamentalsRead';
import { EARNINGS_WARNING_DAYS } from '../services/api';
import useMissingInputWarning from '../hooks/useMissingInputWarning';

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);
const signedPct = (v) => `${v >= 0 ? '+' : '−'}${Math.abs(v).toFixed(1)}%`;

function Tile({ label, value, sub, flagged, checked, uncheckedNote = null }) {
  return (
    <div className={`rounded-lg p-2.5 ${checked ? 'bg-gray-700/40 border border-gray-700' : 'border border-dashed border-gray-600'}`}>
      <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold">
        <span className={`font-bold ${!checked ? 'text-gray-500' : flagged ? 'text-amber-400' : 'text-green-400'}`}>
          {!checked ? '–' : flagged ? '⚑' : '✓'}
        </span>{' '}{label}
      </div>
      <div className="font-mono text-gray-100 mt-0.5">{checked ? value : uncheckedNote ? 'not meaningful' : 'no data'}</div>
      <div className="text-xs text-gray-400 mt-0.5">{checked ? sub : uncheckedNote || 'not checked'}</div>
    </div>
  );
}

function PEGuide({ pe }) {
  const d = describePE(pe);
  if (d.state === 'not_reported') {
    return <div className="text-sm text-gray-400">P/E not reported by the data feed.</div>;
  }
  if (d.state === 'negative') {
    return <div className="text-sm text-gray-300">P/E is negative: the company's trailing 12-month earnings are negative.</div>;
  }
  // Strip spans 0-40; anything above is pinned to the right end.
  const pos = Math.min(100, (d.pe / 40) * 100);
  return (
    <div>
      <div className="flex justify-between items-baseline">
        <span className="text-sm text-gray-300">P/E guide</span>
        <span className="font-mono text-gray-100">
          {d.state === 'extreme' ? `>${PE_EXTREME}` : d.pe.toFixed(1)}{' '}
          <span className="font-sans text-xs text-gray-400">{d.band.label}</span>
        </span>
      </div>
      <div className="relative h-2 mt-2 rounded-full flex overflow-visible">
        <span className="h-full bg-gray-600 rounded-l-full" style={{ width: `${(15 / 40) * 100}%` }} />
        <span className="h-full bg-gray-500" style={{ width: `${(10 / 40) * 100}%` }} />
        <span className="h-full bg-gray-600 rounded-r-full" style={{ width: `${(15 / 40) * 100}%` }} />
        <span className="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 w-3 h-3 rounded-full bg-white border-2 border-gray-900" style={{ left: `${pos}%` }} />
      </div>
      <div className="flex text-[10px] text-gray-500 mt-1">
        <span style={{ width: `${(15 / 40) * 100}%` }}>under {PE_GUIDE_BANDS[0].max}</span>
        <span style={{ width: `${(10 / 40) * 100}%` }}>{PE_GUIDE_BANDS[0].max}–{PE_GUIDE_BANDS[1].max}</span>
        <span>{PE_GUIDE_BANDS[1].max}+</span>
      </div>
      <div className="text-xs text-gray-400 mt-1">
        {d.state === 'extreme'
          ? 'Earnings are close to zero, so the ratio is huge and says little.'
          : `Investors pay $${Math.round(d.pe)} for each $1 of yearly profit.`}
        {' '}Context only, never a flag: for swing trades P/E doesn't predict the move (O'Neil); a high P/E mainly means bigger jumps on earnings.
      </div>
    </div>
  );
}

function EarningsRow({ earnings }) {
  const e = describeEarnings(earnings);
  const highlight = e.state === 'soon' || e.state === 'today';
  const text = {
    error: "Couldn't check the earnings calendar.",
    none: 'No earnings date found in the feed.',
    past: `Last date in the feed: ${e.date} (${Math.abs(e.days ?? 0)} day${Math.abs(e.days ?? 0) === 1 ? '' : 's'} ago); no upcoming date listed.`,
    today: `${e.date} · today. The price can jump either way on the report.`,
    soon: `${e.date} · in ${e.days} day${e.days === 1 ? '' : 's'}. Within a week: decide before then whether to hold through the report.`,
    later: `${e.date} · in ${e.days} days. If you'll still hold on that date, the price can jump either way on the report.`,
  }[e.state];
  return (
    <div className={`rounded-lg px-3 py-2 text-sm ${highlight ? 'bg-amber-900/30 border border-amber-700/50 text-amber-200' : 'bg-gray-700/30 border border-gray-700 text-gray-300'}`}>
      <span className="font-semibold">Next earnings</span> · {text}
    </div>
  );
}

export default function FundamentalsRead({ ticker, fundamental, rawFundamentals, earnings, quoteType, name }) {
  const screen = useMemo(() => screenFundamentalRedFlags(fundamental), [fundamental]);
  const etf = detectEtf({ fundamentalAssessment: fundamental?.assessment, quoteType, name });
  const state = etf.etf ? 'not_applicable' : screen.state;
  const data = fundamental?.data || {};
  const basis = revenueBasis(rawFundamentals?.fieldSources);
  const sources = describeSources(rawFundamentals?.fieldSources, rawFundamentals?.source);
  const negativeEquity = isNum(data.debtToEquity) && data.debtToEquity < 0;

  const missing = [];
  if (state === 'unavailable') missing.push('fundamentals feed returned nothing');
  if (state !== 'not_applicable' && state !== 'unavailable' && screen.missing.length) missing.push(`missing: ${screen.missing.join(', ')}`);
  if (describeEarnings(earnings).state === 'error') missing.push('earnings calendar fetch failed');
  if (etf.basis === 'name') missing.push('ETF inferred from name (no quoteType)');
  useMissingInputWarning('Fundamentals', ticker, missing);

  const flagged = (metric) => screen.flags.some((f) => f.metric === metric);
  const checked = (metric) => screen.checked.includes(metric);

  const headline = {
    no_flags: <span className="text-gray-100">No red flags</span>,
    flags: <span className="text-amber-400">⚑ {screen.flags.length} red flag{screen.flags.length === 1 ? '' : 's'}</span>,
    unavailable: <span className="text-gray-300">Can't check</span>,
    not_applicable: <span className="text-gray-300">Not applicable</span>,
  }[state];

  const subline = {
    no_flags: (screen.missing.length || negativeEquity)
      ? `${screen.checked.length - (negativeEquity ? 1 : 0)} of 3 checks ran; none tripped.`
      : 'All 3 checks ran. None tripped.',
    flags: screen.flags.map((f) => ({ revenueGrowth: 'Sales are shrinking.', roe: 'Return on equity is negative.', debtToEquity: 'Debt is heavy.' }[f.metric])).join(' '),
    unavailable: "The fundamentals data didn't come back. This is not the same as \"no flags\".",
    not_applicable: etf.basis === 'name'
      ? "This looks like an ETF from its name. It holds many companies, so there's no single business to check."
      : "This is an ETF. It holds many companies, so there's no single business to check.",
  }[state];

  return (
    <div data-testid="card-fundamentals" className="bg-gray-800 rounded-lg p-6">
      <div data-card-head className="flex justify-between items-start gap-3 mb-1">
        <h3 className="text-lg font-semibold text-blue-400">🏢 Fundamentals</h3>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-900/40 text-amber-300 shrink-0">◇ INFO</span>
      </div>
      <p data-card-head className="text-sm text-gray-400 mb-3">Is the business behind the stock in trouble? Facts, not a score.</p>

      <div className="text-xl font-bold">{headline}</div>
      <p className="text-sm text-gray-300 mt-1">{subline}</p>

      {state !== 'not_applicable' && (
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 mt-4">
          <Tile
            label="Sales"
            checked={state !== 'unavailable' && checked('revenueGrowth')}
            flagged={flagged('revenueGrowth')}
            value={isNum(data.revenueGrowth) ? signedPct(data.revenueGrowth) : ''}
            sub={`flag if falling ${Math.abs(RED_FLAG_THRESHOLDS.revenueGrowthMax)}%+${basis ? ` · ${basis}` : ''}`}
          />
          <Tile
            label="Return on equity"
            checked={state !== 'unavailable' && checked('roe')}
            flagged={flagged('roe')}
            value={isNum(data.roe) ? `ROE ${data.roe.toFixed(1)}%` : ''}
            sub={`flag if below ${RED_FLAG_THRESHOLDS.roeMax}%`}
          />
          <Tile
            label="Debt"
            checked={state !== 'unavailable' && checked('debtToEquity') && !negativeEquity}
            flagged={flagged('debtToEquity')}
            value={isNum(data.debtToEquity) ? `D/E ${data.debtToEquity.toFixed(2)}` : ''}
            sub={`flag if above ${RED_FLAG_THRESHOLDS.debtToEquityMin.toFixed(1)} · weaker signal for banks, utilities, REITs`}
            uncheckedNote={negativeEquity ? `D/E ${data.debtToEquity.toFixed(2)}: negative equity, ratio not meaningful` : null}
          />
        </div>
      )}

      {state !== 'not_applicable' && (
        <div className="mt-4">
          {state === 'unavailable'
            ? <div className="text-sm text-gray-400">P/E comes from the same fundamentals feed, so it is missing too.</div>
            : <PEGuide pe={rawFundamentals?.pe} />}
        </div>
      )}

      <div className="mt-4">
        <EarningsRow earnings={earnings} />
        {state === 'unavailable' && <div className="text-xs text-gray-500 mt-1">Earnings dates come from a separate source, so they can still show.</div>}
      </div>

      {state !== 'not_applicable' && state !== 'unavailable' && (
        <div className="text-xs text-gray-500 mt-3">
          Source: {sources || 'unknown'}. The live fundamentals feed disagrees with STA's backtest data about 40% of
          the time (sales growth most), so this card only flags clear facts and never scores. The three cutoffs haven't been backtested.
        </div>
      )}

      <details className="mt-3 text-xs text-gray-400">
        <summary className="cursor-pointer text-blue-400">How these checks were chosen</summary>
        <div className="mt-2 space-y-2">
          <p><b className="text-gray-300">Sales falling {Math.abs(RED_FLAG_THRESHOLDS.revenueGrowthMax)}% or more:</b> the canon buys growing businesses
            (O'Neil's "A"). Fast-shrinking sales are a real risk over a multi-week hold, even with a clean chart. Depending on the source, the
            number is the latest quarter vs a year ago or the last fiscal year.</p>
          <p><b className="text-gray-300">Negative return on equity:</b> the company lost money relative to its shareholders' equity. A plain fact.
            Companies with negative equity (some heavy buyback names) can show odd ROE even when profitable.</p>
          <p><b className="text-gray-300">Debt/Equity above {RED_FLAG_THRESHOLDS.debtToEquityMin.toFixed(1)}:</b> heavy borrowing. Banks, utilities and
            REITs carry high debt by design, so a flag on those is weaker.</p>
          <p><b className="text-gray-300">Next earnings:</b> O'Neil and Minervini avoid holding a fresh swing trade through a report, because the price
            can gap far past any stop. Highlighted within the app's {EARNINGS_WARNING_DAYS}-day earnings warning window.</p>
          <p><b className="text-gray-300">P/E guide:</b> trailing P/E (price ÷ the last 12 months of earnings). Under 15 is Graham's "cheap", 15–25 is
            typical for the S&amp;P 500, above 25 means the market expects growth. Never a flag.</p>
          <p><b className="text-gray-300">Left out on purpose:</b> earnings growth (O'Neil's "C"). STA's field is a year-over-year rate that swings
            wildly when last year's earnings were tiny, so it misleads as a red flag (Day 119).</p>
        </div>
      </details>
    </div>
  );
}
