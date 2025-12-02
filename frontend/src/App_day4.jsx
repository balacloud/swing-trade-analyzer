import React, { useState, useEffect } from 'react';
import { 
  TrendingUp, 
  TrendingDown, 
  Minus, 
  AlertCircle, 
  CheckCircle, 
  XCircle, 
  Loader2,
  RefreshCw,
  Search,
  Activity,
  DollarSign,
  Target,
  Shield
} from 'lucide-react';
import { fetchAnalysisData, checkHealth } from './services/api';
import { analyzeStock, formatAnalysisForDisplay } from './utils/scoringEngine';
import { formatRS, getRSColor, getRSTrendIcon } from './utils/rsCalculator';

function App() {
  // State
  const [ticker, setTicker] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [backendConnected, setBackendConnected] = useState(false);
  
  // Check backend connection on mount
  useEffect(() => {
    checkHealth().then(setBackendConnected);
  }, []);
  
  // Handle stock analysis
  const handleAnalyze = async () => {
    if (!ticker.trim()) {
      setError('Please enter a ticker symbol');
      return;
    }
    
    setLoading(true);
    setError(null);
    setAnalysis(null);
    
    try {
      // Fetch data from backend
      const data = await fetchAnalysisData(ticker.toUpperCase());
      
      // Run analysis
      const result = analyzeStock(data.stock, data.spy);
      const formatted = formatAnalysisForDisplay(result);
      
      setAnalysis(formatted);
    } catch (err) {
      setError(err.message || 'Failed to analyze stock');
    } finally {
      setLoading(false);
    }
  };
  
  // Handle enter key
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') handleAnalyze();
  };
  
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-6xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Activity className="w-8 h-8 text-blue-600" />
              <div>
                <h1 className="text-xl font-bold text-gray-900">Swing Trade Analyzer</h1>
                <p className="text-sm text-gray-500">v1.0 - 75-Point Scoring System</p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <div className={`w-2 h-2 rounded-full ${backendConnected ? 'bg-green-500' : 'bg-red-500'}`} />
              <span className="text-sm text-gray-600">
                {backendConnected ? 'Backend Connected' : 'Backend Offline'}
              </span>
            </div>
          </div>
        </div>
      </header>
      
      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 py-6">
        {/* Search Box */}
        <div className="bg-white rounded-lg shadow-sm border p-4 mb-6">
          <div className="flex gap-3">
            <div className="flex-1 relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type="text"
                value={ticker}
                onChange={(e) => setTicker(e.target.value.toUpperCase())}
                onKeyPress={handleKeyPress}
                placeholder="Enter ticker symbol (e.g., AAPL, NVDA)"
                className="w-full pl-10 pr-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                disabled={loading}
              />
            </div>
            <button
              onClick={handleAnalyze}
              disabled={loading || !backendConnected}
              className="px-6 py-3 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center gap-2"
            >
              {loading ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  Analyzing...
                </>
              ) : (
                <>
                  <RefreshCw className="w-5 h-5" />
                  Analyze
                </>
              )}
            </button>
          </div>
          
          {/* Quick picks */}
          <div className="mt-3 flex gap-2 text-sm">
            <span className="text-gray-500">Quick:</span>
            {['AAPL', 'NVDA', 'MSFT', 'META', 'AVGO'].map(t => (
              <button
                key={t}
                onClick={() => { setTicker(t); }}
                className="px-2 py-1 bg-gray-100 rounded hover:bg-gray-200 text-gray-700"
              >
                {t}
              </button>
            ))}
          </div>
        </div>
        
        {/* Error Display */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6 flex items-center gap-3">
            <AlertCircle className="w-5 h-5 text-red-500" />
            <span className="text-red-700">{error}</span>
          </div>
        )}
        
        {/* Analysis Results */}
        {analysis && (
          <div className="space-y-6">
            {/* Verdict Card */}
            <VerdictCard analysis={analysis} />
            
            {/* Score Breakdown */}
            <ScoreBreakdown analysis={analysis} />
            
            {/* RS Analysis */}
            <RSCard rs={analysis.rs} />
            
            {/* Quality Gates */}
            <QualityGatesCard gates={analysis.qualityGates} criticalFails={analysis.criticalFails} />
            
            {/* Trade Setup (if BUY) */}
            {analysis.tradeSetup && <TradeSetupCard setup={analysis.tradeSetup} />}
          </div>
        )}
        
        {/* Empty State */}
        {!analysis && !loading && !error && (
          <div className="bg-white rounded-lg shadow-sm border p-12 text-center">
            <Activity className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">Enter a ticker to analyze</h3>
            <p className="text-gray-500">Get a complete swing trade recommendation with entry, stop, and target prices.</p>
          </div>
        )}
      </main>
      
      {/* Footer */}
      <footer className="border-t bg-white mt-8">
        <div className="max-w-6xl mx-auto px-4 py-4 text-center text-sm text-gray-500">
          <p>Based on Minervini SEPA + O'Neil CAN SLIM methodologies. Not financial advice.</p>
          <p className="mt-1">Data source: Yahoo Finance via yfinance</p>
        </div>
      </footer>
    </div>
  );
}

