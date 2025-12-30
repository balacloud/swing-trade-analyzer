/**
 * Swing Trade Analyzer - Main App Component
 * v2.0: Integrated with Defeat Beta for rich fundamentals
 * v2.1: Added TradingView screener scan tab (Day 12)
 * v2.2: Added Support & Resistance Trade Setup display (Day 14)
 * v2.3: Added Validation tab for data quality monitoring (Day 17)
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

                {/* Trade Setup Card (S&R) */}
                {srData && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h3 className="text-lg font-semibold mb-4 text-blue-400">🎯 Trade Setup</h3>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                      <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                        <div className="text-gray-400 text-sm mb-1">Entry</div>
                        <div className="text-xl font-bold text-green-400">{formatCurrency(srData.suggestedEntry)}</div>
                      </div>
                      <div className="bg-gray-700/50 rounded-lg p-4 text-center">
                        <div className="text-gray-400 text-sm mb-1">Stop Loss</div>
                        <div className="text-xl font-bold text-red-400">{formatCurrency(srData.suggestedStop)}</div>
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
                {analysisResult.indicators && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h3 className="text-lg font-semibold mb-4 text-blue-400">📉 Technical Indicators</h3>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                      <div>
                        <span className="text-gray-400">RSI (14):</span>
                        <span className={`ml-2 ${getRsiColor(analysisResult.indicators.rsi)}`}>
                          {analysisResult.indicators.rsi?.toFixed(1) || 'N/A'}
                        </span>
                      </div>
                      <div>
                        <span className="text-gray-400">8 EMA:</span>
                        <span className={`ml-2 ${
                          analysisResult.currentPrice > analysisResult.indicators.ema8 ? 'text-green-400' : 'text-red-400'
                        }`}>
                          {formatCurrency(analysisResult.indicators.ema8)}
                        </span>
                      </div>
                      <div>
                        <span className="text-gray-400">21 EMA:</span>
                        <span className={`ml-2 ${
                          analysisResult.currentPrice > analysisResult.indicators.ema21 ? 'text-green-400' : 'text-red-400'
                        }`}>
                          {formatCurrency(analysisResult.indicators.ema21)}
                        </span>
                      </div>
                      <div>
                        <span className="text-gray-400">50 SMA:</span>
                        <span className={`ml-2 ${
                          analysisResult.currentPrice > analysisResult.indicators.sma50 ? 'text-green-400' : 'text-red-400'
                        }`}>
                          {formatCurrency(analysisResult.indicators.sma50)}
                        </span>
                      </div>
                      <div>
                        <span className="text-gray-400">200 SMA:</span>
                        <span className={`ml-2 ${
                          analysisResult.currentPrice > analysisResult.indicators.sma200 ? 'text-green-400' : 'text-red-400'
                        }`}>
                          {formatCurrency(analysisResult.indicators.sma200)}
                        </span>
                      </div>
                      <div>
                        <span className="text-gray-400">ATR:</span>
                        <span className="ml-2">{formatCurrency(analysisResult.indicators.atr)}</span>
                      </div>
                    </div>
                  </div>
                )}
              </div>
            )}
          </>
        )}

        {/* ==================== SCAN TAB ==================== */}
        {activeTab === 'scan' && (
          <>
            {/* Scan Controls */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <div className="flex flex-col md:flex-row gap-4 items-start md:items-end">
                {/* Strategy Selector */}
                <div className="flex-1">
                  <label className="block text-gray-400 text-sm mb-2">Scanning Strategy</label>
                  <select
                    value={selectedStrategy}
                    onChange={(e) => setSelectedStrategy(e.target.value)}
                    className="w-full bg-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    <option value="reddit">🔥 Reddit Swing Trading (Mid-cap+, High Volume)</option>
                    <option value="minervini">📈 Minervini SEPA (Large-cap Momentum)</option>
                    <option value="momentum">🚀 Sustainable Momentum (5-50% gains)</option>
                    <option value="value">💎 Value + Momentum (Quality at Fair Price)</option>
                  </select>
                </div>
                
                {/* Scan Button */}
                <button
                  onClick={runScan}
                  disabled={scanLoading}
                  className="bg-green-600 hover:bg-green-700 px-8 py-3 rounded-lg font-semibold disabled:opacity-50 whitespace-nowrap"
                >
                  {scanLoading ? '🔍 Scanning...' : '🔍 Scan for Opportunities'}
                </button>
              </div>

              {/* Strategy Description */}
              {strategies?.strategies?.[selectedStrategy] && (
                <div className="mt-4 p-3 bg-gray-700/50 rounded-lg">
                  <div className="text-sm text-gray-300">
                    <strong>{strategies.strategies[selectedStrategy].name}:</strong>{' '}
                    {strategies.strategies[selectedStrategy].description}
                  </div>
                  <div className="text-xs text-gray-500 mt-1">
                    Focus: {strategies.strategies[selectedStrategy].focus}
                  </div>
                </div>
              )}
            </div>

            {/* Scan Error */}
            {scanError && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6 text-red-200">
                {scanError}
              </div>
            )}

            {/* Scan Results */}
            {scanResults && (
              <div className="bg-gray-800 rounded-lg p-6">
                <div className="flex justify-between items-center mb-4">
                  <h2 className="text-xl font-bold">
                    📋 Scan Results
                    <span className="text-sm font-normal text-gray-400 ml-2">
                      ({scanResults.returned} of {scanResults.totalMatches} matches)
                    </span>
                  </h2>
                  <span className="text-xs text-gray-500">
                    {new Date(scanResults.timestamp).toLocaleTimeString()}
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
                        <th className="text-right py-3 px-2">Mkt Cap</th>
                        <th className="text-right py-3 px-2">RSI</th>
                        <th className="text-right py-3 px-2">RelVol</th>
                        <th className="text-right py-3 px-2">% from High</th>
                        <th className="text-left py-3 px-2">Sector</th>
                        <th className="text-center py-3 px-2">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {scanResults.candidates.map((candidate, idx) => (
                        <tr 
                          key={candidate.ticker}
                          className={`border-b border-gray-700/50 hover:bg-gray-700/30 cursor-pointer ${
                            idx % 2 === 0 ? 'bg-gray-800/50' : ''
                          }`}
                          onClick={() => analyzeStock(candidate.ticker)}
                        >
                          <td className="py-3 px-2 font-bold text-blue-400">{candidate.ticker}</td>
                          <td className="py-3 px-2 text-gray-300 max-w-[150px] truncate">{candidate.name}</td>
                          <td className="py-3 px-2 text-right">{formatCurrency(candidate.price)}</td>
                          <td className="py-3 px-2 text-right text-gray-400">{formatMarketCap(candidate.marketCap)}</td>
                          <td className={`py-3 px-2 text-right ${getRsiColor(candidate.rsi)}`}>
                            {candidate.rsi?.toFixed(0) || 'N/A'}
                          </td>
                          <td className={`py-3 px-2 text-right ${
                            candidate.relativeVolume >= 2 ? 'text-green-400' :
                            candidate.relativeVolume >= 1.5 ? 'text-green-300' : 'text-gray-400'
                          }`}>
                            {candidate.relativeVolume?.toFixed(1)}x
                          </td>
                          <td className={`py-3 px-2 text-right ${
                            candidate.pctFrom52wHigh >= -5 ? 'text-green-400' :
                            candidate.pctFrom52wHigh >= -15 ? 'text-yellow-400' : 'text-gray-400'
                          }`}>
                            {formatPercent(candidate.pctFrom52wHigh, 1)}
                          </td>
                          <td className="py-3 px-2 text-gray-400 text-xs max-w-[100px] truncate">{candidate.sector}</td>
                          <td className="py-3 px-2 text-center">
                            <button
                              onClick={(e) => {
                                e.stopPropagation();
                                analyzeStock(candidate.ticker);
                              }}
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

                {/* Scan Notes */}
                <div className="mt-4 text-xs text-gray-500">
                  <p>💡 Click any row to run full 75-point analysis. All candidates are in Stage 2 uptrends (50 SMA &gt; 200 SMA).</p>
                </div>
              </div>
            )}

            {/* Empty State */}
            {!scanResults && !scanLoading && !scanError && (
              <div className="bg-gray-800 rounded-lg p-12 text-center">
                <div className="text-6xl mb-4">🔍</div>
                <h3 className="text-xl font-bold text-gray-300 mb-2">Ready to Scan</h3>
                <p className="text-gray-500 mb-4">
                  Select a strategy and click "Scan for Opportunities" to find swing trade candidates.
                </p>
              </div>
            )}
          </>
        )}

        {/* ==================== VALIDATE TAB (Day 17) ==================== */}
        {activeTab === 'validate' && (
          <>
            {/* Validation Controls */}
            <div className="bg-gray-800 rounded-lg p-6 mb-6">
              <h2 className="text-xl font-bold mb-4 text-blue-400">✅ Data Validation Engine</h2>
              <p className="text-gray-400 text-sm mb-4">
                Compare our data against external sources (StockAnalysis, Finviz) to ensure accuracy.
              </p>
              
              <div className="flex flex-col md:flex-row gap-4 items-start md:items-end">
                <div className="flex-1">
                  <label className="block text-gray-400 text-sm mb-2">Tickers to Validate (comma-separated)</label>
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
          <p>Day 17 - Validation Engine UI | 75-Point Scoring System</p>
          <p className="mt-1">Based on Mark Minervini SEPA + William O'Neil CAN SLIM</p>
        </div>
      </div>
    </div>
  );
}

export default App;