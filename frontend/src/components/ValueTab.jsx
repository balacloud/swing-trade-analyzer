/**
 * ValueTab — Day 75 (Phase 1)
 * Value investing lens: Buffett / Graham / Lynch / Damodaran / Greenblatt.
 * Completely isolated from swing verdict and categorical assessment.
 * Phase 1: ROIC, ROE, Graham Number, FCF Yield, P/E, PEG/PEGY (Finnhub + yfinance).
 * Phase 2 (future): earnings history, interest coverage, EV/EBIT, DCF Lite.
 */

import React, { useState, useEffect } from 'react';
import { fetchValueData } from '../services/api';

// ── Helpers ──────────────────────────────────────────────────────────────────

const VERDICT_STYLES = {
  strong:     { dot: 'bg-emerald-400', text: 'text-emerald-400', label: 'Strong' },
  decent:     { dot: 'bg-amber-400',   text: 'text-amber-400',   label: 'Decent' },
  weak:       { dot: 'bg-rose-400',    text: 'text-rose-400',    label: 'Weak' },
  attractive: { dot: 'bg-emerald-400', text: 'text-emerald-400', label: 'Attractive' },
  fair:       { dot: 'bg-amber-400',   text: 'text-amber-400',   label: 'Fair' },
  stretched:  { dot: 'bg-rose-400',    text: 'text-rose-400',    label: 'Stretched' },
  na:         { dot: 'bg-gray-600',    text: 'text-gray-500',    label: 'N/A' },
  insufficient_data: { dot: 'bg-gray-600', text: 'text-gray-500', label: 'Insufficient data' },
};

function verdictStyle(verdict) {
  return VERDICT_STYLES[verdict] || VERDICT_STYLES.na;
}

function DotsScore({ verdict, total = 5 }) {
  const filled = { strong: 4, attractive: 4, decent: 3, fair: 3, weak: 2, stretched: 1, na: 0, insufficient_data: 0 }[verdict] ?? 0;
  const style = verdictStyle(verdict);
  return (
    <div className="flex gap-1 items-center">
      {Array.from({ length: total }).map((_, i) => (
        <div key={i} className={`w-2.5 h-2.5 rounded-full ${i < filled ? style.dot : 'bg-gray-700'}`} />
      ))}
    </div>
  );
}

function VerdictBadge({ verdict }) {
  const s = verdictStyle(verdict);
  return (
    <span className={`text-xs font-semibold uppercase tracking-wide ${s.text}`}>
      {s.label}
    </span>
  );
}

function NACard({ reason, metric }) {
  const messages = {
    negative_eps:        'Negative EPS — not applicable at this time',
    negative_book_value: 'Negative book value — not applicable',
    data_missing:        'Data not available',
    negative_earnings:   'Company not yet profitable',
  };
  return (
    <div className="bg-gray-800/60 rounded-lg p-3 border border-gray-700/50">
      <div className="text-gray-500 text-sm font-medium mb-1">{metric}</div>
      <div className="text-gray-600 text-xs italic">{messages[reason] || 'N/A'}</div>
      <div className="text-gray-700 text-xs mt-1">Not a negative signal</div>
    </div>
  );
}

// ── Sub-cards ─────────────────────────────────────────────────────────────────

function MetricRow({ label, value, unit = '', subtext, verdict, attribution }) {
  const s = verdictStyle(verdict);
  return (
    <div className="flex items-start justify-between py-2 border-b border-gray-700/40 last:border-0">
      <div>
        <div className="flex items-center gap-2">
          <span className="text-gray-300 text-sm font-medium">{label}</span>
          {attribution && (
            <span className="text-xs px-1.5 py-0.5 rounded bg-gray-700 text-gray-400">{attribution}</span>
          )}
        </div>
        {subtext && <div className="text-gray-500 text-xs mt-0.5">{subtext}</div>}
      </div>
      <div className="text-right ml-4 shrink-0">
        {verdict === 'na' ? (
          <span className="text-gray-600 text-sm">—</span>
        ) : (
          <>
            <div className="text-white text-sm font-semibold">{value}{unit}</div>
            <VerdictBadge verdict={verdict} />
          </>
        )}
      </div>
    </div>
  );
}

