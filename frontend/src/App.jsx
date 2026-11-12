/**
 * Swing Trade Analyzer - Main App Component
 * v2.0: Multi-Source Data Intelligence (TwelveData, Finnhub, FMP, yfinance, Stooq)
 * v2.1: Added TradingView screener scan tab (Day 12)
 * v2.2: Added Support & Resistance Trade Setup display (Day 14)
 * v2.3: Added Validation tab for data quality monitoring (Day 17)
 * v2.4: Fixed rsData overwrite bug (Day 18)
 * v2.5: Added Trade Viability display - Option D (Day 22)
 * v2.6: Added expandable Score Breakdown with explanations (Day 23)
 * v2.7: Day 26 - Fixed Risk/Reward display when null
 * v2.8: Day 26 - Added pullback re-entry zones for extended stocks
 * v2.9: Day 27 - Added Simplified Binary Scoring tab (research-backed minimalist system)
 * v3.0: Day 28 - Added Settings tab + Position Sizing Calculator (Van Tharp principles)
 * v3.1: Day 28 - Added auto-fill integration: Analysis → Position Calculator flow
 * v3.2: Day 29 - Added Session Refresh button (clears backend cache + resets frontend state)
 * v3.3: Day 33 - MTF Confluence UI (badges, starred levels, weekly levels dropdown)
 * v3.4: Day 33 - Fundamentals transparency (data source banner, health check)
 * v3.5: Day 34 - TradingView Widget (collapsible RSI/MACD chart)
 * v3.6: Day 37 - start.sh/stop.sh scripts, architecture cleanup
 * v3.7: Day 38 - Data Sources tab (transparency UI)
 * v3.8: Day 39 - Dual Entry Strategy UI (ADX badges, 4H RSI confirmation)
 * v3.9: Day 42 - Data source labels for all score sections (Technical, Sentiment, Risk/Macro)
 * v4.0: Day 44 - Categorical Assessment System (v4.5) - replaces 75-point numerical scoring
 * v4.1: Day 44 - Actionable Recommendation Card - clear guidance above assessment section
 * v4.2: Day 49 - Indicator Coherence Fixes:
 *       - R:R Filter: Cards grayed out + "⛔ R:R < 1" badge when R:R < 1.0
 *       - ADX Logic: Corrected entry strategy suggestions (ADX >=25=preferred, 20-25=viable, <20=caution)
 *       - Distribution Warning: "⚠️ DIST" badge when RVOL high + OBV falling
 * v4.3: Day 49 - UI Cohesiveness Fixes (from Test_2):
 *       - Entry uses nearest support: Fixed Math.max() instead of support[0]
 *       - Position/Reason aligned: Position now says "wait" when ADX < 20
 *       - VIABLE badge specificity: Shows "PULLBACK OK", "MOMENTUM OK", or "BOTH VIABLE"
 * v4.4: Day 50 - UI Cohesiveness Fixes (from exhaustive re-test):
 *       - Issue #1: Hide Position Size banner when verdict=AVOID or ADX<20 (was conflicting)
 *       - Issue #2: Added Retry button to error display for transient API failures
 *       - Issue #3: Entry cards always shown (grayed out with warning) instead of hidden
 *       - Issue #5: Warning when AVOID verdict but setup shows VIABLE badge
 */

import React, { useState, useEffect, useRef } from 'react';
import { fetchFullAnalysisData, checkBackendHealth, fetchScanStrategies, fetchScanResults, runValidation, clearBackendCache, clearMarketCache, fetchDataProvenance, getCacheStatus, fetchSectorRotation, fetchMRSignal, fetchMRScan, fetchBreakoutBatch, fetchBreakout, fetchSupportResistance } from './services/api';
import { calculateScore } from './utils/scoringEngine';
import { calculateSimplifiedAnalysis } from './utils/simplifiedScoring';
import { calculatePositionSize, loadSettings, saveSettings, getDefaultSettings } from './utils/positionSizing';
import { runCategoricalAssessment, getActionablePatterns } from './utils/categoricalAssessment';
import PullbackPlan from './components/PullbackPlan'; // Day 123: redesign Step 3, Trade Setup pullback plan
import RegimeRead from './components/RegimeRead'; // Day 123: redesign Step 4
import TechnicalRead from './components/TechnicalRead'; // Day 123: redesign Step 4
import { getLiquidityThreshold } from './utils/liquidityThresholds'; // Day 83
import { getAbsoluteMomentumRead } from './utils/absoluteMomentum'; // Day 117: dual momentum's second leg, informational only
// DecisionMatrix removed Day 70 — simplicity premium (full+simple views sufficient)
// BottomLineCard removed Day 82 (user feedback: verdict banner + What's Good/Risky
// duplicated the Verdict Card + Categorical Assessment card elsewhere on this page —
// three separate renderings of the same BUY/HOLD/AVOID verdict). Day 123: the
// HOLDING_PERIODS config it owned was removed with the holding-period selector.
import SectorRotationTab from './components/SectorRotationTab'; // Day 62: v4.24 Sector Rotation Phase 2
import ContextTab from './components/ContextTab'; // Day 62: v4.24 Context Tab
import ValueTab from './components/ValueTab'; // Day 75: Value investing lens
import MRRead from './components/MRRead'; // Day 123: redesign Step 5 (replaces MRSignalCard)
import PatternMiniCard from './components/PatternMiniCard'; // Day 83: shared VCP/Cup&Handle/Flat Base tile
import FundamentalsRead from './components/FundamentalsRead'; // Day 123: redesign Step 6
import PriceStructureCard from './components/PriceStructureCard'; // Day 72: Price Structure narrative
import AutomatedPaperTradingPanel from './components/AutomatedPaperTradingPanel'; // Day 87: automated engine ledger status + manual trigger
import { generatePriceStructure } from './utils/priceStructureNarrative'; // Day 72
import {
  createTrade, closeTrade, calculateStatistics, getSQNRating,
  loadTrades, saveTrades, addTrade, updateTrade, deleteTrade,
  downloadTradesCSV, TradeStatus
} from './utils/forwardTesting';

// Day 124: header line under the ticker. The backend fills a missing sector/industry with
// the string 'Unknown' (an ETF has neither), which printed as "Unknown • Unknown".
const describeClassification = (sector, industry, quoteType) => {
  if (quoteType === 'ETF') return 'Exchange-traded fund (ETF)';
  const parts = [sector, industry].filter(v => v && v !== 'Unknown');
  return parts.length > 0 ? parts.join(' • ') : 'Sector and industry not reported';
};

