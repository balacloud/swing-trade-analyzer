/**
 * Swing Trade Analyzer - Main App Component
 * v2.0: Integrated with Defeat Beta for rich fundamentals
 */

import React, { useState, useEffect } from 'react';
import { fetchAnalysisData, checkBackendHealth } from './services/api';
import { calculateScore } from './utils/scoringEngine';
import { calculateRS } from './utils/rsCalculator';

function App() {
  const [ticker, setTicker] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [backendStatus, setBackendStatus] = useState({ healthy: false });
  const [analysisResult, setAnalysisResult] = useState(null);

  // Quick picks for testing
  const quickPicks = ['AVGO', 'NVDA', 'AAPL', 'META', 'MSFT', 'NFLX', 'PLTR'];

  // Check backend health on mount
  useEffect(() => {
    checkBackendHealth().then(setBackendStatus);
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

    try {
      // Fetch all data (stock, fundamentals, SPY, VIX)
      const data = await fetchAnalysisData(targetTicker);
      
      // Calculate score using enriched data
      const result = calculateScore(data.stock, data.spy, data.vix);
      
      // Add RS data
      const rsData = calculateRS(data.stock, data.spy);
      result.rsData = rsData;
      
      setAnalysisResult(result);
      
    } catch (err) {
      setError(err.message || 'Failed to analyze stock');
    } finally {
      setLoading(false);
    }
  };

  // Format currency
  const formatCurrency = (value) => {
    if (value === null || value === undefined) return 'N/A';
    return `$${value.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
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

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-blue-400">🎯 Swing Trade Analyzer</h1>
          <p className="text-gray-400 mt-2">Minervini SEPA + CAN SLIM Methodology</p>
          
          {/* Backend Status */}
          <div className="mt-4 flex justify-center items-center gap-2">
            <span className={`w-3 h-3 rounded-full ${backendStatus.healthy ? 'bg-green-500' : 'bg-red-500'}`}></span>
            <span className="text-sm text-gray-400">
              Backend {backendStatus.healthy ? 'Connected' : 'Disconnected'}
              {backendStatus.defeatbetaAvailable && ' • Defeat Beta ✓'}
            </span>
          </div>
        </div>

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
                    <div className="text-gray-400 text-sm">Stock vs SPY</div>
                    <div className="text-sm mt-1">
                      <span className={analysisResult.rsData.stockReturn >= 0 ? 'text-green-400' : 'text-red-400'}>
                        {formatPercent(analysisResult.rsData.stockReturn)}
                      </span>
                      <span className="text-gray-500"> vs </span>
                      <span className={analysisResult.rsData.spyReturn >= 0 ? 'text-green-400' : 'text-red-400'}>
                        {formatPercent(analysisResult.rsData.spyReturn)}
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
                      {data.value !== undefined && (
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

        {/* Footer */}
        <div className="mt-8 text-center text-gray-500 text-sm">
          <p>Day 5 - Defeat Beta Integration | 75-Point Scoring System</p>
          <p className="mt-1">Based on Mark Minervini SEPA + William O'Neil CAN SLIM</p>
        </div>
      </div>
    </div>
  );
}

export default App;