// Verdict Card Component
function VerdictCard({ analysis }) {
  const verdictColors = {
    BUY: 'bg-green-50 border-green-200',
    HOLD: 'bg-yellow-50 border-yellow-200',
    AVOID: 'bg-red-50 border-red-200'
  };
  
  const verdictTextColors = {
    BUY: 'text-green-700',
    HOLD: 'text-yellow-700',
    AVOID: 'text-red-700'
  };
  
  const VerdictIcon = {
    BUY: CheckCircle,
    HOLD: Minus,
    AVOID: XCircle
  }[analysis.verdict.action];
  
  return (
    <div className={`rounded-lg border-2 p-6 ${verdictColors[analysis.verdict.action]}`}>
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <VerdictIcon className={`w-12 h-12 ${verdictTextColors[analysis.verdict.action]}`} />
          <div>
            <div className="flex items-center gap-3">
              <span className="text-2xl font-bold text-gray-900">{analysis.ticker}</span>
              <span className="text-xl text-gray-600">{analysis.price}</span>
            </div>
            <div className={`text-3xl font-bold ${verdictTextColors[analysis.verdict.action]}`}>
              {analysis.verdict.action}
            </div>
          </div>
        </div>
        <div className="text-right">
          <div className="text-4xl font-bold text-gray-900">{analysis.score}</div>
          <div className="text-sm text-gray-500">Score ({analysis.scorePercentage})</div>
          <div className="text-sm text-gray-600 mt-1">
            Confidence: <span className="font-medium">{analysis.verdict.confidence}</span>
          </div>
        </div>
      </div>
      <p className="mt-4 text-gray-700">{analysis.verdict.reason}</p>
    </div>
  );
}

