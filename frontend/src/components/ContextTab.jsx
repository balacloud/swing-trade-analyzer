// ContextTab.jsx — Day 62, v4.24
// Pre-flight macro context: Calendar/Yield Cycles (A) + Economic Indicators (B) + News (C)
// PRE-FLIGHT CONTEXT ONLY — does NOT modify verdicts. Human is the final decision-maker.

import { useState, useEffect, useCallback } from 'react';
import RegimeBanner from './RegimeBanner';
import CycleCard from './CycleCard';
import ArticleRow from './ArticleRow';
import ConflictCheck from './ConflictCheck';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:5001';

// ─── Loaders ─────────────────────────────────────────────────────────────────
async function fetchJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json();
}

// ─── Helpers ─────────────────────────────────────────────────────────────────
function SectionHeader({ title, subtitle, badge }) {
  return (
    <div className="flex items-center justify-between mb-3">
      <div>
        <h3 className="text-white font-semibold text-sm">{title}</h3>
        {subtitle && <p className="text-gray-500 text-xs">{subtitle}</p>}
      </div>
      {badge && (
        <span className="text-xs text-gray-500 bg-gray-700/50 px-2 py-0.5 rounded">{badge}</span>
      )}
    </div>
  );
}

function LoadingSpinner({ label }) {
  return (
    <div className="flex items-center gap-2 py-8 justify-center text-gray-500 text-sm">
      <span className="animate-spin text-base">⏳</span>
      {label}
    </div>
  );
}

function SummaryBar({ summary, label }) {
  if (!summary) return null;
  return (
    <div className="flex gap-2 mt-3 flex-wrap text-xs">
      <span className="text-gray-500">{label}:</span>
      <span className="text-green-400">{summary.favorable} Favorable</span>
      <span className="text-yellow-400">{summary.neutral} Neutral</span>
      <span className="text-red-400">{summary.adverse} Adverse</span>
    </div>
  );
}

// ─── Options Block Status ─────────────────────────────────────────────────────
function OptionsBlockStatus({ optionsBlock }) {
  if (!optionsBlock) return null;
  const { has_options_block, reason } = optionsBlock;
  return (
    <div className={`rounded border px-3 py-2 text-xs mt-3 ${
      has_options_block
        ? 'bg-red-900/30 border-red-700 text-red-300'
        : 'bg-green-900/20 border-green-700/50 text-green-400'
    }`}>
      {has_options_block
        ? `🚫 Options Block Active — ${reason} · Avoid entering new positions`
        : '✅ No Options Block — No FOMC or Quad Witching within danger window'}
    </div>
  );
}

// ─── Historical Composite Box ─────────────────────────────────────────────────
function CompositeBox({ composite }) {
  if (!composite) return null;
  return (
    <div className="rounded bg-gray-700/40 border border-gray-600 p-3 mt-3 text-xs">
      <div className="text-white font-semibold mb-1">📜 {composite.title}</div>
      <div className="text-gray-300">{composite.description}</div>
      {composite.avg_return && (
        <div className="text-yellow-400 mt-1">{composite.avg_return}</div>
      )}
      {composite.source && (
        <div className="text-gray-600 mt-1">{composite.source}</div>
      )}
    </div>
  );
}

// ─── Short Interest ───────────────────────────────────────────────────────────
function ShortInterestRow({ short_interest }) {
  if (!short_interest) return null;
  const { short_pct_float, short_ratio, assessment } = short_interest;
  const color = assessment === 'High' ? 'text-red-400'
              : assessment === 'Low'  ? 'text-green-400'
              : 'text-yellow-400';
  return (
    <div className="flex items-center justify-between text-xs mt-2 py-2 border-t border-gray-700">
      <span className="text-gray-400">Short Interest</span>
      <span className={`font-mono ${color}`}>
        {short_pct_float != null ? `${short_pct_float}% float` : 'N/A'}
        {short_ratio != null ? ` · ${short_ratio}d to cover` : ''}
        {' · '}{assessment}
      </span>
    </div>
  );
}