function App() {
  // Tab state
  const [activeTab, setActiveTab] = useState('analyze'); // 'analyze', 'scan', or 'validate'
  
  // Analysis state
  const [ticker, setTicker] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [backendStatus, setBackendStatus] = useState({ healthy: false });
  const [analysisResult, setAnalysisResult] = useState(null);
  const [srData, setSrData] = useState(null);
  const [patternsData, setPatternsData] = useState(null); // Day 44: Pattern detection
  const [actionablePatternsData, setActionablePatternsData] = useState(null); // Day 47: Actionable patterns ≥60%
  const [earningsData, setEarningsData] = useState(null); // Day 49: v4.10 Earnings Calendar
  const [categoricalResult, setCategoricalResult] = useState(null); // Day 44: v4.5 Categorical Assessment
  const [rawAnalysisData, setRawAnalysisData] = useState(null); // Day 53: Stored for re-assessment on period change
  const [mrSignalData, setMrSignalData] = useState(null); // Tier 3B: Mean-reversion signal
  const [mrSignalLoading, setMrSignalLoading] = useState(false); // Tier 3B: MR loading state
  const [breakoutData, setBreakoutData] = useState(null); // Day 82: single-ticker breakout status
  const [breakoutLoading, setBreakoutLoading] = useState(false); // Day 83 fix (Task E1): was missing entirely
  // Day 83 fix (Task E2): guards fetchMRSignal/fetchBreakout against a slow
  // response for an earlier search overwriting a newer one's card — neither
  // card displays which ticker it's for, so the mismatch would otherwise be
  // undetectable. Updated synchronously at the start of every analyzeStock()
  // call, checked before each of those two setters fires.
  const latestTickerRequestRef = useRef(null);
  // Day 83 fix (Task E3): identifies the most recent Scan tab request, see
  // loadBreakoutBadges()/runScan() below.
  const scanRequestIdRef = useRef(0);
  const [priceStructure, setPriceStructure] = useState(null); // Day 72: Price Structure narrative

  // Forward Testing state (Day 47: v4.7)
  const [forwardTrades, setForwardTrades] = useState(() => loadTrades());
  const [showAddTradeModal, setShowAddTradeModal] = useState(false);
  const [newTradeForm, setNewTradeForm] = useState({
    ticker: '', entryPrice: '', stopPrice: '', targetPrice: '', shares: '', notes: ''
  });
  const [closeTradeId, setCloseTradeId] = useState(null);
  const [closeTradePrice, setCloseTradePrice] = useState('');

  // Scan state
  const [scanLoading, setScanLoading] = useState(false);
  const [scanError, setScanError] = useState(null);
  const [scanResults, setScanResults] = useState(null);
  // Day 111: Mean-Reversion scanner — wires the already-existing fetchMRScan()
  // (backend /api/mr/scan, live since Day 81) to a UI button for the first time.
  const [mrScanLoading, setMrScanLoading] = useState(false);
  const [mrScanError, setMrScanError] = useState(null);
  const [mrScanResults, setMrScanResults] = useState(null);
  const [selectedStrategy, setSelectedStrategy] = useState('reddit');
  const [strategies, setStrategies] = useState(null);
  const [selectedMarketIndex, setSelectedMarketIndex] = useState('all');

  // Breakout badges (Day 81, Breakout Enhancement Plan Task 2.2)
  // ticker -> { status, humanAction, breakoutLevel, rvol, checks, warnings } | { error }
  const [breakoutBadges, setBreakoutBadges] = useState({});
  const [breakoutBadgesLoading, setBreakoutBadgesLoading] = useState(false);
  // Set of tickers actually included in the last batch request (the top-20 slice),
  // tracked independently of the response so the Scan tab can tell "never sent —
  // beyond the 20-row cap" apart from "sent, but no result came back" (see the
  // Scan table's Breakout column render logic below).
  const [breakoutBadgesRequested, setBreakoutBadgesRequested] = useState(new Set());


  // Validation state (Day 17)
  const [validationLoading, setValidationLoading] = useState(false);
  const [validationError, setValidationError] = useState(null);
  const [validationResults, setValidationResults] = useState(null);
  const [validationTickers, setValidationTickers] = useState('AAPL, NVDA, MSFT');

  // Score breakdown expanded state (Day 23)

  // Simplified analysis state (Day 27)
  const [simplifiedResult, setSimplifiedResult] = useState(null);
  const [analysisView, setAnalysisView] = useState('full'); // 'full' or 'simple' — default full since Day 124 (redesign Step 7; was simple from Day 75)

  // Settings state (Day 28)
  const [settings, setSettings] = useState(getDefaultSettings);

  // Position Calculator state (Day 28)
  const [calcEntry, setCalcEntry] = useState('');
  const [calcStop, setCalcStop] = useState('');
  const [calcTicker, setCalcTicker] = useState('');
  const [positionResult, setPositionResult] = useState(null);

  // Session refresh state (Day 29)
  const [refreshing, setRefreshing] = useState(false);
  const [lastRefresh, setLastRefresh] = useState(null);
  const [refreshMessage, setRefreshMessage] = useState(null); // Feedback message

  // Day 70: Collapsible sections for progressive disclosure (simplicity premium)
  // Keys: 'priceRS', 'patterns' (Day 123: holdingPeriod/categorical/indicators sections removed)
  // Default: all collapsed (undefined = falsy = collapsed)
  const [expandedSections, setExpandedSections] = useState({});
  const toggleSection = (key) => setExpandedSections(prev => ({ ...prev, [key]: !prev[key] }));

  // Data Sources state (Day 38)
  const [provenanceData, setProvenanceData] = useState(null);
  const [provenanceLoading, setProvenanceLoading] = useState(false);
  const [cacheStatus, setCacheStatus] = useState(null);
  const [providerHealth, setProviderHealth] = useState(null);

  // Sector Rotation state (Day 58 - v4.19)
  const [sectorRotation, setSectorRotation] = useState(null);
  const [sectorRotationError, setSectorRotationError] = useState(null);
  // Bumped by handleSessionRefresh/handleSectorRefresh so the Sectors tab's
  // own lazy-loaded sub-sections (Sub-Industry Watch, SRPS Pullback Screener)
  // know to discard their local `data` and refetch — see their own comments.
  const [sectorRefreshTrigger, setSectorRefreshTrigger] = useState(0);
  const [sectorRefreshing, setSectorRefreshing] = useState(false);

  // Day 94: shared so both mount-load and the tab's Retry button use the same logic
  const loadSectorRotation = () => {
    setSectorRotationError(null);
    fetchSectorRotation()
      .then(setSectorRotation)
      .catch(err => {
        console.error('Failed to load sector rotation:', err);
        setSectorRotationError(err.message || 'Failed to fetch sector rotation data');
      });
  };

  // Scoped Sectors-tab refresh (the tab's own "🔄 Refresh" button) — clears
  // only the backend's market_cache table (Sector Rotation, Sub-Industry
  // Watch, SRPS Pullback Screener, Market Phase) rather than the full
  // "Refresh Session" reset's every-ticker OHLCV/fundamentals wipe, since
  // none of that is relevant to "this tab looks stale." Was previously
  // impossible from inside the tab at all — the cached backend response
  // could go stale (Golden Rule 31 territory) with no in-tab way to force
  // a fresh pull short of the blunt, session-wide Refresh Session button.
  const handleSectorRefresh = async () => {
    setSectorRefreshing(true);
    try {
      await clearMarketCache();
    } catch (err) {
      console.error('Failed to clear market cache:', err);
      // Non-fatal — still attempt the refetch below; a stale cache would
      // otherwise just get served again, so this doesn't make anything worse.
    }
    setSectorRotationError(null);
    try {
      const fresh = await fetchSectorRotation();
      setSectorRotation(fresh);
    } catch (err) {
      console.error('Failed to load sector rotation:', err);
      setSectorRotationError(err.message || 'Failed to fetch sector rotation data');
    }
    setSectorRefreshTrigger(prev => prev + 1);
    setSectorRefreshing(false);
  };

  // Sector filter state (Day 62 - v4.24 Phase 2: "Scan for Rank 1")
  const [sectorFilter, setSectorFilter] = useState(null); // null = no filter, sector object = filtered

  // Handle "Scan for [sector]" from SectorRotationTab
  const handleScanForSector = (sector) => {
    setSectorFilter(sector);
    setActiveTab('scan');
  };

  // Data Freshness state (Day 59 - v4.20 Cache Audit)
  const [dataFreshness, setDataFreshness] = useState(null);

  // Quick picks for testing
  const quickPicks = ['AVGO', 'NVDA', 'AAPL', 'META', 'MSFT', 'NFLX', 'PLTR']; 

  // Check backend health, load strategies, and load settings on mount
  // v4.14: Check multi-source provider status on startup
  useEffect(() => {
    checkBackendHealth(true).then(setBackendStatus);
    fetchScanStrategies()
      .then(setStrategies)
      .catch(err => console.error('Failed to load strategies:', err));
    // Day 58: Load sector rotation data on startup
    loadSectorRotation();
    // Load saved settings
    setSettings(loadSettings());
  }, []);

  // v4.30: Auto-refresh provenance when analysis result arrives while datasources tab is open
  useEffect(() => {
    if (activeTab === 'datasources' && analysisResult?.ticker) {
      setProvenanceLoading(true);
      fetchDataProvenance(analysisResult.ticker)
        .then(setProvenanceData)
        .finally(() => setProvenanceLoading(false));
    }
  }, [analysisResult, activeTab]); // eslint-disable-line react-hooks/exhaustive-deps

  // Day 123 (Step 6): holding-period re-assessment effect removed with the selector.

  // Session Refresh - Clear backend cache and reset frontend state (Day 29)
  const handleSessionRefresh = async () => {
    setRefreshing(true);
    setRefreshMessage(null);
    try {
      // Clear backend cache
      await clearBackendCache();

      // Reset frontend state
      setAnalysisResult(null);
      setSrData(null);
      setPatternsData(null);
      setSimplifiedResult(null);
      setScanResults(null);
      setValidationResults(null);
      setError(null);
      setScanError(null);
      setValidationError(null);
      setPositionResult(null);
      setCalcEntry('');
      setCalcStop('');
      setCalcTicker('');
      setTicker('');

      // Re-fetch sector rotation (cache-cleared above, but the frontend was
      // still holding whatever it fetched at mount) and signal the Sectors
      // tab's own lazy-loaded sub-sections to discard their stale data too.
      loadSectorRotation();
      setSectorRefreshTrigger(prev => prev + 1);

      // Refresh backend status with provider check
      const status = await checkBackendHealth(true);
      setBackendStatus(status);

      // Record refresh time
      const refreshTime = new Date().toLocaleTimeString();
      setLastRefresh(refreshTime);

      // Show success feedback
      setRefreshMessage({
        type: 'success',
        text: `Session refreshed at ${refreshTime}. Backend cache cleared. Frontend state reset. Ready for fresh data.`
      });

      // Auto-hide message after 5 seconds
      setTimeout(() => setRefreshMessage(null), 5000);

    } catch (err) {
      console.error('Session refresh failed:', err);
      setRefreshMessage({
        type: 'error',
        text: `Refresh failed: ${err.message}`
      });
    } finally {
      setRefreshing(false);
    }
  };

  // Update settings and save to localStorage
  const updateSettings = (newSettings) => {
    setSettings(newSettings);
    saveSettings(newSettings);
  };

  // Day 58: Look up sector rotation context for a stock
  const getSectorContext = (stockSector) => {
    if (!sectorRotation || !stockSector) return null;
    const etfTicker = sectorRotation.mapping?.[stockSector];
    if (!etfTicker) return null;
    return sectorRotation.sectors?.find(s => s.etf === etfTicker) || null;
  };

  // Calculate position when inputs change
  const runPositionCalculation = () => {
    const entry = parseFloat(calcEntry);
    const stop = parseFloat(calcStop);
    if (!entry || !stop) {
      setPositionResult(null);
      return;
    }
    // Day 29: Pass options for max position size and manual shares
    // Tier 2A: VIX-based position scaling
    const vixCurrent = rawAnalysisData?.vix?.current;
    const vixMultiplier = vixCurrent == null ? 1.0 : vixCurrent < 20 ? 1.0 : vixCurrent <= 30 ? 0.75 : 0.50;
    const options = {
      maxPositionPercent: settings.maxPositionPercent || 25,
      manualShares: settings.useManualShares ? (settings.manualShares || 0) : 0,
      vixMultiplier,
    };
    const result = calculatePositionSize(settings.accountSize, settings.riskPercent, entry, stop, options);
    setPositionResult(result);
  };

  // Auto-fill position calculator from analysis and navigate to Settings (Day 28 integration)
  const autoFillPositionCalculator = (tickerSymbol, entry, stop) => {
    if (!entry || !stop) return;

    // Set calculator values
    setCalcTicker(tickerSymbol);
    setCalcEntry(entry.toFixed(2));
    setCalcStop(stop.toFixed(2));

    // Day 29: Pass options for max position size (don't use manual shares on auto-fill)
    // Tier 2A: VIX-based position scaling
    const vixCurrent = rawAnalysisData?.vix?.current;
    const vixMultiplier = vixCurrent == null ? 1.0 : vixCurrent < 20 ? 1.0 : vixCurrent <= 30 ? 0.75 : 0.50;
    const options = {
      maxPositionPercent: settings.maxPositionPercent || 25,
      manualShares: 0, // Auto-fill always uses calculated shares
      vixMultiplier,
    };
    const result = calculatePositionSize(settings.accountSize, settings.riskPercent, entry, stop, options);
    setPositionResult(result);

    // Switch to Settings tab
    setActiveTab('settings');
  };

  // Analyze stock
  const analyzeStock = async (tickerToAnalyze) => {
    const targetTicker = tickerToAnalyze || ticker;
    if (!targetTicker) {
      setError('Please enter a ticker symbol');
      return;
    }

    setLoading(true);
    setError(null);
    setAnalysisResult(null);
    setSrData(null);
    setPatternsData(null);
    setCategoricalResult(null);
    setSimplifiedResult(null);
    setMrSignalData(null);
    setPriceStructure(null);
    setBreakoutData(null);
    setActiveTab('analyze');

    // Day 83 fix (Task E2): record this as the latest requested ticker so the
    // two async fetches below can detect if a newer search superseded them
    // before their response arrives.
    latestTickerRequestRef.current = targetTicker;

    // Tier 3B: Fetch MR signal in parallel (non-blocking)
    setMrSignalLoading(true);
    fetchMRSignal(targetTicker)
      .then(data => {
        if (latestTickerRequestRef.current === targetTicker) setMrSignalData(data);
      })
      .catch(() => {
        if (latestTickerRequestRef.current === targetTicker) setMrSignalData(null);
      })
      .finally(() => {
        if (latestTickerRequestRef.current === targetTicker) setMrSignalLoading(false);
      });

    // Day 82: Fetch breakout status in parallel (non-blocking, same pattern as MR signal)
    setBreakoutLoading(true); // Day 83 fix (Task E1)
    fetchBreakout(targetTicker)
      .then(data => {
        if (latestTickerRequestRef.current === targetTicker) setBreakoutData(data);
      })
      .catch(() => {
        if (latestTickerRequestRef.current === targetTicker) setBreakoutData(null);
      })
      .finally(() => {
        if (latestTickerRequestRef.current === targetTicker) setBreakoutLoading(false);
      });

    try {
      const data = await fetchFullAnalysisData(targetTicker);
      const result = calculateScore(data.stock, data.spy, data.vix);

      // Day 27: Also calculate simplified binary analysis
      const simplified = calculateSimplifiedAnalysis(data.stock, data.spy, data.sr);

      // Day 44: v4.5 Categorical Assessment System
      // Day 47: v4.6.2 - Added ADX data for entry preference logic
      const trendTemplate = data.patterns?.trendTemplate || null;
      const adxData = data.sr?.meta?.adx || null;  // ADX for entry preference
      const categorical = runCategoricalAssessment(
        data.stock,
        data.spy,
        data.vix,
        data.fearGreed,
        trendTemplate,
        result.breakdown?.technical,
        data.stock.fundamentals,  // Pass raw fundamentals, not breakdown
        targetTicker,
        adxData,  // v4.6.2: Pass ADX for entry preference
        'standard'  // Day 123: fixed; the holding-period selector was removed (verdict weighting only)
      );

      setAnalysisResult(result);
      setSrData(data.sr);
      setPatternsData(data.patterns); // Day 44: Pattern detection

      // Day 47: v4.6.2 - Calculate actionable patterns (≥60% confidence only)
      const atr = data.sr?.meta?.atr || null;
      // Day 118 (Phase 4): pass the local `data.sr`, NOT the `srData` state
      // variable — setSrData() two lines above is async, so reading `srData`
      // here in the same synchronous block risks the pre-update stale value.
      // `data.sr` is the just-fetched payload, already resolved.
      const actionablePatterns = getActionablePatterns(data.patterns, atr, data.sr);
      setActionablePatternsData(actionablePatterns);

      // Day 123: Fear & Greed is no longer displayed (Assessment Breakdown removed); it still
      // reaches runCategoricalAssessment above via data.fearGreed.
      setEarningsData(data.earnings); // Day 49: v4.10 Earnings Calendar
      setCategoricalResult(categorical); // Day 44: v4.5 Categorical Assessment

      // Day 72: Price Structure narrative (display-only, no verdict impact)
      // Day 83 fix (Task A3): pass BOTH the raw patterns payload (still needed for
      // trendTemplate) AND the computed actionablePatterns.actionablePatterns array —
      // priceStructureNarrative.js's Priority-5 "pattern forming" watch item was
      // reading patterns?.actionablePatterns, a field that only exists on
      // getActionablePatterns()'s frontend-computed result, never on the raw API
      // payload. Passing just the raw payload meant that watch item could never fire.
      setPriceStructure(generatePriceStructure(data.sr, data.patterns, actionablePatterns.actionablePatterns));
      setSimplifiedResult(simplified);
      setTicker(targetTicker);

      // Day 58: Update sector rotation from analysis data (reliable — cached per trading day)
      // Day 94: also clears a stale sectorRotationError — this is a second path that can
      // deliver fresh data after the Sectors tab's own mount fetch failed.
      if (data.sectorRotation) {
        setSectorRotation(data.sectorRotation);
        setSectorRotationError(null);
      }

      // Day 59: Update data freshness for UI meter
      if (data.freshness) {
        setDataFreshness(data.freshness);
      }

      // v4.13: Store raw data for re-assessment when holding period changes
      setRawAnalysisData({
        stock: data.stock,
        spy: data.spy,
        qqq: data.qqq,  // Day 124: Market backdrop card (this literal is a whitelist, Golden Rule 30)
        vix: data.vix,
        fearGreed: data.fearGreed,
        trendTemplate,
        technicalBreakdown: result.breakdown?.technical,
        fundamentals: data.stock.fundamentals,
        ticker: targetTicker,
        adxData,
      });
      
    } catch (err) {
      setError(err.message || 'Failed to analyze stock');
    } finally {
      setLoading(false);
    }
  };

  // Breakout badge display config (Day 81, Breakout Enhancement Plan Task 2.2)
  // Colors per docs/claude/design/BREAKOUT_ENGINE_SPEC.md §13. Labels are
  // STATE descriptions, not signals — badge text must never read as "Buy".
  // Day 84: NOT_READY now shown with a muted badge (per spec §13's own
  // "Muted" treatment) instead of hidden entirely — hiding it was
  // indistinguishable from the breakout check having failed/not run at all.
  const BREAKOUT_BADGE_CONFIG = {
    BREAKOUT_CONFIRMED: { label: 'Breakout Confirmed', color: 'bg-green-900/40 text-green-400 border-green-700' },
    RETEST_ENTRY: { label: 'Retest Entry', color: 'bg-blue-900/40 text-blue-400 border-blue-700' },
    BREAKOUT_WATCH: { label: 'Breakout Watch', color: 'bg-amber-900/40 text-amber-400 border-amber-700' },
    BUILDING_BASE: { label: 'Building Base', color: 'bg-gray-700/40 text-gray-400 border-gray-600' },
    SUPPLY_WARNING: { label: 'Supply Warning', color: 'bg-red-900/40 text-red-400 border-red-700' },
    FAILED_BREAKOUT: { label: 'Failed Breakout', color: 'bg-red-900/40 text-red-400 border-red-700' },
    EXTENDED_CHASE_RISK: { label: 'Extended', color: 'bg-orange-900/40 text-orange-400 border-orange-700' },
    NOT_READY: { label: 'Not Ready', color: 'bg-gray-800/40 text-gray-500 border-gray-700' },
  };

  // Scan for candidates
  // N2: Nirmal's curated watchlist — extracted from Nirmals_Trading_April2026.md
  const NIRMAL_WATCHLIST = [
    'SMCI', 'NVDA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'AMD', 'TSLA',
    'PLTR', 'ORCL', 'CRM', 'MU', 'MARA', 'JNJ', 'JPM', 'VZ', 'TXN',
    'HOOD', 'COP', 'PYPL',
  ];

  // Day 85: user's own curated watchlist — sourced from their Notion "Master
  // Investment Framework Hub" (4 frameworks: AI Supply Chain, CanGem, STRATUM,
  // QUBIT). Manually synced, not a live Notion fetch — re-pull and update this
  // list when the user updates their Notion pages (their own cadence is a
  // weekly rerun at most). Scope/exclusions documented in
  // docs/claude/design/MASTER_FRAMEWORK_WATCHLIST_SCOPE.md — notably: QUBIT
  // framework excluded entirely (self-labeled all-Stage-0-1 speculative),
  // STRATUM's raw-material Layer 0 tier excluded (same reason), and 3
  // ASX/LSE-listed tickers dropped (exchanges not supported by scan_queries.py).
  const MASTER_FRAMEWORK_WATCHLIST = [
    // AI Supply Chain v3.0 (35)
    'GEV', 'ETN', 'GIB-A.TO', 'TSM', 'VRT', 'GLW', 'CCO.TO', 'APH', 'ANET', 'FN',
    'ASML', 'CEG', 'DELL', 'BWXT', 'MOD', 'ALAB', 'TMUS', 'HPE', 'KEYS', 'HPQ',
    'NVDA', 'AVGO', 'MU', 'MRVL', 'ONTO', 'CAMT', 'ORCL', 'FCX', 'AMD', 'CLF',
    'TEL', 'PWR', 'LEU', 'ATI', 'IFNNY',
    // CanGem v3.1 (28 new, deduplicated against AI Supply Chain)
    'MDA.TO', 'ASTL.TO', 'BDT.TO', 'CGY.TO', 'PNG.V', 'CVE.TO', 'WSP.TO',
    'ATRL.TO', 'NTR.TO', 'MRE.TO', 'LNR.TO', 'CNQ.TO', 'SU.TO', 'TRP.TO',
    'ENB.TO', 'CAE.TO', 'MAL.TO', 'BBD-B.TO', 'CLS.TO', 'T.TO', 'BCE.TO',
    'STRL', 'CW', 'DY', 'EME', 'ENS', 'VST',
    // STRATUM v1.0 — Layer 1 established watchlist only (14 new)
    'TECK-B.TO', 'KXS.TO', 'ARE.TO', 'CS.TO', 'PLTR', 'CGNX', 'LSCC', 'RKLB',
    'NOC', 'PATH', 'NET', 'ASTS', 'ISRG', 'XYL',
  ];

  // Day 97: HUB-65 — curated watchlist from a sibling options-research
  // project ("HUB_EXTENDED"/"HUB_CORE"), captured 2026-07-22. Also the
  // universe backing the automated paper-trading engine's new HUB-65
  // mean-reversion track (backend/mean_reversion.py's HUB_UNIVERSE) — same
  // 64 tickers, kept in sync manually if this watchlist is ever edited,
  // same two-lists-that-can-drift risk as Master Framework Watchlist's own
  // Notion-sync note above. VIX excluded (not a tradeable equity for scan
  // purposes); see mean_reversion.py's HUB_UNIVERSE comment for why.
  const HUB_WATCHLIST = [
    'CEG', 'ETN', 'ANET', 'ALAB', 'MOD', 'GLW', 'APH', 'FN', 'DELL', 'HPE', 'HPQ',
    'TMUS', 'KEYS', 'NOC', 'CGNX', 'ISRG', 'XYL', 'SMCI', 'ARM', 'ON', 'QCOM',
    'TSM', 'AMAT', 'LRCX', 'KLAC', 'ASML', 'LSCC', 'CCJ', 'OKLO', 'BWXT', 'FCX',
    'MP', 'TECK', 'WDC', 'SNOW', 'NET', 'SHOP', 'DDOG', 'PATH', 'GIB', 'HOOD',
    'SOFI', 'AFRM', 'UPST', 'NIO', 'LI', 'XPEV', 'JD', 'GS', 'LUNR', 'RKLB',
    'RIVN', 'ASTS', 'OXY', 'TRP', 'NFLX', 'POET', 'SMH', 'URA', 'XLF', 'XBI',
    'GDX', 'SOXX', 'DRAM',
  ];

  // Shared batch S/R fetch for any curated-ticker-list "watchlist" scan
  // strategy (Nirmal's Watchlist, Master Framework Watchlist) — same
  // convention: batch fetchSupportResistance() calls, null-per-ticker on
  // failure, majority-failure treated as a real error rather than a false
  // "no matches" (Day 83 fix, Task A5, generalized Day 85 for the 2nd
  // watchlist so both share one implementation instead of copy-pasting it).
  // Day 85: volume/change now come from fetchSupportResistance() itself (free
  // — already computed from the OHLCV bars it fetches, no extra API call).
  // name/sector/marketCap stay null — those need a real fundamentals/quote
  // call this endpoint doesn't make, and the user chose not to pay that cost.
  const fetchWatchlistCandidates = async (tickers, label) => {
    const results = await Promise.all(
      tickers.map(async (ticker) => {
        const d = await fetchSupportResistance(ticker);
        if (!d) return null;
        return {
          ticker,
          name: ticker,
          sector: null,
          price: d.currentPrice ?? null,
          change: d.change ?? null,
          volume: d.volume ?? null,
          marketCap: null,
        };
      })
    );
    const candidates = results.filter(Boolean);
    const failedCount = tickers.length - candidates.length;
    if (failedCount > tickers.length / 2) {
      throw new Error(
        `Failed to fetch ${failedCount}/${tickers.length} tickers in ${label} — backend may be unavailable`
      );
    }
    return candidates;
  };

  // Breakout badges: one batch call for the top 20 rows, fired after scan
  // results render — does not block the initial table paint (Task 2.2 design).
  // Day 83 fix (Task E3): scanId guards against a slower earlier scan's badge
  // response overwriting a faster, newer scan's results — same stale-response
  // race as Task E2, scoped to the Scan tab instead of ticker search.
  const loadBreakoutBadges = async (tickers, scanId) => {
    const topTickers = (tickers || []).slice(0, 20);
    if (topTickers.length === 0) return;
    setBreakoutBadgesLoading(true);
    // Recorded before the request resolves, so it reflects what was actually
    // sent even if the whole batch call throws below.
    if (scanRequestIdRef.current === scanId) setBreakoutBadgesRequested(new Set(topTickers));
    try {
      const data = await fetchBreakoutBatch(topTickers);
      if (scanRequestIdRef.current === scanId) setBreakoutBadges(data.results || {});
    } catch (err) {
      console.error('Breakout batch fetch failed:', err);
    } finally {
      if (scanRequestIdRef.current === scanId) setBreakoutBadgesLoading(false);
    }
  };

  const runScan = async () => {
    // Day 83 fix (Task E3): identifies this specific scan invocation so
    // loadBreakoutBadges() can detect being superseded by a newer scan.
    scanRequestIdRef.current += 1;
    const thisScanId = scanRequestIdRef.current;

    setScanLoading(true);
    setScanError(null);
    setScanResults(null);
    setBreakoutBadges({});

    try {
      // N2/Day85: curated watchlists — batch SR fetch (all cached), no backend
      // strategy needed. Day 83 fix (Task A5): was hardcoding http://localhost:5001
      // directly (bypassing API_BASE_URL) and swallowing every per-ticker failure
      // to null with no error propagation — a full backend outage rendered as a
      // false "no stocks matched" instead of the red error box the other
      // strategies correctly show. Now reuses the shared fetchSupportResistance()
      // (same API_BASE_URL) via fetchWatchlistCandidates(), which also treats
      // "most/all requests failed" as a real error, not a false "no matches".
      if (selectedStrategy === 'nirmal') {
        const candidates = await fetchWatchlistCandidates(NIRMAL_WATCHLIST, "Nirmal's Watchlist");
        setScanResults({
          strategy: "Nirmal's Watchlist",
          marketIndex: 'all',
          totalMatches: candidates.length,
          returned: candidates.length,
          candidates,
        });
        loadBreakoutBadges(candidates.map(c => c.ticker), thisScanId);
        return;
      }

      if (selectedStrategy === 'masterFramework') {
        const candidates = await fetchWatchlistCandidates(MASTER_FRAMEWORK_WATCHLIST, 'Master Framework Watchlist');
        setScanResults({
          strategy: 'Master Framework Watchlist',
          marketIndex: 'all',
          totalMatches: candidates.length,
          returned: candidates.length,
          candidates,
        });
        loadBreakoutBadges(candidates.map(c => c.ticker), thisScanId);
        return;
      }

      if (selectedStrategy === 'hub') {
        const candidates = await fetchWatchlistCandidates(HUB_WATCHLIST, 'HUB-65 Watchlist');
        setScanResults({
          strategy: 'HUB-65 Watchlist',
          marketIndex: 'all',
          totalMatches: candidates.length,
          returned: candidates.length,
          candidates,
        });
        loadBreakoutBadges(candidates.map(c => c.ticker), thisScanId);
        return;
      }

      const results = await fetchScanResults(selectedStrategy, 50, selectedMarketIndex);
      setScanResults(results);
      loadBreakoutBadges((results.candidates || []).map(c => c.ticker), thisScanId);
    } catch (err) {
      setScanError(err.message || 'Failed to scan for candidates');
    } finally {
      setScanLoading(false);
    }
  };

  // Day 111: scan the fixed 54-ticker MR universe for active RSI(2)<10 +
  // above-200SMA signals. Separate system from the TradingView-based scan
  // above (different backend endpoint, different response shape) — kept
  // independent rather than forced into the strategy dropdown.
  const runMrScan = async () => {
    setMrScanLoading(true);
    setMrScanError(null);
    setMrScanResults(null);
    try {
      const results = await fetchMRScan();
      if (!results) throw new Error('MR scan returned no data — check the backend is running');
      setMrScanResults(results);
    } catch (err) {
      setMrScanError(err.message || 'Failed to scan for MR signals');
    } finally {
      setMrScanLoading(false);
    }
  };

  // Run validation (Day 17)
  const handleRunValidation = async () => {
    const tickers = validationTickers
      .split(',')
      .map(t => t.trim().toUpperCase())
      .filter(t => t.length > 0);

    if (tickers.length === 0) {
      setValidationError('Please enter at least one ticker');
      return;
    }

    setValidationLoading(true);
    setValidationError(null);
    setValidationResults(null);

    try {
      const results = await runValidation(tickers);
      setValidationResults(results);
    } catch (err) {
      setValidationError(err.message || 'Failed to run validation');
    } finally {
      setValidationLoading(false);
    }
  };

  // Format currency
  const formatCurrency = (value) => {
    if (value === null || value === undefined) return 'N/A';
    return `$${value.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  };

  // Format large numbers (market cap)
  const formatMarketCap = (value) => {
    if (value === null || value === undefined) return 'N/A';
    if (value >= 1e12) return `$${(value / 1e12).toFixed(1)}T`;
    if (value >= 1e9) return `$${(value / 1e9).toFixed(1)}B`;
    if (value >= 1e6) return `$${(value / 1e6).toFixed(0)}M`;
    return `$${value.toLocaleString()}`;
  };

  // Format percentage
  const formatPercent = (value, decimals = 1) => {
    if (value === null || value === undefined) return 'N/A';
    return `${value >= 0 ? '+' : ''}${value.toFixed(decimals)}%`;
  };

  // Get RSI color
  // Get validation status color
  const getValidationStatusColor = (status) => {
    switch (status) {
      case 'pass': return 'text-green-400 bg-green-900/30';
      case 'fail': return 'text-red-400 bg-red-900/30';
      case 'warning': return 'text-yellow-400 bg-yellow-900/30';
      case 'skip': return 'text-gray-400 bg-gray-700/30';
      default: return 'text-gray-400';
    }
  };

  // Get quality score color
  const getQualityColor = (score) => {
    if (score >= 90) return 'text-green-400';
    if (score >= 75) return 'text-green-300';
    if (score >= 60) return 'text-yellow-400';
    return 'text-red-400';
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold text-blue-400">🎯 Swing Trade Analyzer</h1>
          <p className="text-gray-400 mt-2">Multi-Engine Swing Trade Analysis</p>
          
          {/* Backend Status + Session Refresh (Day 29) */}
          <div className="mt-4 flex justify-center items-center gap-4">
            <div className="flex items-center gap-2">
              <span className={`w-3 h-3 rounded-full ${backendStatus.healthy ? 'bg-green-500' : 'bg-red-500'}`}></span>
              <span className="text-sm text-gray-400">
                Backend {backendStatus.healthy ? 'Connected' : 'Disconnected'}
                {/* v4.14: Multi-Source Data Provider status */}
                {backendStatus.dataProviderAvailable && (
                  <span className="text-green-400"> • Multi-Source ✓</span>
                )}
                {!backendStatus.dataProviderAvailable && backendStatus.healthy && (
                  <span className="text-yellow-400"> • Single-Source ⚠️</span>
                )}
                {backendStatus.tradingviewAvailable && ' • TradingView ✓'}
                {backendStatus.srEngineAvailable && ' • S&R ✓'}
                {backendStatus.validationAvailable && ' • Validation ✓'}
              </span>
            </div>
            <button
              onClick={handleSessionRefresh}
              disabled={refreshing}
              className={`px-3 py-1 rounded-lg text-sm font-medium transition-colors ${
                refreshing
                  ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                  : 'bg-orange-600 hover:bg-orange-700 text-white'
              }`}
              title="Clear cache and reset session for fresh data"
            >
              {refreshing ? '🔄 Refreshing...' : '🔄 Refresh Session'}
            </button>
            {lastRefresh && (
              <span className="text-xs text-gray-500">Last: {lastRefresh}</span>
            )}
          </div>

          {/* Refresh Feedback Banner (Day 29) */}
          {refreshMessage && (
            <div className={`mt-4 mx-auto max-w-2xl px-4 py-3 rounded-lg text-sm flex items-center justify-between ${
              refreshMessage.type === 'success'
                ? 'bg-green-900/50 border border-green-600 text-green-300'
                : 'bg-red-900/50 border border-red-600 text-red-300'
            }`}>
              <span>
                {refreshMessage.type === 'success' ? '✅ ' : '❌ '}
                {refreshMessage.text}
              </span>
              <button
                onClick={() => setRefreshMessage(null)}
                className="ml-4 text-gray-400 hover:text-white"
              >
                ✕
              </button>
            </div>
          )}
        </div>

        {/* Tab Navigation */}
        <div className="flex justify-center mb-6">
          <div className="bg-gray-800 rounded-lg p-1 inline-flex">
            <button
              onClick={() => setActiveTab('analyze')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'analyze'
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              📊 Analyze Stock
            </button>
            <button
              onClick={() => setActiveTab('scan')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'scan'
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              🔍 Scan Market
            </button>
            <button
              onClick={() => setActiveTab('sectors')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'sectors'
                  ? 'bg-green-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              🔄 Sectors
            </button>
            <button
              onClick={() => setActiveTab('context')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'context'
                  ? 'bg-purple-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              🔭 Context
            </button>
            <button
              onClick={() => setActiveTab('value')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'value'
                  ? 'bg-amber-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              💎 Value
            </button>
            <button
              onClick={() => setActiveTab('validate')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'validate'
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              ✅ Validate Data
            </button>
            <button
              onClick={() => {
                setActiveTab('datasources');
                // Fetch cache status when tab is selected
                getCacheStatus().then(setCacheStatus);
                // Fetch live provider health
                checkBackendHealth().then(h => setProviderHealth(h?.providers || null));
                // Fetch provenance for current ticker if analyzed
                if (analysisResult?.ticker) {
                  setProvenanceLoading(true);
                  fetchDataProvenance(analysisResult.ticker)
                    .then(setProvenanceData)
                    .finally(() => setProvenanceLoading(false));
                }
              }}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'datasources'
                  ? 'bg-cyan-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              📡 Data Sources
            </button>
            <button
              onClick={() => setActiveTab('forward')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'forward'
                  ? 'bg-green-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              📈 Forward Test
            </button>
            <button
              onClick={() => setActiveTab('settings')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                activeTab === 'settings'
                  ? 'bg-purple-600 text-white'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              ⚙️ Settings
            </button>
          </div>
        </div>

        {/* ==================== ANALYZE TAB ==================== */}
        {activeTab === 'analyze' && (
          <>
            {/* Search Input */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <div className="flex gap-4">
                <input
                  type="text"
                  value={ticker}
                  onChange={(e) => setTicker(e.target.value.toUpperCase())}
                  onKeyPress={(e) => e.key === 'Enter' && analyzeStock()}
                  placeholder="Enter ticker symbol (e.g., AAPL)"
                  className="flex-1 bg-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button
                  onClick={() => analyzeStock()}
                  disabled={loading}
                  className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-lg font-semibold disabled:opacity-50"
                >
                  {loading ? 'Analyzing...' : 'Analyze'}
                </button>
              </div>
              
              {/* Quick Picks */}
              <div className="mt-4 flex flex-wrap gap-2">
                <span className="text-gray-400 text-sm">Quick picks:</span>
                {quickPicks.map((t) => (
                  <button
                    key={t}
                    onClick={() => analyzeStock(t)}
                    className="bg-gray-700 hover:bg-gray-600 px-3 py-1 rounded text-sm"
                  >
                    {t}
                  </button>
                ))}
              </div>
            </div>

            {/* Day 27: View Toggle - Full vs Simple */}
            {analysisResult && !loading && (
              <div className="flex justify-center mb-6">
                <div className="bg-gray-800 rounded-lg p-1 inline-flex">
                  <button
                    onClick={() => setAnalysisView('full')}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                      analysisView === 'full'
                        ? 'bg-blue-600 text-white'
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    Full Analysis
                  </button>
                  <button
                    onClick={() => setAnalysisView('simple')}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                      analysisView === 'simple'
                        ? 'bg-green-600 text-white'
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    ✅ Simple Checklist (9 criteria)
                  </button>
                </div>
              </div>
            )}

            {/* Error Display - Day 50: Added retry button */}
            {error && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6 text-red-200">
                <div className="flex items-center justify-between">
                  <span>{error}</span>
                  <button
                    onClick={() => analyzeStock(ticker)}
                    className="ml-4 px-3 py-1 bg-red-700 hover:bg-red-600 rounded text-sm font-medium transition-colors"
                  >
                    Retry
                  </button>
                </div>
              </div>
            )}

            {/* Loading State */}
            {loading && (
              <div className="bg-gray-800 rounded-lg p-12 text-center">
                <div className="text-4xl mb-4">⏳</div>
                <p className="text-gray-400">Analyzing {ticker}...</p>
              </div>
            )}

            {/* Analysis Results */}
            {analysisResult && !loading && analysisView === 'full' && (
              <div className="space-y-6">
                {/* Day 123 (redesign Step 6): Holding Period selector removed — its only effect was the
                    BUY/HOLD/AVOID verdict's tech/fund weighting, and that verdict is no longer shown. */}
                {/* Day 124 (user): the market backdrop is the first card, then the stock. */}
                <RegimeRead
                  spy={rawAnalysisData?.spy}
                  qqq={rawAnalysisData?.qqq}
                  vix={rawAnalysisData?.vix}
                  ticker={analysisResult.ticker}
                  onOpenContext={() => { setActiveTab('context'); window.scrollTo({ top: 0 }); }}
                />
                {/* Verdict Card - v4.5 Categorical Assessment (Neutral design) */}
                <div className="rounded-lg p-6 bg-gray-800 border border-gray-700">
                  <div className="flex justify-between items-center">
                    <div>
                      <h2 className="text-2xl font-bold text-white">{analysisResult.ticker} - {analysisResult.name}</h2>
                      <p className="text-gray-400">
                        {describeClassification(analysisResult.sector, analysisResult.industry, rawAnalysisData?.stock?.quoteType)}
                        {(() => {
                          const sc = getSectorContext(analysisResult.sector);
                          if (!sc) return null;
                          const qColors = { Leading: 'bg-green-600', Weakening: 'bg-yellow-600', Lagging: 'bg-red-600', Improving: 'bg-blue-600' };
                          return (
                            <span className={`ml-2 px-1.5 py-0.5 rounded text-xs font-medium text-white ${qColors[sc.quadrant] || 'bg-gray-600'}`}
                              title={`${sc.name} (${sc.etf}) — RS: ${sc.rsRatio} | Mom: ${sc.rsMomentum > 0 ? '+' : ''}${sc.rsMomentum} | Rank: ${sc.rank}/11`}>
                              {sc.etf} {sc.quadrant.toUpperCase()}
                            </span>
                          );
                        })()}
                      </p>
                      <div className="flex items-center gap-2 mt-1">
                        <p className="text-gray-500 text-sm">{formatCurrency(analysisResult.currentPrice)}</p>
                        {/* Day 49: v4.10 Earnings Warning Badge */}
                        {earningsData?.hasUpcoming && (
                          <span
                            title={`${earningsData.recommendation}\n\nEarnings Date: ${earningsData.earningsDate}\nDays Until: ${earningsData.daysUntil}`}
                            className={`px-2 py-0.5 rounded text-xs font-medium cursor-help ${
                              earningsData.daysUntil <= 3
                                ? 'bg-red-600 text-white animate-pulse'
                                : 'bg-yellow-600 text-white'
                            }`}
                          >
                            {earningsData.warning}
                          </span>
                        )}
                        {/* Day 59: Data Freshness Meter */}
                        {dataFreshness?.sources?.length > 0 && (
                          <div className="flex items-center gap-1 ml-2" title="Data freshness per source (hover dots for details)">
                            <span className="text-gray-600 text-xs mr-0.5">Data:</span>
                            {dataFreshness.sources.map((src, i) => {
                              const dotColor = src.status === 'fresh' ? 'bg-green-500' :
                                               src.status === 'aging' ? 'bg-yellow-500' :
                                               src.status === 'stale' ? 'bg-red-500' :
                                               src.status === 'live' ? 'bg-blue-500' : 'bg-gray-500';
                              const ageLabel = src.ageMinutes === 0 ? 'Live' :
                                              src.ageMinutes < 60 ? `${Math.round(src.ageMinutes)}m ago` :
                                              src.ageMinutes < 1440 ? `${(src.ageMinutes / 60).toFixed(1)}h ago` :
                                              `${(src.ageMinutes / 1440).toFixed(1)}d ago`;
                              return (
                                <span key={i}
                                  className={`w-2 h-2 rounded-full ${dotColor} cursor-help`}
                                  title={`${src.name}: ${ageLabel}${src.source ? ` (${src.source})` : ''}`}
                                />
                              );
                            })}
                          </div>
                        )}
                      </div>
                    </div>
                    {/* Day 123 (redesign Step 4): the BUY/HOLD/AVOID badge and the T/F/S/R letter
                        row were here. The Full view now leads with the Regime band and the
                        Technical Read card below (Day 109 decisions; Day 119 plan Phase 3). The
                        Simple view keeps its own TRADE / No Trade checklist verdict. (Step 6 later removed the
                        Assessment Breakdown and BUY/HOLD/AVOID everywhere.) */}
                  </div>
                </div>

                {/* Day 123 (Step 6): the fundamentals-unavailable banner moved into the Fundamentals card's "Can't check" state. */}
                {/* Day 124: Market backdrop moved to the top of the page (above the stock header). */}
                <TechnicalRead
                  ticker={analysisResult.ticker}
                  technical={categoricalResult?.technical}
                  adxData={categoricalResult?.adxData || null}
                  rsData={analysisResult.rsData}
                  patternsData={patternsData}
                  price={analysisResult.currentPrice}
                  ema21={analysisResult.indicators?.ema21}
                  priceHistory={rawAnalysisData?.stock?.priceHistory}
                  srData={srData}
                />
                <MRRead mrData={mrSignalData} loading={mrSignalLoading} ticker={analysisResult.ticker} />

                {/* Price & RS Info — Day 70: collapsed by default */}
                <div className="bg-gray-800 rounded-lg">
                  <button
                    onClick={() => toggleSection('priceRS')}
                    className="flex items-center gap-2 w-full px-6 py-4 text-left hover:bg-gray-700/30 transition-colors rounded-lg"
                  >
                    <span className="text-sm text-gray-500">{expandedSections.priceRS ? '▼' : '▶'}</span>
                    <span className="text-lg font-semibold text-blue-400">Price & Relative Strength</span>
                    <span className="ml-auto text-xs text-gray-500">
                      {formatCurrency(analysisResult.currentPrice)} | RS {analysisResult.rsData?.rs52Week?.toFixed(2) || 'N/A'}
                    </span>
                  </button>
                </div>
                {expandedSections.priceRS && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {/* Price Card */}
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h3 className="text-lg font-semibold mb-4 text-blue-400">💰 Price Data</h3>
                    <div className="space-y-2">
                      <div className="flex justify-between">
                        <span className="text-gray-400">Current Price:</span>
                        <span className="font-bold">{formatCurrency(analysisResult.currentPrice)}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-gray-400">52-Week High:</span>
                        <span>{formatCurrency(analysisResult.fiftyTwoWeekHigh)}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-gray-400">52-Week Low:</span>
                        <span>{formatCurrency(analysisResult.fiftyTwoWeekLow)}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-gray-400">% from High:</span>
                        <span className={analysisResult.pctFromHigh >= -10 ? 'text-green-400' : 'text-yellow-400'}>
                          {formatPercent(analysisResult.pctFromHigh)}
                        </span>
                      </div>
                      {/* Day 53: Average Daily Dollar Volume - critical for swing trade liquidity */}
                      {/* Day 83 fix (Task A4): cap-aware coloring, sourced from the same shared
                          threshold Quality Gates and the Simple Checklist use — was a flat
                          $10M/$50M split regardless of market cap, a 3rd, different liquidity
                          standard from the other two views. */}
                      {(() => {
                        const avgVol = rawAnalysisData?.stock?.avgVolume || 0;
                        const dollarVol = avgVol * (analysisResult.currentPrice || 0);
                        const marketCap = rawAnalysisData?.stock?.fundamentals?.marketCap || rawAnalysisData?.stock?.marketCap || 0;
                        const { threshold: liquidityThreshold } = getLiquidityThreshold(marketCap);
                        const color = dollarVol >= liquidityThreshold * 2 ? 'text-green-400' : dollarVol >= liquidityThreshold ? 'text-yellow-400' : 'text-red-400';
                        return (
                          <div className="flex justify-between">
                            <span className="text-gray-400">Liquidity (Daily $):</span>
                            <span className={`font-semibold ${color}`}>
                              {dollarVol > 0 ? formatMarketCap(dollarVol) : 'N/A'}
                            </span>
                          </div>
                        );
                      })()}
                    </div>
                  </div>

                  {/* RS Card */}
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h3 className="text-lg font-semibold mb-4 text-blue-400">📈 Relative Strength</h3>
                    <div className="space-y-2">
                      <div className="flex justify-between">
                        <span className="text-gray-400">RS vs S&P 500:</span>
                        {/* Day 83 fix (Task B4): color and value both key off rs52Week now
                            (was rsRatio for color, rs52Week for value — same underlying
                            number aliased in scoringEngine.js, harmless today but fragile
                            if they ever diverged).
                            Day 107 audit fix: bands were still 1.2/1.0 (pre-Day-78-revert) —
                            realigned to the frozen Strong>=1.0/Weak<0.8 bands, matching the
                            RS Interpretation block below (which already had it right). */}
                        <span className={`font-bold ${analysisResult.rsData?.rs52Week >= 1.0 ? 'text-green-400' : analysisResult.rsData?.rs52Week >= 0.8 ? 'text-yellow-400' : 'text-red-400'}`}>
                          {analysisResult.rsData?.rs52Week?.toFixed(2) || 'N/A'}
                        </span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-gray-400">Stock 52W Return:</span>
                        <span className={analysisResult.rsData?.stock52wReturn >= 0 ? 'text-green-400' : 'text-red-400'}>
                          {formatPercent(analysisResult.rsData?.stock52wReturn)}
                        </span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-gray-400">S&P 52W Return:</span>
                        <span>{formatPercent(analysisResult.rsData?.spy52wReturn)}</span>
                      </div>
                      <div className="flex justify-between">
                        {/* Day 83 fix (Task B4): relabeled — this is a linear rescale of the
                            rs52Week ratio shown above (rsCalculator.js's own comment admits
                            "simplified version - ideally would be percentile vs all stocks"),
                            not an independent IBD-style percentile rank vs. the market. */}
                        <span className="text-gray-400 cursor-help" title="A linear rescale of the RS ratio above, NOT a percentile rank vs. all stocks (that would require ranking against the full market).">RS Rating (scaled, not a percentile):</span>
                        <span className={`font-bold ${analysisResult.rsData?.rsRating >= 70 ? 'text-green-400' : analysisResult.rsData?.rsRating >= 50 ? 'text-yellow-400' : 'text-red-400'}`}>
                          {analysisResult.rsData?.rsRating || 'N/A'}
                        </span>
                      </div>
                      {/* Day 53: RS Interpretation - computed in rsCalculator.js but was never displayed */}
                      {analysisResult.rsData?.interpretation && (
                        <div className="mt-2 pt-2 border-t border-gray-700">
                          <span className={`text-xs ${analysisResult.rsData?.rs52Week >= 1.0 ? 'text-green-400' : analysisResult.rsData?.rs52Week >= 0.8 ? 'text-yellow-400' : 'text-red-400'}`}>
                            {analysisResult.rsData.interpretation}
                          </span>
                        </div>
                      )}
                      {/* Day 117: absolute momentum — dual momentum's second leg
                          (Antonacci 2014). Informational only: gates nothing, scores
                          nothing, and is deliberately NOT wired into the RS colour
                          bands above. Reuses rsData.stock52wReturn, already computed
                          by rsCalculator.js and mapped in scoringEngine.js — no new
                          arithmetic anywhere. Backtested as Config G
                          (backtest_holistic.py:491-501) and deliberately NOT shipped
                          as a gate: it excluded 1 of 75 trades. Full reasoning:
                          docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md */}
                      {(() => {
                        const abs = getAbsoluteMomentumRead(analysisResult.rsData?.stock52wReturn);
                        if (!abs) return null;
                        return (
                          <div
                            className="mt-2 pt-2 border-t border-gray-700 text-xs text-gray-400"
                            title="Dual momentum's second leg (Antonacci, 2014). Relative strength above asks whether the stock beat the market; this asks whether it beat cash. The 5% figure is a static risk-free proxy carried from this project's own Day 107 backtest, not a live T-bill yield. Informational only — it does not affect any score, the verdict, or the Simple Checklist."
                          >
                            <span className="text-gray-500">Absolute momentum (info only): </span>{abs.text}
                          </div>
                        );
                      })()}
                    </div>
                  </div>
                </div>
                )}

                {/* Trade Setup Card (S&R) - Day 22. Day 123 (redesign Step 3): pullback plan only;
                    the viability badge, "Stock not recommended" warning and advice banner are
                    gone (they counted the momentum plan the card no longer shows). Step 4: the
                    indicator chips and the volume read moved to the Technical Read's Entry
                    checks (4H RSI dropped: its tooltip described momentum entries). The card
                    always renders; PullbackPlan says why when srData is missing. */}
                {analysisResult && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <div className="flex justify-between items-start gap-3 mb-1">
                      <h3 className="text-lg font-semibold text-blue-400">🎯 Trade Setup</h3>
                      <div className="flex gap-1.5 shrink-0">
                        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-gray-700 text-gray-300">⚙ LEVELS</span>
                        <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-900/40 text-amber-300">◇ YOUR CALL</span>
                      </div>
                    </div>
                    <p className="text-sm text-gray-400 mb-4">The pullback plan: wait for a dip to support, then buy. Plain arithmetic, not a tested system.</p>
                    <PullbackPlan srData={srData} ticker={analysisResult.ticker} />
                    {/* Day 123: levels need srData; when it failed, PullbackPlan above already says so. */}
                    {srData && (<>
                    {/* Day 40: Removed legacy Trade Levels Grid - now using dual strategy cards above */}
                    {/* Day 26: Show actual S&R levels - Day 33: Enhanced with MTF confluence */}
                    <div className="mt-4 pt-3 border-t border-gray-700">
                      {/* Day 33: MTF Confluence Badge */}
                      {srData.meta?.mtf?.enabled && (
                        <div className="mb-3 flex items-center justify-center gap-2">
                          <div className={`px-3 py-1 rounded-full text-xs font-semibold ${
                            srData.meta.mtf.confluence_pct >= 40 ? 'bg-green-900/50 text-green-300 border border-green-700' :
                            srData.meta.mtf.confluence_pct >= 20 ? 'bg-yellow-900/50 text-yellow-300 border border-yellow-700' :
                            'bg-gray-700/50 text-gray-400 border border-gray-600'
                          }`}>
                            MTF Confluence: {srData.meta.mtf.confluence_pct?.toFixed(0)}%
                            <span className="ml-1 opacity-70">
                              ({srData.meta.mtf.confluent_levels}/{srData.meta.mtf.total_levels} levels
                              {/* Day 115: projected (ATR/Fibonacci-synthetic) levels are now excluded
                                  from this ratio entirely, not just silently dragging it down — say
                                  so, so an improved percentage doesn't read as unexplained. */}
                              {srData.meta.mtf.projected_excluded > 0 && `, ${srData.meta.mtf.projected_excluded} projected excluded`})
                            </span>
                          </div>
                        </div>
                      )}
                      <div className="grid grid-cols-2 gap-4 text-xs">
                        <div>
                          <div className="text-green-400 font-semibold mb-1">Support Levels</div>
                          {srData.support?.length > 0 ? (
                            <div className="space-y-0.5">
                              {srData.support.slice().sort((a, b) => b - a).map((level, i) => {
                                const levelKey = level.toFixed(2);
                                const mtfInfo = srData.meta?.mtf?.confluence_map?.[levelKey];
                                const isConfluent = mtfInfo?.confluent;
                                return (
                                  <div key={i} className={`text-gray-400 ${isConfluent ? 'font-medium' : ''}`}>
                                    {/* Day 115: surface the graduated strength_label (Strong/Moderate/Weak)
                                        instead of a flat "Confluent with weekly level" — the descriptive-
                                        state convention this redesign already uses elsewhere (Regime,
                                        Technical Read, Fundamentals). Falls back to the old text if
                                        strength_label is absent (older cached response shape). */}
                                    {isConfluent && <span className="text-yellow-400 mr-1" title={mtfInfo?.strength_label ? `Confluent with weekly level (${mtfInfo.strength_label})` : 'Confluent with weekly level'}>★</span>}
                                    S{i + 1}: <span className={`font-mono ${isConfluent ? 'text-green-200' : 'text-green-300'}`}>{formatCurrency(level)}</span>
                                    <span className="text-gray-500 ml-1">
                                      ({((srData.currentPrice - level) / srData.currentPrice * 100).toFixed(1)}% below)
                                    </span>
                                  </div>
                                );
                              })}
                            </div>
                          ) : (
                            <div className="text-gray-500 italic">None within range</div>
                          )}
                        </div>
                        <div>
                          <div className="text-red-400 font-semibold mb-1">Resistance Levels</div>
                          {srData.resistance?.length > 0 ? (
                            <div className="space-y-0.5">
                              {srData.resistance.slice().sort((a, b) => a - b).map((level, i) => {
                                const levelKey = level.toFixed(2);
                                const mtfInfo = srData.meta?.mtf?.confluence_map?.[levelKey];
                                const isConfluent = mtfInfo?.confluent;
                                return (
                                  <div key={i} className={`text-gray-400 ${isConfluent ? 'font-medium' : ''}`}>
                                    {/* Day 115: surface the graduated strength_label (Strong/Moderate/Weak)
                                        instead of a flat "Confluent with weekly level" — the descriptive-
                                        state convention this redesign already uses elsewhere (Regime,
                                        Technical Read, Fundamentals). Falls back to the old text if
                                        strength_label is absent (older cached response shape). */}
                                    {isConfluent && <span className="text-yellow-400 mr-1" title={mtfInfo?.strength_label ? `Confluent with weekly level (${mtfInfo.strength_label})` : 'Confluent with weekly level'}>★</span>}
                                    R{i + 1}: <span className={`font-mono ${isConfluent ? 'text-red-200' : 'text-red-300'}`}>{formatCurrency(level)}</span>
                                    <span className="text-gray-500 ml-1">
                                      ({((level - srData.currentPrice) / srData.currentPrice * 100).toFixed(1)}% above)
                                    </span>
                                  </div>
                                );
                              })}
                            </div>
                          ) : (
                            <div className="text-gray-500 italic">None within range</div>
                          )}
                        </div>
                      </div>
                      {/* Day 33: Weekly Levels (collapsed by default) */}
                      {srData.meta?.mtf?.enabled && (srData.meta.mtf.weekly_support?.length > 0 || srData.meta.mtf.weekly_resistance?.length > 0) && (
                        <details className="mt-3 text-xs">
                          <summary className="text-gray-500 cursor-pointer hover:text-gray-400">
                            Weekly Levels ({srData.meta.mtf.weekly_support?.length || 0} support, {srData.meta.mtf.weekly_resistance?.length || 0} resistance)
                          </summary>
                          <div className="mt-2 grid grid-cols-2 gap-4 pl-2 border-l-2 border-gray-700">
                            <div>
                              {srData.meta.mtf.weekly_support?.slice().sort((a, b) => b - a).map((level, i) => (
                                <div key={i} className="text-gray-500">
                                  W-S{i + 1}: <span className="text-green-400/70 font-mono">${level.toFixed(2)}</span>
                                </div>
                              ))}
                            </div>
                            <div>
                              {srData.meta.mtf.weekly_resistance?.slice().sort((a, b) => a - b).map((level, i) => (
                                <div key={i} className="text-gray-500">
                                  W-R{i + 1}: <span className="text-red-400/70 font-mono">${level.toFixed(2)}</span>
                                </div>
                              ))}
                            </div>
                          </div>
                        </details>
                      )}
                      <div className="mt-2 text-xs text-gray-500 text-center">
                        Method: {srData.method} • ATR: {srData.meta?.atr ? `$${srData.meta.atr.toFixed(2)}` : 'N/A'}
                        {srData.meta?.mtf?.enabled && <span> • MTF: Weekly</span>}
                      </div>
                    </div>
                    </>)}
                  </div>
                )}

                {/* Day 123 (redesign Step 6): Fundamentals card, after the Trade Setup (mockup order). */}
                <FundamentalsRead
                  ticker={analysisResult.ticker}
                  fundamental={categoricalResult?.fundamental}
                  rawFundamentals={rawAnalysisData?.stock?.fundamentals}
                  earnings={earningsData}
                  quoteType={rawAnalysisData?.stock?.quoteType}
                  name={analysisResult.name}
                />

                {/* Price Structure Card — Day 72: Tier 2, between Trade Setup and Pattern Detection */}
                <PriceStructureCard
                  srData={srData}
                  priceStructure={priceStructure}
                  expanded={!!expandedSections.priceStructure}
                  onToggle={() => toggleSection('priceStructure')}
                />

                {/* Pattern Detection Card — Day 70: collapsed by default */}
                {patternsData && (
                  <div className="bg-gray-800 rounded-lg">
                    <button
                      onClick={() => toggleSection('patterns')}
                      className="flex items-center gap-2 w-full px-6 py-4 text-left hover:bg-gray-700/30 transition-colors rounded-lg"
                    >
                      <span className="text-sm text-gray-500">{expandedSections.patterns ? '▼' : '▶'}</span>
                      <span className="text-lg font-semibold text-purple-400">Pattern Detection</span>
                      {patternsData.summary?.count > 0 && (
                        <span className="ml-2 px-2 py-0.5 rounded-full text-xs font-bold bg-purple-900/50 text-purple-300 border border-purple-600">
                          {patternsData.summary.count} Pattern{patternsData.summary.count > 1 ? 's' : ''}
                        </span>
                      )}
                      <span className="ml-auto text-xs text-gray-500">
                        {patternsData.summary?.bestPattern || 'No strong patterns'}
                      </span>
                    </button>
                    {expandedSections.patterns && (
                    <div className="px-6 pb-6">
                    <div className="flex justify-between items-center mb-4">
                      <h3 className="text-lg font-semibold text-purple-400">VCP, Cup & Handle, Flat Base</h3>
                    </div>

                    {/* Trend Template Score */}
                    {patternsData.trendTemplate && (
                      <div className="mb-4 p-3 rounded-lg bg-gray-700/50 border border-gray-600">
                        <div className="flex justify-between items-center mb-2">
                          <span className="text-gray-300 font-medium cursor-help" title="Mark Minervini's 8-point Trend Template. Stocks meeting 7+/8 criteria are in a Stage 2 uptrend - ideal for swing trades.">
                            Trend Template
                          </span>
                          <span className={`font-bold ${
                            patternsData.trendTemplate.criteria_met >= 7 ? 'text-green-400' :
                            patternsData.trendTemplate.criteria_met >= 5 ? 'text-yellow-400' :
                            'text-red-400'
                          }`}>
                            {patternsData.trendTemplate.criteria_met}/8
                          </span>
                        </div>
                        <div className="grid grid-cols-2 gap-1 text-xs">
                          {Object.entries(patternsData.trendTemplate.criteria || {}).map(([key, value]) => (
                            <div key={key} className="flex items-center gap-1">
                              <span className={value ? 'text-green-400' : 'text-red-400'}>{value ? '✓' : '✗'}</span>
                              <span className="text-gray-400">{key.replace(/_/g, ' ')}</span>
                            </div>
                          ))}
                        </div>
                        {patternsData.trendTemplate.in_stage2_uptrend && (
                          <div className="mt-2 text-xs text-green-400 font-medium">
                            ✅ In Stage 2 Uptrend (ideal for swing trades)
                          </div>
                        )}
                      </div>
                    )}

                    {/* Pattern Cards — Day 83: 3 copy-pasted blocks replaced with PatternMiniCard */}
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                      <PatternMiniCard
                        title="VCP"
                        tooltip="Volatility Contraction Pattern (VCP) - Mark Minervini's signature pattern. Price makes a series of smaller pullbacks, showing selling pressure drying up before breakout."
                        pattern={patternsData.patterns?.vcp}
                        highlightStatus="at_pivot"
                        statRows={[
                          { label: 'Contractions', value: patternsData.patterns?.vcp?.contractions_count || 0 },
                          {
                            label: 'Tight Base',
                            value: patternsData.patterns?.vcp?.tight_base ? 'Yes' : 'No',
                            colorClass: patternsData.patterns?.vcp?.tight_base ? 'text-green-400' : 'text-gray-500',
                          },
                        ]}
                        description="Sellers exhausted — each pullback smaller. Lowest risk breakout entry."
                      />
                      <PatternMiniCard
                        title="Cup & Handle"
                        tooltip="Cup and Handle - William O'Neil's classic pattern. U-shaped cup formation followed by a small handle pullback before breakout."
                        pattern={patternsData.patterns?.cupHandle}
                        highlightStatus="complete"
                        statRows={[
                          { label: 'Cup Depth', value: `${patternsData.patterns?.cupHandle?.cup?.depth_pct?.toFixed(1) || 'N/A'}%` },
                          {
                            label: 'U-Shaped',
                            value: patternsData.patterns?.cupHandle?.cup?.u_shaped ? 'Yes' : 'No',
                            colorClass: patternsData.patterns?.cupHandle?.cup?.u_shaped ? 'text-green-400' : 'text-gray-500',
                          },
                        ]}
                        description="Institutional accumulation. Handle shakes out weak hands before real move."
                      />
                      <PatternMiniCard
                        title="Flat Base"
                        tooltip="Flat Base - Tight consolidation after a strong uptrend. Price moves sideways in a narrow range as the stock digests gains before continuing higher."
                        pattern={patternsData.patterns?.flatBase}
                        highlightStatus="forming"
                        statRows={[
                          { label: 'Range', value: `${patternsData.patterns?.flatBase?.base?.range_pct?.toFixed(1) || 'N/A'}%` },
                          {
                            label: 'Prior Uptrend',
                            value: `${patternsData.patterns?.flatBase?.prior_uptrend?.pct?.toFixed(0) || 'N/A'}%`,
                            colorClass: patternsData.patterns?.flatBase?.prior_uptrend?.has_30pct_move ? 'text-green-400' : 'text-gray-500',
                          },
                        ]}
                        description="Digesting gains in tight range. Compression before next leg up."
                      />
                    </div>

                    {/* Day 47: Actionable Patterns Section (≥60% confidence only) */}
                    {actionablePatternsData?.summary?.hasActionable && (
                      <div className="mt-4 p-3 bg-green-900/20 border border-green-600 rounded-lg">
                        <div className="flex items-center gap-2 mb-3">
                          <span className="text-green-400 font-semibold">✅ Actionable Patterns</span>
                          <span className="text-xs text-gray-400">(≥60% confidence)</span>
                        </div>
                        <div className="space-y-3">
                          {actionablePatternsData.actionablePatterns.map((pattern, idx) => (
                            <div key={idx} className="bg-gray-800/50 rounded p-3">
                              <div className="flex justify-between items-center mb-2">
                                <div className="flex items-center gap-2">
                                  <span className="font-medium text-green-300">{pattern.name}</span>
                                  {/* Breakout Quality Badge */}
                                  {pattern.breakout?.quality && (
                                    <span className={`text-xs px-1.5 py-0.5 rounded ${
                                      pattern.breakout.quality === 'High' ? 'bg-green-600 text-white' :
                                      pattern.breakout.quality === 'Medium' ? 'bg-yellow-600 text-white' :
                                      pattern.breakout.quality === 'Low' ? 'bg-red-600 text-white' :
                                      pattern.breakout.quality === 'Approaching' ? 'bg-blue-600 text-white' :
                                      'bg-gray-600 text-gray-200'
                                    }`} title={pattern.breakout.reasons?.join(' | ')}>
                                      {pattern.breakout.quality} Breakout
                                    </span>
                                  )}
                                </div>
                                <span className="text-xs px-2 py-0.5 bg-green-600 text-white rounded">
                                  {pattern.confidence}%
                                </span>
                              </div>
                              <div className="grid grid-cols-3 gap-2 text-xs mb-2">
                                <div className="text-center p-1 bg-gray-700/50 rounded">
                                  <div className="text-gray-400">Trigger</div>
                                  <div className="text-blue-400 font-mono font-medium">${pattern.triggerPrice?.toFixed(2)}</div>
                                </div>
                                <div className="text-center p-1 bg-gray-700/50 rounded">
                                  <div className="text-gray-400">Stop</div>
                                  <div className="text-red-400 font-mono font-medium">${pattern.stopPrice?.toFixed(2)}</div>
                                </div>
                                <div className="text-center p-1 bg-gray-700/50 rounded">
                                  <div className="text-gray-400">Target</div>
                                  <div className="text-green-400 font-mono font-medium">
                                    {pattern.targetPrice != null ? `$${pattern.targetPrice.toFixed(2)}` : '—'}
                                  </div>
                                </div>
                              </div>
                              {/* Day 112: show where the target number comes from (measured move vs. legacy flat %).
                                  Day 118: VCP's flat_pct_legacy basis retired — replaced by 'resistance' /
                                  'vcp_contraction' (real structural target, Phase 4). */}
                              {pattern.targetBasis && (
                                <div className="text-[11px] text-gray-500 mb-2">
                                  {pattern.targetBasis === 'cup_depth' ? 'Target = pivot + cup depth (measured move)' :
                                   pattern.targetBasis === 'base_depth' ? 'Target = pivot + base height (measured move)' :
                                   pattern.targetBasis === 'resistance' ? `Target = nearest real resistance ($${pattern.targetPrice?.toFixed(2)})` :
                                   pattern.targetBasis === 'vcp_contraction' ? 'Target = pivot + largest contraction depth (no real resistance overhead)' :
                                   null}
                                </div>
                              )}
                              {pattern.targetPrice == null && (
                                <div className="text-[11px] text-gray-500 mb-2">
                                  No structural target — pattern geometry unavailable for this ticker.
                                </div>
                              )}
                              {/* Volume Confirmation Row */}
                              {pattern.breakout?.volumeRatio != null && (
                                <div className="flex items-center gap-2 text-xs mb-2">
                                  <span className={pattern.breakout.volumeConfirmed ? 'text-green-400' : 'text-yellow-400'}>
                                    {pattern.breakout.volumeConfirmed ? '✓' : '⚠'} Volume: {pattern.breakout.volumeRatio}x avg
                                  </span>
                                  <span className="text-gray-500">
                                    {pattern.breakout.volumeConfirmed ? '(confirmed ≥1.5x)' : '(needs 1.5x+ for confirmation)'}
                                  </span>
                                </div>
                              )}
                              <div className="flex justify-between items-center text-xs">
                                <span className="text-gray-400">{pattern.riskReward != null ? `R:R ${pattern.riskReward}:1` : 'R:R —'}</span>
                                <span className={`${
                                  pattern.breakout?.isTradeable ? 'text-green-400 font-medium' :
                                  pattern.status === 'at_pivot' || pattern.status === 'complete' ? 'text-yellow-400' :
                                  pattern.status === 'broken_out' ? 'text-green-400' :
                                  'text-gray-400'
                                }`}>
                                  {pattern.breakout?.isTradeable ? '🎯 Ready to Trade' : pattern.action}
                                </span>
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Day 47: Patterns below threshold (transparency) */}
                    {actionablePatternsData?.belowThreshold?.length > 0 && (
                      <div className="mt-2 p-2 bg-gray-700/30 rounded-lg">
                        <div className="text-xs text-gray-500">
                          Patterns below 60% threshold:{' '}
                          {actionablePatternsData.belowThreshold.map((p, i) => (
                            <span key={i} className="text-gray-400">
                              {p.name} ({p.confidence}%)
                              {i < actionablePatternsData.belowThreshold.length - 1 ? ', ' : ''}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Summary */}
                    {patternsData.summary?.bestPattern && !actionablePatternsData?.summary?.hasActionable && (
                      <div className="mt-3 p-2 bg-purple-900/30 rounded-lg text-center text-sm">
                        <span className="text-purple-300">Best Pattern: </span>
                        <span className="font-semibold text-purple-200">{patternsData.summary.bestPattern}</span>
                        <span className="text-purple-300"> ({patternsData.summary.bestConfidence}% confidence)</span>
                        <div className="text-xs text-gray-400 mt-1">
                          Below 60% actionability threshold
                        </div>
                      </div>
                    )}

                    <div className="mt-3 text-xs text-gray-500 text-center">
                      Data: Multi-Source (OHLCV) • Quality: algorithmic detection • Threshold: ≥60% for actionability
                    </div>
                    </div>
                    )}
                  </div>
                )}

                {/* TradingView Chart removed Day 70 — simplicity premium (S&R in Trade Setup is sufficient) */}

                {/* BottomLineCard removed Day 82 — redundant with the Verdict Card
                    (top of page) and Categorical Assessment card (below): same
                    BUY/HOLD/AVOID verdict and the same underlying tech/fund/risk
                    facts, just reworded a third time. */}

                {/* Day 82: Breakout state card — single-ticker /api/breakout/<ticker>,
                    same 8-state engine and badge styling as the Scan tab's batch
                    column. State only, never a signal (BREAKOUT_ENGINE_SPEC.md §13). */}
                {/* Day 83 fix (Task E1): loading skeleton (was missing — card just
                    popped in with no feedback while fetching); p-6/text-lg to match
                    neighbor cards (was p-4/text-sm); removed the mb-4 (parent already
                    uses space-y-6, so it was double-spacing); surfaces breakoutLevel
                    and active warnings, previously fetched but silently dropped. */}
                {breakoutLoading && (
                  <div className="bg-gray-800 rounded-lg p-6 animate-pulse">
                    <div className="h-4 bg-gray-700 rounded w-1/3"></div>
                  </div>
                )}
                {!breakoutLoading && breakoutData && !breakoutData.error && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <div className="flex items-center justify-between mb-2">
                      <h3 className="text-lg font-semibold text-gray-300">🚀 Breakout Status</h3>
                      {(() => {
                        const cfg = BREAKOUT_BADGE_CONFIG[breakoutData.status];
                        if (!cfg) return <span className="text-xs text-gray-500">{breakoutData.status}</span>;
                        return (
                          <span className={`text-xs font-medium px-2 py-0.5 rounded border ${cfg.color}`}>
                            {cfg.label}
                          </span>
                        );
                      })()}
                    </div>
                    <p className="text-sm text-gray-400">{breakoutData.humanAction}</p>
                    <div className="flex flex-wrap gap-3 mt-1">
                      {breakoutData.rvol != null && (
                        <p className="text-xs text-gray-500">RVOL: {breakoutData.rvol.toFixed(2)}x</p>
                      )}
                      {breakoutData.breakoutLevel != null && (
                        <p className="text-xs text-gray-500">Breakout Level: {formatCurrency(breakoutData.breakoutLevel)}</p>
                      )}
                    </div>
                    {breakoutData.warnings && Object.values(breakoutData.warnings).some(Boolean) && (
                      <div className="mt-2 flex flex-wrap gap-1">
                        {Object.entries(breakoutData.warnings)
                          .filter(([, active]) => active)
                          .map(([key]) => (
                            <span
                              key={key}
                              className="text-xs px-2 py-0.5 rounded border bg-red-900/40 text-red-400 border-red-700"
                            >
                              {key.replace(/([A-Z])/g, ' $1').replace(/^./, c => c.toUpperCase())}
                            </span>
                          ))}
                      </div>
                    )}
                  </div>
                )}

                {/* Day 123 (redesign Step 6): Assessment Breakdown, Raw Indicators and Quality Gate Warnings
                    removed. Their content lives in the Technical Read (trend, RS), market band (risk),
                    Fundamentals card and Price & RS card (liquidity); the BUY/HOLD/AVOID verdict is no
                    longer shown anywhere (user decision). */}
              </div>
            )}

            {/* ==================== SIMPLIFIED VIEW (Day 27) ==================== */}
            {analysisResult && !loading && analysisView === 'simple' && simplifiedResult && (
              <div className="space-y-6">
                {/* Simplified Verdict Card */}
                <div className={`rounded-lg p-6 ${
                  simplifiedResult.verdict === 'TRADE' ? 'bg-green-600' : 'bg-gray-700'
                }`}>
                  <div className="flex justify-between items-center">
                    <div>
                      <h2 className="text-2xl font-bold">{analysisResult.ticker} - {analysisResult.name}</h2>
                      <p className="text-white/80">
                        {describeClassification(analysisResult.sector, analysisResult.industry, rawAnalysisData?.stock?.quoteType)}
                        {(() => {
                          const sc = getSectorContext(analysisResult.sector);
                          if (!sc) return null;
                          const qColors = { Leading: 'bg-green-700', Weakening: 'bg-yellow-700', Lagging: 'bg-red-700', Improving: 'bg-blue-700' };
                          return (
                            <span className={`ml-2 px-1.5 py-0.5 rounded text-xs font-medium text-white ${qColors[sc.quadrant] || 'bg-gray-600'}`}
                              title={`${sc.name} (${sc.etf}) — RS: ${sc.rsRatio} | Mom: ${sc.rsMomentum > 0 ? '+' : ''}${sc.rsMomentum} | Rank: ${sc.rank}/11`}>
                              {sc.etf} {sc.quadrant.toUpperCase()}
                            </span>
                          );
                        })()}
                        {breakoutData && !breakoutData.error && (() => {
                          const cfg = BREAKOUT_BADGE_CONFIG[breakoutData.status];
                          if (!cfg) return null;
                          return (
                            <span
                              className={`ml-2 px-1.5 py-0.5 rounded text-xs font-medium border ${cfg.color}`}
                              title={breakoutData.humanAction || cfg.label}
                            >
                              {cfg.label}
                            </span>
                          );
                        })()}
                      </p>
                    </div>
                    <div className="text-right">
                      <div className="text-4xl font-bold">
                        {simplifiedResult.verdict === 'TRADE' ? '✅ TRADE' : '⏸️ No Trade'}
                      </div>
                      <div className="text-xl">{simplifiedResult.passCount}/{simplifiedResult.totalCriteria} criteria met</div>
                    </div>
                  </div>
                </div>

                {/* 9 Binary Criteria Cards */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  {Object.entries(simplifiedResult.criteria).map(([key, criterion]) => (
                    <div
                      key={key}
                      className={`rounded-lg p-5 border-2 ${
                        criterion.pass
                          ? 'bg-green-900/30 border-green-600'
                          : 'bg-red-900/20 border-red-700/50'
                      }`}
                    >
                      <div className="flex items-start justify-between mb-2">
                        <div className="flex items-center gap-3">
                          <span className="text-3xl">
                            {criterion.pass ? '✅' : '❌'}
                          </span>
                          <div>
                            <h4 className="font-bold text-lg">
                              {criterion.label}
                            </h4>
                            <span className={`text-sm ${criterion.pass ? 'text-green-400' : 'text-red-400'}`}>
                              {criterion.pass ? 'PASS' : 'FAIL'}
                            </span>
                          </div>
                        </div>
                      </div>
                      <p className="text-sm text-gray-300 mt-2">
                        {criterion.reason}
                      </p>
                      {/* Day 117: absolute momentum — dual momentum's second leg,
                          shown only on the Momentum card, using the SAME 1-year
                          return the RS gate above just evaluated
                          (simplifiedScoring.js). Informational only: it is not a
                          tenth criterion, it never changes `pass`, `passCount`,
                          `totalCriteria`, `verdict` or `summary`, and no other
                          criterion renders it (explicit `key === 'momentum'`
                          rather than a generic field, so the shared card shape
                          stays a pass/fail shape).
                          docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md */}
                      {key === 'momentum' && (() => {
                        const abs = getAbsoluteMomentumRead(criterion.stockReturnPct);
                        if (!abs) return null;
                        return (
                          <p
                            className="text-xs text-gray-400 mt-2 pt-2 border-t border-gray-600/50"
                            title="Dual momentum's second leg (Antonacci, 2014). The criterion above asks whether the stock beat SPY; this asks whether it beat cash. Note that whenever SPY's own trailing year is above the cash bar, passing the criterion above already implies clearing this one — this line only tells you something new in a flat or falling market. The 5% figure is a static risk-free proxy from this project's own Day 107 backtest, not a live T-bill yield. Informational only — it is not one of the 9 criteria and does not affect the pass/fail count or the verdict."
                          >
                            <span className="text-gray-500">Absolute momentum (info only, not one of the 9): </span>{abs.text}
                          </p>
                        );
                      })()}
                    </div>
                  ))}
                </div>

                {/* Decision Summary */}
                <div className={`rounded-lg p-6 ${
                  simplifiedResult.verdict === 'TRADE'
                    ? 'bg-green-900/30 border border-green-600'
                    : 'bg-gray-800 border border-gray-600'
                }`}>
                  <h3 className="text-lg font-semibold mb-3">
                    {simplifiedResult.verdict === 'TRADE' ? '🎯 Trade Decision' : '⏸️ No Trade'}
                  </h3>
                  <p className="text-gray-300 mb-4">{simplifiedResult.summary}</p>

                  {simplifiedResult.verdict === 'TRADE' && srData && (
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4 pt-4 border-t border-gray-700">
                      <div className="text-center">
                        <div className="text-gray-400 text-sm">Entry</div>
                        <div className="text-xl font-bold text-green-400">{formatCurrency(srData.suggestedEntry)}</div>
                      </div>
                      <div className="text-center">
                        <div className="text-gray-400 text-sm">Stop</div>
                        {/* Day 123: backend leaves suggestedStop empty when ATR is missing (was a fake 3%). */}
                        {srData.suggestedStop != null
                          ? <div className="text-xl font-bold text-red-400">{formatCurrency(srData.suggestedStop)}</div>
                          : <div className="text-sm text-gray-400 mt-1">unavailable (no ATR)</div>}
                      </div>
                      <div className="text-center">
                        <div className="text-gray-400 text-sm">Target</div>
                        <div className="text-xl font-bold text-blue-400">{formatCurrency(srData.suggestedTarget)}</div>
                      </div>
                      <div className="text-center">
                        <div className="text-gray-400 text-sm">R:R</div>
                        <div className="text-xl font-bold text-yellow-400">
                          {srData.riskReward != null ? `${srData.riskReward.toFixed(2)}:1` : 'N/A'}
                        </div>
                      </div>
                    </div>
                  )}

                  {/* Day 123: say why the sizing button is missing instead of hiding it silently */}
                  {simplifiedResult.verdict === 'TRADE' && srData?.suggestedEntry && srData.suggestedStop == null && (
                    <div className="mt-4 text-sm text-gray-400">Position sizing needs a stop, and the stop is unavailable (ATR missing).</div>
                  )}
                  {/* Calculate Position Button - Day 28 Integration */}
                  {simplifiedResult.verdict === 'TRADE' && srData?.suggestedEntry && srData?.suggestedStop && (
                    <button
                      onClick={() => autoFillPositionCalculator(
                        analysisResult?.ticker || ticker,
                        srData.suggestedEntry,
                        srData.suggestedStop
                      )}
                      className="w-full mt-4 bg-purple-600 hover:bg-purple-700 px-6 py-3 rounded-lg font-semibold transition-colors flex items-center justify-center gap-2"
                    >
                      📊 Calculate Position Size →
                    </button>
                  )}
                </div>

                {/* Methodology Note */}
                <div className="bg-gray-800/50 rounded-lg p-4 text-xs text-gray-500">
                  <p><strong>Simplified Binary System</strong> - Day 27, enhanced Day 60 with Minervini SEPA + backtest-validated filters</p>
                  <p className="mt-1">Based on: AQR Momentum Research • Turtle Trading Principles • Minervini SEPA Criteria • Holistic 3-Layer Backtest</p>
                  <p className="mt-2 text-gray-400">
                    <strong>Rule:</strong> ALL 9 criteria must be YES to take a trade. Any NO = no trade. No exceptions.
                  </p>
                </div>

                {/* Day 123 (Step 6): the "Full Assessment (for comparison)" BUY/HOLD/AVOID strip is removed
                    (verdict no longer shown anywhere); the link to the full view stays. */}
                <div className="bg-gray-800 rounded-lg p-4 flex justify-end">
                  <button
                    onClick={() => setAnalysisView('full')}
                    className="text-blue-400 hover:text-blue-300 text-sm"
                  >
                    View Full Analysis →
                  </button>
                </div>
              </div>
            )}

            {/* Empty State */}
            {!analysisResult && !loading && !error && (
              <div className="bg-gray-800 rounded-lg p-12 text-center">
                <div className="text-6xl mb-4">📊</div>
                <h3 className="text-xl font-bold text-gray-300 mb-2">Analyze a Stock</h3>
                <p className="text-gray-500 mb-4">
                  Enter a ticker symbol or click a quick pick to analyze a stock.
                </p>
                <p className="text-gray-600 text-sm">
                  9-criterion Simple Checklist • Multi-Engine Trend, Reversion & Value Analysis
                </p>
              </div>
            )}
          </>
        )}

        {/* ==================== SCAN TAB ==================== */}
        {activeTab === 'scan' && (
          <>
            {/* Strategy & Market Index Selector */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <div className="flex gap-4 items-center">
                <select
                  value={selectedStrategy}
                  onChange={(e) => setSelectedStrategy(e.target.value)}
                  className="flex-1 bg-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="nirmal">👁 Nirmal's Watchlist — 20 curated picks</option>
                  <option value="masterFramework">🏛️ Master Framework Watchlist — 76 curated picks</option>
                  <option value="hub">🔬 HUB-65 Watchlist — 64 curated picks</option>
                  {strategies ? (
                    (strategies.strategies || []).map((strategy) => (
                      <option key={strategy.id} value={strategy.id}>{strategy.name}: {strategy.description}</option>
                    ))
                  ) : (
                    <>
                      <option value="reddit">Reddit - Popular momentum</option>
                      <option value="minervini">Large-Cap Momentum Filter</option>
                      <option value="momentum">Momentum - Strong 52w</option>
                      <option value="value">Value - Quality discounts</option>
                      <option value="best">Best Candidates - Backtested Config C picks</option>
                      <option value="breakout">🚀 Near Breakout - Within 8% of 52W high</option>
                    </>
                  )}
                </select>
                <select
                  value={selectedMarketIndex}
                  onChange={(e) => setSelectedMarketIndex(e.target.value)}
                  className="bg-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="all">All US Stocks</option>
                  <option value="sp500">S&P 500</option>
                  <option value="nasdaq100">NASDAQ 100</option>
                  <option value="dow30">Dow 30</option>
                  <option disabled>──────────</option>
                  <option value="tsx60">TSX 60 (Canada)</option>
                  <option value="canada">All Canadian Stocks</option>
                </select>
                <button
                  onClick={runScan}
                  disabled={scanLoading}
                  className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-lg font-semibold disabled:opacity-50"
                >
                  {scanLoading ? '⏳ Scanning...' : '🔍 Scan'}
                </button>
              </div>

              {/* Day 111: Mean-Reversion scanner — separate system, own button.
                  Day 124: the old "confirmed Day 111 (PF 2.75)" was priced at the entry-day
                  close (Golden Rule 60). The honest next-open record lives on the Analyze
                  page's MR card and the Forward Test tab (one source: get_mr_track_record). */}
              <div className="flex items-center gap-3 mt-4 pt-4 border-t border-gray-700">
                <span className="text-sm text-gray-400 flex-1">
                  Or check the 54-ticker liquid universe for active Mean-Reversion signals
                  (RSI(2)&lt;10, above 200-SMA, $10+/$25M+ ADV) — the one positive forward-test edge;
                  its next-open track record is on each stock's Mean-Reversion card.
                </span>
                <button
                  onClick={runMrScan}
                  disabled={mrScanLoading}
                  className="bg-teal-600 hover:bg-teal-700 px-6 py-2.5 rounded-lg font-semibold disabled:opacity-50 text-sm whitespace-nowrap"
                >
                  {mrScanLoading ? '⏳ Scanning...' : '🔄 MR Signals'}
                </button>
              </div>
            </div>

            {/* Day 111: MR scan error */}
            {mrScanError && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6">
                <p className="text-red-200 font-medium">MR Scan Error</p>
                <p className="text-red-300 text-sm mt-1">{mrScanError}</p>
              </div>
            )}

            {/* Day 111: MR scan results */}
            {mrScanResults && !mrScanLoading && (
              <div className="bg-gray-800 rounded-lg p-6 mb-6 border border-teal-700/40">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-lg font-semibold text-teal-400">
                    🔄 Mean-Reversion Signals — {mrScanResults.found} of {mrScanResults.scanned} tickers
                  </h3>
                </div>
                {mrScanResults.found === 0 ? (
                  <p className="text-gray-400 text-sm">
                    No active MR signals right now — that's the common state, not an error.
                    RSI(2)&lt;10 is a genuine short-term extreme; most days, most tickers won't qualify.
                  </p>
                ) : (
                  <div className="space-y-2">
                    {mrScanResults.signals.map((signal) => (
                      <div
                        key={signal.ticker}
                        onClick={() => analyzeStock(signal.ticker)}
                        className="flex items-center justify-between bg-gray-700/60 hover:bg-gray-700 rounded-lg px-4 py-3 cursor-pointer transition-colors"
                      >
                        <div className="flex items-center gap-4">
                          <span className="font-bold text-white w-16">{signal.ticker}</span>
                          <span className="text-sm text-gray-300">RSI(2) <span className="text-teal-400 font-medium">{signal.rsi2}</span></span>
                          <span className="text-sm text-gray-300">${signal.current_price}</span>
                        </div>
                        <div className="flex items-center gap-4 text-sm text-gray-400">
                          {/* Day 123: the tested plan, not the old ATR stop / +2 ATR target (never tested) */}
                          <span>{signal.rules ? `Tested plan: buy the open after the signal · stop ${Math.round(signal.rules.stop_pct * 100)}% below fill` : 'plan unavailable'}</span>
                          <span className="text-gray-500">{signal.exit_rule}</span>
                          {signal.asOf && <span className="text-gray-500">as of {signal.asOf} close</span>}
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* Day 62: Sector filter banner */}
            {sectorFilter && (
              <div className="bg-green-900/40 border border-green-600/60 rounded-lg p-3 mb-4 flex items-center justify-between">
                <span className="text-green-300 text-sm">
                  🔄 Filtering by: <span className="font-semibold">{sectorFilter.name} ({sectorFilter.etf})</span>
                  <span className={`ml-2 text-xs px-2 py-0.5 rounded ${
                    sectorFilter.quadrant === 'Leading' ? 'bg-green-700 text-green-100' :
                    sectorFilter.quadrant === 'Improving' ? 'bg-blue-700 text-blue-100' :
                    sectorFilter.quadrant === 'Weakening' ? 'bg-yellow-700 text-yellow-100' :
                    'bg-red-700 text-red-100'
                  }`}>{sectorFilter.quadrant} · Rank #{sectorFilter.rank}</span>
                  <span className="text-green-500 ml-2 text-xs">— scan results filtered to this sector</span>
                </span>
                <button
                  onClick={() => setSectorFilter(null)}
                  className="text-green-400 hover:text-white text-sm px-2 py-0.5 rounded hover:bg-green-700/40 transition-colors"
                >
                  ✕ Clear
                </button>
              </div>
            )}

            {/* Scan Error */}
            {scanError && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6">
                <p className="text-red-200 font-medium">Backend Error</p>
                <p className="text-red-300 text-sm mt-1">{scanError}</p>
                <p className="text-red-400 text-xs mt-2">Check that the backend is running on port 5001 and TradingView screener is installed.</p>
              </div>
            )}

            {/* Scan Results */}
            {scanResults && !scanLoading && (() => {
              // Compute filtered candidates once — used for count AND rows
              // Uses getSectorContext mapping (ETF lookup) instead of string-match,
              // because TradingView sector names differ from GICS/SPDR names.
              // e.g. TradingView "Non-Energy Minerals" → XLB (Materials)
              const filteredCandidates = sectorFilter
                ? (scanResults.candidates || []).filter(s =>
                    getSectorContext(s.sector)?.etf === sectorFilter.etf
                  )
                : (scanResults.candidates || []);
              return (
              <div className="bg-gray-800 rounded-lg p-6">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-lg font-semibold text-blue-400">
                    📋 Scan Results: {scanResults.strategy}
                    {scanResults.marketIndex && scanResults.marketIndex !== 'all' && (
                      <span className="ml-2 text-sm font-normal text-yellow-400">
                        ({scanResults.marketIndex === 'sp500' ? 'S&P 500' : scanResults.marketIndex === 'nasdaq100' ? 'NASDAQ 100' : scanResults.marketIndex === 'dow30' ? 'Dow 30' : scanResults.marketIndex === 'tsx60' ? 'TSX 60' : scanResults.marketIndex === 'canada' ? 'All Canadian' : scanResults.marketIndex})
                      </span>
                    )}
                  </h3>
                  <span className="text-gray-400 text-sm">
                    {sectorFilter
                      ? `${filteredCandidates.length} of ${scanResults.returned} showing (${sectorFilter.name} filter)`
                      : `${scanResults.returned} of ${scanResults.totalMatches} matches`}
                  </span>
                </div>

                {/* Empty-state when sector filter returns nothing */}
                {sectorFilter && filteredCandidates.length === 0 && (
                  <div className="text-center py-8 text-gray-400">
                    <div className="text-3xl mb-2">🔍</div>
                    <p className="font-medium">No <span className="text-yellow-400">{sectorFilter.name}</span> stocks in current scan results</p>
                    <p className="text-sm text-gray-500 mt-1">
                      The current scan returned {scanResults.returned} candidates — none are in the {sectorFilter.name} sector.
                    </p>
                    <p className="text-sm text-gray-500 mt-1">
                      Run a new scan with the sector filter active to find {sectorFilter.name} stocks meeting the criteria.
                    </p>
                  </div>
                )}

                {/* Results Table */}
                {filteredCandidates.length > 0 && (
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="text-gray-400 border-b border-gray-700">
                        <th className="text-left py-3 px-2">Ticker</th>
                        <th className="text-left py-3 px-2">Name</th>
                        <th className="text-left py-3 px-2">Sector</th>
                        <th className="text-right py-3 px-2">Price</th>
                        <th className="text-right py-3 px-2">Change</th>
                        <th className="text-right py-3 px-2">Volume</th>
                        <th className="text-right py-3 px-2">Market Cap</th>
                        <th className="text-center py-3 px-2">Breakout</th>
                        <th className="text-center py-3 px-2">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredCandidates.map((stock) => (
                        <tr key={stock.ticker} className="border-b border-gray-700/50 hover:bg-gray-700/30">
                          <td className="py-3 px-2 font-bold text-blue-400">{stock.ticker}</td>
                          <td className="py-3 px-2 text-gray-300">{stock.name?.slice(0, 30)}</td>
                          <td className="py-3 px-2">
                            {(() => {
                              const sc = getSectorContext(stock.sector);
                              if (!sc) return <span className="text-gray-500 text-xs">{stock.sector || '—'}</span>;
                              const qColors = { Leading: 'text-green-400', Weakening: 'text-yellow-400', Lagging: 'text-red-400', Improving: 'text-blue-400' };
                              return (
                                <span className={`text-xs font-medium ${qColors[sc.quadrant] || 'text-gray-400'}`}
                                  title={`${sc.name} (${sc.etf}) — RS: ${sc.rsRatio} | Mom: ${sc.rsMomentum > 0 ? '+' : ''}${sc.rsMomentum} | Rank: ${sc.rank}/11`}>
                                  {sc.etf} {sc.quadrant}
                                </span>
                              );
                            })()}
                          </td>
                          <td className="py-3 px-2 text-right font-mono">{formatCurrency(stock.price)}</td>
                          <td className={`py-3 px-2 text-right ${stock.change >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                            {stock.change != null ? formatPercent(stock.change) : 'N/A'}
                          </td>
                          <td className="py-3 px-2 text-right text-gray-400">
                            {stock.volume ? (stock.volume / 1e6).toFixed(1) + 'M' : 'N/A'}
                          </td>
                          <td className="py-3 px-2 text-right text-gray-400">{formatMarketCap(stock.marketCap)}</td>
                          <td className="py-3 px-2 text-center">
                            {/* Day 81 (Breakout Enhancement Plan Task 2.2): badge is STATE, not a
                                signal — never render a green badge as a buy recommendation
                                (BREAKOUT_ENGINE_SPEC.md §13/§15, a hard rule). Explicit != null
                                checks throughout (Day 68 falsy-render gotcha).
                                Day 106 fix: this cell used to collapse "beyond the 20-row cap",
                                "batch call failed", "per-ticker data error", and a genuine
                                NOT_READY engine result into one indistinguishable "—" glyph
                                (ROADMAP.md priority #9). Each now gets its own honest, still-muted
                                label instead of hiding behind a dash (Golden Rule: visible state
                                over hidden — a bare "—" reads as broken, not as "nothing to see
                                here"). */}
                            {(() => {
                              if (breakoutBadgesLoading) {
                                return <span className="text-gray-600 text-xs">…</span>;
                              }
                              if (!breakoutBadgesRequested.has(stock.ticker)) {
                                return (
                                  <span className="text-gray-600 text-xs" title="Beyond the top-20 rows checked per scan — see note below the table">
                                    Not checked
                                  </span>
                                );
                              }
                              const b = breakoutBadges[stock.ticker];
                              if (b == null) {
                                return (
                                  <span className="text-gray-500 text-xs" title="Requested, but no result came back (the batch call may have failed)">
                                    Unavailable
                                  </span>
                                );
                              }
                              if (b.error != null) {
                                return (
                                  <span className="text-amber-600/80 text-xs" title={b.error}>
                                    Data error
                                  </span>
                                );
                              }
                              const cfg = BREAKOUT_BADGE_CONFIG[b.status] || BREAKOUT_BADGE_CONFIG.NOT_READY;
                              if (cfg == null) {
                                return <span className="text-gray-500 text-xs">{b.status}</span>;
                              }
                              return (
                                <span
                                  className={`text-xs font-medium px-2 py-0.5 rounded border ${cfg.color}`}
                                  title={b.humanAction || cfg.label}
                                >
                                  {cfg.label}
                                </span>
                              );
                            })()}
                          </td>
                          <td className="py-3 px-2 text-center">
                            <button
                              onClick={() => analyzeStock(stock.ticker)}
                              className="bg-blue-600 hover:bg-blue-700 px-3 py-1 rounded text-xs"
                            >
                              Analyze
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                  {/* Day 83 (Task E4) + Day 106: rows beyond the batch endpoint's 20-ticker
                      cap now render their own "Not checked" label per-row (see the Breakout
                      column above) — this note is a secondary, at-a-glance summary of the
                      same fact, not the only place it's surfaced anymore. */}
                  {filteredCandidates.length > 20 && (
                    <div className="text-xs text-gray-500 text-center mt-3">
                      Breakout status checked for top 20 results only.
                    </div>
                  )}
                </div>
                )}

                {/* No matching stocks message (no sector filter, scan truly empty) */}
                {!sectorFilter && (!scanResults.candidates || scanResults.candidates.length === 0) && (
                  <div className="text-center py-8 text-gray-400">
                    <div className="text-3xl mb-2">📭</div>
                    <p className="font-medium">No stocks matched the {scanResults.strategy} criteria</p>
                    <p className="text-sm text-gray-500 mt-1">
                      {scanResults.marketIndex && scanResults.marketIndex !== 'all'
                        ? `Try broadening the market filter (currently: ${scanResults.marketIndex === 'sp500' ? 'S&P 500' : scanResults.marketIndex === 'nasdaq100' ? 'NASDAQ 100' : scanResults.marketIndex === 'dow30' ? 'Dow 30' : scanResults.marketIndex === 'tsx60' ? 'TSX 60' : 'All Canadian'}) or switching strategy.`
                        : 'Try a different strategy or check back when market conditions change.'}
                    </p>
                  </div>
                )}
              </div>
              );
            })()}

            {/* Loading State */}
            {scanLoading && (
              <div className="bg-gray-800 rounded-lg p-12 text-center">
                <div className="text-4xl mb-4">🔍</div>
                <p className="text-gray-400">Scanning market for {selectedStrategy} candidates...</p>
              </div>
            )}

            {/* Empty State */}
            {!scanResults && !scanLoading && !scanError && (
              <div className="bg-gray-800 rounded-lg p-12 text-center">
                <div className="text-6xl mb-4">🔍</div>
                <h3 className="text-xl font-bold text-gray-300 mb-2">Market Scanner</h3>
                <p className="text-gray-500 mb-4">
                  Select a strategy and click "Scan" to find trading opportunities.
                </p>
                <p className="text-gray-600 text-sm">
                  Powered by TradingView Screener • S&P 500 + TSX 60 Universe
                </p>
              </div>
            )}
          </>
        )}

        {/* ==================== SECTORS TAB ==================== */}
        {/* Day 62: v4.24 Sector Rotation Phase 2 */}
        {activeTab === 'sectors' && (
          <SectorRotationTab
            sectorRotation={sectorRotation}
            sectorRotationError={sectorRotationError}
            onRetry={loadSectorRotation}
            onScanForSector={handleScanForSector}
            refreshTrigger={sectorRefreshTrigger}
            onRefresh={handleSectorRefresh}
            refreshing={sectorRefreshing}
          />
        )}

        {/* ==================== CONTEXT TAB ==================== */}
        {/* Day 62: v4.24 Pre-flight macro context (FRED cycles + econ + AV news) */}
        {activeTab === 'context' && (
          <ContextTab ticker={analysisResult?.ticker || null} />
        )}

        {/* ==================== VALUE TAB ==================== */}
        {/* Day 75: Value investing lens — Buffett/Graham/Lynch/Damodaran/Greenblatt */}
        {activeTab === 'value' && (
          <ValueTab ticker={analysisResult?.ticker || null} />
        )}

        {/* ==================== VALIDATE TAB ==================== */}
        {activeTab === 'validate' && (
          <>
            {/* Validation Input */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <div className="flex gap-4">
                <div className="flex-1">
                  <input
                    type="text"
                    value={validationTickers}
                    onChange={(e) => setValidationTickers(e.target.value.toUpperCase())}
                    placeholder="AAPL, NVDA, MSFT"
                    className="w-full bg-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <button
                  onClick={handleRunValidation}
                  disabled={validationLoading}
                  className="bg-purple-600 hover:bg-purple-700 px-8 py-3 rounded-lg font-semibold disabled:opacity-50 whitespace-nowrap"
                >
                  {validationLoading ? '⏳ Validating...' : '✅ Run Validation'}
                </button>
              </div>

              <div className="mt-3 text-xs text-gray-500">
                ⚠️ Note: Validation uses web scraping which takes ~10-15 seconds per ticker.
              </div>
            </div>

            {/* Validation Error */}
            {validationError && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6 text-red-200">
                {validationError}
              </div>
            )}

            {/* Loading State */}
            {validationLoading && (
              <div className="bg-gray-800 rounded-lg p-12 text-center">
                <div className="text-4xl mb-4">⏳</div>
                <p className="text-gray-400">Running validation... This may take 10-30 seconds.</p>
                <p className="text-gray-500 text-sm mt-2">Fetching data from StockAnalysis and Finviz...</p>
              </div>
            )}

            {/* Validation Results */}
            {validationResults && !validationLoading && (
              <div className="space-y-6">
                {/* Summary Card */}
                <div className="bg-gray-800 rounded-lg p-6">
                  <div className="flex justify-between items-start mb-4">
                    <div>
                      <h3 className="text-lg font-semibold text-blue-400">📊 Validation Summary</h3>
                      <p className="text-xs text-gray-500">Run ID: {validationResults.runId}</p>
                    </div>
                    <div className="text-right">
                      <div className={`text-3xl font-bold ${getQualityColor(validationResults.summary.qualityScore)}`}>
                        {validationResults.summary.qualityScore}%
                      </div>
                      <div className="text-sm text-gray-400">Quality Score</div>
                    </div>
                  </div>

                  {/* Metrics Grid */}
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                      <div className="text-2xl font-bold text-blue-400">{validationResults.summary.totalChecks}</div>
                      <div className="text-xs text-gray-400">Total Checks</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                      <div className="text-2xl font-bold text-green-400">{validationResults.summary.coverageRate}%</div>
                      <div className="text-xs text-gray-400">Coverage Rate</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                      <div className="text-2xl font-bold text-green-400">{validationResults.summary.accuracyRate}%</div>
                      <div className="text-xs text-gray-400">Accuracy Rate</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                      <div className="flex justify-center gap-2 text-lg font-bold">
                        <span className="text-green-400">{validationResults.summary.passed}✓</span>
                        <span className="text-red-400">{validationResults.summary.failed}✗</span>
                        <span className="text-yellow-400">{validationResults.summary.warnings}⚠</span>
                      </div>
                      <div className="text-xs text-gray-400">Pass / Fail / Warn</div>
                    </div>
                  </div>
                </div>

                {/* Per-Ticker Results */}
                {validationResults.tickerResults.map((tickerResult) => (
                  <div key={tickerResult.ticker} className="bg-gray-800 rounded-lg p-6">
                    <div className="flex justify-between items-center mb-4">
                      <h3 className="text-lg font-semibold">
                        <span className="text-blue-400">{tickerResult.ticker}</span>
                        <span className={`ml-3 px-2 py-1 rounded text-xs ${
                          tickerResult.overallStatus === 'pass' ? 'bg-green-900/50 text-green-400' :
                          tickerResult.overallStatus === 'fail' ? 'bg-red-900/50 text-red-400' :
                          'bg-yellow-900/50 text-yellow-400'
                        }`}>
                          {tickerResult.overallStatus.toUpperCase()}
                        </span>
                      </h3>
                      <div className="text-sm text-gray-400">
                        {tickerResult.passCount}✓ {tickerResult.failCount}✗ {tickerResult.warningCount}⚠ {tickerResult.skipCount}⊘
                      </div>
                    </div>

                    {/* Results Table */}
                    <div className="overflow-x-auto">
                      <table className="w-full text-sm">
                        <thead>
                          <tr className="text-gray-400 border-b border-gray-700 text-xs">
                            <th className="text-left py-2 px-2">Metric</th>
                            <th className="text-right py-2 px-2">Our Value</th>
                            <th className="text-right py-2 px-2">External</th>
                            <th className="text-left py-2 px-2">Source</th>
                            <th className="text-right py-2 px-2">Variance</th>
                            <th className="text-center py-2 px-2">Status</th>
                          </tr>
                        </thead>
                        <tbody>
                          {tickerResult.results.map((result, idx) => (
                            <tr key={idx} className="border-b border-gray-700/30 hover:bg-gray-700/20">
                              <td className="py-2 px-2 text-gray-300">{result.metric}</td>
                              <td className="py-2 px-2 text-right font-mono">
                                {result.ourValue !== null ? 
                                  (typeof result.ourValue === 'number' ? result.ourValue.toFixed(2) : result.ourValue) 
                                  : <span className="text-gray-500">null</span>}
                              </td>
                              <td className="py-2 px-2 text-right font-mono">
                                {result.externalValue !== null ? 
                                  (typeof result.externalValue === 'number' ? result.externalValue.toFixed(2) : result.externalValue) 
                                  : <span className="text-gray-500">null</span>}
                              </td>
                              <td className="py-2 px-2 text-gray-400 text-xs">{result.externalSource}</td>
                              <td className="py-2 px-2 text-right">
                                {result.variancePct !== null ? 
                                  <span className={result.variancePct > result.tolerancePct ? 'text-red-400' : 'text-gray-400'}>
                                    {result.variancePct.toFixed(1)}%
                                  </span> 
                                  : '-'}
                              </td>
                              <td className="py-2 px-2 text-center">
                                <span className={`px-2 py-0.5 rounded text-xs ${getValidationStatusColor(result.status)}`}>
                                  {result.status.toUpperCase()}
                                </span>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                ))}

                {/* Info Note */}
                <div className="bg-gray-800/50 rounded-lg p-4 text-xs text-gray-500">
                  <p><strong>Quality Score</strong> = Coverage × Accuracy. This is the TRUE system health metric.</p>
                  <p className="mt-1"><strong>Coverage</strong> = % of checks with external data available.</p>
                  <p className="mt-1"><strong>Accuracy</strong> = % of validated checks that passed.</p>
                </div>
              </div>
            )}

            {/* Empty State */}
            {!validationResults && !validationLoading && !validationError && (
              <div className="bg-gray-800 rounded-lg p-12 text-center">
                <div className="text-6xl mb-4">✅</div>
                <h3 className="text-xl font-bold text-gray-300 mb-2">Data Validation</h3>
                <p className="text-gray-500 mb-4">
                  Enter tickers and click "Run Validation" to verify data accuracy against external sources.
                </p>
                <p className="text-gray-600 text-sm">
                  Sources: StockAnalysis (prices, P/E, EPS) • Finviz (ROE, D/E, Revenue Growth)
                </p>
              </div>
            )}
          </>
        )}

        {/* ==================== FORWARD TESTING TAB (Day 47: v4.7) ==================== */}
        {activeTab === 'forward' && (
          <>
            {/* Day 87: Automated paper trading engine — separate from the manual journal below */}
            <AutomatedPaperTradingPanel />

            {/* Statistics Overview */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold text-green-400">📈 Forward Testing Statistics</h3>
                <div className="flex gap-2">
                  <button
                    onClick={() => setShowAddTradeModal(true)}
                    className="px-4 py-2 bg-green-600 hover:bg-green-700 rounded-lg text-white font-medium transition-colors"
                  >
                    + Add Trade
                  </button>
                  {forwardTrades.length > 0 && (
                    <button
                      onClick={() => downloadTradesCSV(forwardTrades)}
                      className="px-4 py-2 bg-gray-600 hover:bg-gray-700 rounded-lg text-white font-medium transition-colors"
                    >
                      Export CSV
                    </button>
                  )}
                </div>
              </div>

              {(() => {
                const stats = calculateStatistics(forwardTrades);
                const sqnRating = getSQNRating(stats.sqn);

                return (
                  <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                    <div className="bg-gray-700/50 rounded-lg p-3 text-center">
                      <div className="text-gray-400 text-xs">Total Trades</div>
                      <div className="text-2xl font-bold text-white">{stats.totalTrades}</div>
                      <div className="text-xs text-gray-500">{stats.openTrades} open</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-3 text-center">
                      <div className="text-gray-400 text-xs">Win Rate</div>
                      <div className={`text-2xl font-bold ${stats.winRate >= 50 ? 'text-green-400' : 'text-yellow-400'}`}>
                        {stats.winRate}%
                      </div>
                      <div className="text-xs text-gray-500">{stats.wins}W / {stats.losses}L</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-3 text-center">
                      <div className="text-gray-400 text-xs">Avg Win R</div>
                      <div className="text-2xl font-bold text-green-400">+{stats.avgWinR}R</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-3 text-center">
                      <div className="text-gray-400 text-xs">Avg Loss R</div>
                      <div className="text-2xl font-bold text-red-400">{stats.avgLossR}R</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-3 text-center">
                      {/* Day 107 audit fix: labeled "Expectancy (R)" — the
                          automated Forward Test panel above shows an
                          "Expectancy" stat too, but that one is a mean
                          %-return figure, not this Van Tharp R-multiple
                          formula. Same word, different statistic. */}
                      <div className="text-gray-400 text-xs">Expectancy (R)</div>
                      <div className={`text-2xl font-bold ${stats.expectancy > 0 ? 'text-green-400' : 'text-red-400'}`}>
                        {stats.expectancy > 0 ? '+' : ''}{stats.expectancy}R
                      </div>
                      <div className="text-xs text-gray-500">${stats.expectancyDollar}/trade</div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-3 text-center" title={sqnRating.description}>
                      <div className="text-gray-400 text-xs">SQN</div>
                      <div className={`text-2xl font-bold text-${sqnRating.color}-400`}>
                        {stats.sqn}
                      </div>
                      <div className="text-xs text-gray-500">{sqnRating.rating}</div>
                    </div>
                    {/* Day 79 (Fable Remediation Task 5.1): execution gap — signal-close vs actual fill */}
                    <div className="bg-gray-700/50 rounded-lg p-3 text-center" title="Avg % difference between your actual entry price and the signal's close price at analysis time">
                      <div className="text-gray-400 text-xs">Avg Entry Slippage</div>
                      <div className={`text-2xl font-bold ${
                        stats.avgEntrySlippagePct == null ? 'text-gray-500' :
                        stats.avgEntrySlippagePct > 0.3 ? 'text-red-400' :
                        stats.avgEntrySlippagePct < -0.3 ? 'text-green-400' : 'text-yellow-400'
                      }`}>
                        {stats.avgEntrySlippagePct != null ? `${stats.avgEntrySlippagePct > 0 ? '+' : ''}${stats.avgEntrySlippagePct}%` : 'N/A'}
                      </div>
                      <div className="text-xs text-gray-500">
                        {stats.slippageSampleSize > 0 ? `n=${stats.slippageSampleSize}` : 'no data yet'}
                      </div>
                    </div>
                  </div>
                );
              })()}

              <div className="mt-4 p-3 bg-gray-700/30 rounded-lg text-xs text-gray-400">
                <strong>Van Tharp Metrics:</strong> R = Initial Risk (Entry - Stop) | R-Multiple = Profit/Loss ÷ R |
                Expectancy = (Win% × AvgWinR) + (Loss% × AvgLossR) | SQN = (MeanR ÷ StdDevR) × √N
              </div>
            </div>

            {/* Trades Table */}
            <div className="bg-gray-800 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-gray-300 mb-4">Trade Journal</h3>

              {forwardTrades.length === 0 ? (
                <div className="text-center py-12 text-gray-500">
                  <div className="text-4xl mb-3">📝</div>
                  <p className="text-lg mb-2">No trades recorded yet</p>
                  <p className="text-sm">Add your first paper trade to start tracking performance</p>
                </div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="text-left text-gray-400 border-b border-gray-700">
                        <th className="pb-2 pr-3">Ticker</th>
                        <th className="pb-2 pr-3">Entry</th>
                        <th className="pb-2 pr-3">Stop</th>
                        <th className="pb-2 pr-3">Target</th>
                        <th className="pb-2 pr-3">Shares</th>
                        <th className="pb-2 pr-3">Status</th>
                        <th className="pb-2 pr-3">R-Multiple</th>
                        <th className="pb-2 pr-3">P/L</th>
                        <th className="pb-2 pr-3">Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {forwardTrades.map(trade => (
                        <tr key={trade.id} className="border-b border-gray-700/50 hover:bg-gray-700/30">
                          <td className="py-2 pr-3 font-mono font-medium text-blue-400">{trade.ticker}</td>
                          <td className="py-2 pr-3 font-mono">${trade.entryPrice.toFixed(2)}</td>
                          <td className="py-2 pr-3 font-mono text-red-400">${trade.stopPrice.toFixed(2)}</td>
                          <td className="py-2 pr-3 font-mono text-green-400">${trade.targetPrice.toFixed(2)}</td>
                          <td className="py-2 pr-3">{trade.shares}</td>
                          <td className="py-2 pr-3">
                            <span className={`px-2 py-0.5 rounded text-xs ${
                              trade.status === TradeStatus.OPEN ? 'bg-blue-900/50 text-blue-300' :
                              trade.status === TradeStatus.CLOSED_WIN ? 'bg-green-900/50 text-green-300' :
                              trade.status === TradeStatus.CLOSED_LOSS || trade.status === TradeStatus.STOPPED_OUT ? 'bg-red-900/50 text-red-300' :
                              'bg-gray-700 text-gray-300'
                            }`}>
                              {trade.status.replace('_', ' ')}
                            </span>
                          </td>
                          <td className={`py-2 pr-3 font-mono ${
                            trade.rMultiple > 0 ? 'text-green-400' :
                            trade.rMultiple < 0 ? 'text-red-400' :
                            'text-gray-400'
                          }`}>
                            {trade.rMultiple !== null ? `${trade.rMultiple > 0 ? '+' : ''}${trade.rMultiple}R` : '-'}
                          </td>
                          <td className={`py-2 pr-3 font-mono ${
                            trade.profitLoss > 0 ? 'text-green-400' :
                            trade.profitLoss < 0 ? 'text-red-400' :
                            'text-gray-400'
                          }`}>
                            {trade.profitLoss !== null ? `${trade.profitLoss > 0 ? '+' : ''}$${trade.profitLoss.toFixed(2)}` : '-'}
                          </td>
                          <td className="py-2 pr-3">
                            {trade.status === TradeStatus.OPEN ? (
                              <div className="flex gap-1">
                                <button
                                  onClick={() => {
                                    setCloseTradeId(trade.id);
                                    setCloseTradePrice('');
                                  }}
                                  className="px-2 py-1 bg-yellow-600 hover:bg-yellow-700 rounded text-xs text-white"
                                >
                                  Close
                                </button>
                                <button
                                  onClick={() => {
                                    const updated = updateTrade(forwardTrades, trade.id,
                                      closeTrade(trade, trade.stopPrice, 'stopped_out')
                                    );
                                    setForwardTrades(updated);
                                  }}
                                  className="px-2 py-1 bg-red-600 hover:bg-red-700 rounded text-xs text-white"
                                >
                                  Stop Hit
                                </button>
                              </div>
                            ) : (
                              <button
                                onClick={() => setForwardTrades(deleteTrade(forwardTrades, trade.id))}
                                className="px-2 py-1 bg-gray-600 hover:bg-gray-700 rounded text-xs text-white"
                              >
                                Delete
                              </button>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>

            {/* Add Trade Modal */}
            {showAddTradeModal && (
              <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
                <div className="bg-gray-800 rounded-lg p-6 max-w-md w-full mx-4">
                  <h3 className="text-lg font-semibold text-green-400 mb-4">Add Paper Trade</h3>

                  <div className="space-y-4">
                    <div>
                      <label className="block text-gray-400 text-sm mb-1">Ticker</label>
                      <input
                        type="text"
                        value={newTradeForm.ticker}
                        onChange={(e) => setNewTradeForm({...newTradeForm, ticker: e.target.value.toUpperCase()})}
                        className="w-full bg-gray-700 rounded px-3 py-2 text-white"
                        placeholder="AAPL"
                      />
                    </div>
                    <div className="grid grid-cols-3 gap-3">
                      <div>
                        <label className="block text-gray-400 text-sm mb-1">Entry $</label>
                        <input
                          type="number"
                          step="0.01"
                          value={newTradeForm.entryPrice}
                          onChange={(e) => setNewTradeForm({...newTradeForm, entryPrice: e.target.value})}
                          className="w-full bg-gray-700 rounded px-3 py-2 text-white"
                        />
                      </div>
                      <div>
                        <label className="block text-gray-400 text-sm mb-1">Stop $</label>
                        <input
                          type="number"
                          step="0.01"
                          value={newTradeForm.stopPrice}
                          onChange={(e) => setNewTradeForm({...newTradeForm, stopPrice: e.target.value})}
                          className="w-full bg-gray-700 rounded px-3 py-2 text-white"
                        />
                      </div>
                      <div>
                        <label className="block text-gray-400 text-sm mb-1">Target $</label>
                        <input
                          type="number"
                          step="0.01"
                          value={newTradeForm.targetPrice}
                          onChange={(e) => setNewTradeForm({...newTradeForm, targetPrice: e.target.value})}
                          className="w-full bg-gray-700 rounded px-3 py-2 text-white"
                        />
                      </div>
                    </div>
                    <div>
                      <label className="block text-gray-400 text-sm mb-1">Shares</label>
                      <input
                        type="number"
                        value={newTradeForm.shares}
                        onChange={(e) => setNewTradeForm({...newTradeForm, shares: e.target.value})}
                        className="w-full bg-gray-700 rounded px-3 py-2 text-white"
                      />
                    </div>
                    <div>
                      <label className="block text-gray-400 text-sm mb-1">Notes (optional)</label>
                      <textarea
                        value={newTradeForm.notes}
                        onChange={(e) => setNewTradeForm({...newTradeForm, notes: e.target.value})}
                        className="w-full bg-gray-700 rounded px-3 py-2 text-white h-20"
                        placeholder="Why are you taking this trade?"
                      />
                    </div>
                  </div>

                  <div className="flex gap-3 mt-6">
                    <button
                      onClick={() => {
                        if (newTradeForm.ticker && newTradeForm.entryPrice && newTradeForm.stopPrice && newTradeForm.shares) {
                          const trade = createTrade({
                            ticker: newTradeForm.ticker,
                            entryPrice: parseFloat(newTradeForm.entryPrice),
                            stopPrice: parseFloat(newTradeForm.stopPrice),
                            targetPrice: parseFloat(newTradeForm.targetPrice) || parseFloat(newTradeForm.entryPrice) * 1.1,
                            shares: parseInt(newTradeForm.shares),
                            notes: newTradeForm.notes,
                            categoricalVerdict: categoricalResult?.verdict?.verdict,
                            // Day 79 (Fable Remediation Task 5.1): signal-close price is only
                            // meaningful if the loaded analysis is for the SAME ticker being
                            // logged — a manual/different-ticker entry has no comparable signal.
                            signalClosePrice: (analysisResult?.ticker?.toUpperCase() === newTradeForm.ticker.toUpperCase())
                              ? (analysisResult?.currentPrice ?? null)
                              : null,
                            // Day 79 (Fable Remediation Task 5.2): regime snapshot — reuses the
                            // existing categoricalResult.riskMacro output, not reimplemented.
                            regimeSnapshot: categoricalResult?.riskMacro ? {
                              vix: categoricalResult.riskMacro.data?.vix ?? null,
                              spyAbove200EMA: categoricalResult.riskMacro.data?.spyAbove200EMA ?? null,
                              sma50Declining: categoricalResult.riskMacro.data?.sma50Declining ?? null,
                              assessment: categoricalResult.riskMacro.assessment ?? null
                            } : null
                          });
                          setForwardTrades(addTrade(forwardTrades, trade));
                          setNewTradeForm({ ticker: '', entryPrice: '', stopPrice: '', targetPrice: '', shares: '', notes: '' });
                          setShowAddTradeModal(false);
                        }
                      }}
                      className="flex-1 px-4 py-2 bg-green-600 hover:bg-green-700 rounded-lg text-white font-medium"
                    >
                      Add Trade
                    </button>
                    <button
                      onClick={() => setShowAddTradeModal(false)}
                      className="px-4 py-2 bg-gray-600 hover:bg-gray-700 rounded-lg text-white"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              </div>
            )}

            {/* Close Trade Modal */}
            {closeTradeId && (
              <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
                <div className="bg-gray-800 rounded-lg p-6 max-w-sm w-full mx-4">
                  <h3 className="text-lg font-semibold text-yellow-400 mb-4">Close Trade</h3>

                  <div>
                    <label className="block text-gray-400 text-sm mb-1">Exit Price $</label>
                    <input
                      type="number"
                      step="0.01"
                      value={closeTradePrice}
                      onChange={(e) => setCloseTradePrice(e.target.value)}
                      className="w-full bg-gray-700 rounded px-3 py-2 text-white"
                      autoFocus
                    />
                  </div>

                  <div className="flex gap-3 mt-6">
                    <button
                      onClick={() => {
                        if (closeTradePrice) {
                          const trade = forwardTrades.find(t => t.id === closeTradeId);
                          if (trade) {
                            const closedTrade = closeTrade(trade, parseFloat(closeTradePrice), 'manual');
                            const updated = forwardTrades.map(t =>
                              t.id === closeTradeId ? closedTrade : t
                            );
                            saveTrades(updated);
                            setForwardTrades(updated);
                          }
                          setCloseTradeId(null);
                          setCloseTradePrice('');
                        }
                      }}
                      className="flex-1 px-4 py-2 bg-yellow-600 hover:bg-yellow-700 rounded-lg text-white font-medium"
                    >
                      Close Trade
                    </button>
                    <button
                      onClick={() => {
                        setCloseTradeId(null);
                        setCloseTradePrice('');
                      }}
                      className="px-4 py-2 bg-gray-600 hover:bg-gray-700 rounded-lg text-white"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              </div>
            )}
          </>
        )}

        {/* ==================== SETTINGS TAB (Day 28) ==================== */}
        {activeTab === 'settings' && (
          <>
            {/* Account Settings */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <h3 className="text-lg font-semibold text-purple-400 mb-4">Account Settings</h3>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {/* Account Size */}
                <div>
                  <label className="block text-gray-400 text-sm mb-2">Account Size ($)</label>
                  <input
                    type="number"
                    value={settings.accountSize}
                    onChange={(e) => updateSettings({ ...settings, accountSize: parseInt(e.target.value) || 0 })}
                    className="w-full bg-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
                    placeholder="10000"
                  />
                  <p className="text-xs text-gray-500 mt-1">Total capital available for trading</p>
                </div>

                {/* Risk Percentage */}
                <div>
                  <label className="block text-gray-400 text-sm mb-2">
                    Risk Per Trade: <span className="text-purple-400 font-bold">{settings.riskPercent}%</span>
                  </label>
                  <input
                    type="range"
                    min="2"
                    max="5"
                    step="0.5"
                    value={settings.riskPercent}
                    onChange={(e) => updateSettings({ ...settings, riskPercent: parseFloat(e.target.value) })}
                    className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-purple-500"
                  />
                  <div className="flex justify-between text-xs text-gray-500 mt-1">
                    <span>2% (Conservative)</span>
                    <span>5% (Aggressive)</span>
                  </div>
                </div>

                {/* Max Position Size (Day 29) */}
                <div>
                  <label className="block text-gray-400 text-sm mb-2">
                    Max Position Size: <span className="text-orange-400 font-bold">{settings.maxPositionPercent || 25}%</span>
                  </label>
                  <input
                    type="range"
                    min="10"
                    max="50"
                    step="5"
                    value={settings.maxPositionPercent || 25}
                    onChange={(e) => updateSettings({ ...settings, maxPositionPercent: parseInt(e.target.value) })}
                    className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-orange-500"
                  />
                  <div className="flex justify-between text-xs text-gray-500 mt-1">
                    <span>10% (Diversified)</span>
                    <span>50% (Concentrated)</span>
                  </div>
                </div>
              </div>

              {/* Current Risk Summary */}
              <div className="mt-6 bg-purple-900/30 border border-purple-700 rounded-lg p-4">
                <div className="grid grid-cols-4 gap-4 text-center">
                  <div>
                    <div className="text-gray-400 text-sm">Account</div>
                    <div className="text-xl font-bold text-purple-400">${settings.accountSize?.toLocaleString()}</div>
                  </div>
                  <div>
                    <div className="text-gray-400 text-sm">Risk %</div>
                    <div className="text-xl font-bold text-purple-400">{settings.riskPercent}%</div>
                  </div>
                  <div>
                    <div className="text-gray-400 text-sm">Max Risk/Trade</div>
                    <div className="text-xl font-bold text-green-400">
                      ${((settings.accountSize * settings.riskPercent) / 100).toFixed(0)}
                    </div>
                  </div>
                  <div>
                    <div className="text-gray-400 text-sm">Max Position</div>
                    <div className="text-xl font-bold text-orange-400">
                      ${((settings.accountSize * (settings.maxPositionPercent || 25)) / 100).toLocaleString()}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Position Sizing Calculator */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <h3 className="text-lg font-semibold text-green-400 mb-4">Position Sizing Calculator</h3>
              <p className="text-gray-400 text-sm mb-4">
                Van Tharp Principle: The 90% that actually matters. Enter your planned trade to calculate position size.
              </p>

              {/* Calculator Inputs */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                <div>
                  <label className="block text-gray-400 text-sm mb-2">Ticker (optional)</label>
                  <input
                    type="text"
                    value={calcTicker}
                    onChange={(e) => setCalcTicker(e.target.value.toUpperCase())}
                    placeholder="AAPL"
                    className="w-full bg-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
                  />
                </div>
                <div>
                  <label className="block text-gray-400 text-sm mb-2">Entry Price ($)</label>
                  <input
                    type="number"
                    step="0.01"
                    value={calcEntry}
                    onChange={(e) => setCalcEntry(e.target.value)}
                    placeholder="150.00"
                    className="w-full bg-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
                  />
                </div>
                <div>
                  <label className="block text-gray-400 text-sm mb-2">Stop Loss ($)</label>
                  <input
                    type="number"
                    step="0.01"
                    value={calcStop}
                    onChange={(e) => setCalcStop(e.target.value)}
                    placeholder="142.50"
                    className="w-full bg-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
                  />
                </div>
              </div>

              {/* Manual Share Override (Day 29) */}
              <div className="flex items-center gap-4 mb-4 p-3 bg-gray-700/30 rounded-lg">
                <label className="flex items-center gap-2 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={settings.useManualShares || false}
                    onChange={(e) => updateSettings({ ...settings, useManualShares: e.target.checked })}
                    className="w-4 h-4 rounded accent-orange-500"
                  />
                  <span className="text-gray-300 text-sm">Override with manual shares</span>
                </label>
                {settings.useManualShares && (
                  <input
                    type="number"
                    value={settings.manualShares || ''}
                    onChange={(e) => updateSettings({ ...settings, manualShares: parseInt(e.target.value) || 0 })}
                    placeholder="100"
                    className="w-24 bg-gray-700 rounded-lg px-3 py-2 text-white text-sm focus:outline-none focus:ring-2 focus:ring-orange-500"
                  />
                )}
                <span className="text-xs text-gray-500 ml-auto">
                  Max position: {settings.maxPositionPercent || 25}% of account
                </span>
              </div>

              <button
                onClick={runPositionCalculation}
                className="w-full bg-green-600 hover:bg-green-700 px-6 py-3 rounded-lg font-semibold"
              >
                Calculate Position Size
              </button>

              {/* Calculation Results */}
              {positionResult && !positionResult.error && (
                <div className="mt-6 space-y-4">
                  {/* Limit Applied Notice (Day 29) */}
                  {positionResult.limitApplied && (
                    <div className="bg-orange-900/30 border border-orange-600 rounded-lg px-4 py-2 text-sm text-orange-300 flex items-center gap-2">
                      <span>⚠️</span>
                      <span>{positionResult.limitApplied}</span>
                    </div>
                  )}

                  {/* Main Result Card */}
                  <div className="bg-green-900/30 border border-green-700 rounded-lg p-6">
                    <div className="text-center mb-4">
                      <div className="text-gray-400 text-sm">Position Size</div>
                      <div className="text-4xl font-bold text-green-400">
                        {positionResult.shares} shares
                      </div>
                      <div className="text-gray-400 mt-1">
                        {calcTicker && <span className="text-green-300">{calcTicker} • </span>}
                        ${positionResult.positionValue?.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} total
                      </div>
                    </div>

                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                      <div className="bg-gray-800/50 rounded-lg p-3">
                        <div className="text-gray-400 text-xs">Entry</div>
                        <div className="text-lg font-bold text-green-400">${positionResult.entryPrice?.toFixed(2)}</div>
                      </div>
                      <div className="bg-gray-800/50 rounded-lg p-3">
                        <div className="text-gray-400 text-xs">Stop</div>
                        <div className="text-lg font-bold text-red-400">${positionResult.stopPrice?.toFixed(2)}</div>
                      </div>
                      <div className="bg-gray-800/50 rounded-lg p-3">
                        <div className="text-gray-400 text-xs">Risk/Share (R)</div>
                        <div className="text-lg font-bold text-yellow-400">${positionResult.riskPerShare?.toFixed(2)}</div>
                      </div>
                      <div className="bg-gray-800/50 rounded-lg p-3">
                        <div className="text-gray-400 text-xs">Total Risk</div>
                        <div className="text-lg font-bold text-red-400">${positionResult.actualRiskAmount?.toFixed(2)}</div>
                      </div>
                    </div>
                  </div>

                  {/* Target Levels */}
                  <div className="bg-gray-700/50 rounded-lg p-4">
                    <div className="text-sm font-semibold text-blue-300 mb-3">Target Levels (R-Multiples)</div>
                    <div className="grid grid-cols-3 gap-4">
                      {positionResult.targets?.map((target) => (
                        <div key={target.label} className="text-center">
                          <div className="text-gray-400 text-xs">{target.label} Target</div>
                          <div className="text-lg font-bold text-blue-400">${target.price?.toFixed(2)}</div>
                          <div className="text-xs text-gray-500">
                            +${((target.price - positionResult.entryPrice) * positionResult.shares).toFixed(0)} profit
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Position Details */}
                  <div className="bg-gray-700/30 rounded-lg p-4 text-sm">
                    <div className="grid grid-cols-2 gap-2">
                      <div className="text-gray-400">Stop Distance:</div>
                      <div className="text-right">{positionResult.stopPercent?.toFixed(1)}% below entry</div>
                      <div className="text-gray-400">Position % of Account:</div>
                      <div className="text-right">{positionResult.positionPercent?.toFixed(1)}%</div>
                      <div className="text-gray-400">Max Risk Allowed:</div>
                      <div className="text-right">${positionResult.maxRiskAmount?.toFixed(2)}</div>
                      <div className="text-gray-400">Actual Risk:</div>
                      <div className="text-right">${positionResult.actualRiskAmount?.toFixed(2)}</div>
                    </div>
                  </div>
                </div>
              )}

              {/* Error Display */}
              {positionResult?.error && (
                <div className="mt-4 bg-red-900/50 border border-red-500 rounded-lg p-4 text-red-200">
                  {positionResult.error}
                </div>
              )}

              {/* Empty State */}
              {!positionResult && (
                <div className="mt-6 text-center text-gray-500 py-8">
                  <div className="text-4xl mb-2">📊</div>
                  <p>Enter entry and stop prices to calculate position size</p>
                </div>
              )}
            </div>

            {/* Van Tharp Reference */}
            <div className="bg-gray-800/50 rounded-lg p-4 text-xs text-gray-500">
              <p className="font-semibold text-gray-400 mb-2">Van Tharp Position Sizing Principles</p>
              <ul className="space-y-1">
                <li>• <strong>R</strong> = Entry - Stop (your initial risk per share)</li>
                <li>• <strong>Position Size</strong> = (Account × Risk%) / R</li>
                <li>• <strong>R-Multiple</strong> = (Exit - Entry) / R (measure results in R, not dollars)</li>
                <li>• <strong>90% of performance</strong> comes from position sizing, not entry signals</li>
              </ul>
            </div>
          </>
        )}

        {/* ==================== DATA SOURCES TAB (Day 38) ==================== */}
        {activeTab === 'datasources' && (
          <>
            {/* Header with Current Ticker */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="text-lg font-semibold text-cyan-400">Data Sources & Provenance</h3>
                  <p className="text-sm text-gray-400 mt-1">
                    Transparency into where your data comes from
                  </p>
                </div>
                {analysisResult?.stock?.ticker && (
                  <div className="bg-cyan-900/50 px-4 py-2 rounded-lg">
                    <span className="text-gray-400 text-sm">Current Ticker: </span>
                    <span className="text-cyan-400 font-bold">{analysisResult.stock.ticker}</span>
                  </div>
                )}
              </div>
            </div>

            {/* Cache Status Overview */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <h4 className="text-md font-semibold text-cyan-400 mb-4">📦 Cache Status</h4>
              {cacheStatus ? (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                  <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                    <div className="text-2xl font-bold text-cyan-400">{cacheStatus.ohlcv?.count || 0}</div>
                    <div className="text-xs text-gray-400">OHLCV Entries</div>
                  </div>
                  <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                    <div className="text-2xl font-bold text-cyan-400">{cacheStatus.fundamentals?.count || 0}</div>
                    <div className="text-xs text-gray-400">Fundamentals Entries</div>
                  </div>
                  <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                    <div className="text-2xl font-bold text-cyan-400">{cacheStatus.database_size_kb || 0} KB</div>
                    <div className="text-xs text-gray-400">Database Size</div>
                  </div>
                  <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                    <div className="text-2xl font-bold text-green-400">
                      {cacheStatus.ohlcv?.hit_rate_24h || 0}%
                    </div>
                    <div className="text-xs text-gray-400">Hit Rate (24h)</div>
                  </div>
                </div>
              ) : (
                <div className="text-gray-500 text-center py-4">Loading cache status...</div>
              )}
            </div>

            {/* Per-Ticker Provenance */}
            {provenanceLoading ? (
              <div className="bg-gray-800 rounded-lg p-6 mb-6 text-center">
                <div className="text-cyan-400">Loading provenance data...</div>
              </div>
            ) : provenanceData ? (
              <div className="bg-gray-800 rounded-lg p-6 mb-6">
                <h4 className="text-md font-semibold text-cyan-400 mb-4">
                  🎯 Provenance for {provenanceData.ticker}
                </h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                  {/* OHLCV Source */}
                  <div className="bg-gray-700/50 rounded-lg p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-gray-300 font-medium">Price Data (OHLCV)</span>
                      <span className={`px-2 py-0.5 rounded text-xs font-medium ${
                        provenanceData.ohlcv.status === 'cached'       ? 'bg-green-900/50 text-green-400' :
                        provenanceData.ohlcv.status === 'just_fetched' ? 'bg-cyan-900/50 text-cyan-300'  :
                                                                          'bg-gray-700 text-gray-400'
                      }`}>
                        {provenanceData.ohlcv.status === 'just_fetched' ? 'JUST FETCHED' : provenanceData.ohlcv.status.toUpperCase()}
                      </span>
                    </div>
                    <div className="text-sm text-gray-400 space-y-1">
                      <div>Source: <span className="text-gray-300">{provenanceData.ohlcv.source}</span></div>
                      {provenanceData.ohlcv.rows != null && (
                        <div>Data points: <span className="text-gray-300">{provenanceData.ohlcv.rows}</span></div>
                      )}
                      {provenanceData.ohlcv.age_hours != null && provenanceData.ohlcv.age_hours >= 0 && (
                        <div>Age: <span className="text-gray-300">{provenanceData.ohlcv.age_hours}h</span></div>
                      )}
                      {provenanceData.ohlcv.expires_in && provenanceData.ohlcv.expires_in !== 'EXPIRED' && (
                        <div>Expires in: <span className="text-yellow-400">{provenanceData.ohlcv.expires_in.split('.')[0]}</span></div>
                      )}
                    </div>
                  </div>

                  {/* Fundamentals Source */}
                  <div className="bg-gray-700/50 rounded-lg p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-gray-300 font-medium">Fundamentals</span>
                      <span className={`px-2 py-0.5 rounded text-xs font-medium ${
                        provenanceData.fundamentals.status === 'cached'       ? 'bg-green-900/50 text-green-400' :
                        provenanceData.fundamentals.status === 'just_fetched' ? 'bg-cyan-900/50 text-cyan-300'  :
                                                                                 'bg-gray-700 text-gray-400'
                      }`}>
                        {provenanceData.fundamentals.status === 'just_fetched' ? 'JUST FETCHED' : provenanceData.fundamentals.status.toUpperCase()}
                      </span>
                    </div>
                    <div className="text-sm text-gray-400 space-y-1">
                      <div>Source: <span className="text-gray-300">{provenanceData.fundamentals.source}</span></div>
                      {provenanceData.fundamentals.age_days != null && provenanceData.fundamentals.age_days > 0 && (
                        <div>Age: <span className="text-gray-300">{provenanceData.fundamentals.age_days} days</span></div>
                      )}
                      {provenanceData.fundamentals.expires_in && provenanceData.fundamentals.expires_in !== 'EXPIRED' && (
                        <div>Expires in: <span className="text-yellow-400">{provenanceData.fundamentals.expires_in.split(',')[0]}</span></div>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <div className="bg-gray-800 rounded-lg p-6 mb-6 text-center">
                <div className="text-6xl mb-4">📊</div>
                <p className="text-gray-400">Analyze a stock first to see its data provenance</p>
                <p className="text-gray-500 text-sm mt-2">Go to "Analyze Stock" tab and analyze a ticker</p>
              </div>
            )}

            {/* Local Calculations Reference */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <h4 className="text-md font-semibold text-cyan-400 mb-4">🔢 Local Calculations</h4>
              <p className="text-sm text-gray-400 mb-4">
                These indicators are calculated locally using industry-standard formulas from OHLCV price data.
              </p>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="text-gray-400 border-b border-gray-700 text-xs">
                      <th className="text-left py-2 px-2">Indicator</th>
                      <th className="text-left py-2 px-2">Source</th>
                      <th className="text-left py-2 px-2">Formula</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(provenanceData?.indicators || [
                      {name: 'SMA 50', source: 'local', formula: 'Sum(Close, 50) / 50'},
                      {name: 'SMA 200', source: 'local', formula: 'Sum(Close, 200) / 200'},
                      {name: 'EMA 8', source: 'local', formula: 'Price * k + EMA_prev * (1-k), k=2/(8+1)'},
                      {name: 'EMA 21', source: 'local', formula: 'Price * k + EMA_prev * (1-k), k=2/(21+1)'},
                      {name: 'ATR 14', source: 'local', formula: 'EMA(TrueRange, 14) where TR=max(H-L, |H-Cp|, |L-Cp|)'},
                      {name: 'RSI 14', source: 'local', formula: '100 - 100/(1 + AvgGain/AvgLoss) [Wilder smoothing]'},
                      {name: 'Avg Volume 20', source: 'local', formula: 'Sum(Volume, 20) / 20'},
                      {name: 'Avg Volume 50', source: 'local', formula: 'Sum(Volume, 50) / 50'},
                      {name: 'RS 52W', source: 'local', formula: 'Stock 52W Return / SPY 52W Return'},
                      {name: 'PEG Ratio', source: 'local', formula: 'PE / (EPS Growth * 100)'}
                    ]).map((ind, idx) => (
                      <tr key={idx} className="border-b border-gray-700/30 hover:bg-gray-700/20">
                        <td className="py-2 px-2 text-gray-300">{ind.name}</td>
                        <td className="py-2 px-2">
                          <span className="px-2 py-0.5 rounded text-xs bg-blue-900/50 text-blue-400">
                            {ind.source}
                          </span>
                        </td>
                        <td className="py-2 px-2 text-gray-400 font-mono text-xs">{ind.formula}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Data Sources Map */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <h4 className="text-md font-semibold text-cyan-400 mb-1">🗺️ Data Source Map</h4>
              <p className="text-xs text-gray-500 mb-4">Live circuit breaker health — refreshed each time you open this tab.</p>

              {/* Cascade chains */}
              <div className="space-y-3 mb-5">
                {[
                  {
                    label: 'Price Data (OHLCV)',
                    activeKey: 'ohlcv',
                    chain: [
                      { name: 'TwelveData', role: 'primary', fields: 'daily bars' },
                      { name: 'yfinance',   role: 'fallback', fields: 'fallback' },
                      { name: 'Stooq',      role: 'fallback', fields: 'last resort' },
                    ],
                  },
                  {
                    label: 'Fundamentals',
                    activeKey: 'fundamentals',
                    chain: [
                      { name: 'Finnhub',       role: 'primary', fields: 'ROE, PE, margins, D/E, beta' },
                      { name: 'AlphaVantage',  role: 'growth',  fields: 'revenueGrowth, epsGrowth (YoY)' },
                      { name: 'yfinance',      role: 'fallback', fields: 'all remaining gaps' },
                    ],
                  },
                  {
                    label: 'Market Data (SPY / VIX)',
                    activeKey: null, // handled per-provider below
                    chain: [
                      { name: 'TwelveData', role: 'primary', fields: 'SPY OHLCV', providerActiveKey: 'ohlcv' },
                      { name: 'yfinance',   role: 'primary', fields: 'VIX quote',  providerActiveKey: 'quote' },
                      { name: 'Finnhub',    role: 'fallback', fields: 'quote fallback' },
                    ],
                  },
                  {
                    label: 'Market Scanning',
                    activeKey: null,
                    chain: [
                      { name: 'TradingView Screener', role: 'primary', fields: 'Reddit/momentum/growth scans' },
                    ],
                  },
                ].map((row, i) => {
                  const activeSource = row.activeKey
                    ? providerHealth?.active_sources?.[row.activeKey]
                    : null;
                  return (
                    <div key={i} className="bg-gray-700/40 rounded-lg p-3">
                      <div className="flex items-center gap-2 mb-2">
                        <span className="text-xs font-semibold text-gray-300">{row.label}</span>
                        {activeSource === 'cache' ? (
                          <span className="text-xs text-gray-500">— <span className="text-gray-400">served from cache</span></span>
                        ) : activeSource ? (
                          <span className="text-xs text-gray-500">
                            — live from <span className="text-cyan-400 font-medium">{activeSource}</span>
                          </span>
                        ) : null}
                      </div>
                      <div className="flex flex-wrap gap-2">
                        {row.chain.map((p, j) => {
                          const ph = providerHealth?.providers?.[p.name.toLowerCase().replace(/\s+/g, '')];
                          const health = ph?.health || (p.name === 'TradingView Screener' ? 'ok' : null);
                          const dailyLeft = ph?.daily_remaining;
                          // Per-provider activeKey override (e.g. Market Data row)
                          const resolvedActiveSource = p.providerActiveKey
                            ? providerHealth?.active_sources?.[p.providerActiveKey]
                            : activeSource;
                          const isActive = !!(resolvedActiveSource &&
                            resolvedActiveSource.toLowerCase() === p.name.toLowerCase().replace(/\s+/g, ''));

                          const borderColor =
                            isActive              ? 'border-cyan-500 ring-1 ring-cyan-500/40' :
                            health === 'ok'       ? 'border-green-600/40' :
                            health === 'degraded' ? 'border-yellow-600/50' :
                            health === 'open'     ? 'border-red-600/50' :
                                                    'border-gray-600/50';
                          const bgColor =
                            isActive              ? 'bg-cyan-900/20' :
                            health === 'ok'       ? 'bg-green-900/10' :
                            health === 'degraded' ? 'bg-yellow-900/20' :
                            health === 'open'     ? 'bg-red-900/20' :
                                                    'bg-gray-700/30';
                          const dot =
                            health === 'ok'       ? 'bg-green-400' :
                            health === 'degraded' ? 'bg-yellow-400' :
                            health === 'open'     ? 'bg-red-400' :
                                                    'bg-gray-500';
                          const roleLabel =
                            p.role === 'primary'  ? 'text-cyan-500' :
                            p.role === 'growth'   ? 'text-purple-400' :
                                                    'text-gray-500';
                          return (
                            <div key={j} className={`border rounded-md px-3 py-2 flex-1 min-w-[140px] ${borderColor} ${bgColor}`}>
                              <div className="flex items-center gap-1.5 mb-0.5">
                                {health && <span className={`w-1.5 h-1.5 rounded-full inline-block flex-shrink-0 ${dot}`} />}
                                <span className={`text-xs font-medium ${isActive ? 'text-cyan-300' : 'text-gray-200'}`}>
                                  {p.name}
                                </span>
                                {isActive ? (
                                  <span className="ml-auto text-xs font-bold text-cyan-400 bg-cyan-900/50 px-1.5 py-0.5 rounded">
                                    ACTIVE
                                  </span>
                                ) : (
                                  <span className={`text-xs ml-auto ${roleLabel}`}>{p.role}</span>
                                )}
                              </div>
                              <div className="text-gray-500 text-xs">{p.fields}</div>
                              {dailyLeft !== undefined && dailyLeft !== -1 && (
                                <div className={`text-xs mt-0.5 ${dailyLeft < 5 ? 'text-yellow-400' : 'text-gray-500'}`}>
                                  {dailyLeft} calls left today
                                </div>
                              )}
                              {health === 'open' && !isActive && (
                                <div className="text-red-400 text-xs mt-0.5">circuit open — skipped</div>
                              )}
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* FMP deprecation notice */}
              <div className="bg-yellow-900/20 border border-yellow-700/40 rounded-lg p-3 text-xs text-yellow-300">
                ⚠️ <strong>FMP (Financial Modeling Prep)</strong> v3 API deprecated Aug 31 2025 for non-legacy accounts. Replaced by AlphaVantage for growth metrics. FMP is kept in the stack for a future paid-plan upgrade.
              </div>
            </div>

            {/* Info Note */}
            <div className="bg-gray-800/50 rounded-lg p-4 text-xs text-gray-500">
              <p><strong>Cache TTL:</strong> OHLCV expires at next market close (4pm ET + 30min buffer). Fundamentals expire after 7 days.</p>
              <p className="mt-1"><strong>Local Calculations:</strong> All technical indicators use industry-standard formulas (Wilder 1978 for RSI/ATR).</p>
            </div>
          </>
        )}

        {/* Footer */}
        <div className="mt-8 text-center text-gray-500 text-sm">
          <p>v4.60 - Multi-Source Data Intelligence</p>
          <p className="mt-1">TwelveData • Finnhub • AlphaVantage • yfinance • Stooq</p>
        </div>
      </div>
    </div>
  );
}

export default App;