function GrahamBar({ grahamValue, currentPrice, pctDiff }) {
  if (!grahamValue || !currentPrice) return null;
  const min = Math.min(grahamValue, currentPrice) * 0.85;
  const max = Math.max(grahamValue, currentPrice) * 1.15;
  const range = max - min;
  const grahamPct = ((grahamValue - min) / range) * 100;
  const pricePct  = ((currentPrice  - min) / range) * 100;
  const overshot  = pctDiff > 0;

  return (
    <div className="mt-3">
      <div className="relative h-1.5 bg-gray-700 rounded-full">
        <div
          className={`absolute h-full rounded-full ${overshot ? 'bg-rose-500/40' : 'bg-emerald-500/40'}`}
          style={{
            left:  `${Math.min(grahamPct, pricePct)}%`,
            width: `${Math.abs(pricePct - grahamPct)}%`,
          }}
        />
        <div
          className="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-3 h-3 rounded-full border-2 border-amber-400 bg-gray-900"
          style={{ left: `${grahamPct}%` }}
          title={`Graham ceiling: $${grahamValue}`}
        />
        <div
          className={`absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-3 h-3 rounded-full border-2 ${overshot ? 'border-rose-400' : 'border-emerald-400'} bg-gray-900`}
          style={{ left: `${pricePct}%` }}
          title={`Current: $${currentPrice}`}
        />
      </div>
      <div className="flex justify-between mt-1.5 text-xs text-gray-500">
        <span className="text-amber-400/80">Ceiling ${ grahamValue}</span>
        <span className={overshot ? 'text-rose-400' : 'text-emerald-400'}>
          {overshot ? '+' : ''}{pctDiff?.toFixed(1)}% {overshot ? 'above' : 'below'}
        </span>
        <span className={overshot ? 'text-rose-400/80' : 'text-emerald-400/80'}>Price ${currentPrice}</span>
      </div>
    </div>
  );
}

// ── Quality column ────────────────────────────────────────────────────────────

function QualityColumn({ quality, meta }) {
  const { roic, roe, fcf_yield, debt_to_equity, profit_margin_pct } = quality;

  return (
    <div className="bg-gray-800 rounded-xl p-4 border border-gray-700">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-amber-400 font-semibold text-sm uppercase tracking-wider">Quality</h3>
        <DotsScore verdict={quality.verdict} />
      </div>

      {/* ROIC */}
      {roic.verdict === 'na' ? (
        <NACard metric="ROIC" reason="data_missing" />
      ) : (
        <MetricRow
          label="ROIC"
          value={roic.value}
          unit="%"
          subtext={`WACC ≈ ${roic.wacc_approx}%  ·  spread ${roic.spread > 0 ? '+' : ''}${roic.spread}pts`}
          verdict={roic.verdict}
          attribution="Damodaran"
        />
      )}

      {/* ROE */}
      {roe.verdict === 'na' ? (
        <NACard metric="ROE (TTM)" reason="data_missing" />
      ) : (
        <MetricRow
          label="ROE"
          value={roe.value}
          unit="%"
          subtext={
            roe.leverage_flag
              ? `⚠️ May be leverage-driven (ROA much lower) · threshold ${roe.threshold}%`
              : `Threshold for ${meta?.cap_size || ''} cap: ${roe.threshold}%`
          }
          verdict={roe.leverage_flag ? 'decent' : roe.verdict}
          attribution="Buffett"
        />
      )}

      {/* FCF Yield */}
      {fcf_yield.verdict === 'na' ? (
        <NACard metric="FCF Yield" reason="data_missing" />
      ) : (
        <MetricRow
          label="FCF Yield"
          value={fcf_yield.value}
          unit="%"
          subtext="Single-year estimate — directional only"
          verdict={fcf_yield.verdict}
          attribution="Damodaran"
        />
      )}

      {/* Supporting data rows */}
      {debt_to_equity != null && (
        <MetricRow
          label="Debt / Equity"
          value={debt_to_equity}
          subtext="Context only — see Net Debt/EBITDA in Phase 2"
          verdict="na"
        />
      )}
      {profit_margin_pct != null && (
        <MetricRow
          label="Net Margin"
          value={profit_margin_pct}
          unit="%"
          subtext="Industry-relative comparison in Phase 2"
          verdict="na"
        />
      )}
    </div>
  );
}

// ── Valuation column ──────────────────────────────────────────────────────────