// ─── Main Component ───────────────────────────────────────────────────────────
export default function ContextTab({ ticker }) {
  const [cyclesData, setCyclesData] = useState(null);
  const [econData, setEconData] = useState(null);
  const [newsData, setNewsData] = useState(null);
  const [overallRegime, setOverallRegime] = useState(null);
  const [optionsBlock, setOptionsBlock] = useState(null);
  const [regimeCounts, setRegimeCounts] = useState(null);
  const [totalIndicators, setTotalIndicators] = useState(10);
  const [cyclesLoading, setCyclesLoading] = useState(false);
  const [newsLoading, setNewsLoading] = useState(false);
  const [cyclesError, setCyclesError] = useState(null);
  const [newsError, setNewsError] = useState(null);

  // Load cycles + econ once on mount
  const loadCyclesEcon = useCallback(async () => {
    setCyclesLoading(true);
    setCyclesError(null);
    try {
      // Use the aggregated context endpoint with a placeholder ticker when no ticker
      const t = ticker || 'SPY';
      const data = await fetchJSON(`${API_BASE}/api/context/${t}`);
      setCyclesData(data.cycles || null);
      setEconData(data.econ || null);
      setOverallRegime(data.overall_regime || null);
      setOptionsBlock(data.options_block || null);
      setRegimeCounts(data.regime_counts || null);
      setTotalIndicators(data.total_indicators || 10);
      // If we also got news in the same call, use it
      if (ticker && data.news) {
        setNewsData(data.news);
      }
    } catch (e) {
      setCyclesError(e.message);
    } finally {
      setCyclesLoading(false);
    }
  }, [ticker]);

  // Load news separately when ticker changes
  const loadNews = useCallback(async (t) => {
    if (!t) return;
    setNewsLoading(true);
    setNewsError(null);
    try {
      const data = await fetchJSON(`${API_BASE}/api/news/${t}`);
      setNewsData(data);
    } catch (e) {
      setNewsError(e.message);
    } finally {
      setNewsLoading(false);
    }
  }, []);

  useEffect(() => {
    loadCyclesEcon();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []); // only on mount

  useEffect(() => {
    if (ticker) {
      loadNews(ticker);
    } else {
      setNewsData(null);
    }
  }, [ticker, loadNews]);

  return (
    <div>
      {/* Disclaimer */}
      <div className="bg-gray-800/50 border border-gray-700 rounded-lg px-4 py-2 mb-5 text-xs text-gray-500">
        🔭 <span className="font-semibold text-gray-400">Pre-Flight Context Only</span> — This tab provides macro
        context for human review. It does <em>not</em> modify trade verdicts. Human is always the final decision-maker.
      </div>

      {/* Overall Regime Banner */}
      {overallRegime && (
        <RegimeBanner
          overall_regime={overallRegime}
          favorable={regimeCounts?.favorable}
          neutral={regimeCounts?.neutral}
          adverse={regimeCounts?.adverse}
          total={totalIndicators}
        />
      )}

      {/* Error state */}
      {cyclesError && (
        <div className="bg-red-900/30 border border-red-700 rounded p-3 mb-4 text-red-300 text-sm">
          ⚠️ Failed to load context data: {cyclesError}
          <button onClick={loadCyclesEcon} className="ml-3 underline text-red-400 hover:text-red-200">
            Retry
          </button>
        </div>
      )}

      {/* 3-column layout */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">

        {/* ── Column A: Calendar & Yield Cycles ── */}
        <div>
          <SectionHeader
            title="📅 Calendar & Yield Cycles"
            subtitle="Global · Cached 6h · No ticker needed"
            badge={cyclesData?.from_cache ? 'cached' : null}
          />
          {cyclesLoading && !cyclesData ? (
            <LoadingSpinner label="Loading cycles…" />
          ) : cyclesData?.cards ? (
            <>
              {cyclesData.cards.map(card => (
                <div key={card.name} className="mb-2">
                  <CycleCard {...card} />
                </div>
              ))}
              <SummaryBar summary={cyclesData.summary} label="Cycles" />
            </>
          ) : !cyclesError ? (
            <div className="text-gray-500 text-sm py-8 text-center">Awaiting data…</div>
          ) : null}
        </div>

        {/* ── Column B: Economic Indicators ── */}
        <div>
          <SectionHeader
            title="📊 Economic Indicators"
            subtitle="FRED CPIAUCSL · FEDFUNDS · UNRATE · MANEMP"
            badge={econData?.from_cache ? 'cached' : null}
          />
          {cyclesLoading && !econData ? (
            <LoadingSpinner label="Loading econ…" />
          ) : econData?.cards ? (
            <>
              {econData.cards.map(card => (
                <div key={card.name} className="mb-2">
                  <CycleCard {...card} />
                </div>
              ))}
              <SummaryBar summary={econData.summary} label="Econ" />
              <CompositeBox composite={econData.composite} />
              <OptionsBlockStatus optionsBlock={optionsBlock} />
              {!econData.fred_available && (
                <div className="mt-3 text-xs text-yellow-500 bg-yellow-900/20 border border-yellow-700/50 rounded px-2 py-1">
                  ⚠️ FRED_API_KEY not configured — econ indicators unavailable
                </div>
              )}
            </>
          ) : !cyclesError ? (
            <div className="text-gray-500 text-sm py-8 text-center">Awaiting data…</div>
          ) : null}
        </div>

        {/* ── Column C: News Sentiment ── */}
        <div>
          <SectionHeader
            title={`📰 News Sentiment${ticker ? ` — ${ticker}` : ''}`}
            subtitle="Alpha Vantage · Short interest: yfinance"
            badge={newsData?.from_cache ? 'cached' : null}
          />
          {!ticker ? (
            <div className="text-gray-500 text-sm py-8 text-center">
              <div className="text-2xl mb-2">🔍</div>
              Enter a ticker in the Analyze tab to load news sentiment
            </div>
          ) : newsLoading ? (
            <LoadingSpinner label={`Loading news for ${ticker}…`} />
          ) : newsError ? (
            <div className="text-red-400 text-sm py-4">
              Failed to load news: {newsError}
              <button onClick={() => loadNews(ticker)} className="ml-2 underline">Retry</button>
            </div>
          ) : newsData ? (
            <>
              {/* Aggregate sentiment */}
              {newsData.aggregate && (
                <div className={`rounded border px-3 py-2 mb-3 text-sm ${
                  newsData.aggregate.label === 'BULLISH'
                    ? 'bg-green-900/30 border-green-600 text-green-300'
                    : newsData.aggregate.label === 'BEARISH'
                    ? 'bg-red-900/30 border-red-700 text-red-300'
                    : 'bg-gray-700/40 border-gray-600 text-gray-300'
                }`}>
                  <span className="font-semibold">{newsData.aggregate.label}</span>
                  {' · avg score: '}{newsData.aggregate.avg_score}
                  {' · '}{newsData.aggregate.bullish}🟢 {newsData.aggregate.neutral}🟡 {newsData.aggregate.bearish}🔴
                </div>
              )}

              {/* Error from engine (e.g., key not configured) */}
              {newsData.error && (
                <div className="text-yellow-500 text-xs bg-yellow-900/20 border border-yellow-700/50 rounded px-2 py-1 mb-3">
                  ⚠️ {newsData.error}
                </div>
              )}

              {/* Article list */}
              {newsData.articles?.length > 0 ? (
                <div>
                  {newsData.articles.map((a, i) => (
                    <ArticleRow key={i} {...a} />
                  ))}
                </div>
              ) : (
                <div className="text-gray-500 text-sm py-4 text-center">
                  No articles found for {ticker}
                </div>
              )}

              {/* Short interest */}
              <ShortInterestRow short_interest={newsData.short_interest} />

              {/* Conflict check */}
              <ConflictCheck
                cyclesRegime={overallRegime}
                newsLabel={newsData.aggregate?.label}
                hasOptionsBlock={optionsBlock?.has_options_block}
              />
            </>
          ) : null}
        </div>
      </div>

      {/* Footer */}
      <div className="mt-6 text-center text-xs text-gray-600">
        Cycles & Econ: FRED API (free) · News: Alpha Vantage (25 req/day free tier) · Cached 6h/4h
      </div>
    </div>
  );
}
