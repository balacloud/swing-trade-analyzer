/**
 * Data Sources tab v2 (Day 126). Plan: docs/claude/design/DATA_SOURCES_TAB_V2_PLAN_DAY126.md.
 *
 * Answers "is this ticker's data right?" and "where does it come from?", not only "is it cached?".
 *   A. Identity strip      exchange, currency, fund type (inferred), where the bars came from
 *   B. Data quality        verdict + only the WARN/FAIL checks (passes collapse into a count)
 *   C. Source chain        the REAL ordered chains with health, calls left, tested coverage and known issues
 *   D. Details (collapsed) cache numbers and the indicator formula table
 * Every block has its own loading / error (with reason + Retry) / empty / data state. Nothing here calls a provider.
 * Text decisions live in utils/dataSourcesView.js (pure, node-tested).
 */
import React from 'react';
import {
  describeIdentity, describeQuality, describeFundamentals, describeChains, provenanceFor,
} from '../utils/dataSourcesView';

const TONE = {
  good: 'text-green-400', warn: 'text-yellow-400', bad: 'text-red-400', muted: 'text-gray-400',
};
const PILL = {
  PASS: 'bg-green-900/50 text-green-300 border-green-700',
  WARN: 'bg-yellow-900/40 text-yellow-300 border-yellow-700',
  FAIL: 'bg-red-900/50 text-red-300 border-red-700',
};
const ICON = { WARN: '⚠️', FAIL: '❌' };
const HEALTH = { ok: ['bg-green-400', 'ok'], degraded: ['bg-yellow-400', 'degraded'], open: ['bg-red-400', 'circuit open'], unknown: ['bg-gray-500', 'unknown'] };
const MARKET = {
  works: 'text-green-300 border-green-800', partial: 'text-yellow-300 border-yellow-800', no: 'text-gray-500 border-gray-700',
  'paid only': 'text-gray-500 border-gray-700', disabled: 'text-gray-500 border-gray-700', 'not tested': 'text-gray-500 border-gray-700',
};

function Box({ children, testid, className = '' }) {
  return <div data-testid={testid} className={`bg-gray-800 rounded-lg p-6 mb-6 ${className}`}>{children}</div>;
}

function Identity({ id }) {
  if (!id) return null;
  const unknown = <span className="text-gray-500">unknown</span>;
  return (
    <Box testid="ds-identity">
      <div className="flex flex-wrap items-center gap-x-4 gap-y-2 text-sm">
        <span className="text-lg font-bold text-cyan-300" data-testid="ds-symbol">{id.symbol || unknown}</span>
        <span className="text-gray-300" data-testid="ds-exchange">{id.exchange || unknown}</span>
        <span className="text-gray-300" data-testid="ds-currency">{id.currency || unknown}</span>
        <span className="px-2 py-0.5 rounded bg-gray-700 text-gray-100" data-testid="ds-class" title={id.basis || 'no basis available'}>
          {id.cls || 'Unknown'}
        </span>
        {id.basis && <span className="text-xs text-gray-500">{id.basis}</span>}
      </div>
      <div className="mt-3 flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-gray-400">
        <span>Data from <b className="text-gray-200" data-testid="ds-datafrom">{id.dataFrom || 'unknown'}</b></span>
        {id.cache && <span className={TONE[id.cache.tone]} data-testid="ds-cachestate">{id.cache.label}</span>}
        {id.session && <span className="text-xs text-gray-500">{id.session}</span>}
      </div>
    </Box>
  );
}

