/**
 * Swing Trade Analyzer - Main App Component
 * v2.0: Integrated with Defeat Beta for rich fundamentals
 * v2.1: Added TradingView screener scan tab (Day 12)
 */

import React, { useState, useEffect } from 'react';
import { fetchAnalysisData, checkBackendHealth, fetchScanStrategies, fetchScanResults } from './services/api';
import { calculateScore } from './utils/scoringEngine';
import { calculateRelativeStrength } from './utils/rsCalculator';

function App() {
  // Tab state
  const [activeTab, setActiveTab] = useState('analyze'); // 'analyze' or 'scan'
  
  // Analysis state
  const [ticker, setTicker] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [backendStatus, setBackendStatus] = useState({ healthy: false });
  const [analysisResult, setAnalysisResult] = useState(null);

  // Scan state
  const [scanLoading, setScanLoading] = useState(false);
  const [scanError, setScanError] = useState(null);
  const [scanResults, setScanResults] = useState(null);
  const [selectedStrategy, setSelectedStrategy] = useState('reddit');
  const [strategies, setStrategies] = useState(null);

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
    setActiveTab('analyze'); // Switch to analyze tab

    try {
      // Fetch all data (stock, fundamentals, SPY, VIX)
      const data = await fetchAnalysisData(targetTicker);
      
      // Calculate score using enriched data
      const result = calculateScore(data.stock, data.spy, data.vix);
      
      // Add RS data (already calculated in scoring engine, but add for display)
      const rsData = calculateRelativeStrength(data.stock, data.spy);
      result.rsData = rsData;
      
      setAnalysisResult(result);
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
    if (rsi >= 70) return 'text-red-400';  // Overbought
    if (rsi <= 30) return 'text-green-400'; // Oversold
    if (rsi >= 50) return 'text-green-300'; // Bullish
    return 'text-yellow-400';
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
                  placeholder="Enter ticker (e.g., AVGO)"
                  className="flex-1 bg-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button
                  onClick={() => analyzeStock()}
                  disabled={loading}
                  className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-semibold disabled:opacity-50"
                >
                  {loading ? 'Analyzing...' : 'Analyze'}
                </button>
              </div>

              {/* Quick Picks */}
              <div className="mt-4 flex flex-wrap gap-2">
                {quickPicks.map((pick) => (
                  <button
                    key={pick}
                    onClick={() => {
                      setTicker(pick);
                      analyzeStock(pick);
                    }}
                    className="bg-gray-700 hover:bg-gray-600 px-3 py-1 rounded text-sm"
                  >
                    {pick}
                  </button>
                ))}
              </div>
            </div>

            {/* Error Message */}
            {error && (
              <div className="bg-red-900/50 border border-red-500 rounded-lg p-4 mb-6 text-red-200">
                {error}
              </div>
            )}

            {/* Analysis Results */}
            {analysisResult && (
              <div className="space-y-6">
                {/* Verdict Card */}
                <div className={`${getVerdictColor(analysisResult.verdict)} rounded-lg p-6 text-center`}>
                  <div className="text-4xl font-bold">{analysisResult.verdict?.verdict}</div>
                  <div className="text-xl mt-2">{analysisResult.ticker} - {analysisResult.name}</div>
                  <div className="mt-2 opacity-90">{analysisResult.verdict?.reason}</div>
                </div>

                {/* Score Overview */}
                <div className="bg-gray-800 rounded-lg p-6">
                  <h2 className="text-xl font-bold mb-4">Score: {analysisResult.totalScore}/75</h2>
                  
                  {/* Score Bar */}
                  <div className="w-full bg-gray-700 rounded-full h-4 mb-6">
                    <div
                      className={`h-4 rounded-full ${
                        analysisResult.totalScore >= 60 ? 'bg-green-500' :
                        analysisResult.totalScore >= 40 ? 'bg-yellow-500' : 'bg-red-500'
                      }`}
                      style={{ width: `${(analysisResult.totalScore / 75) * 100}%` }}
                    ></div>
                  </div>

                  {/* Score Breakdown */}
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="bg-gray-700 rounded-lg p-4 text-center">
                      <div className="text-gray-400 text-sm">Technical</div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.breakdown?.technical?.score, 40)}`}>
                        {analysisResult.breakdown?.technical?.score}/40
                      </div>
                    </div>
                    <div className="bg-gray-700 rounded-lg p-4 text-center">
                      <div className="text-gray-400 text-sm">
                        Fundamental
                        {analysisResult.breakdown?.fundamental?.dataQuality === 'rich' && (
                          <span className="text-green-400 ml-1">★</span>
                        )}
                      </div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.breakdown?.fundamental?.score, 20)}`}>
                        {analysisResult.breakdown?.fundamental?.score}/20
                      </div>
                    </div>
                    <div className="bg-gray-700 rounded-lg p-4 text-center">
                      <div className="text-gray-400 text-sm">Sentiment</div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.breakdown?.sentiment?.score, 10)}`}>
                        {analysisResult.breakdown?.sentiment?.score}/10
                      </div>
                    </div>
                    <div className="bg-gray-700 rounded-lg p-4 text-center">
                      <div className="text-gray-400 text-sm">Risk/Macro</div>
                      <div className={`text-2xl font-bold ${getScoreColor(analysisResult.breakdown?.risk?.score, 5)}`}>
                        {analysisResult.breakdown?.risk?.score}/5
                      </div>
                    </div>
                  </div>
                </div>

                {/* Relative Strength */}
                {analysisResult.rsData && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h2 className="text-xl font-bold mb-4">📊 Relative Strength</h2>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                      <div>
                        <div className="text-gray-400 text-sm">52-Week RS</div>
                        <div className={`text-2xl font-bold ${
                          analysisResult.rsData.rs52Week >= 1.2 ? 'text-green-400' :
                          analysisResult.rsData.rs52Week >= 1.0 ? 'text-green-300' :
                          analysisResult.rsData.rs52Week >= 0.8 ? 'text-yellow-400' : 'text-red-400'
                        }`}>
                          {analysisResult.rsData.rs52Week?.toFixed(2) || 'N/A'}
                        </div>
                      </div>
                      <div>
                        <div className="text-gray-400 text-sm">13-Week RS</div>
                        <div className={`text-2xl font-bold ${
                          analysisResult.rsData.rs13Week >= 1.0 ? 'text-green-400' :
                          analysisResult.rsData.rs13Week >= 0.8 ? 'text-yellow-400' : 'text-red-400'
                        }`}>
                          {analysisResult.rsData.rs13Week?.toFixed(2) || 'N/A'}
                        </div>
                      </div>
                      <div>
                        <div className="text-gray-400 text-sm">RS Rating</div>
                        <div className="text-2xl font-bold text-blue-400">
                          {analysisResult.rsData.rsRating || 'N/A'}
                        </div>
                      </div>
                      <div>
                        <div className="text-gray-400 text-sm">Stock vs SPY (52w)</div>
                        <div className="text-sm mt-1">
                          <span className={analysisResult.rsData.stockReturn52w >= 0 ? 'text-green-400' : 'text-red-400'}>
                            {analysisResult.rsData.stockReturn52w !== null && analysisResult.rsData.stockReturn52w !== undefined 
                              ? `${analysisResult.rsData.stockReturn52w >= 0 ? '+' : ''}${analysisResult.rsData.stockReturn52w}%` 
                              : 'N/A'}
                          </span>
                          <span className="text-gray-500"> vs </span>
                          <span className={analysisResult.rsData.spyReturn52w >= 0 ? 'text-green-400' : 'text-red-400'}>
                            {analysisResult.rsData.spyReturn52w !== null && analysisResult.rsData.spyReturn52w !== undefined 
                              ? `${analysisResult.rsData.spyReturn52w >= 0 ? '+' : ''}${analysisResult.rsData.spyReturn52w}%` 
                              : 'N/A'}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* Fundamental Details */}
                {analysisResult.breakdown?.fundamental && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h2 className="text-xl font-bold mb-4">
                      💰 Fundamentals
                      <span className="text-sm font-normal text-gray-400 ml-2">
                        (Source: {analysisResult.breakdown.fundamental.dataSource})
                      </span>
                    </h2>
                    <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                      {Object.entries(analysisResult.breakdown.fundamental.details || {}).map(([key, data]) => (
                        <div key={key} className="text-center">
                          <div className="text-gray-400 text-sm capitalize">{key.replace(/([A-Z])/g, ' $1')}</div>
                          <div className={`text-lg font-bold ${getScoreColor(data.score, data.max)}`}>
                            {data.score}/{data.max}
                          </div>
                          {data.value !== undefined && data.value !== null && (
                            <div className="text-xs text-gray-500">
                              {typeof data.value === 'number' ? 
                                (key.includes('Growth') || key === 'roe' ? formatPercent(data.value) : data.value.toFixed(2)) 
                                : 'N/A'}
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Quality Gates */}
                {analysisResult.qualityGates && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h2 className="text-xl font-bold mb-4">
                      🚦 Quality Gates
                      <span className={`ml-2 text-sm ${
                        analysisResult.qualityGates.passed ? 'text-green-400' : 'text-red-400'
                      }`}>
                        {analysisResult.qualityGates.passed ? '✓ All Passed' : `✗ ${analysisResult.qualityGates.criticalFails} Failed`}
                      </span>
                    </h2>
                    
                    {analysisResult.qualityGates.gates?.length > 0 ? (
                      <div className="space-y-2">
                        {analysisResult.qualityGates.gates.map((gate, i) => (
                          <div key={i} className="flex items-center justify-between bg-red-900/30 rounded p-3">
                            <span className="text-red-400">✗ {gate.name}</span>
                            <span className="text-gray-400">{gate.value} (need {gate.threshold})</span>
                          </div>
                        ))}
                      </div>
                    ) : (
                      <div className="text-green-400">✓ All quality checks passed</div>
                    )}
                  </div>
                )}

                {/* Technical Indicators */}
                {analysisResult.indicators && (
                  <div className="bg-gray-800 rounded-lg p-6">
                    <h2 className="text-xl font-bold mb-4">📈 Technical Indicators</h2>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                      <div>
                        <span className="text-gray-400">Price:</span>
                        <span className="ml-2">{formatCurrency(analysisResult.currentPrice)}</span>
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
                  {strategies?.notes && <p className="mt-1">{strategies.notes}</p>}
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
                <p className="text-gray-600 text-sm">
                  All strategies filter for NYSE/NASDAQ stocks in Stage 2 uptrends with institutional-quality criteria.
                </p>
              </div>
            )}
          </>
        )}

        {/* Footer */}
        <div className="mt-8 text-center text-gray-500 text-sm">
          <p>Day 12 - TradingView Screener Integration | 75-Point Scoring System</p>
          <p className="mt-1">Based on Mark Minervini SEPA + William O'Neil CAN SLIM</p>
        </div>
      </div>
    </div>
  );
}

export default App;