function ValuationColumn({ valuation }) {
  const { graham_number, pe, peg, dividend_yield_pct } = valuation;

  return (
    <div className="bg-gray-800 rounded-xl p-4 border border-gray-700">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-amber-400 font-semibold text-sm uppercase tracking-wider">Valuation</h3>
        <DotsScore verdict={valuation.verdict} />
      </div>

      {/* Graham Number */}
      <div className="mb-3 pb-3 border-b border-gray-700/40">
        <div className="flex items-center justify-between mb-1">
          <div className="flex items-center gap-2">
            <span className="text-gray-300 text-sm font-medium">Graham Number</span>
            <span className="text-xs px-1.5 py-0.5 rounded bg-gray-700 text-gray-400">Graham</span>
          </div>
          {graham_number.applicable === true && (
            <VerdictBadge verdict={graham_number.verdict === 'below_ceiling' ? 'attractive' : 'stretched'} />
          )}
        </div>

        {graham_number.applicable === true ? (
          <>
            <div className="text-xs text-gray-500 mb-1">
              Ceiling: <span className="text-amber-400">${graham_number.value}</span>
              {graham_number.sector_warning && (
                <span className="ml-2 text-gray-600 italic">
                  · Book value may understate value for this sector
                </span>
              )}
            </div>
            <GrahamBar
              grahamValue={graham_number.value}
              currentPrice={graham_number.current_price}
              pctDiff={graham_number.pct_diff}
            />
          </>
        ) : (
          <div className="text-gray-600 text-xs italic mt-1">
            {graham_number.reason === 'negative_eps' && 'Negative EPS — not applicable at this time'}
            {graham_number.reason === 'negative_book_value' && 'Negative book value — not applicable'}
            {graham_number.reason === 'data_missing' && 'Data not available'}
            {!graham_number.reason && 'Not applicable'}
            <span className="ml-2 text-gray-700">· Not a negative signal</span>
          </div>
        )}
      </div>

      {/* P/E */}
      {pe.verdict === 'na' ? (
        <NACard metric="P/E Ratio" reason={pe.reason || 'data_missing'} />
      ) : (
        <MetricRow
          label="P/E Ratio"
          value={pe.value}
          unit="×"
          subtext="Absolute P/E · sector comparison in Phase 2"
          verdict={pe.verdict}
          attribution="Graham"
        />
      )}

      {/* PEG / PEGY */}
      {peg.verdict === 'na' ? (
        <NACard metric={dividend_yield_pct > 1.5 ? 'PEGY' : 'PEG'} reason="data_missing" />
      ) : (
        <MetricRow
          label={peg.type === 'pegy' ? 'PEGY' : 'PEG'}
          value={peg.value}
          unit="×"
          subtext={`Fair value ≈ 1.0  ·  ${peg.type === 'pegy' ? 'includes dividend yield' : 'growth stocks only'}${peg.source === 'finnhub' ? '' : ' · approximate'}`}
          verdict={peg.verdict}
          attribution="Lynch"
        />
      )}

      {dividend_yield_pct > 0 && (
        <MetricRow
          label="Dividend Yield"
          value={dividend_yield_pct}
          unit="%"
          verdict="na"
        />
      )}
    </div>
  );
}

// ── Investor strip (footer) ───────────────────────────────────────────────────