function Quality({ view, fundamentals, onRetry, hasTicker }) {
  if (!hasTicker) {
    return (
      <Box testid="ds-quality">
        <h4 className="text-md font-semibold text-cyan-400 mb-1">Data quality</h4>
        <p className="text-sm text-gray-400">Analyze a ticker on the Analyze tab to see its data quality here. Source health and the cache are below.</p>
      </Box>
    );
  }
  return (
    <Box testid="ds-quality">
      <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
        <h4 className="text-md font-semibold text-cyan-400">Data quality</h4>
        {view.state === 'ok' && (
          <span data-testid="ds-quality-verdict" data-level={view.level} className={`px-3 py-0.5 rounded-full border text-xs font-semibold ${PILL[view.level] || PILL.WARN}`}>{view.level}</span>
        )}
      </div>

      {view.state === 'loading' && <p className="text-sm text-cyan-400">Loading data quality…</p>}

      {view.state === 'error' && (
        <div data-testid="ds-error" className="rounded-lg border border-red-700 bg-red-900/30 p-3 text-sm text-red-200 flex flex-wrap items-center justify-between gap-2">
          <span>Couldn't load data quality: {view.message}</span>
          <button data-testid="ds-retry" onClick={onRetry} className="px-3 py-1 rounded bg-red-700 hover:bg-red-600 text-white text-xs font-semibold">Retry</button>
        </div>
      )}

      {(view.state === 'not_cached' || view.state === 'unavailable') && <p className="text-sm text-gray-400">{view.message}</p>}

      {view.state === 'ok' && (
        <>
          <p className="text-xs text-gray-500 mb-3" data-testid="ds-quality-header">{view.header}</p>
          {(view.splits || []).map((t) => <p key={t} className="text-xs text-blue-300 mb-2" data-testid="ds-split-note">{t}</p>)}
          {view.rows.length === 0 ? (
            <p className="text-sm text-green-400" data-testid="ds-quality-allpass">All {view.total} checks passed.</p>
          ) : (
            <ul className="space-y-2">
              {view.rows.map((r) => (
                <li key={r.name} data-testid="ds-quality-row" data-level={r.level} className="text-sm">
                  <span className="mr-2">{ICON[r.level]}</span>
                  <b className={r.level === 'FAIL' ? 'text-red-300' : 'text-yellow-300'}>{r.label}</b>
                  <span className="text-gray-300">: {r.note}</span>
                </li>
              ))}
              {view.passedCount > 0 && <li className="text-xs text-gray-500">{view.passedCount} other check{view.passedCount === 1 ? '' : 's'} passed.</li>}
            </ul>
          )}
          {view.audit && (
            <p data-testid="ds-audit" className="mt-3 text-xs text-gray-400">
              Last audit ({view.audit.date}{view.audit.stale ? `, ${view.audit.ageDays} days old` : ''}): <span className={view.audit.level === 'FAIL' ? 'text-red-300' : 'text-yellow-300'}>{view.audit.line}</span>
            </p>
          )}
        </>
      )}
      {fundamentals && <p className={`mt-3 text-xs ${TONE[fundamentals.tone]}`} data-testid="ds-fundamentals">{fundamentals.text}</p>}
    </Box>
  );
}

function ChainRow({ r, group }) {
  const [dot, label] = HEALTH[r.health] || HEALTH.unknown;
  return (
    <div data-testid="ds-chain-row" data-provider={r.name} data-group={group} className="py-2 border-b border-gray-700/40 last:border-0">
      <div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-sm">
        <span className="font-medium text-gray-100">{r.label}</span>
        {r.role && <span className="text-xs text-gray-500">{r.role}</span>}
        <span className="flex items-center gap-1 text-xs text-gray-400"><i className={`inline-block w-2 h-2 rounded-full ${dot}`} />{label}</span>
        {r.callsLeft !== null && <span className="text-xs text-cyan-400">{r.callsLeft} calls left today</span>}
        {r.markets.map((m) => (
          <span key={m.market} className={`px-1.5 py-0.5 rounded border text-[11px] ${MARKET[m.status] || MARKET['not tested']}`}>{m.market}: {m.status}</span>
        ))}
      </div>
      {r.note && <p className="mt-1 text-xs text-gray-500">{r.note}</p>}
    </div>
  );
}

function Chain({ chains, tradingviewAvailable }) {
  if (!chains.available) {
    return <Box testid="ds-chain"><h4 className="text-md font-semibold text-cyan-400 mb-1">Where the data comes from</h4><p className="text-sm text-gray-400">{chains.message}</p></Box>;
  }
  const cov = chains.coverage;
  return (
    <Box testid="ds-chain">
      <h4 className="text-md font-semibold text-cyan-400 mb-1">Where the data comes from</h4>
      <p className="text-xs text-gray-500 mb-3" data-testid="ds-coverage">
        Each source is tried in order. Markets covered are as tested{cov.tested ? ` on ${cov.tested}` : ''}{cov.report ? ` (${cov.report})` : ''}.
        {cov.error && <span className="text-yellow-400"> {cov.error === 'Coverage table not loaded.' ? 'Loading the coverage table…' : `Coverage table unavailable: ${cov.error}`}</span>}
      </p>
      <h5 className="text-xs uppercase tracking-wider text-gray-500 mt-2">Prices</h5>
      {chains.price.map((r) => <ChainRow key={r.name} r={r} group="price" />)}
      <h5 className="text-xs uppercase tracking-wider text-gray-500 mt-4">Fundamentals</h5>
      {chains.fundamentals.map((r) => <ChainRow key={r.name} r={r} group="fundamentals" />)}
      {chains.disabled.length > 0 && <p className="mt-3 text-xs text-gray-500">Disabled: {chains.disabled.join(', ')} (not in any chain).</p>}
      {tradingviewAvailable != null && <p className="mt-1 text-xs text-gray-500">Market scanning: TradingView Screener, {tradingviewAvailable ? 'available' : 'not available'}.</p>}
      <details className="mt-3 text-sm">
        <summary className="cursor-pointer text-blue-400">Intraday, quote, stock info and earnings chains</summary>
        <div className="mt-2 space-y-1 text-xs text-gray-400">
          {chains.other.map((o) => (
            <div key={o.key}><b className="text-gray-300">{o.title}:</b> {o.rows.map((r) => r.label).join(' → ') || 'none'}</div>
          ))}
        </div>
      </details>
    </Box>
  );
}