// Score Breakdown Component
function ScoreBreakdown({ analysis }) {
  const categories = [
    { name: 'Technical', score: analysis.breakdown.technical, max: 40, color: 'bg-blue-500' },
    { name: 'Fundamental', score: analysis.breakdown.fundamental, max: 20, color: 'bg-purple-500' },
    { name: 'Sentiment', score: analysis.breakdown.sentiment, max: 10, color: 'bg-orange-500' },
    { name: 'Risk/Macro', score: analysis.breakdown.risk, max: 5, color: 'bg-gray-500' }
  ];
  
  return (
    <div className="bg-white rounded-lg shadow-sm border p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">Score Breakdown</h3>
      <div className="space-y-4">
        {categories.map(cat => {
          const [current, max] = cat.score.split('/').map(Number);
          const percentage = (current / max) * 100;
          
          return (
            <div key={cat.name}>
              <div className="flex justify-between mb-1">
                <span className="text-sm font-medium text-gray-700">{cat.name}</span>
                <span className="text-sm text-gray-600">{cat.score}</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div 
                  className={`${cat.color} h-2 rounded-full transition-all duration-500`}
                  style={{ width: `${percentage}%` }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

// RS Card Component
function RSCard({ rs }) {
  if (!rs) return null;
  
  return (
    <div className="bg-white rounded-lg shadow-sm border p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
        <TrendingUp className="w-5 h-5 text-blue-600" />
        Relative Strength Analysis
      </h3>
      
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
        <div className="bg-gray-50 rounded-lg p-4">
          <div className="text-sm text-gray-500 mb-1">52-Week RS</div>
          <div className={`text-2xl font-bold ${getRSColor(rs.rs52Week)}`}>
            {formatRS(rs.rs52Week)}
          </div>
        </div>
        <div className="bg-gray-50 rounded-lg p-4">
          <div className="text-sm text-gray-500 mb-1">13-Week RS</div>
          <div className={`text-2xl font-bold ${getRSColor(rs.rs13Week)}`}>
            {formatRS(rs.rs13Week)}
          </div>
        </div>
        <div className="bg-gray-50 rounded-lg p-4">
          <div className="text-sm text-gray-500 mb-1">RS Rating</div>
          <div className="text-2xl font-bold text-gray-900">{rs.rsRating || 'N/A'}</div>
        </div>
        <div className="bg-gray-50 rounded-lg p-4">
          <div className="text-sm text-gray-500 mb-1">Trend</div>
          <div className="text-2xl font-bold">
            {getRSTrendIcon(rs.rsTrend)} {rs.rsTrend}
          </div>
        </div>
      </div>
      
      <div className="bg-blue-50 rounded-lg p-4">
        <div className="flex items-start gap-2">
          <Activity className="w-5 h-5 text-blue-600 mt-0.5" />
          <div>
            <div className="font-medium text-blue-900">{rs.interpretation}</div>
            <div className="text-sm text-blue-700 mt-1">
              Stock: {rs.stockReturn52w > 0 ? '+' : ''}{rs.stockReturn52w}% vs SPY: {rs.spyReturn52w > 0 ? '+' : ''}{rs.spyReturn52w}% (52 weeks)
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// Quality Gates Card Component
function QualityGatesCard({ gates, criticalFails }) {
  return (
    <div className="bg-white rounded-lg shadow-sm border p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
        <Shield className="w-5 h-5 text-blue-600" />
        Quality Gates
      </h3>
      
      {criticalFails.length > 0 && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-3 mb-4">
          <div className="font-medium text-red-800 mb-1">Critical Failures ({criticalFails.length})</div>
          <ul className="text-sm text-red-700 space-y-1">
            {criticalFails.map((fail, i) => (
              <li key={i} className="flex items-center gap-2">
                <XCircle className="w-4 h-4" />
                {fail}
              </li>
            ))}
          </ul>
        </div>
      )}
      
      <div className="space-y-2">
        {gates.map((gate, i) => (
          <div key={i} className="flex items-center gap-3 p-2 rounded hover:bg-gray-50">
            {gate.passes ? (
              <CheckCircle className="w-5 h-5 text-green-500" />
            ) : (
              <XCircle className="w-5 h-5 text-red-500" />
            )}
            <div className="flex-1">
              <span className="font-medium text-gray-900">{gate.name}</span>
              <p className="text-sm text-gray-600">{gate.reason}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// Trade Setup Card Component
function TradeSetupCard({ setup }) {
  return (
    <div className="bg-green-50 border-2 border-green-200 rounded-lg p-6">
      <h3 className="text-lg font-semibold text-green-900 mb-4 flex items-center gap-2">
        <Target className="w-5 h-5" />
        Trade Setup
      </h3>
      
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
        <div className="bg-white rounded-lg p-4 border border-green-200">
          <div className="text-sm text-gray-500 mb-1">Entry Price</div>
          <div className="text-xl font-bold text-gray-900">${setup.entry}</div>
        </div>
        <div className="bg-white rounded-lg p-4 border border-red-200">
          <div className="text-sm text-gray-500 mb-1">Stop Loss</div>
          <div className="text-xl font-bold text-red-600">${setup.stopLoss}</div>
          <div className="text-xs text-gray-500">1.2x ATR</div>
        </div>
        <div className="bg-white rounded-lg p-4 border border-green-200">
          <div className="text-sm text-gray-500 mb-1">Target</div>
          <div className="text-xl font-bold text-green-600">${setup.target}</div>
          <div className="text-xs text-gray-500">2:1 R:R</div>
        </div>
        <div className="bg-white rounded-lg p-4 border border-blue-200">
          <div className="text-sm text-gray-500 mb-1">Position Size</div>
          <div className="text-xl font-bold text-blue-600">{setup.shares} shares</div>
          <div className="text-xs text-gray-500">${setup.positionValue} (1% risk)</div>
        </div>
      </div>
      
      <div className="bg-white rounded-lg p-4 border border-green-200">
        <div className="grid grid-cols-3 gap-4 text-center">
          <div>
            <div className="text-sm text-gray-500">Risk/Share</div>
            <div className="font-bold text-gray-900">${setup.riskPerShare}</div>
          </div>
          <div>
            <div className="text-sm text-gray-500">ATR</div>
            <div className="font-bold text-gray-900">${setup.atr}</div>
          </div>
          <div>
            <div className="text-sm text-gray-500">Max Risk</div>
            <div className="font-bold text-gray-900">${setup.riskAmount}</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
