/**
 * Swing Trade Analyzer - Main App Component
 * v2.0: Integrated with Defeat Beta for rich fundamentals
 * v2.1: Added TradingView screener scan tab (Day 12)
 * v2.2: Added Support & Resistance Trade Setup display (Day 14)
 * v2.3: Added Validation tab for data quality monitoring (Day 17)
 * v2.4: Fixed rsData overwrite bug (Day 18)
 * v2.5: Added Trade Viability display - Option D (Day 22)
 */

import React, { useState, useEffect } from 'react';
import { fetchFullAnalysisData, checkBackendHealth, fetchScanStrategies, fetchScanResults, runValidation } from './services/api';
import { calculateScore } from './utils/scoringEngine';
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

  // Quick picks for testing
  const quickPicks = ['AVGO', 'NVDA', 'AAPL', 'META', 'MSFT', 'NFLX', 'PLTR']; 

  // Check backend health and load strategies on mount
  useEffect(() => {
    checkBackendHealth().then(setBackendStatus);
    fetchScanStrategies()
      .then(setStrategies)
      .catch(err => console.error('Failed to load strategies:', err));
  }, []);

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
    setActiveTab('analyze');

    try {
      const data = await fetchFullAnalysisData(targetTicker);
      const result = calculateScore(data.stock, data.spy, data.vix);
      //const rsData = calculateRelativeStrength(data.stock, data.spy);
      //result.rsData = rsData;
      
      setAnalysisResult(result);
      setSrData(data.sr);
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

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold text-blue-400">🎯 Swing Trade Analyzer</h1>
          <p className="text-gray-400 mt-2">Minervini SEPA + CAN SLIM Methodology</p>
          
          {/* Backend Status */}
          <div className="mt-4 flex justify-center items-center gap-2">
            <span className={`w-3 h-3 rounded-full ${backendStatus.healthy ? 'bg-green-500' : 'bg-red-500'}`}></span>
            <span className="text-sm text-gray-400">
              Backend {backendStatus.healthy ? 'Connected' : 'Disconnected'}
              {backendStatus.defeatbetaAvailable && ' • Defeat Beta ✓'}
              {backendStatus.tradingviewAvailable && ' • TradingView ✓'}
              {backendStatus.srEngineAvailable && ' • S&R ✓'}
              {backendStatus.validationAvailable && ' • Validation ✓'}
            </span>
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
            {analysisResult && !loading && (
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
                        <div className={`text-xl font-bold ${srData.riskReward >= 2 ? 'text-green-400' : srData.riskReward >= 1.5 ? 'text-yellow-400' : 'text-red-400'}`}>
                          {srData.riskReward?.toFixed(2)}:1
                        </div>
                      </div>
                    </div>
                    <div className="mt-4 text-xs text-gray-500 text-center">
                      Method: {srData.method} • Support levels: {srData.support?.length || 0} • Resistance levels: {srData.resistance?.length || 0}
                      {srData.meta?.atr && ` • ATR: $${srData.meta.atr.toFixed(2)}`}
                    </div>
                  </div>
                )}

                {/* Score Breakdown */}
                <div className="bg-gray-800 rounded-lg p-6">
                  <h3 className="text-lg font-semibold mb-4 text-blue-400">📊 Score Breakdown</h3>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="bg-gray-700/50 rounded-lg p-4">
                      <div className="text-gray-400 text-sm">Technical</div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.technical || 0, 40)}`}>
                        {analysisResult.scores?.technical || 0}/40
                      </div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-4">
                      <div className="text-gray-400 text-sm">Fundamental</div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.fundamental || 0, 20)}`}>
                        {analysisResult.scores?.fundamental || 0}/20
                      </div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-4">
                      <div className="text-gray-400 text-sm">Sentiment</div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.sentiment || 0, 10)}`}>
                        {analysisResult.scores?.sentiment || 0}/10
                      </div>
                    </div>
                    <div className="bg-gray-700/50 rounded-lg p-4">
                      <div className="text-gray-400 text-sm">Risk/Macro</div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.scores?.risk || 0, 5)}`}>
                        {analysisResult.scores?.risk || 0}/5
                      </div>
                    </div>
                  </div>
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
                          <td className="py-3 px-2 text-right font-mono">{formatCurrency(stock.close)}</td>
                          <td className={`py-3 px-2 text-right ${stock.change >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                            {formatPercent(stock.change)}
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

        {/* Footer */}
        <div className="mt-8 text-center text-gray-500 text-sm">
          <p>Day 22 - Trade Viability (Option D) | 75-Point Scoring System</p>
          <p className="mt-1">Based on Mark Minervini SEPA + William O'Neil CAN SLIM</p>
        </div>
      </div>
    </div>
  );
}

export default App;