function Details({ cacheStatus, provenance }) {
  const indicators = provenance && !provenance.error && Array.isArray(provenance.indicators) ? provenance.indicators : null;
  return (
    <details className="bg-gray-800 rounded-lg p-4 mb-6 text-sm" data-testid="ds-details">
      <summary className="cursor-pointer text-blue-400">Cache numbers and how indicators are calculated</summary>
      <div className="mt-4">
        {cacheStatus && !cacheStatus.error ? (
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4 text-center">
            {/* Day 126 (Statement Audit): a missing number is a dash, never a fake "0 KB" / "0%" */}
            {[['OHLCV entries', cacheStatus.ohlcv?.count ?? '—'], ['Fundamentals entries', cacheStatus.fundamentals?.count ?? '—'],
              ['Database size', cacheStatus.database_size_kb != null ? `${cacheStatus.database_size_kb} KB` : '—'],
              ['Hit rate (24h)', cacheStatus.ohlcv?.hit_rate_24h != null ? `${cacheStatus.ohlcv.hit_rate_24h}%` : '—']].map(([k, v]) => (
              <div key={k} className="bg-gray-700/50 rounded-lg p-3"><div className="text-xl font-bold text-cyan-400">{v}</div><div className="text-xs text-gray-400">{k}</div></div>
            ))}
          </div>
        ) : <p className="text-gray-500 mb-4">{cacheStatus?.error ? `Cache status unavailable: ${cacheStatus.error}` : 'Loading cache status…'}</p>}
        <p className="text-xs text-gray-500 mb-3">Prices are cached until the next market close (4pm ET + 30 min). Fundamentals for 7 days.</p>
        {indicators ? (
          <table className="w-full text-xs" data-testid="ds-indicators">
            <thead><tr className="text-left text-gray-400 border-b border-gray-700"><th className="py-1 px-2">Indicator</th><th className="py-1 px-2">From</th><th className="py-1 px-2">How</th></tr></thead>
            <tbody>{indicators.map((ind) => (
              <tr key={ind.name} className="border-b border-gray-700/30"><td className="py-1 px-2 text-gray-300">{ind.name}</td><td className="py-1 px-2 text-blue-400">{ind.source}</td><td className="py-1 px-2 text-gray-400">{ind.formula}</td></tr>
            ))}</tbody>
          </table>
        ) : <p className="text-gray-500" data-testid="ds-indicators-unavailable">{provenance?.indicators_error ? `Indicator table unavailable: ${provenance.indicators_error}` : 'Indicator formulas unavailable (no provenance for this ticker).'}</p>}
      </div>
    </details>
  );
}

export default function DataSourcesTab({
  ticker, stock, provenance: rawProvenance, loading, providerHealth, tradingviewAvailable, coverage, cacheStatus, onRetry,
}) {
  const provenance = provenanceFor(rawProvenance, ticker);   // never show ticker A's source next to ticker B's identity
  const identity = ticker ? describeIdentity(stock, provenance) : null;
  const quality = describeQuality(provenance, { loading });
  const fundamentals = ticker && !loading && quality.state === 'ok' ? describeFundamentals(stock, provenance) : null;
  const chains = describeChains(providerHealth, coverage);
  return (
    <div data-testid="data-sources-tab">
      <Box testid="ds-header">
        <h3 className="text-lg font-semibold text-cyan-400">Data Sources</h3>
        <p className="text-sm text-gray-400 mt-1">Is this ticker's data right, and where does it come from?</p>
      </Box>
      <Identity id={identity} />
      <Quality view={quality} fundamentals={fundamentals} onRetry={onRetry} hasTicker={!!ticker} />
      <Chain chains={chains} tradingviewAvailable={tradingviewAvailable} />
      <Details cacheStatus={cacheStatus} provenance={provenance} />
    </div>
  );
}