function InvestorStrip({ data }) {
  const [open, setOpen] = useState(false);
  const { quality, valuation } = data;

  const investors = [
    {
      name: 'Buffett',
      color: 'text-yellow-400',
      bg: 'bg-yellow-900/20',
      border: 'border-yellow-800/30',
      metric: 'ROE',
      value: quality.roe.value != null ? `${quality.roe.value}%` : 'N/A',
      verdict: quality.roe.verdict,
      note: quality.roe.leverage_flag ? 'May be leverage-driven' : null,
    },
    {
      name: 'Graham',
      color: 'text-blue-400',
      bg: 'bg-blue-900/20',
      border: 'border-blue-800/30',
      metric: 'Graham #',
      value: valuation.graham_number.applicable === true
        ? `$${valuation.graham_number.value}`
        : 'N/A',
      verdict: valuation.graham_number.applicable === true
        ? (valuation.graham_number.verdict === 'below_ceiling' ? 'attractive' : 'stretched')
        : 'na',
    },
    {
      name: 'Lynch',
      color: 'text-green-400',
      bg: 'bg-green-900/20',
      border: 'border-green-800/30',
      metric: valuation.peg.type === 'pegy' ? 'PEGY' : 'PEG',
      value: valuation.peg.value != null ? `${valuation.peg.value}×` : 'N/A',
      verdict: valuation.peg.verdict,
    },
    {
      name: 'Damodaran',
      color: 'text-rose-400',
      bg: 'bg-rose-900/20',
      border: 'border-rose-800/30',
      metric: 'ROIC',
      value: quality.roic.value != null ? `${quality.roic.value}%` : 'N/A',
      verdict: quality.roic.verdict,
      note: quality.roic.spread != null ? `${quality.roic.spread > 0 ? '+' : ''}${quality.roic.spread}pts vs WACC` : null,
    },
  ];

  return (
    <div className="mt-4">
      <button
        onClick={() => setOpen(o => !o)}
        className="w-full flex items-center justify-between text-gray-500 hover:text-gray-300 text-xs py-2 transition-colors"
      >
        <span className="uppercase tracking-wider font-medium">Investor Lens Summary</span>
        <span>{open ? '▲' : '▼'}</span>
      </button>

      {open && (
        <div className="grid grid-cols-2 gap-2 mt-2 sm:grid-cols-4">
          {investors.map(inv => {
            const s = verdictStyle(inv.verdict);
            return (
              <div key={inv.name} className={`rounded-lg p-3 border ${inv.bg} ${inv.border}`}>
                <div className={`text-xs font-semibold mb-1 ${inv.color}`}>{inv.name}</div>
                <div className="text-gray-400 text-xs">{inv.metric}</div>
                <div className="text-white text-sm font-semibold mt-0.5">{inv.value}</div>
                <div className={`text-xs mt-0.5 ${s.text}`}>{s.label}</div>
                {inv.note && <div className="text-gray-600 text-xs mt-0.5 italic">{inv.note}</div>}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

// ── Main component ────────────────────────────────────────────────────────────

export default function ValueTab({ ticker }) {
  const [data, setData]       = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState(null);

  useEffect(() => {
    if (!ticker) { setData(null); return; }
    setLoading(true);
    setError(null);
    fetchValueData(ticker)
      .then(d => {
        if (d?.error) setError(d.error);
        else setData(d);
      })
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, [ticker]);

  // ── No ticker selected ──
  if (!ticker) {
    return (
      <div className="flex flex-col items-center justify-center py-20 text-center">
        <div className="text-4xl mb-4">💎</div>
        <h2 className="text-gray-400 text-lg font-medium mb-2">Value Analysis</h2>
        <p className="text-gray-600 text-sm max-w-sm">
          Analyze a stock first, then return here for a Buffett / Graham / Lynch / Damodaran lens.
        </p>
      </div>
    );
  }

  // ── Loading ──
  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center py-20">
        <div className="animate-spin text-3xl mb-4">💎</div>
        <p className="text-gray-400 text-sm">Loading value analysis for {ticker}…</p>
      </div>
    );
  }

  // ── Error ──
  if (error) {
    return (
      <div className="bg-gray-800 rounded-xl p-6 text-center">
        <div className="text-rose-400 font-medium mb-1">Could not load value analysis</div>
        <div className="text-gray-500 text-sm">{error}</div>
      </div>
    );
  }

  if (!data) return null;

  const { overall, cap_size, sector, meta } = data;
  const qStyle = verdictStyle(overall.quality_verdict);
  const vStyle = verdictStyle(overall.valuation_verdict);
  const capLabel = cap_size === 'large' ? 'Large Cap' : cap_size === 'mid' ? 'Mid Cap' : cap_size === 'small' ? 'Small Cap' : '';

  return (
    <div className="max-w-4xl mx-auto space-y-4">

      {/* ── Hero scorecard ── */}
      <div className="bg-gray-800 rounded-xl border border-amber-800/30 overflow-hidden">
        <div className="bg-amber-900/20 px-5 py-3 flex items-center justify-between border-b border-amber-800/20">
          <div>
            <span className="text-amber-400 font-semibold text-sm">💎 Value Analysis</span>
            <span className="text-gray-500 text-sm ml-2">· {ticker}</span>
            {capLabel && <span className="text-gray-600 text-xs ml-2">· {capLabel}</span>}
            {sector && sector !== 'Unknown' && <span className="text-gray-600 text-xs ml-1">· {sector}</span>}
          </div>
          <span className="text-gray-600 text-xs">3–5 year lens</span>
        </div>

        <div className="px-5 py-4">
          <div className="grid grid-cols-2 gap-6 mb-3">
            <div>
              <div className="text-gray-500 text-xs uppercase tracking-wider mb-2">Quality</div>
              <div className="flex items-center gap-3">
                <DotsScore verdict={overall.quality_verdict} />
                <span className={`font-semibold text-sm ${qStyle.text}`}>{qStyle.label}</span>
              </div>
            </div>
            <div>
              <div className="text-gray-500 text-xs uppercase tracking-wider mb-2">Valuation</div>
              <div className="flex items-center gap-3">
                <DotsScore verdict={overall.valuation_verdict} />
                <span className={`font-semibold text-sm ${vStyle.text}`}>{vStyle.label}</span>
              </div>
            </div>
          </div>
          <p className="text-gray-300 text-sm">{overall.summary}</p>
          <p className="text-gray-600 text-xs mt-2 italic">
            ⚠️ This analysis does not affect the swing verdict or categorical assessment.
          </p>
        </div>
      </div>

      {/* ── Two-column grid ── */}
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
        <QualityColumn quality={data.quality} meta={{ cap_size }} />
        <ValuationColumn valuation={data.valuation} />
      </div>

      {/* ── Investor strip ── */}
      <div className="bg-gray-800 rounded-xl p-4 border border-gray-700">
        <InvestorStrip data={data} />
      </div>

      {/* ── Phase note ── */}
      <div className="text-gray-700 text-xs text-center pb-2">
        {meta?.phase_note}
      </div>
    </div>
  );
}
