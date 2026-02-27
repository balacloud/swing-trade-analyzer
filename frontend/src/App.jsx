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

import React, { useState, useEffect } from 'react';
import { fetchFullAnalysisData, checkBackendHealth, fetchScanStrategies, fetchScanResults, runValidation, clearBackendCache, fetchDataProvenance, getCacheStatus, fetchSectorRotation } from './services/api';
import { calculateScore } from './utils/scoringEngine';
import { calculateSimplifiedAnalysis } from './utils/simplifiedScoring';
import { calculatePositionSize, loadSettings, saveSettings, getDefaultSettings } from './utils/positionSizing';
import { runCategoricalAssessment, getActionablePatterns } from './utils/categoricalAssessment';
import { calculateRiskReward, hasViabilityContradiction, getViabilityBadge } from './utils/riskRewardCalc';
import BottomLineCard, { HOLDING_PERIODS } from './components/BottomLineCard';
import DecisionMatrix from './components/DecisionMatrix';
import {
  createTrade, closeTrade, calculateStatistics, getSQNRating,
  loadTrades, saveTrades, addTrade, updateTrade, deleteTrade,
  downloadTradesCSV, TradeStatus
} from './utils/forwardTesting';
//import { calculateRelativeStrength } from './utils/rsCalculator';

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
  const [fearGreedData, setFearGreedData] = useState(null); // Day 44: v4.5 Fear & Greed
  const [earningsData, setEarningsData] = useState(null); // Day 49: v4.10 Earnings Calendar
  const [categoricalResult, setCategoricalResult] = useState(null); // Day 44: v4.5 Categorical Assessment
  const [holdingPeriod, setHoldingPeriod] = useState('standard'); // Day 53: v4.13 Holding Period Selector
  const [rawAnalysisData, setRawAnalysisData] = useState(null); // Day 53: Stored for re-assessment on period change

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
  const [selectedStrategy, setSelectedStrategy] = useState('reddit');
  const [strategies, setStrategies] = useState(null);
  const [selectedMarketIndex, setSelectedMarketIndex] = useState('all');

  // Validation state (Day 17)
  const [validationLoading, setValidationLoading] = useState(false);
  const [validationError, setValidationError] = useState(null);
  const [validationResults, setValidationResults] = useState(null);
  const [validationTickers, setValidationTickers] = useState('AAPL, NVDA, MSFT');

  // Score breakdown expanded state (Day 23)
  const [expandedScore, setExpandedScore] = useState(null); // 'technical', 'fundamental', 'sentiment', 'risk'

  // Simplified analysis state (Day 27)
  const [simplifiedResult, setSimplifiedResult] = useState(null);
  const [analysisView, setAnalysisView] = useState('full'); // 'full' or 'simple'

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

  // TradingView widget state (Day 34)
  const [tvWidgetCollapsed, setTvWidgetCollapsed] = useState(true); // Collapsed by default

  // Data Sources state (Day 38)
  const [provenanceData, setProvenanceData] = useState(null);
  const [provenanceLoading, setProvenanceLoading] = useState(false);
  const [cacheStatus, setCacheStatus] = useState(null);

  // Sector Rotation state (Day 58 - v4.19)
  const [sectorRotation, setSectorRotation] = useState(null);

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
    fetchSectorRotation()
      .then(setSectorRotation)
      .catch(err => console.error('Failed to load sector rotation:', err));
    // Load saved settings
    setSettings(loadSettings());
  }, []);

  // v4.13: Re-run categorical assessment when holding period changes (no API re-fetch needed)
  useEffect(() => {
    if (!rawAnalysisData) return;
    const { stock, spy, vix, fearGreed, trendTemplate, technicalBreakdown, fundamentals, ticker: rawTicker, adxData } = rawAnalysisData;
    const categorical = runCategoricalAssessment(
      stock, spy, vix, fearGreed, trendTemplate,
      technicalBreakdown, fundamentals, rawTicker,
      adxData, holdingPeriod
    );
    setCategoricalResult(categorical);
  }, [holdingPeriod]); // eslint-disable-line react-hooks/exhaustive-deps

  // Session Refresh - Clear backend cache and reset frontend state (Day 29)
  const handleSessionRefresh = async () => {
    setRefreshing(true);
    setRefreshMessage(null);
    try {
      // Clear backend cache and get result
      const cacheResult = await clearBackendCache();

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
      setExpandedScore(null);
      setPositionResult(null);
      setCalcEntry('');
      setCalcStop('');
      setCalcTicker('');
      setTicker('');

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
    const etfTicker = sectorRotation.mapping[stockSector];
    if (!etfTicker) return null;
    return sectorRotation.sectors.find(s => s.etf === etfTicker) || null;
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
    const options = {
      maxPositionPercent: settings.maxPositionPercent || 25,
      manualShares: settings.useManualShares ? (settings.manualShares || 0) : 0
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
    const options = {
      maxPositionPercent: settings.maxPositionPercent || 25,
      manualShares: 0 // Auto-fill always uses calculated shares
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
    setFearGreedData(null);
    setCategoricalResult(null);
    setSimplifiedResult(null);
    setActiveTab('analyze');

    try {
      const data = await fetchFullAnalysisData(targetTicker);
      const result = calculateScore(data.stock, data.spy, data.vix);
      //const rsData = calculateRelativeStrength(data.stock, data.spy);
      //result.rsData = rsData;

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
        holdingPeriod  // v4.13: Pass holding period for signal weighting
      );

      setAnalysisResult(result);
      setSrData(data.sr);
      setPatternsData(data.patterns); // Day 44: Pattern detection

      // Day 47: v4.6.2 - Calculate actionable patterns (≥60% confidence only)
      const atr = data.sr?.meta?.atr || null;
      const actionablePatterns = getActionablePatterns(data.patterns, atr);
      setActionablePatternsData(actionablePatterns);

      setFearGreedData(data.fearGreed); // Day 44: v4.5 Fear & Greed
      setEarningsData(data.earnings); // Day 49: v4.10 Earnings Calendar
      setCategoricalResult(categorical); // Day 44: v4.5 Categorical Assessment
      setSimplifiedResult(simplified);
      setTicker(targetTicker);

      // Day 58: Update sector rotation from analysis data (reliable — cached per trading day)
      if (data.sectorRotation) {
        setSectorRotation(data.sectorRotation);
      }

      // Day 59: Update data freshness for UI meter
      if (data.freshness) {
        setDataFreshness(data.freshness);
      }

      // v4.13: Store raw data for re-assessment when holding period changes
      setRawAnalysisData({
        stock: data.stock,
        spy: data.spy,
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

  // Scan for candidates
  const runScan = async () => {
    setScanLoading(true);
    setScanError(null);
    setScanResults(null);

    try {
      const results = await fetchScanResults(selectedStrategy, 50, selectedMarketIndex);
      setScanResults(results);
    } catch (err) {
      setScanError(err.message || 'Failed to scan for candidates');
    } finally {
      setScanLoading(false);
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

  // Get verdict color
  const getVerdictColor = (verdict) => {
    switch (verdict?.verdict) {
      case 'BUY': return 'bg-green-600';
      case 'HOLD': return 'bg-yellow-500';
      case 'AVOID': return 'bg-red-600';
      default: return 'bg-gray-500';
    }
  };

  // Get score color
  const getScoreColor = (score, max) => {
    const pct = (score / max) * 100;
    if (pct >= 80) return 'text-green-600';
    if (pct >= 60) return 'text-green-500';
    if (pct >= 40) return 'text-yellow-500';
    return 'text-red-500';
  };

  // Get RSI color
  const getRsiColor = (rsi) => {
    if (rsi >= 70) return 'text-red-400';
    if (rsi <= 30) return 'text-green-400';
    if (rsi >= 50) return 'text-green-300';
    return 'text-yellow-400';
  };

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

  // Get trade viability color and icon (Day 22)
  const getViabilityStyle = (viable) => {
    switch (viable) {
      case 'YES': return { 
        bg: 'bg-green-600', 
        text: 'text-white', 
        icon: '✅',
        label: 'VIABLE'
      };
      case 'CAUTION': return { 
        bg: 'bg-yellow-500', 
        text: 'text-black', 
        icon: '⚠️',
        label: 'CAUTION'
      };
      case 'NO': return { 
        bg: 'bg-red-600', 
        text: 'text-white', 
        icon: '🚫',
        label: 'NOT VIABLE'
      };
      default: return { 
        bg: 'bg-gray-600', 
        text: 'text-white', 
        icon: '❓',
        label: 'UNKNOWN'
      };
    }
  };

  // Generate actionable recommendation based on categorical assessment + trade viability (Day 44)
  // Day 46 Fix: Align recommendation message with entryPreference (Pullback vs Momentum)
  const generateActionableRecommendation = (categoricalResult, srData, currentPrice) => {
    if (!categoricalResult) return null;

    const verdict = categoricalResult.verdict?.verdict;
    const entryPreference = categoricalResult.verdict?.entryPreference;
    const viability = srData?.meta?.tradeViability;
    const nearestSupport = srData?.support?.length > 0 ? Math.max(...srData.support) : null;

    // Entry preference parsing
    const isPullbackPreferred = entryPreference?.includes('Pullback');

    // Calculate support zone (5% range around nearest support)
    const supportZoneLow = nearestSupport ? (nearestSupport * 0.97).toFixed(2) : null;
    const supportZoneHigh = nearestSupport ? (nearestSupport * 1.02).toFixed(2) : null;

    // Calculate % away from support (how far current price is above support)
    const pctFromSupport = nearestSupport && currentPrice
      ? (((currentPrice - nearestSupport) / nearestSupport) * 100).toFixed(1)
      : null;

    // Is pullback entry significantly below current price? (>10% = meaningful pullback)
    const pullbackIsFarBelow = nearestSupport && currentPrice
      ? ((currentPrice - nearestSupport) / currentPrice) > 0.10
      : false;

    // Recommendation logic based on verdict + viability + entryPreference combination
    let recommendation = {
      action: '',
      details: '',
      alertPrice: null,
      bgColor: 'bg-gray-700',
      borderColor: 'border-gray-600',
      textColor: 'text-gray-300',
      icon: '📋',
      actionType: 'RESEARCH' // EXECUTE, WATCHLIST, WAIT, AVOID, RESEARCH
    };

    // BUY verdict scenarios
    if (verdict === 'BUY') {
      if (viability?.viable === 'YES') {
        // Day 46: Check if pullback preferred with significant distance
        if (isPullbackPreferred && pullbackIsFarBelow) {
          recommendation = {
            action: 'READY - PREFER PULLBACK',
            details: `Strong stock but ${pctFromSupport}% above support. Wait for pullback to ~$${nearestSupport?.toFixed(2)} for better R:R.`,
            alertPrice: nearestSupport,
            bgColor: 'bg-gradient-to-r from-green-600 to-emerald-600',
            borderColor: 'border-green-400',
            textColor: 'text-white',
            icon: '🎯',
            actionType: 'EXECUTE'
          };
        } else {
          recommendation = {
            action: 'READY TO TRADE',
            details: `Strong setup near support (${pctFromSupport}% away). Consider entry at current price with stop below $${nearestSupport?.toFixed(2) || 'support'}.`,
            alertPrice: null,
            bgColor: 'bg-gradient-to-r from-green-600 to-emerald-600',
            borderColor: 'border-green-400',
            textColor: 'text-white',
            icon: '🎯',
            actionType: 'EXECUTE'
          };
        }
      } else if (viability?.viable === 'CAUTION') {
        recommendation = {
          action: 'ADD TO WATCHLIST',
          details: supportZoneLow && supportZoneHigh
            ? `Good stock, but ${pctFromSupport}% above support. Set alert for pullback to $${supportZoneLow}-${supportZoneHigh} zone.`
            : `Good stock, but extended from support levels. Wait for a pullback before entry.`,
          alertPrice: nearestSupport,
          bgColor: 'bg-gradient-to-r from-blue-600 to-indigo-600',
          borderColor: 'border-blue-400',
          textColor: 'text-white',
          icon: '👀',
          actionType: 'WATCHLIST'
        };
      } else {
        // viability NO
        recommendation = {
          action: 'WAIT FOR PULLBACK',
          details: supportZoneLow && supportZoneHigh
            ? `Quality stock but extended. Wait for pullback to $${supportZoneLow}-${supportZoneHigh} zone before entry.`
            : `Quality stock but significantly extended. Wait for a meaningful pullback to establish new support levels.`,
          alertPrice: nearestSupport,
          bgColor: 'bg-gradient-to-r from-amber-600 to-orange-600',
          borderColor: 'border-amber-400',
          textColor: 'text-white',
          icon: '⏳',
          actionType: 'WAIT'
        };
      }
    }
    // HOLD verdict scenarios
    else if (verdict === 'HOLD') {
      if (viability?.viable === 'YES') {
        // Day 46 Fix: Use support as alert price (entry), not resistance
        // Show pullback preference if applicable
        if (isPullbackPreferred && pullbackIsFarBelow) {
          recommendation = {
            action: 'WATCHLIST - WAIT FOR PULLBACK',
            details: `Mixed signals. Wait for pullback to ~$${nearestSupport?.toFixed(2)} (${pctFromSupport}% below) for better entry.`,
            alertPrice: nearestSupport,
            bgColor: 'bg-gradient-to-r from-cyan-600 to-teal-600',
            borderColor: 'border-cyan-400',
            textColor: 'text-white',
            icon: '📊',
            actionType: 'WATCHLIST'
          };
        } else {
          recommendation = {
            action: 'WATCHLIST - MONITOR',
            details: `Decent setup near support (${pctFromSupport}% away). Watch for improving technicals or sentiment.`,
            alertPrice: nearestSupport, // Day 46: Changed from nearestResistance to nearestSupport
            bgColor: 'bg-gradient-to-r from-cyan-600 to-teal-600',
            borderColor: 'border-cyan-400',
            textColor: 'text-white',
            icon: '📊',
            actionType: 'WATCHLIST'
          };
        }
      } else {
        recommendation = {
          action: 'NOT NOW - PATIENCE',
          details: `Mixed signals and not near support. Set alert at $${nearestSupport?.toFixed(2) || 'lower levels'} and wait for better entry.`,
          alertPrice: nearestSupport,
          bgColor: 'bg-gradient-to-r from-slate-600 to-gray-600',
          borderColor: 'border-slate-400',
          textColor: 'text-white',
          icon: '⏸️',
          actionType: 'WAIT'
        };
      }
    }
    // AVOID verdict scenarios
    else {
      recommendation = {
        action: 'SKIP THIS ONE',
        details: `Does not meet criteria. Look for stocks with stronger technicals/fundamentals in a favorable regime.`,
        alertPrice: null,
        bgColor: 'bg-gradient-to-r from-red-700 to-rose-700',
        borderColor: 'border-red-500',
        textColor: 'text-white',
        icon: '🚫',
        actionType: 'AVOID'
      };
    }

    return recommendation;
  };

  // Generate plain English explanation for scores (Day 23)
  const generateScoreExplanation = (analysisResult) => {
    if (!analysisResult) return null;
    
    const tech = analysisResult.breakdown?.technical;
    const techScore = analysisResult.scores?.technical || 0;
    const fundScore = analysisResult.scores?.fundamental || 0;
    const totalScore = analysisResult.totalScore || 0;
    const currentPrice = analysisResult.currentPrice;
    const indicators = analysisResult.indicators;
    
    const reasons = [];
    
    // Technical explanation
    if (techScore < 20) {
      if (tech?.details?.trendStructure?.score === 0) {
        reasons.push(`Price ($${currentPrice?.toFixed(2)}) is below the 50 SMA ($${indicators?.sma50?.toFixed(2)}) - not in a Stage 2 uptrend`);
      }
      if (tech?.details?.shortTermTrend?.score === 0) {
        reasons.push(`Short-term momentum is weak - price below 8 EMA ($${indicators?.ema8?.toFixed(2)})`);
      }
    } else if (techScore >= 30) {
      reasons.push(`Strong technical setup with price above key moving averages`);
    }
    
    // Fundamental explanation
    if (fundScore >= 15) {
      reasons.push(`Solid fundamentals with good growth metrics`);
    } else if (fundScore < 10) {
      reasons.push(`Weak fundamentals - review EPS/Revenue growth`);
    }
    
    // Overall verdict context
    if (totalScore >= 60) {
      return { type: 'positive', reasons, summary: 'This stock meets most Minervini criteria for a swing trade.' };
    } else if (totalScore >= 40) {
      return { type: 'neutral', reasons, summary: 'Mixed signals - some criteria met, but not ideal setup.' };
    } else {
      return { type: 'negative', reasons, summary: 'Does not meet swing trade criteria. Wait for better setup.' };
    }
  };

  // Get sub-score label and description (Day 23)
  const getSubScoreInfo = (category, key, details) => {
    const labels = {
      technical: {
        trendStructure: { label: 'Trend Structure', desc: 'Price > 50 SMA > 200 SMA', icon: '📈' },
        shortTermTrend: { label: 'Short-term Trend', desc: 'Price > 8 EMA > 21 EMA', icon: '⚡' },
        volume: { label: 'Volume', desc: '≥1.5x 50-day average', icon: '📊' },
        relativeStrength: { label: 'Relative Strength', desc: 'Outperforming S&P 500', icon: '💪' }
      },
      fundamental: {
        epsGrowth: { label: 'EPS Growth', desc: 'Target ≥25%', icon: '💰' },
        revenueGrowth: { label: 'Revenue Growth', desc: 'Target ≥20%', icon: '📈' },
        roe: { label: 'ROE', desc: 'Target ≥15%', icon: '🎯' },
        debtToEquity: { label: 'Debt/Equity', desc: 'Target <0.5', icon: '⚖️' },
        forwardPe: { label: 'Forward P/E', desc: 'Target <20', icon: '📉' }
      }
    };
    return labels[category]?.[key] || { label: key, desc: '', icon: '•' };
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold text-blue-400">🎯 Swing Trade Analyzer</h1>
          <p className="text-gray-400 mt-2">Minervini SEPA + CAN SLIM Methodology</p>
          
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
                // Fetch provenance for current ticker if analyzed
                if (analysisResult?.stock?.ticker) {
                  setProvenanceLoading(true);
                  fetchDataProvenance(analysisResult.stock.ticker)
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
                    📊 Full Analysis (75-pt)
                  </button>
                  <button
                    onClick={() => setAnalysisView('matrix')}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                      analysisView === 'matrix'
                        ? 'bg-indigo-600 text-white'
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    🎯 Decision Matrix
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
                {/* v4.13: Holding Period Selector Toggle */}
                <div className="flex items-center gap-3 bg-gray-800/50 rounded-lg px-4 py-3">
                  <span className="text-sm text-gray-400 font-medium">Holding Period:</span>
                  <div className="flex gap-1">
                    {Object.entries(HOLDING_PERIODS).map(([key, config]) => (
                      <button
                        key={key}
                        className={`px-3 py-1.5 rounded-md text-sm font-medium transition-all ${
                          holdingPeriod === key
                            ? 'bg-blue-600 text-white shadow-lg'
                            : 'bg-gray-700 text-gray-400 hover:bg-gray-600 hover:text-gray-200'
                        }`}
                        onClick={() => setHoldingPeriod(key)}
                        title={`${config.name}: Tech ${Math.round(config.techWeight * 100)}% / Fund ${Math.round(config.fundWeight * 100)}%`}
                      >
                        {config.label}
                      </button>
                    ))}
                  </div>
                  <span className="text-xs text-gray-500 ml-2">
                    Tech {Math.round(HOLDING_PERIODS[holdingPeriod].techWeight * 100)}% / Fund {Math.round(HOLDING_PERIODS[holdingPeriod].fundWeight * 100)}%
                  </span>
                </div>

                {/* Verdict Card - v4.5 Categorical Assessment (Neutral design) */}
                <div className="rounded-lg p-6 bg-gray-800 border border-gray-700">
                  <div className="flex justify-between items-center">
                    <div>
                      <h2 className="text-2xl font-bold text-white">{analysisResult.ticker} - {analysisResult.name}</h2>
                      <p className="text-gray-400">
                        {analysisResult.sector} • {analysisResult.industry}
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
                    <div className="text-right">
                      <div className={`text-4xl font-bold px-4 py-2 rounded-lg ${
                        (categoricalResult?.verdict?.verdict || analysisResult.verdict?.verdict) === 'BUY'
                          ? 'text-green-400 bg-green-900/30 border border-green-600'
                          : (categoricalResult?.verdict?.verdict || analysisResult.verdict?.verdict) === 'HOLD'
                          ? 'text-yellow-400 bg-yellow-900/30 border border-yellow-600'
                          : 'text-red-400 bg-red-900/30 border border-red-600'
                      }`}>
                        {categoricalResult?.verdict?.verdict || analysisResult.verdict?.verdict || 'N/A'}
                      </div>
                      {categoricalResult && (
                        <div className="text-xs text-gray-500 mt-2 space-x-2">
                          <span className={categoricalResult.technical?.assessment === 'Strong' ? 'text-green-400' : categoricalResult.technical?.assessment === 'Decent' ? 'text-yellow-400' : 'text-red-400'}>
                            T:{categoricalResult.technical?.assessment?.charAt(0)}
                          </span>
                          <span className={categoricalResult.fundamental?.assessment === 'Strong' ? 'text-green-400' : categoricalResult.fundamental?.assessment === 'Decent' ? 'text-yellow-400' : categoricalResult.fundamental?.assessment === 'N/A' ? 'text-gray-400' : 'text-red-400'}>
                            F:{categoricalResult.fundamental?.assessment?.charAt(0)}
                          </span>
                          <span className={categoricalResult.sentiment?.assessment === 'Strong' ? 'text-green-400' : categoricalResult.sentiment?.assessment === 'Neutral' ? 'text-gray-400' : 'text-red-400'}>
                            S:{categoricalResult.sentiment?.assessment?.charAt(0)}
                          </span>
                          <span className={categoricalResult.riskMacro?.assessment === 'Favorable' ? 'text-green-400' : categoricalResult.riskMacro?.assessment === 'Neutral' ? 'text-yellow-400' : 'text-red-400'}>
                            R:{categoricalResult.riskMacro?.assessment?.charAt(0)}
                          </span>
                        </div>
                      )}
                    </div>
                  </div>
                </div>

                {/* Day 33: Data Source Status Banner - Prominent visibility for transparency */}
                {analysisResult.breakdown?.fundamental?.dataQuality &&
                 analysisResult.breakdown.fundamental.dataQuality !== 'rich' && (
                  <div className={`rounded-lg px-4 py-3 flex items-center gap-3 ${
                    analysisResult.breakdown.fundamental.dataQuality === 'unavailable'
                      ? 'bg-red-900/40 border border-red-700/50'
                      : 'bg-yellow-900/40 border border-yellow-700/50'
                  }`}>
                    <span className="text-2xl">
                      {analysisResult.breakdown.fundamental.dataQuality === 'unavailable' ? '⚠️' : '📡'}
                    </span>
                    <div className="flex-1">
                      <div className={`font-medium ${
                        analysisResult.breakdown.fundamental.dataQuality === 'unavailable'
                          ? 'text-red-300' : 'text-yellow-300'
                      }`}>
                        {analysisResult.breakdown.fundamental.dataQuality === 'unavailable'
                          ? 'Fundamentals Unavailable'
                          : 'Using Backup Data Source'}
                      </div>
                      <div className="text-xs text-gray-400">
                        {analysisResult.breakdown.fundamental.dataQuality === 'unavailable'
                          ? 'All data providers failed (Finnhub, FMP, yfinance). Fundamental score may be incomplete.'
                          : 'Primary providers unavailable. Using fallback source (limited data, may be slightly delayed).'}
                      </div>
                    </div>
                    <div className={`text-xs px-2 py-1 rounded ${
                      analysisResult.breakdown.fundamental.dataQuality === 'unavailable'
                        ? 'bg-red-800/50 text-red-300'
                        : 'bg-yellow-800/50 text-yellow-300'
                    }`}>
                      {analysisResult.breakdown.fundamental.dataSource || 'yfinance'}
                    </div>
                  </div>
                )}

                {/* Price & RS Info */}
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
                      {(() => {
                        const avgVol = rawAnalysisData?.stock?.avgVolume || 0;
                        const dollarVol = avgVol * (analysisResult.currentPrice || 0);
                        const color = dollarVol >= 50e6 ? 'text-green-400' : dollarVol >= 10e6 ? 'text-yellow-400' : 'text-red-400';
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
                        <span className={`font-bold ${analysisResult.rsData?.rsRatio >= 1.2 ? 'text-green-400' : analysisResult.rsData?.rsRatio >= 1.0 ? 'text-yellow-400' : 'text-red-400'}`}>
                          {analysisResult.rsData?.rs52Week?.toFixed(2) || analysisResult.rsData?.rsRatio?.toFixed(2) || 'N/A'}
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
                        <span className="text-gray-400">RS Rating:</span>
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
                    </div>
                  </div>
                </div>

                {/* Trade Setup Card (S&R) - Day 22: Enhanced with Viability */}
                {/* Day 49: Calculate R:R viability for badge specificity */}
                {srData && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    {/* Day 49: Pre-calculate R:R for viability badge */}
                    {/* Day 61: Uses shared riskRewardCalc utility (DRY) */}
                    {(() => {
                      const rr = calculateRiskReward(srData, srData.currentPrice);
                      const { pullbackRR: pullbackRRValue, momentumRR: momentumRRValue, pullbackViable, momentumViable, anyViable, nearestSupport } = rr;
                      const badge = getViabilityBadge(rr);
                      const viabilityLabel = badge.label;
                      const viabilityBg = badge.bg;
                      const viabilityIcon = badge.icon;

                      // Day 50: Check for AVOID verdict + VIABLE conflict
                      const verdictIsAvoid = categoricalResult?.verdict?.verdict === 'AVOID';
                      const anyViableSetup = anyViable;

                      return (
                        <>
                          {/* Header with Viability Badge - Day 49: Shows which strategy is viable */}
                          <div className="flex justify-between items-center mb-4">
                            <h3 className="text-lg font-semibold text-blue-400">🎯 Trade Setup</h3>
                            <div className="flex items-center gap-2">
                              <div className={`px-3 py-1 rounded-full text-sm font-bold ${viabilityBg} text-white`}>
                                {viabilityIcon} {viabilityLabel}
                              </div>
                              {/* Day 50: Warning when AVOID verdict but setup is viable */}
                              {verdictIsAvoid && anyViableSetup && (
                                <span className="text-yellow-400 text-xs" title="Setup viable but stock fundamentals/technicals don't support trading">
                                  ⚠️ Stock not recommended
                                </span>
                              )}
                            </div>
                          </div>
                        </>
                      );
                    })()}

                    {/* Viability Advice Banner (Day 22) */}
                    {/* Day 53 Bug #8: Backend viability (support distance) can contradict frontend R:R check */}
                    {/* Day 61: Uses shared riskRewardCalc utility (DRY) */}
                    {srData.meta?.tradeViability && (() => {
                      const _rr = calculateRiskReward(srData, srData.currentPrice);
                      const hasContradiction = hasViabilityContradiction(srData, _rr);
                      const backendViable = srData.meta.tradeViability.viable;

                      return (
                      <div className={`mb-4 p-3 rounded-lg text-sm ${
                        hasContradiction ? 'bg-yellow-900/30 border border-yellow-700 text-yellow-300' :
                        backendViable === 'YES' ? 'bg-green-900/30 border border-green-700 text-green-300' :
                        backendViable === 'CAUTION' ? 'bg-yellow-900/30 border border-yellow-700 text-yellow-300' :
                        backendViable === 'NO' ? 'bg-red-900/30 border border-red-700 text-red-300' :
                        'bg-gray-700/30 border border-gray-600 text-gray-300'
                      }`}>
                        <div className="flex justify-between items-start">
                          <div>
                            <span className="font-semibold">
                              {hasContradiction ? '⚠️ ' :
                               backendViable === 'YES' ? '✅ ' :
                               backendViable === 'CAUTION' ? '⚠️ ' :
                               backendViable === 'NO' ? '🚫 ' : ''}
                              {hasContradiction
                                ? 'Structural stop is sound, but R:R insufficient at current price'
                                : srData.meta.tradeViability.advice}
                            </span>
                            {/* Day 50: Hide position_size_advice when it conflicts with verdict/ADX */}
                            {srData.meta.tradeViability.position_size_advice &&
                             categoricalResult?.verdict?.verdict !== 'AVOID' &&
                             (srData.meta?.adx?.adx || 0) >= 20 && (
                              <div className="mt-1 text-xs opacity-80">
                                Position Size: {srData.meta.tradeViability.position_size_advice}
                              </div>
                            )}
                          </div>
                          <div className="text-right text-xs space-y-1">
                            {srData.meta.tradeViability.support_distance_pct !== null && (
                              <div>Support: {srData.meta.tradeViability.support_distance_pct}% away</div>
                            )}
                            {srData.meta.tradeViability.risk_reward_context && (
                              <div>R:R Context: {srData.meta.tradeViability.risk_reward_context}</div>
                            )}
                            {/* Day 39: ADX + RSI indicators - Day 40: Added tooltips */}
                            <div className="flex justify-end gap-2 mt-1">
                              {srData.meta?.adx && (
                                <span
                                  title={`ADX measures trend strength.\n≥25 = Strong trend (Pullback strategy preferred)\n<25 = Weak/ranging (Momentum strategy suggested)\nCurrent: ${srData.meta.adx.trend_strength}`}
                                  className={`px-1.5 py-0.5 rounded text-[10px] font-medium cursor-help ${
                                  srData.meta.adx.trend_strength === 'very_strong' ? 'bg-green-600 text-white' :
                                  srData.meta.adx.trend_strength === 'strong' ? 'bg-green-700 text-green-100' :
                                  srData.meta.adx.trend_strength === 'weak' ? 'bg-yellow-700 text-yellow-100' :
                                  'bg-red-700 text-red-100'
                                }`}>
                                  ADX {srData.meta.adx.adx}
                                </span>
                              )}
                              {srData.meta?.rsi_4h && (
                                <span
                                  title={`4-Hour RSI momentum indicator.\n<40 = Oversold (good entry zone)\n40-60 = Neutral\n>60 = Overbought (avoid new entries)\nUsed to confirm momentum entries.`}
                                  className={`px-1.5 py-0.5 rounded text-[10px] font-medium cursor-help ${
                                  srData.meta.rsi_4h.momentum === 'overbought' ? 'bg-red-600 text-white' :
                                  srData.meta.rsi_4h.momentum === 'strong' ? 'bg-green-600 text-white' :
                                  srData.meta.rsi_4h.momentum === 'neutral' ? 'bg-blue-600 text-white' :
                                  srData.meta.rsi_4h.momentum === 'weak' ? 'bg-yellow-600 text-white' :
                                  'bg-purple-600 text-white'
                                }`}>
                                  4H RSI {srData.meta.rsi_4h.rsi_4h}
                                </span>
                              )}
                              {/* Day 49 (v4.9): OBV indicator */}
                              {srData.meta?.obv && (
                                <span
                                  title={`On-Balance Volume (OBV):\n${srData.meta.obv.signal}\n\nOBV Trend: ${srData.meta.obv.trend}\nChange: ${srData.meta.obv.obv_change_pct}%\nDivergence: ${srData.meta.obv.divergence}`}
                                  className={`px-1.5 py-0.5 rounded text-[10px] font-medium cursor-help ${
                                  srData.meta.obv.divergence === 'bullish' ? 'bg-green-600 text-white' :
                                  srData.meta.obv.divergence === 'bearish' ? 'bg-red-600 text-white' :
                                  srData.meta.obv.trend === 'rising' ? 'bg-green-700 text-green-100' :
                                  srData.meta.obv.trend === 'falling' ? 'bg-red-700 text-red-100' :
                                  'bg-gray-600 text-gray-100'
                                }`}>
                                  OBV {srData.meta.obv.trend === 'rising' ? '↑' : srData.meta.obv.trend === 'falling' ? '↓' : '→'}
                                </span>
                              )}
                              {/* Day 49 (v4.9): RVOL (Relative Volume) display */}
                              {srData.meta?.rvol && (
                                <span
                                  title={`Relative Volume (RVOL):\nCurrent volume vs 50-day average.\n≥1.5x = High interest (breakout confirmation)\n1.0-1.5x = Normal activity\n<1.0x = Low interest\n\nCurrent: ${srData.meta.rvol_display}`}
                                  className={`px-1.5 py-0.5 rounded text-[10px] font-medium cursor-help ${
                                  srData.meta.rvol >= 2.0 ? 'bg-green-600 text-white' :
                                  srData.meta.rvol >= 1.5 ? 'bg-green-700 text-green-100' :
                                  srData.meta.rvol >= 1.0 ? 'bg-blue-700 text-blue-100' :
                                  'bg-gray-600 text-gray-100'
                                }`}>
                                  Vol {srData.meta.rvol_display}
                                </span>
                              )}
                              {/* Day 49: Distribution Warning - High RVOL + OBV Falling = big money selling */}
                              {srData.meta?.rvol >= 1.5 && srData.meta?.obv?.trend === 'falling' && (
                                <span
                                  title="⚠️ Distribution Signal:\nHigh volume (≥1.5x avg) + Falling OBV\n\nPossible Meaning:\n• Large players may be selling into strength\n• Volume expansion but money leaving the stock\n• Be cautious with new long positions\n\nThis doesn't mean the stock will fall, but suggests caution."
                                  className="px-1.5 py-0.5 rounded text-[10px] font-medium cursor-help bg-orange-600 text-white animate-pulse">
                                  ⚠️ DIST
                                </span>
                              )}
                            </div>
                          </div>
                        </div>
                      </div>
                      );
                    })()}

                    {/* Day 39: Dual Entry Strategy Cards - Side by Side (ALL stocks) */}
                    {/* Day 49: Fixed R:R filter + ADX-based suggestion logic + nearest support fix */}
                    {srData.support?.length > 0 && (
                      <div className="mb-4">
                        {(() => {
                          // Day 49: Fix - use nearest support (highest value below current price)
                          // Support array is not sorted, so find max to get nearest
                          const nearestSupport = Math.max(...srData.support);
                          const currentPrice = srData.currentPrice;
                          const adx = srData.meta?.adx;
                          const rsi4h = srData.meta?.rsi_4h;
                          const atr = srData.meta?.atr || 0;
                          const adxValue = adx?.adx || 0;

                          // Day 49: Corrected ADX-based strategy preference
                          // ADX >= 25: Strong trend - prefer pullback entries
                          // ADX 20-25: Weak trend - either strategy viable
                          // ADX < 20: No trend - wait, don't suggest entries
                          const strongTrend = adxValue >= 25;
                          const weakTrend = adxValue >= 20 && adxValue < 25;
                          const noTrend = adxValue < 20;

                          // Pullback Strategy calculations
                          const pullbackEntry = nearestSupport;
                          const pullbackStop = nearestSupport - (atr * 2);
                          const pullbackTarget = srData.suggestedTarget || currentPrice * 1.10;
                          const pullbackRisk = pullbackEntry - pullbackStop;
                          const pullbackReward = pullbackTarget - pullbackEntry;
                          const pullbackRRValue = pullbackRisk > 0 ? pullbackReward / pullbackRisk : 0;
                          const pullbackRR = pullbackRRValue > 0 ? pullbackRRValue.toFixed(2) : 'N/A';

                          // Momentum Strategy calculations
                          const momentumEntry = currentPrice;
                          const momentumStop = nearestSupport - (atr * 1.5);
                          const momentumTarget = pullbackTarget;
                          const momentumRisk = momentumEntry - momentumStop;
                          const momentumReward = momentumTarget - momentumEntry;
                          const momentumRRValue = momentumRisk > 0 ? momentumReward / momentumRisk : 0;
                          const momentumRR = momentumRRValue > 0 ? momentumRRValue.toFixed(2) : 'N/A';

                          const rsiConfirmed = rsi4h && rsi4h.entry_signal;

                          // Day 49: R:R filter - don't suggest entries with R:R < 1.0
                          const pullbackViable = pullbackRRValue >= 1.0;
                          const momentumViable = momentumRRValue >= 1.0;

                          // Day 50: Show warning but ALWAYS show entry cards (grayed out when not viable)
                          const showNoTrendWarning = noTrend && !pullbackViable && !momentumViable;

                          return (
                            <>
                              {/* Day 50: Warning banner shown when no trend and both R:R < 1 */}
                              {showNoTrendWarning && (
                                <div className="bg-yellow-900/30 border border-yellow-700 rounded-lg p-4 text-center mb-3">
                                  <span className="text-yellow-400 font-medium">⚠️ Wait for Better Setup</span>
                                  <div className="text-gray-400 text-sm mt-1">
                                    ADX {adxValue.toFixed(1)} indicates no trend. R:R unfavorable at current levels.
                                  </div>
                                </div>
                              )}
                              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                              {/* Strategy A: Pullback */}
                              <div className={`rounded-lg p-4 ${
                                !pullbackViable ? 'bg-red-900/20 border border-red-800/50 opacity-60' :
                                strongTrend ? 'bg-green-900/30 border-2 border-green-600' :
                                'bg-gray-800/50 border border-gray-700'
                              }`}>
                                <div className="flex items-center justify-between mb-3">
                                  <span className="font-semibold text-gray-200 cursor-help" title="Wait for price to pull back to support level before entering. Lower risk, better R:R, but may miss fast moves.">Entry Strategy: Pullback</span>
                                  {!pullbackViable && <span className="text-red-400 text-xs font-medium" title="Risk/Reward below 1.0 - trade not favorable">⛔ R:R &lt; 1</span>}
                                  {pullbackViable && strongTrend && <span className="text-green-400 text-xs font-medium cursor-help" title="ADX ≥25 indicates strong trend. Pullback entries work best in trending markets.">★ PREFERRED</span>}
                                </div>
                                <div className="space-y-2 text-sm">
                                  <div className="flex justify-between">
                                    <span className="text-gray-400">Entry</span>
                                    <span className="text-gray-200 font-mono">{formatCurrency(pullbackEntry)}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400">Stop</span>
                                    <span className="text-red-400 font-mono">{formatCurrency(pullbackStop)}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400">Target</span>
                                    <span className="text-green-400 font-mono">{formatCurrency(pullbackTarget)}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400 cursor-help" title="Risk-to-Reward ratio. >2:1 is good, >3:1 is excellent. Shows potential reward per $1 risked.">R:R</span>
                                    <span className={`font-mono ${parseFloat(pullbackRR) >= 2 ? 'text-green-400' : parseFloat(pullbackRR) >= 1 ? 'text-yellow-400' : 'text-red-400'}`}>{pullbackRR}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400 cursor-help" title="Position size recommendation based on trend strength. Full = ADX 25+, Reduced = ADX 20-25, Wait = ADX <20">Position</span>
                                    <span className={`${strongTrend ? 'text-green-400' : weakTrend ? 'text-yellow-400' : 'text-gray-400'}`}>
                                      {strongTrend ? 'full' : weakTrend ? 'reduced' : 'wait'}
                                    </span>
                                  </div>
                                  <div className="pt-2 border-t border-gray-700">
                                    <span className="text-gray-400 text-xs">Reason</span>
                                    <div className="text-gray-300 text-xs mt-1">
                                      {adxValue >= 30
                                        ? `ADX ${adxValue.toFixed(1)} very strong trend; momentum entry viable`
                                        : strongTrend
                                        ? `ADX ${adxValue.toFixed(1)} strong trend; pullback preferred for better R:R`
                                        : weakTrend
                                        ? `ADX ${adxValue.toFixed(1)} moderate trend; reduce position size`
                                        : `ADX ${adxValue.toFixed(1)} no trend; wait for trend to develop`
                                      }
                                    </div>
                                  </div>
                                </div>
                              </div>

                              {/* Strategy B: Momentum */}
                              <div className={`rounded-lg p-4 ${
                                !momentumViable ? 'bg-red-900/20 border border-red-800/50 opacity-60' :
                                weakTrend && momentumViable && rsiConfirmed ? 'bg-blue-900/30 border-2 border-blue-600' :
                                'bg-gray-800/50 border border-gray-700'
                              }`}>
                                <div className="flex items-center justify-between mb-3">
                                  <span className="font-semibold text-gray-200 cursor-help" title="Enter at current price on breakout/momentum. Higher risk (wider stop), but captures immediate moves. Use half position.">Entry Strategy: Momentum</span>
                                  {!momentumViable && <span className="text-red-400 text-xs font-medium" title="Risk/Reward below 1.0 - trade not favorable">⛔ R:R &lt; 1</span>}
                                  {momentumViable && weakTrend && rsiConfirmed && <span className="text-blue-400 text-xs font-medium cursor-help" title="ADX 20-25 with RSI confirmation. Momentum entry viable with proper risk management.">★ VIABLE</span>}
                                  {momentumViable && noTrend && <span className="text-yellow-400 text-xs font-medium cursor-help" title="ADX <20 no trend. Consider waiting for better setup.">⚠️ CAUTION</span>}
                                </div>
                                <div className="space-y-2 text-sm">
                                  <div className="flex justify-between">
                                    <span className="text-gray-400">Entry</span>
                                    <span className="text-gray-200 font-mono">{formatCurrency(momentumEntry)}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400">Stop</span>
                                    <span className="text-red-400 font-mono">{formatCurrency(momentumStop)}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400">Target</span>
                                    <span className="text-green-400 font-mono">{formatCurrency(momentumTarget)}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400 cursor-help" title="Risk-to-Reward ratio. >2:1 is good, >3:1 is excellent. Momentum entries typically have lower R:R due to wider stops.">R:R</span>
                                    <span className={`font-mono ${parseFloat(momentumRR) >= 2 ? 'text-green-400' : parseFloat(momentumRR) >= 1 ? 'text-yellow-400' : 'text-red-400'}`}>{momentumRR}</span>
                                  </div>
                                  <div className="flex justify-between">
                                    <span className="text-gray-400 cursor-help" title="Position size recommendation. 'Half' = reduced position due to higher risk from entering at current price with wider stop.">Position</span>
                                    <span className="text-yellow-400">half</span>
                                  </div>
                                  <div className="pt-2 border-t border-gray-700 space-y-1">
                                    <div className="flex justify-between">
                                      <span className="text-gray-400 text-xs cursor-help" title="4-hour timeframe RSI. Used to confirm momentum entries. <40 is oversold (good), >60 is overbought (avoid).">4H RSI</span>
                                      <span className={`text-xs font-mono ${rsi4h ? (rsi4h.entry_signal ? 'text-green-400' : 'text-yellow-400') : 'text-gray-500'}`}>
                                        {rsi4h ? rsi4h.rsi_4h : 'N/A'}
                                      </span>
                                    </div>
                                    <div className="flex justify-between">
                                      <span className="text-gray-400 text-xs cursor-help" title="Entry confirmed when 4H RSI shows oversold (<40) or rising from lows. 'not_confirmed' means wait for better entry.">Confirmation</span>
                                      <span className={`text-xs ${rsiConfirmed ? 'text-green-400' : 'text-red-400'}`}>
                                        {rsiConfirmed ? 'confirmed' : 'not_confirmed'}
                                      </span>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                            </>
                          );
                        })()}
                      </div>
                    )}

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
                              ({srData.meta.mtf.confluent_levels}/{srData.meta.mtf.total_levels} levels)
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
                                    {isConfluent && <span className="text-yellow-400 mr-1" title="Confluent with weekly level">★</span>}
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
                                    {isConfluent && <span className="text-yellow-400 mr-1" title="Confluent with weekly level">★</span>}
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
                  </div>
                )}

                {/* Pattern Detection Card - Day 44: VCP, Cup & Handle, Flat Base */}
                {patternsData && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <div className="flex justify-between items-center mb-4">
                      <h3 className="text-lg font-semibold text-purple-400">📐 Pattern Detection</h3>
                      {patternsData.summary?.count > 0 && (
                        <div className="px-3 py-1 rounded-full text-sm font-bold bg-purple-900/50 text-purple-300 border border-purple-600">
                          {patternsData.summary.count} Pattern{patternsData.summary.count > 1 ? 's' : ''} Found
                        </div>
                      )}
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

                    {/* Pattern Cards */}
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                      {/* VCP Pattern */}
                      <div className={`rounded-lg p-3 ${
                        patternsData.patterns?.vcp?.detected
                          ? 'bg-green-900/30 border border-green-600'
                          : 'bg-gray-700/30 border border-gray-600'
                      }`}>
                        <div className="flex justify-between items-center mb-2">
                          <span className="font-medium text-gray-200 cursor-help" title="Volatility Contraction Pattern (VCP) - Mark Minervini's signature pattern. Price makes a series of smaller pullbacks, showing selling pressure drying up before breakout.">VCP</span>
                          <span className={`text-xs px-2 py-0.5 rounded ${
                            patternsData.patterns?.vcp?.detected ? 'bg-green-600 text-white' : 'bg-gray-600 text-gray-300'
                          }`}>
                            {patternsData.patterns?.vcp?.confidence || 0}%
                          </span>
                        </div>
                        <div className="text-xs space-y-1">
                          <div className="flex justify-between text-gray-400">
                            <span>Contractions</span>
                            <span className="text-gray-300">{patternsData.patterns?.vcp?.contractions_count || 0}</span>
                          </div>
                          <div className="flex justify-between text-gray-400">
                            <span>Tight Base</span>
                            <span className={patternsData.patterns?.vcp?.tight_base ? 'text-green-400' : 'text-gray-500'}>
                              {patternsData.patterns?.vcp?.tight_base ? 'Yes' : 'No'}
                            </span>
                          </div>
                          <div className="flex justify-between text-gray-400">
                            <span>Status</span>
                            <span className={`${
                              patternsData.patterns?.vcp?.status === 'at_pivot' ? 'text-yellow-400' :
                              patternsData.patterns?.vcp?.status === 'broken_out' ? 'text-green-400' :
                              'text-gray-300'
                            }`}>
                              {patternsData.patterns?.vcp?.status || 'N/A'}
                            </span>
                          </div>
                          {patternsData.patterns?.vcp?.pivot_price && (
                            <div className="flex justify-between text-gray-400">
                              <span>Pivot</span>
                              <span className="text-blue-400 font-mono">${patternsData.patterns.vcp.pivot_price.toFixed(2)}</span>
                            </div>
                          )}
                          <div className="text-gray-500 italic mt-1.5 pt-1.5 border-t border-gray-600">
                            Sellers exhausted — each pullback smaller. Lowest risk breakout entry.
                          </div>
                        </div>
                      </div>

                      {/* Cup & Handle Pattern */}
                      <div className={`rounded-lg p-3 ${
                        patternsData.patterns?.cupHandle?.detected
                          ? 'bg-green-900/30 border border-green-600'
                          : 'bg-gray-700/30 border border-gray-600'
                      }`}>
                        <div className="flex justify-between items-center mb-2">
                          <span className="font-medium text-gray-200 cursor-help" title="Cup and Handle - William O'Neil's classic pattern. U-shaped cup formation followed by a small handle pullback before breakout.">Cup & Handle</span>
                          <span className={`text-xs px-2 py-0.5 rounded ${
                            patternsData.patterns?.cupHandle?.detected ? 'bg-green-600 text-white' : 'bg-gray-600 text-gray-300'
                          }`}>
                            {patternsData.patterns?.cupHandle?.confidence || 0}%
                          </span>
                        </div>
                        <div className="text-xs space-y-1">
                          <div className="flex justify-between text-gray-400">
                            <span>Cup Depth</span>
                            <span className="text-gray-300">{patternsData.patterns?.cupHandle?.cup?.depth_pct?.toFixed(1) || 'N/A'}%</span>
                          </div>
                          <div className="flex justify-between text-gray-400">
                            <span>U-Shaped</span>
                            <span className={patternsData.patterns?.cupHandle?.cup?.u_shaped ? 'text-green-400' : 'text-gray-500'}>
                              {patternsData.patterns?.cupHandle?.cup?.u_shaped ? 'Yes' : 'No'}
                            </span>
                          </div>
                          <div className="flex justify-between text-gray-400">
                            <span>Status</span>
                            <span className={`${
                              patternsData.patterns?.cupHandle?.status === 'complete' ? 'text-yellow-400' :
                              patternsData.patterns?.cupHandle?.status === 'broken_out' ? 'text-green-400' :
                              'text-gray-300'
                            }`}>
                              {patternsData.patterns?.cupHandle?.status || 'N/A'}
                            </span>
                          </div>
                          {patternsData.patterns?.cupHandle?.pivot_price && (
                            <div className="flex justify-between text-gray-400">
                              <span>Pivot</span>
                              <span className="text-blue-400 font-mono">${patternsData.patterns.cupHandle.pivot_price.toFixed(2)}</span>
                            </div>
                          )}
                          <div className="text-gray-500 italic mt-1.5 pt-1.5 border-t border-gray-600">
                            Institutional accumulation. Handle shakes out weak hands before real move.
                          </div>
                        </div>
                      </div>

                      {/* Flat Base Pattern */}
                      <div className={`rounded-lg p-3 ${
                        patternsData.patterns?.flatBase?.detected
                          ? 'bg-green-900/30 border border-green-600'
                          : 'bg-gray-700/30 border border-gray-600'
                      }`}>
                        <div className="flex justify-between items-center mb-2">
                          <span className="font-medium text-gray-200 cursor-help" title="Flat Base - Tight consolidation after a strong uptrend. Price moves sideways in a narrow range as the stock digests gains before continuing higher.">Flat Base</span>
                          <span className={`text-xs px-2 py-0.5 rounded ${
                            patternsData.patterns?.flatBase?.detected ? 'bg-green-600 text-white' : 'bg-gray-600 text-gray-300'
                          }`}>
                            {patternsData.patterns?.flatBase?.confidence || 0}%
                          </span>
                        </div>
                        <div className="text-xs space-y-1">
                          <div className="flex justify-between text-gray-400">
                            <span>Range</span>
                            <span className="text-gray-300">{patternsData.patterns?.flatBase?.base?.range_pct?.toFixed(1) || 'N/A'}%</span>
                          </div>
                          <div className="flex justify-between text-gray-400">
                            <span>Prior Uptrend</span>
                            <span className={patternsData.patterns?.flatBase?.prior_uptrend?.has_30pct_move ? 'text-green-400' : 'text-gray-500'}>
                              {patternsData.patterns?.flatBase?.prior_uptrend?.pct?.toFixed(0) || 'N/A'}%
                            </span>
                          </div>
                          <div className="flex justify-between text-gray-400">
                            <span>Status</span>
                            <span className={`${
                              patternsData.patterns?.flatBase?.status === 'forming' ? 'text-yellow-400' :
                              patternsData.patterns?.flatBase?.status === 'broken_out' ? 'text-green-400' :
                              'text-gray-300'
                            }`}>
                              {patternsData.patterns?.flatBase?.status || 'N/A'}
                            </span>
                          </div>
                          {patternsData.patterns?.flatBase?.pivot_price && (
                            <div className="flex justify-between text-gray-400">
                              <span>Pivot</span>
                              <span className="text-blue-400 font-mono">${patternsData.patterns.flatBase.pivot_price.toFixed(2)}</span>
                            </div>
                          )}
                          <div className="text-gray-500 italic mt-1.5 pt-1.5 border-t border-gray-600">
                            Digesting gains in tight range. Compression before next leg up.
                          </div>
                        </div>
                      </div>
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
                                  <div className="text-green-400 font-mono font-medium">${pattern.targetPrice?.toFixed(2)}</div>
                                </div>
                              </div>
                              {/* Volume Confirmation Row */}
                              {pattern.breakout?.volumeRatio && (
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
                                <span className="text-gray-400">R:R {pattern.riskReward}:1</span>
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

                {/* TradingView Widget - Day 34: Supplementary RSI/MACD view */}
                {analysisResult && (
                  <div className="bg-gray-800 rounded-lg p-4">
                    <button
                      onClick={() => setTvWidgetCollapsed(!tvWidgetCollapsed)}
                      className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors w-full text-left"
                    >
                      <span className="text-lg">{tvWidgetCollapsed ? '▶' : '▼'}</span>
                      <span className="font-medium">📺 TradingView Chart</span>
                      <span className="text-xs text-gray-500 ml-auto">RSI, MACD, Volume</span>
                    </button>

                    {!tvWidgetCollapsed && (
                      <div className="mt-3">
                        <div className="border border-gray-700 rounded-lg overflow-hidden">
                          {/* TradingView Advanced Chart Widget */}
                          <div
                            className="tradingview-widget-container"
                            style={{ height: '400px' }}
                          >
                            <iframe
                              key={analysisResult.ticker} // Force re-render on ticker change
                              src={`https://www.tradingview.com/widgetembed/?frameElementId=tradingview_widget&symbol=${analysisResult.ticker}&interval=D&hidesidetoolbar=0&symboledit=0&saveimage=0&toolbarbg=f1f3f6&studies=%5B%22RSI%40tv-basicstudies%22%2C%22MACD%40tv-basicstudies%22%5D&theme=dark&style=1&timezone=America%2FNew_York&withdateranges=1&showpopupbutton=0&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en&utm_source=localhost&utm_medium=widget_new&utm_campaign=chart&utm_term=${analysisResult.ticker}`}
                              style={{ width: '100%', height: '400px', border: 'none' }}
                              title={`TradingView Chart for ${analysisResult.ticker}`}
                              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            />
                          </div>
                        </div>
                        <div className="bg-yellow-900/20 text-yellow-400/80 text-xs p-2 text-center rounded-b-lg border-x border-b border-yellow-700/30 mt-0">
                          ⚠️ Our S&R levels are shown in Trade Setup above. This widget provides supplementary RSI/MACD indicators.
                        </div>
                      </div>
                    )}
                  </div>
                )}

                {/* v4.13: Bottom Line Card - replaces old Actionable Recommendation (Day 44) */}
                <BottomLineCard
                  categoricalResult={categoricalResult}
                  srData={srData}
                  currentPrice={analysisResult?.currentPrice}
                  holdingPeriod={holdingPeriod}
                />

                {/* Categorical Assessment - v4.5 (Day 44) */}
                {categoricalResult && (
                <div className="bg-gray-800 rounded-lg p-6">
                  <h3 className="text-lg font-semibold mb-4 text-blue-400">📊 Assessment <span className="text-xs text-gray-500 font-normal ml-2">Click to expand</span></h3>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    {/* Technical Card */}
                    <div
                      className={`bg-gray-700/50 rounded-lg p-4 cursor-pointer transition-all hover:bg-gray-700 ${expandedScore === 'technical' ? 'ring-2 ring-blue-500' : ''}`}
                      onClick={() => setExpandedScore(expandedScore === 'technical' ? null : 'technical')}
                    >
                      <div className="flex justify-between items-center">
                        <div className="text-gray-400 text-sm">Technical</div>
                        <span className="text-gray-500 text-xs">{expandedScore === 'technical' ? '▼' : '▶'}</span>
                      </div>
                      <div className={`text-xl font-bold ${
                        categoricalResult.technical.assessment === 'Strong' ? 'text-green-400' :
                        categoricalResult.technical.assessment === 'Decent' ? 'text-yellow-400' : 'text-red-400'
                      }`}>
                        {categoricalResult.technical.assessment}
                      </div>
                    </div>
                    {/* Fundamental Card */}
                    <div
                      className={`bg-gray-700/50 rounded-lg p-4 cursor-pointer transition-all hover:bg-gray-700 ${expandedScore === 'fundamental' ? 'ring-2 ring-blue-500' : ''}`}
                      onClick={() => setExpandedScore(expandedScore === 'fundamental' ? null : 'fundamental')}
                    >
                      <div className="flex justify-between items-center">
                        <div className="text-gray-400 text-sm">Fundamental</div>
                        <span className="text-gray-500 text-xs">{expandedScore === 'fundamental' ? '▼' : '▶'}</span>
                      </div>
                      <div className={`text-xl font-bold ${
                        categoricalResult.fundamental.assessment === 'Strong' ? 'text-green-400' :
                        categoricalResult.fundamental.assessment === 'Decent' ? 'text-yellow-400' :
                        categoricalResult.fundamental.assessment === 'N/A' || categoricalResult.fundamental.assessment === 'Unknown' ? 'text-gray-400' : 'text-red-400'
                      }`}>
                        {categoricalResult.fundamental.assessment}
                      </div>
                    </div>
                    {/* Sentiment Card */}
                    <div
                      className={`bg-gray-700/50 rounded-lg p-4 cursor-pointer transition-all hover:bg-gray-700 ${expandedScore === 'sentiment' ? 'ring-2 ring-blue-500' : ''}`}
                      onClick={() => setExpandedScore(expandedScore === 'sentiment' ? null : 'sentiment')}
                    >
                      <div className="flex justify-between items-center">
                        <div className="text-gray-400 text-sm">Sentiment</div>
                        <span className="text-gray-500 text-xs">{expandedScore === 'sentiment' ? '▼' : '▶'}</span>
                      </div>
                      <div className={`text-xl font-bold ${
                        categoricalResult.sentiment.assessment === 'Strong' ? 'text-green-400' :
                        categoricalResult.sentiment.assessment === 'Neutral' ? 'text-gray-300' : 'text-red-400'
                      }`}>
                        {categoricalResult.sentiment.assessment}
                      </div>
                      {fearGreedData && (
                        <div className="text-xs text-gray-500 mt-1">F&G: {fearGreedData.value}</div>
                      )}
                    </div>
                    {/* Risk/Macro Card */}
                    <div
                      className={`bg-gray-700/50 rounded-lg p-4 cursor-pointer transition-all hover:bg-gray-700 ${expandedScore === 'risk' ? 'ring-2 ring-blue-500' : ''}`}
                      onClick={() => setExpandedScore(expandedScore === 'risk' ? null : 'risk')}
                    >
                      <div className="flex justify-between items-center">
                        <div className="text-gray-400 text-sm">Risk/Macro</div>
                        <span className="text-gray-500 text-xs">{expandedScore === 'risk' ? '▼' : '▶'}</span>
                      </div>
                      <div className={`text-xl font-bold ${
                        categoricalResult.riskMacro.assessment === 'Favorable' ? 'text-green-400' :
                        categoricalResult.riskMacro.assessment === 'Neutral' ? 'text-yellow-400' : 'text-red-400'
                      }`}>
                        {categoricalResult.riskMacro.assessment}
                      </div>
                    </div>
                  </div>

                  {/* Expanded Details Panel */}
                  {expandedScore && (
                    <div className="mt-4 bg-gray-700/30 rounded-lg p-4 border border-gray-600">
                      {expandedScore === 'technical' && categoricalResult.technical && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">📈 Technical Assessment: {categoricalResult.technical.assessment}</div>
                          <ul className="list-disc list-inside space-y-1 text-gray-400 text-sm">
                            {categoricalResult.technical.reasons.map((reason, idx) => (
                              <li key={idx}>{reason}</li>
                            ))}
                          </ul>
                          {categoricalResult.technical.data && (
                            <div className="grid grid-cols-2 gap-2 text-xs text-gray-500 mt-3 pt-2 border-t border-gray-600">
                              <div>Trend Template: {categoricalResult.technical.data.trendTemplateScore}</div>
                              <div>RSI: {categoricalResult.technical.data.rsi?.toFixed(1)}</div>
                              <div>RS vs SPY: {categoricalResult.technical.data.rs52Week?.toFixed(2)}x</div>
                            </div>
                          )}
                          <div className="text-xs text-gray-500 mt-2">Data: Multi-Source OHLCV + Pattern Detection</div>
                        </div>
                      )}
                      {expandedScore === 'fundamental' && categoricalResult.fundamental && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">💼 Fundamental Assessment: {categoricalResult.fundamental.assessment}</div>
                          <ul className="list-disc list-inside space-y-1 text-gray-400 text-sm">
                            {categoricalResult.fundamental.reasons.map((reason, idx) => (
                              <li key={idx}>{reason}</li>
                            ))}
                          </ul>
                          <div className="text-xs text-gray-500 mt-2 pt-2 border-t border-gray-600">
                            Data: {categoricalResult.fundamental.data?.dataSource || 'Multi-Source'}
                          </div>
                        </div>
                      )}
                      {expandedScore === 'sentiment' && categoricalResult.sentiment && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">📰 Sentiment Assessment: {categoricalResult.sentiment.assessment}</div>
                          <ul className="list-disc list-inside space-y-1 text-gray-400 text-sm">
                            {categoricalResult.sentiment.reasons.map((reason, idx) => (
                              <li key={idx}>{reason}</li>
                            ))}
                          </ul>
                          {fearGreedData && (
                            <div className="mt-3 pt-2 border-t border-gray-600">
                              <div className="flex items-center gap-2">
                                <span className="text-gray-400 text-sm">Fear & Greed Index:</span>
                                <span className={`text-lg font-bold ${
                                  fearGreedData.value >= 60 && fearGreedData.value <= 80 ? 'text-green-400' :
                                  fearGreedData.value >= 35 && fearGreedData.value < 60 ? 'text-gray-300' : 'text-red-400'
                                }`}>{fearGreedData.value}</span>
                                <span className="text-gray-500 text-sm">({fearGreedData.rating})</span>
                              </div>
                              <div className="w-full bg-gray-600 rounded-full h-3 mt-2">
                                <div
                                  className={`h-3 rounded-full ${
                                    fearGreedData.value < 25 ? 'bg-red-500' :
                                    fearGreedData.value < 35 ? 'bg-orange-500' :
                                    fearGreedData.value < 60 ? 'bg-gray-400' :
                                    fearGreedData.value < 80 ? 'bg-green-500' : 'bg-red-500'
                                  }`}
                                  style={{ width: `${fearGreedData.value}%` }}
                                ></div>
                              </div>
                              <div className="flex justify-between text-xs text-gray-500 mt-1">
                                <span>Extreme Fear</span>
                                <span>Neutral</span>
                                <span>Extreme Greed</span>
                              </div>
                            </div>
                          )}
                          <div className="text-xs text-gray-500 mt-2">Data: {fearGreedData?.source || 'CNN Fear & Greed Index'}</div>
                        </div>
                      )}
                      {expandedScore === 'risk' && categoricalResult.riskMacro && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">⚡ Risk/Macro Assessment: {categoricalResult.riskMacro.assessment}</div>
                          <ul className="list-disc list-inside space-y-1 text-gray-400 text-sm">
                            {categoricalResult.riskMacro.reasons.map((reason, idx) => (
                              <li key={idx}>{reason}</li>
                            ))}
                          </ul>
                          <div className="grid grid-cols-2 gap-4 text-sm mt-3 pt-2 border-t border-gray-600">
                            <div>
                              <span className="text-gray-400">VIX:</span>
                              <span className={`ml-2 ${
                                categoricalResult.riskMacro.data?.vix < 20 ? 'text-green-400' :
                                categoricalResult.riskMacro.data?.vix <= 30 ? 'text-yellow-400' : 'text-red-400'
                              }`}>
                                {categoricalResult.riskMacro.data?.vix?.toFixed(1) || 'N/A'}
                              </span>
                            </div>
                            <div>
                              <span className="text-gray-400">SPY Regime:</span>
                              <span className={`ml-2 ${categoricalResult.riskMacro.data?.spyAbove200EMA ? 'text-green-400' : 'text-red-400'}`}>
                                {categoricalResult.riskMacro.data?.spyAbove200EMA ? 'Bull' : 'Bear'}
                              </span>
                            </div>
                          </div>
                          <div className="text-xs text-gray-500 mt-2">Data: Multi-Source (VIX, SPY)</div>
                        </div>
                      )}
                    </div>
                  )}

                  {/* Categorical Verdict Summary */}
                  <div className={`mt-4 p-4 rounded-lg text-sm ${
                    categoricalResult.verdict.verdict === 'BUY' ? 'bg-green-900/20 border border-green-800' :
                    categoricalResult.verdict.verdict === 'AVOID' ? 'bg-red-900/20 border border-red-800' :
                    'bg-yellow-900/20 border border-yellow-800'
                  }`}>
                    <div className="font-semibold mb-2 text-gray-200">
                      💡 Why This Verdict?
                    </div>
                    <p className="text-gray-400 mb-2">{categoricalResult.verdict.reason}</p>
                    <div className="text-xs text-gray-500">
                      Criteria: Need 2+ Strong categories with Favorable/Neutral risk for BUY
                    </div>
                  </div>
                </div>
                )}

                {/* Technical Indicators */}
                <div className="bg-gray-800 rounded-lg p-6">
                  <h3 className="text-lg font-semibold mb-4 text-blue-400">📉 Technical Indicators</h3>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                    <div>
                      <span className="text-gray-400">RSI (14): </span>
                      <span className={getRsiColor(analysisResult.indicators?.rsi)}>
                        {analysisResult.indicators?.rsi?.toFixed(1) || 'N/A'}
                      </span>
                    </div>
                    <div>
                      <span className="text-gray-400">8 EMA: </span>
                      <span className="text-green-400">{formatCurrency(analysisResult.indicators?.ema8)}</span>
                    </div>
                    <div>
                      <span className="text-gray-400">21 EMA: </span>
                      <span className="text-green-400">{formatCurrency(analysisResult.indicators?.ema21)}</span>
                    </div>
                    <div>
                      <span className="text-gray-400">50 SMA: </span>
                      <span className="text-green-400">{formatCurrency(analysisResult.indicators?.sma50)}</span>
                    </div>
                    <div>
                      <span className="text-gray-400">200 SMA: </span>
                      <span className="text-green-400">{formatCurrency(analysisResult.indicators?.sma200)}</span>
                    </div>
                    <div>
                      <span className="text-gray-400">ATR: </span>
                      <span className="text-yellow-400">
                        {analysisResult.indicators?.atr ? formatCurrency(analysisResult.indicators.atr) : 'N/A'}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Quality Gates */}
                {analysisResult.qualityGates && analysisResult.qualityGates.gates?.length > 0 && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h3 className="text-lg font-semibold mb-4 text-red-400">⚠️ Quality Gate Warnings</h3>
                    <div className="space-y-2">
                      {analysisResult.qualityGates.gates.map((gate, idx) => (
                        <div key={idx} className="bg-red-900/30 rounded p-3 text-sm">
                          <span className="font-semibold text-red-400">{gate.name}:</span>{' '}
                          <span className="text-gray-300">{gate.value}</span>
                          <span className="text-gray-500"> (threshold: {gate.threshold})</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* ==================== DECISION MATRIX VIEW (Day 53) ==================== */}
            {analysisResult && !loading && analysisView === 'matrix' && (
              <div className="space-y-6">
                {/* Day 53: Holding Period Selector (same as full view) */}
                <div className="flex items-center gap-3 bg-gray-800/50 rounded-lg px-4 py-3">
                  <span className="text-sm text-gray-400 font-medium">Holding Period:</span>
                  <div className="flex gap-1">
                    {Object.entries(HOLDING_PERIODS).map(([key, config]) => (
                      <button
                        key={key}
                        className={`px-3 py-1.5 rounded-md text-sm font-medium transition-all ${
                          holdingPeriod === key
                            ? 'bg-blue-600 text-white shadow-lg'
                            : 'bg-gray-700 text-gray-400 hover:bg-gray-600 hover:text-gray-200'
                        }`}
                        onClick={() => setHoldingPeriod(key)}
                        title={`${config.name}: Tech ${Math.round(config.techWeight * 100)}% / Fund ${Math.round(config.fundWeight * 100)}%`}
                      >
                        {config.label}
                      </button>
                    ))}
                  </div>
                </div>

                <DecisionMatrix
                  categoricalResult={categoricalResult}
                  analysisResult={analysisResult}
                  srData={srData}
                  patternsData={patternsData}
                  holdingPeriod={holdingPeriod}
                  currentPrice={analysisResult?.currentPrice}
                />
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
                        {analysisResult.sector} • {analysisResult.industry}
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
                      </p>
                    </div>
                    <div className="text-right">
                      <div className="text-4xl font-bold">
                        {simplifiedResult.verdict === 'TRADE' ? '✅ TRADE' : '⏸️ PASS'}
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
                        <div className="text-xl font-bold text-red-400">{formatCurrency(srData.suggestedStop)}</div>
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
                    <strong>Rule:</strong> ALL 9 criteria must be YES to take a trade. Any NO = PASS. No exceptions.
                  </p>
                </div>

                {/* Compare with Full Assessment */}
                <div className="bg-gray-800 rounded-lg p-4">
                  <div className="flex justify-between items-center">
                    <div>
                      <span className="text-gray-400 text-sm">Full Assessment (for comparison):</span>
                      <span className={`ml-2 font-bold ${
                        categoricalResult?.verdict?.verdict === 'BUY' ? 'text-green-400' :
                        categoricalResult?.verdict?.verdict === 'HOLD' ? 'text-yellow-400' : 'text-red-400'
                      }`}>
                        {categoricalResult?.verdict?.verdict || analysisResult.verdict?.verdict}
                      </span>
                      {categoricalResult && (
                        <span className="ml-2 text-xs text-gray-500">
                          (T:{categoricalResult.technical?.assessment?.charAt(0)} F:{categoricalResult.fundamental?.assessment?.charAt(0)} S:{categoricalResult.sentiment?.assessment?.charAt(0)} R:{categoricalResult.riskMacro?.assessment?.charAt(0)})
                        </span>
                      )}
                    </div>
                    <button
                      onClick={() => setAnalysisView('full')}
                      className="text-blue-400 hover:text-blue-300 text-sm"
                    >
                      View Full Analysis →
                    </button>
                  </div>
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
                  75-point scoring system • Minervini SEPA + CAN SLIM methodology
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
                  {strategies ? (
                    (strategies.strategies || []).map((strategy) => (
                      <option key={strategy.id} value={strategy.id}>{strategy.name}: {strategy.description}</option>
                    ))
                  ) : (
                    <>
                      <option value="reddit">Reddit - Popular momentum</option>
                      <option value="minervini">Minervini - Stage 2 leaders</option>
                      <option value="momentum">Momentum - Strong 52w</option>
                      <option value="value">Value - Quality discounts</option>
                      <option value="best">Best Candidates - Backtested Config C picks</option>
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
            </div>

            {/* Scan Error */}
            {scanError && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6">
                <p className="text-red-200 font-medium">Backend Error</p>
                <p className="text-red-300 text-sm mt-1">{scanError}</p>
                <p className="text-red-400 text-xs mt-2">Check that the backend is running on port 5001 and TradingView screener is installed.</p>
              </div>
            )}

            {/* Scan Results */}
            {scanResults && !scanLoading && (
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
                    {scanResults.returned} of {scanResults.totalMatches} matches
                  </span>
                </div>

                {/* Results Table */}
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
                        <th className="text-center py-3 px-2">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {scanResults.candidates?.map((stock) => (
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
                </div>

                {/* No matching stocks message */}
                {(!scanResults.candidates || scanResults.candidates.length === 0) && (
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
            )}

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
                      <div className="text-gray-400 text-xs">Expectancy</div>
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
                            categoricalVerdict: categoricalResult?.verdict?.verdict
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
                      <span className={`px-2 py-0.5 rounded text-xs ${
                        provenanceData.ohlcv.status === 'cached'
                          ? 'bg-green-900/50 text-green-400'
                          : 'bg-blue-900/50 text-blue-400'
                      }`}>
                        {provenanceData.ohlcv.status.toUpperCase()}
                      </span>
                    </div>
                    <div className="text-sm text-gray-400 space-y-1">
                      <div>Source: <span className="text-gray-300">{provenanceData.ohlcv.source}</span></div>
                      {provenanceData.ohlcv.rows && (
                        <div>Data points: <span className="text-gray-300">{provenanceData.ohlcv.rows}</span></div>
                      )}
                      {provenanceData.ohlcv.age_hours && (
                        <div>Age: <span className="text-gray-300">{provenanceData.ohlcv.age_hours}h</span></div>
                      )}
                      {provenanceData.ohlcv.expires_in && (
                        <div>Expires in: <span className="text-yellow-400">{provenanceData.ohlcv.expires_in.split('.')[0]}</span></div>
                      )}
                    </div>
                  </div>

                  {/* Fundamentals Source */}
                  <div className="bg-gray-700/50 rounded-lg p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-gray-300 font-medium">Fundamentals</span>
                      <span className={`px-2 py-0.5 rounded text-xs ${
                        provenanceData.fundamentals.status === 'cached'
                          ? 'bg-green-900/50 text-green-400'
                          : 'bg-blue-900/50 text-blue-400'
                      }`}>
                        {provenanceData.fundamentals.status.toUpperCase()}
                      </span>
                    </div>
                    <div className="text-sm text-gray-400 space-y-1">
                      <div>Source: <span className="text-gray-300">{provenanceData.fundamentals.source}</span></div>
                      {provenanceData.fundamentals.age_days && (
                        <div>Age: <span className="text-gray-300">{provenanceData.fundamentals.age_days} days</span></div>
                      )}
                      {provenanceData.fundamentals.expires_in && (
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
              <h4 className="text-md font-semibold text-cyan-400 mb-4">🗺️ Data Source Map</h4>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="text-gray-400 border-b border-gray-700 text-xs">
                      <th className="text-left py-2 px-2">Data Type</th>
                      <th className="text-left py-2 px-2">Primary Source</th>
                      <th className="text-left py-2 px-2">Fallback</th>
                      <th className="text-left py-2 px-2">Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(provenanceData?.data_sources ? [
                      {type: 'Price Data (OHLCV)', primary: provenanceData.data_sources.prices?.name, fallback: provenanceData.data_sources.prices?.fallback || '-', status: provenanceData.data_sources.prices?.status},
                      {type: 'Fundamentals', primary: provenanceData.data_sources.fundamentals_primary?.name, fallback: provenanceData.data_sources.fundamentals_fallback?.name, status: provenanceData.data_sources.fundamentals_primary?.status},
                      {type: 'Market Data (SPY/VIX)', primary: provenanceData.data_sources.market_data?.name, fallback: '-', status: provenanceData.data_sources.market_data?.status},
                      {type: 'Market Scanning', primary: provenanceData.data_sources.scanning?.name, fallback: '-', status: provenanceData.data_sources.scanning?.status}
                    ] : [
                      {type: 'Price Data (OHLCV)', primary: 'TwelveData', fallback: 'yfinance → Stooq', status: 'available'},
                      {type: 'Fundamentals', primary: 'Finnhub + FMP', fallback: 'yfinance', status: 'available'},
                      {type: 'Market Data (SPY/VIX)', primary: 'TwelveData (SPY) / yfinance (VIX)', fallback: 'yfinance → Finnhub', status: 'available'},
                      {type: 'Market Scanning', primary: 'TradingView Screener', fallback: '-', status: 'available'}
                    ]).map((src, idx) => (
                      <tr key={idx} className="border-b border-gray-700/30 hover:bg-gray-700/20">
                        <td className="py-2 px-2 text-gray-300">{src.type}</td>
                        <td className="py-2 px-2 text-gray-400">{src.primary}</td>
                        <td className="py-2 px-2 text-gray-500">{src.fallback}</td>
                        <td className="py-2 px-2">
                          <span className={`px-2 py-0.5 rounded text-xs ${
                            src.status === 'available'
                              ? 'bg-green-900/50 text-green-400'
                              : 'bg-red-900/50 text-red-400'
                          }`}>
                            {src.status?.toUpperCase()}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
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
          <p>v4.14 - Multi-Source Data Intelligence</p>
          <p className="mt-1">TwelveData • Finnhub • FMP • yfinance • Stooq</p>
        </div>
      </div>
    </div>
  );
}

export default App;