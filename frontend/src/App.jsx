/**
 * Swing Trade Analyzer - Main App Component
 * v2.0: Integrated with Defeat Beta for rich fundamentals
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
 */

import React, { useState, useEffect } from 'react';
import { fetchFullAnalysisData, checkBackendHealth, fetchScanStrategies, fetchScanResults, runValidation, clearBackendCache } from './services/api';
import { calculateScore } from './utils/scoringEngine';
import { calculateSimplifiedAnalysis } from './utils/simplifiedScoring';
import { calculatePositionSize, loadSettings, saveSettings, getDefaultSettings } from './utils/positionSizing';
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

  // Scan state
  const [scanLoading, setScanLoading] = useState(false);
  const [scanError, setScanError] = useState(null);
  const [scanResults, setScanResults] = useState(null);
  const [selectedStrategy, setSelectedStrategy] = useState('reddit');
  const [strategies, setStrategies] = useState(null);

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

  // Quick picks for testing
  const quickPicks = ['AVGO', 'NVDA', 'AAPL', 'META', 'MSFT', 'NFLX', 'PLTR']; 

  // Check backend health, load strategies, and load settings on mount
  useEffect(() => {
    checkBackendHealth().then(setBackendStatus);
    fetchScanStrategies()
      .then(setStrategies)
      .catch(err => console.error('Failed to load strategies:', err));
    // Load saved settings
    setSettings(loadSettings());
  }, []);

  // Session Refresh - Clear backend cache and reset frontend state (Day 29)
  const handleSessionRefresh = async () => {
    setRefreshing(true);
    try {
      // Clear backend cache
      await clearBackendCache();

      // Reset frontend state
      setAnalysisResult(null);
      setSrData(null);
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

      // Refresh backend status
      const status = await checkBackendHealth();
      setBackendStatus(status);

      // Record refresh time
      setLastRefresh(new Date().toLocaleTimeString());

    } catch (err) {
      console.error('Session refresh failed:', err);
      setError('Failed to refresh session: ' + err.message);
    } finally {
      setRefreshing(false);
    }
  };

  // Update settings and save to localStorage
  const updateSettings = (newSettings) => {
    setSettings(newSettings);
    saveSettings(newSettings);
  };

  // Calculate position when inputs change
  const runPositionCalculation = () => {
    const entry = parseFloat(calcEntry);
    const stop = parseFloat(calcStop);
    if (!entry || !stop) {
      setPositionResult(null);
      return;
    }
    const result = calculatePositionSize(settings.accountSize, settings.riskPercent, entry, stop);
    setPositionResult(result);
  };

  // Auto-fill position calculator from analysis and navigate to Settings (Day 28 integration)
  const autoFillPositionCalculator = (tickerSymbol, entry, stop) => {
    if (!entry || !stop) return;

    // Set calculator values
    setCalcTicker(tickerSymbol);
    setCalcEntry(entry.toFixed(2));
    setCalcStop(stop.toFixed(2));

    // Calculate position immediately
    const result = calculatePositionSize(settings.accountSize, settings.riskPercent, entry, stop);
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
    setSimplifiedResult(null);
    setActiveTab('analyze');

    try {
      const data = await fetchFullAnalysisData(targetTicker);
      const result = calculateScore(data.stock, data.spy, data.vix);
      //const rsData = calculateRelativeStrength(data.stock, data.spy);
      //result.rsData = rsData;

      // Day 27: Also calculate simplified binary analysis
      const simplified = calculateSimplifiedAnalysis(data.stock, data.spy, data.sr);

      setAnalysisResult(result);
      setSrData(data.sr);
      setSimplifiedResult(simplified);
      setTicker(targetTicker);
      
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
      const results = await fetchScanResults(selectedStrategy, 50);
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
                {backendStatus.defeatbetaAvailable && ' • Defeat Beta ✓'}
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
                    onClick={() => setAnalysisView('simple')}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                      analysisView === 'simple'
                        ? 'bg-green-600 text-white'
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    ✅ Simple Checklist (4 criteria)
                  </button>
                </div>
              </div>
            )}

            {/* Error Display */}
            {error && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6 text-red-200">
                {error}
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
                {/* Verdict Card */}
                <div className={`rounded-lg p-6 ${getVerdictColor(analysisResult.verdict)}`}>
                  <div className="flex justify-between items-center">
                    <div>
                      <h2 className="text-2xl font-bold">{analysisResult.ticker} - {analysisResult.name}</h2>
                      <p className="text-white/80">{analysisResult.sector} • {analysisResult.industry}</p>
                    </div>
                    <div className="text-right">
                      <div className="text-4xl font-bold">{analysisResult.verdict?.verdict || 'N/A'}</div>
                      <div className="text-xl">{analysisResult.totalScore}/75 points</div>
                    </div>
                  </div>
                </div>

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
                        <span className={`font-bold ${analysisResult.rsData?.rsRating === 'Strong' ? 'text-green-400' : analysisResult.rsData?.rsRating === 'Moderate' ? 'text-yellow-400' : 'text-red-400'}`}>
                          {analysisResult.rsData?.rsRating || 'N/A'}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Trade Setup Card (S&R) - Day 22: Enhanced with Viability */}
                {srData && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    {/* Header with Viability Badge */}
                    <div className="flex justify-between items-center mb-4">
                      <h3 className="text-lg font-semibold text-blue-400">🎯 Trade Setup</h3>
                      {srData.meta?.tradeViability && (
                        <div className={`px-3 py-1 rounded-full text-sm font-bold ${getViabilityStyle(srData.meta.tradeViability.viable).bg} ${getViabilityStyle(srData.meta.tradeViability.viable).text}`}>
                          {getViabilityStyle(srData.meta.tradeViability.viable).icon} {getViabilityStyle(srData.meta.tradeViability.viable).label}
                        </div>
                      )}
                    </div>

                    {/* Viability Advice Banner (Day 22) */}
                    {srData.meta?.tradeViability && (
                      <div className={`mb-4 p-3 rounded-lg text-sm ${
                        srData.meta.tradeViability.viable === 'YES' ? 'bg-green-900/30 border border-green-700 text-green-300' :
                        srData.meta.tradeViability.viable === 'CAUTION' ? 'bg-yellow-900/30 border border-yellow-700 text-yellow-300' :
                        srData.meta.tradeViability.viable === 'NO' ? 'bg-red-900/30 border border-red-700 text-red-300' :
                        'bg-gray-700/30 border border-gray-600 text-gray-300'
                      }`}>
                        <div className="flex justify-between items-start">
                          <div>
                            <span className="font-semibold">
                              {srData.meta.tradeViability.viable === 'YES' && '✅ '}
                              {srData.meta.tradeViability.viable === 'CAUTION' && '⚠️ '}
                              {srData.meta.tradeViability.viable === 'NO' && '🚫 '}
                              {srData.meta.tradeViability.advice}
                            </span>
                            {srData.meta.tradeViability.position_size_advice && (
                              <div className="mt-1 text-xs opacity-80">
                                Position Size: {srData.meta.tradeViability.position_size_advice}
                              </div>
                            )}
                          </div>
                          <div className="text-right text-xs">
                            {srData.meta.tradeViability.support_distance_pct !== null && (
                              <div>Support: {srData.meta.tradeViability.support_distance_pct}% away</div>
                            )}
                            {srData.meta.tradeViability.risk_reward_context && (
                              <div>R:R Context: {srData.meta.tradeViability.risk_reward_context}</div>
                            )}
                          </div>
                        </div>
                      </div>
                    )}

                    {/* Day 26: Pullback Guidance for CAUTION (wide stop) cases */}
                    {srData.meta?.tradeViability?.viable === 'CAUTION' && srData.support?.length > 0 && (
                      <div className="mb-4 p-3 rounded-lg text-sm bg-yellow-900/20 border border-yellow-700/50 text-yellow-200">
                        <div className="font-semibold mb-2">📍 Entry Options for Wide Stop</div>
                        <div className="text-xs space-y-2">
                          {(() => {
                            const nearestSupport = srData.support[0];
                            const currentPrice = srData.currentPrice;
                            const pullbackPct = ((currentPrice - nearestSupport) / currentPrice * 100).toFixed(1);
                            return (
                              <>
                                <div className="flex items-start gap-2">
                                  <span className="text-yellow-400 font-bold">A.</span>
                                  <div>
                                    <span className="text-yellow-100">Enter HALF position now</span>
                                    <span className="text-yellow-400"> → Add remaining at </span>
                                    <span className="text-yellow-100 font-mono">{formatCurrency(nearestSupport)}</span>
                                  </div>
                                </div>
                                <div className="flex items-start gap-2">
                                  <span className="text-yellow-400 font-bold">B.</span>
                                  <div>
                                    <span className="text-yellow-100">Wait for pullback to </span>
                                    <span className="text-yellow-100 font-mono">{formatCurrency(nearestSupport)}</span>
                                    <span className="text-yellow-400"> ({pullbackPct}% drop) for full position</span>
                                  </div>
                                </div>
                                <div className="mt-2 text-yellow-500/80 italic text-[11px]">
                                  Support at {formatCurrency(nearestSupport)} allows tighter stop placement and better R:R
                                </div>
                              </>
                            );
                          })()}
                        </div>
                      </div>
                    )}

                    {/* Day 26: Pullback Guidance for Extended Stocks (NO viable) */}
                    {srData.meta?.tradeViability?.viable === 'NO' && srData.allSupport?.length > 0 && (
                      <div className="mb-4 p-3 rounded-lg text-sm bg-blue-900/30 border border-blue-700 text-blue-300">
                        <div className="font-semibold mb-1">📍 Pullback Re-Entry Zones</div>
                        <div className="text-xs space-y-1">
                          {(() => {
                            // Get nearest historical support levels (highest ones = closest to price)
                            const sortedSupport = [...srData.allSupport].sort((a, b) => b - a);
                            const nearestSupport = sortedSupport[0];
                            const secondSupport = sortedSupport[1];
                            const currentPrice = srData.currentPrice;
                            const pullbackPct = ((currentPrice - nearestSupport) / currentPrice * 100).toFixed(1);

                            return (
                              <>
                                <div>
                                  <span className="text-blue-200">Primary zone:</span> {formatCurrency(nearestSupport)}
                                  <span className="text-blue-400 ml-1">({pullbackPct}% pullback needed)</span>
                                </div>
                                {secondSupport && (
                                  <div>
                                    <span className="text-blue-200">Secondary zone:</span> {formatCurrency(secondSupport)}
                                    <span className="text-blue-400 ml-1">({((currentPrice - secondSupport) / currentPrice * 100).toFixed(1)}% pullback)</span>
                                  </div>
                                )}
                                <div className="mt-2 text-blue-400 italic">
                                  Set price alert at ${nearestSupport?.toFixed(2)} and wait for confirmation before entry.
                                </div>
                              </>
                            );
                          })()}
                        </div>
                      </div>
                    )}

                    {/* Trade Levels Grid */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                      <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                        <div className="text-gray-400 text-sm mb-1">Entry</div>
                        <div className="text-xl font-bold text-green-400">{formatCurrency(srData.suggestedEntry)}</div>
                      </div>
                      <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                        <div className="text-gray-400 text-sm mb-1">Stop Loss</div>
                        <div className="text-xl font-bold text-red-400">{formatCurrency(srData.suggestedStop)}</div>
                        {srData.meta?.tradeViability?.stop_suggestion && srData.suggestedStop !== srData.meta.tradeViability.stop_suggestion && (
                          <div className="text-xs text-gray-500 mt-1">
                            Alt: {formatCurrency(srData.meta.tradeViability.stop_suggestion)}
                          </div>
                        )}
                      </div>
                      <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                        <div className="text-gray-400 text-sm mb-1">Target</div>
                        <div className="text-xl font-bold text-blue-400">{formatCurrency(srData.suggestedTarget)}</div>
                      </div>
                      <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                        <div className="text-gray-400 text-sm mb-1">Risk/Reward</div>
                        <div className={`text-xl font-bold ${
                          srData.riskReward == null ? 'text-gray-400' :
                          srData.riskReward >= 2 ? 'text-green-400' :
                          srData.riskReward >= 1.5 ? 'text-yellow-400' : 'text-red-400'
                        }`}>
                          {srData.riskReward != null ? `${srData.riskReward.toFixed(2)}:1` : 'N/A'}
                        </div>
                      </div>
                    </div>
                    {/* Day 26: Show actual S&R levels */}
                    <div className="mt-4 pt-3 border-t border-gray-700">
                      <div className="grid grid-cols-2 gap-4 text-xs">
                        <div>
                          <div className="text-green-400 font-semibold mb-1">Support Levels</div>
                          {srData.support?.length > 0 ? (
                            <div className="space-y-0.5">
                              {srData.support.slice().sort((a, b) => b - a).map((level, i) => (
                                <div key={i} className="text-gray-400">
                                  S{i + 1}: <span className="text-green-300 font-mono">{formatCurrency(level)}</span>
                                  <span className="text-gray-500 ml-1">
                                    ({((srData.currentPrice - level) / srData.currentPrice * 100).toFixed(1)}% below)
                                  </span>
                                </div>
                              ))}
                            </div>
                          ) : (
                            <div className="text-gray-500 italic">None within range</div>
                          )}
                        </div>
                        <div>
                          <div className="text-red-400 font-semibold mb-1">Resistance Levels</div>
                          {srData.resistance?.length > 0 ? (
                            <div className="space-y-0.5">
                              {srData.resistance.slice().sort((a, b) => a - b).map((level, i) => (
                                <div key={i} className="text-gray-400">
                                  R{i + 1}: <span className="text-red-300 font-mono">{formatCurrency(level)}</span>
                                  <span className="text-gray-500 ml-1">
                                    ({((level - srData.currentPrice) / srData.currentPrice * 100).toFixed(1)}% above)
                                  </span>
                                </div>
                              ))}
                            </div>
                          ) : (
                            <div className="text-gray-500 italic">None within range</div>
                          )}
                        </div>
                      </div>
                      <div className="mt-2 text-xs text-gray-500 text-center">
                        Method: {srData.method} • ATR: {srData.meta?.atr ? `$${srData.meta.atr.toFixed(2)}` : 'N/A'}
                      </div>
                    </div>
                  </div>
                )}

                {/* Score Breakdown - Enhanced with expandable details (Day 23) */}
                <div className="bg-gray-800 rounded-lg p-6">
                  <h3 className="text-lg font-semibold mb-4 text-blue-400">📊 Score Breakdown <span className="text-xs text-gray-500 font-normal ml-2">Click to expand</span></h3>
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
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.technical || 0, 40)}`}>
                        {analysisResult.scores?.technical || 0}/40
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
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.fundamental || 0, 20)}`}>
                        {analysisResult.scores?.fundamental || 0}/20
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
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.sentiment || 0, 10)}`}>
                        {analysisResult.scores?.sentiment || 0}/10
                      </div>
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
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.risk || 0, 5)}`}>
                        {analysisResult.scores?.risk || 0}/5
                      </div>
                    </div>
                  </div>

                  {/* Expanded Details Panel */}
                  {expandedScore && (
                    <div className="mt-4 bg-gray-700/30 rounded-lg p-4 border border-gray-600">
                      {expandedScore === 'technical' && analysisResult.breakdown?.technical?.details && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">📈 Technical Breakdown</div>
                          {Object.entries(analysisResult.breakdown.technical.details).map(([key, data]) => {
                            const info = getSubScoreInfo('technical', key, data);
                            const pct = (data.score / data.max) * 100;
                            return (
                              <div key={key} className="flex items-center gap-3">
                                <span className="text-lg">{info.icon}</span>
                                <div className="flex-1">
                                  <div className="flex justify-between text-sm">
                                    <span className="text-gray-300">{info.label}</span>
                                    <span className={`font-mono ${data.score === data.max ? 'text-green-400' : data.score === 0 ? 'text-red-400' : 'text-yellow-400'}`}>
                                      {data.score}/{data.max}
                                    </span>
                                  </div>
                                  <div className="w-full bg-gray-600 rounded-full h-2 mt-1">
                                    <div 
                                      className={`h-2 rounded-full ${pct >= 80 ? 'bg-green-500' : pct >= 50 ? 'bg-yellow-500' : 'bg-red-500'}`}
                                      style={{ width: `${pct}%` }}
                                    ></div>
                                  </div>
                                  <div className="text-xs text-gray-500 mt-1">{info.desc}</div>
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      )}
                      {expandedScore === 'fundamental' && analysisResult.breakdown?.fundamental?.details && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">💼 Fundamental Breakdown</div>
                          {/* Day 25: ETF Note */}
                          {analysisResult.breakdown.fundamental.isETF && (
                            <div className="bg-blue-900/30 border border-blue-700 rounded-lg p-3 text-sm text-blue-300 mb-3">
                              📊 {analysisResult.breakdown.fundamental.etfNote || 'This is an ETF - fundamental scoring does not apply.'}
                            </div>
                          )}
                          {/* Day 25: Extreme Value Context */}
                          {analysisResult.breakdown.fundamental.extremeValueContext?.length > 0 && (
                            <div className="bg-amber-900/30 border border-amber-700 rounded-lg p-3 text-sm mb-3">
                              <div className="text-amber-300 font-semibold mb-2">⚠️ Unusual Values Detected</div>
                              {analysisResult.breakdown.fundamental.extremeValueContext.map((ctx, idx) => (
                                <div key={idx} className="text-amber-200 text-xs mb-1">
                                  <strong>{ctx.metric}:</strong> {ctx.explanation}
                                </div>
                              ))}
                            </div>
                          )}
                          {Object.entries(analysisResult.breakdown.fundamental.details).map(([key, data]) => {
                            const info = getSubScoreInfo('fundamental', key, data);
                            const pct = (data.score / data.max) * 100;
                            return (
                              <div key={key} className="flex items-center gap-3">
                                <span className="text-lg">{info.icon}</span>
                                <div className="flex-1">
                                  <div className="flex justify-between text-sm">
                                    <span className="text-gray-300">{info.label}</span>
                                    <span className="text-gray-400 text-xs">
                                      {data.value !== null && data.value !== undefined ?
                                        (typeof data.value === 'number' ? data.value.toFixed(1) : data.value) : 'N/A'}
                                    </span>
                                    <span className={`font-mono ${data.score === data.max ? 'text-green-400' : data.score === 0 ? 'text-red-400' : 'text-yellow-400'}`}>
                                      {data.score}/{data.max}
                                    </span>
                                  </div>
                                  <div className="w-full bg-gray-600 rounded-full h-2 mt-1">
                                    <div
                                      className={`h-2 rounded-full ${pct >= 80 ? 'bg-green-500' : pct >= 50 ? 'bg-yellow-500' : 'bg-red-500'}`}
                                      style={{ width: `${pct}%` }}
                                    ></div>
                                  </div>
                                  <div className="text-xs text-gray-500 mt-1">{info.desc}</div>
                                </div>
                              </div>
                            );
                          })}
                          <div className="text-xs text-gray-500 mt-2 pt-2 border-t border-gray-600">
                            Data: {analysisResult.breakdown.fundamental.dataSource || 'yfinance'} • Quality: {analysisResult.breakdown.fundamental.dataQuality || 'unknown'}
                          </div>
                        </div>
                      )}
                      {expandedScore === 'sentiment' && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">📰 Sentiment Breakdown</div>
                          <div className="bg-yellow-900/30 border border-yellow-700 rounded-lg p-3 text-sm text-yellow-300">
                            ⚠️ Sentiment is currently a placeholder (5/10 default). Real news/social sentiment analysis coming in a future update.
                          </div>
                        </div>
                      )}
                      {expandedScore === 'risk' && (
                        <div className="space-y-3">
                          <div className="text-sm font-semibold text-blue-300 mb-3">⚡ Risk/Macro Breakdown</div>
                          <div className="grid grid-cols-2 gap-4 text-sm">
                            <div>
                              <span className="text-gray-400">VIX Level:</span>
                              <span className="ml-2 text-gray-200">
                                {analysisResult.breakdown?.risk?.details?.vix?.value?.toFixed(1) || 'N/A'}
                              </span>
                              <span className="ml-2 text-xs text-gray-500">
                                ({analysisResult.breakdown?.risk?.details?.vix?.score || 0}/{analysisResult.breakdown?.risk?.details?.vix?.max || 2} pts)
                              </span>
                            </div>
                            <div>
                              <span className="text-gray-400">S&P Regime:</span>
                              <span className={`ml-2 ${analysisResult.breakdown?.risk?.details?.spyRegime?.aboveSma200 ? 'text-green-400' : 'text-red-400'}`}>
                                {analysisResult.breakdown?.risk?.details?.spyRegime?.aboveSma200 ? 'Bullish' : 'Bearish'}
                              </span>
                              <span className="ml-2 text-xs text-gray-500">
                                ({analysisResult.breakdown?.risk?.details?.spyRegime?.score || 0}/2 pts)
                              </span>
                            </div>
                          </div>
                          <div className="text-sm">
                            <span className="text-gray-400">Market Breadth:</span>
                            <span className="ml-2 text-gray-200">Neutral</span>
                            <span className="ml-2 text-xs text-gray-500">(placeholder - 1/1 pts)</span>
                          </div>
                        </div>
                      )}
                    </div>
                  )}

                  {/* Plain English Summary */}
                  {generateScoreExplanation(analysisResult) && (
                    <div className={`mt-4 p-4 rounded-lg text-sm ${
                      generateScoreExplanation(analysisResult).type === 'positive' ? 'bg-green-900/20 border border-green-800' :
                      generateScoreExplanation(analysisResult).type === 'negative' ? 'bg-red-900/20 border border-red-800' :
                      'bg-yellow-900/20 border border-yellow-800'
                    }`}>
                      <div className="font-semibold mb-2 text-gray-200">
                        💡 Why This Score?
                      </div>
                      <ul className="list-disc list-inside space-y-1 text-gray-400">
                        {generateScoreExplanation(analysisResult).reasons.map((reason, idx) => (
                          <li key={idx}>{reason}</li>
                        ))}
                      </ul>
                      <div className="mt-2 text-gray-300 font-medium">
                        {generateScoreExplanation(analysisResult).summary}
                      </div>
                    </div>
                  )}
                </div>

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
                      <p className="text-white/80">{analysisResult.sector} • {analysisResult.industry}</p>
                    </div>
                    <div className="text-right">
                      <div className="text-4xl font-bold">
                        {simplifiedResult.verdict === 'TRADE' ? '✅ TRADE' : '⏸️ PASS'}
                      </div>
                      <div className="text-xl">{simplifiedResult.passCount}/4 criteria met</div>
                    </div>
                  </div>
                </div>

                {/* 4 Binary Criteria Cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
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
                  <p><strong>Simplified Binary System</strong> - Day 27 Research-Backed Approach</p>
                  <p className="mt-1">Based on: AQR Momentum Research • Turtle Trading Principles • Academic Factor Evidence</p>
                  <p className="mt-2 text-gray-400">
                    <strong>Rule:</strong> ALL 4 criteria must be YES to take a trade. Any NO = PASS. No exceptions.
                  </p>
                </div>

                {/* Compare with Full Score */}
                <div className="bg-gray-800 rounded-lg p-4">
                  <div className="flex justify-between items-center">
                    <div>
                      <span className="text-gray-400 text-sm">Full System Score (for comparison):</span>
                      <span className={`ml-2 font-bold ${
                        analysisResult.totalScore >= 60 ? 'text-green-400' :
                        analysisResult.totalScore >= 40 ? 'text-yellow-400' : 'text-red-400'
                      }`}>
                        {analysisResult.totalScore}/75 → {analysisResult.verdict?.verdict}
                      </span>
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
            {/* Strategy Selector */}
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
                    </>
                  )}
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
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6 text-red-200">
                {scanError}
              </div>
            )}

            {/* Scan Results */}
            {scanResults && !scanLoading && (
              <div className="bg-gray-800 rounded-lg p-6">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-lg font-semibold text-blue-400">
                    📋 Scan Results: {scanResults.strategy}
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

        {/* ==================== SETTINGS TAB (Day 28) ==================== */}
        {activeTab === 'settings' && (
          <>
            {/* Account Settings */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <h3 className="text-lg font-semibold text-purple-400 mb-4">Account Settings</h3>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
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
              </div>

              {/* Current Risk Summary */}
              <div className="mt-6 bg-purple-900/30 border border-purple-700 rounded-lg p-4">
                <div className="grid grid-cols-3 gap-4 text-center">
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

              <button
                onClick={runPositionCalculation}
                className="w-full bg-green-600 hover:bg-green-700 px-6 py-3 rounded-lg font-semibold"
              >
                Calculate Position Size
              </button>

              {/* Calculation Results */}
              {positionResult && !positionResult.error && (
                <div className="mt-6 space-y-4">
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

        {/* Footer */}
        <div className="mt-8 text-center text-gray-500 text-sm">
          <p>Day 29 - Session Refresh + Comprehensive Testing</p>
          <p className="mt-1">Fresh data, accurate analysis</p>
        </div>
      </div>
    </div>
  );
}

export default App;