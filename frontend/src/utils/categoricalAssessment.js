/**
 * Categorical Assessment System for Swing Trade Analyzer
 * v4.5: Replaces 75-point numerical scoring with categorical assessments
 *
 * Day 44: Initial implementation
 *
 * Categories:
 * - Technical: Strong / Decent / Weak
 * - Fundamental: Strong / Decent / Weak
 * - Sentiment: Strong / Neutral / Weak (Fear & Greed Index)
 * - Risk/Macro: Favorable / Neutral / Unfavorable
 *
 * Rationale:
 * - Score-to-return correlation = 0.011 (essentially ZERO)
 * - System works as a FILTER, not a RANKER
 * - Categorical assessments honestly represent this reality
 */

// Known ETF tickers - these don't have traditional fundamentals
const ETF_TICKERS = ['SPY', 'QQQ', 'IWM', 'DIA', 'VOO', 'VTI', 'VEA', 'VWO', 'VNQ',
                     'BND', 'AGG', 'GLD', 'SLV', 'USO', 'XLF', 'XLK', 'XLE', 'XLV',
                     'XLI', 'XLP', 'XLY', 'XLB', 'XLU', 'ARKK', 'ARKG', 'ARKW'];

/**
 * Assess Technical Strength
 *
 * Criteria:
 * - Strong: Trend Template 7-8/8, RSI 50-70, above all key MAs
 * - Decent: Trend Template 5-6/8, RSI 40-80, above 50 EMA
 * - Weak: Trend Template <5/8, RSI overbought/oversold, below key MAs
 *
 * @param {object} technicalData - Technical indicators from scoring engine
 * @param {object} trendTemplate - Minervini's 8-point Trend Template from pattern detection
 * @param {number} rsi - Current RSI(14) value
 * @returns {object} { assessment, reasons, data }
 */
export function assessTechnical(technicalData, trendTemplate, rsi) {
  const reasons = [];
  const data = {};

  // Get trend template pass count (API returns criteria_met, not criteria_passed)
  const passCount = trendTemplate?.criteria_met || trendTemplate?.criteria_passed || 0;
  const totalCriteria = trendTemplate?.total_criteria || 8;
  const hasTrendTemplate = trendTemplate !== null && trendTemplate !== undefined;
  data.trendTemplateScore = `${passCount}/${totalCriteria}`;
  data.trendTemplateAvailable = hasTrendTemplate;

  // Get RSI value (prefer passed RSI, fallback to technicalData)
  const rsiValue = rsi || technicalData?.indicators?.rsi || 50;
  data.rsi = rsiValue;

  // Get price vs MA status from technical scoring
  const trendScore = technicalData?.details?.trendStructure?.score || 0;
  const trendMax = technicalData?.details?.trendStructure?.max || 15;
  const priceAbove200SMA = trendScore >= 5;  // Stage 2 at minimum
  const perfectTrend = trendScore >= 15;     // Price > 50 SMA > 200 SMA
  data.priceAbove200SMA = priceAbove200SMA;
  data.perfectTrend = perfectTrend;
  data.trendScore = `${trendScore}/${trendMax}`;

  // Get RS data
  const rs52Week = technicalData?.rsData?.rs52Week || 1.0;
  data.rs52Week = rs52Week;

  // Determine assessment
  let assessment = 'Weak';

  // Strong: 7-8/8 trend template, RSI 50-70, good RS
  if (passCount >= 7 && rsiValue >= 50 && rsiValue <= 70 && rs52Week >= 1.0) {
    assessment = 'Strong';
    reasons.push(`Trend Template: ${passCount}/8 Minervini criteria passed`);
    reasons.push(`RSI ${rsiValue.toFixed(1)} in optimal pullback range (50-70)`);
    if (rs52Week >= 1.2) {
      reasons.push(`Strong RS: ${rs52Week.toFixed(2)}x vs SPY (outperforming)`);
    }
  }
  // Decent: 5-6/8 trend template, RSI 40-80
  else if (passCount >= 5 && rsiValue >= 40 && rsiValue <= 80) {
    assessment = 'Decent';
    reasons.push(`Trend Template: ${passCount}/8 criteria passed (needs 7+ for Strong)`);
    if (rsiValue < 50) {
      reasons.push(`RSI ${rsiValue.toFixed(1)} slightly weak but acceptable`);
    } else if (rsiValue > 70) {
      reasons.push(`RSI ${rsiValue.toFixed(1)} elevated - watch for reversal`);
    } else {
      reasons.push(`RSI ${rsiValue.toFixed(1)} in good range`);
    }
  }
  // Weak: Below thresholds - provide detailed feedback
  else {
    assessment = 'Weak';

    // Trend template issues
    if (!hasTrendTemplate) {
      reasons.push('Pattern detection unavailable');
    } else if (passCount === 0) {
      reasons.push(`Trend Template: 0/8 criteria - NOT in Stage 2 uptrend`);
      reasons.push('Stock may be in Stage 1 (base), Stage 3 (top), or Stage 4 (decline)');
    } else if (passCount < 5) {
      reasons.push(`Trend Template: Only ${passCount}/8 criteria passed (needs 5+ for Decent)`);
    }

    // RSI issues
    if (rsiValue < 30) {
      reasons.push(`RSI ${rsiValue.toFixed(1)} deeply oversold - avoid catching falling knives`);
    } else if (rsiValue < 40) {
      reasons.push(`RSI ${rsiValue.toFixed(1)} oversold - weak momentum`);
    } else if (rsiValue > 80) {
      reasons.push(`RSI ${rsiValue.toFixed(1)} overbought - risky entry point`);
    }

    // RS issues
    if (rs52Week < 0.8) {
      reasons.push(`Weak RS: ${rs52Week.toFixed(2)}x vs SPY (significantly underperforming)`);
    } else if (rs52Week < 1.0) {
      reasons.push(`Below-average RS: ${rs52Week.toFixed(2)}x vs SPY`);
    }

    // Price structure context
    if (!priceAbove200SMA) {
      reasons.push('Below 200 SMA - bearish long-term trend');
    }
  }

  // Ensure we always have at least one reason
  if (reasons.length === 0) {
    reasons.push(`Technical analysis: Mixed signals`);
  }

  return {
    assessment,
    reasons,
    data,
    color: assessment === 'Strong' ? 'green' : assessment === 'Decent' ? 'yellow' : 'red'
  };
}

/**
 * Assess Fundamental Strength
 *
 * Criteria:
 * - Strong: ROE > 15%, Revenue Growth > 10%, Debt/Equity < 1.0, Positive EPS
 * - Decent: ROE 8-15%, Revenue Growth 0-10%, Debt/Equity 1.0-2.0
 * - Weak: ROE < 8%, Negative growth, High debt, Negative EPS
 *
 * @param {object} fundamentals - Fundamental data from backend
 * @param {string} ticker - Stock ticker (for ETF detection)
 * @returns {object} { assessment, reasons, data }
 */
export function assessFundamental(fundamentals, ticker) {
  const reasons = [];
  const data = {};

  // Check for ETF
  const isETF = ETF_TICKERS.includes(ticker?.toUpperCase());
  if (isETF) {
    return {
      assessment: 'N/A',
      reasons: ['ETFs do not have traditional fundamentals'],
      data: { isETF: true },
      color: 'gray'
    };
  }

  // Check for unavailable data
  if (!fundamentals || fundamentals.dataQuality === 'unavailable') {
    return {
      assessment: 'Unknown',
      reasons: ['Fundamental data temporarily unavailable'],
      data: { dataQuality: 'unavailable' },
      color: 'gray'
    };
  }

  // Extract fundamental metrics
  const roe = fundamentals.roe;
  const revenueGrowth = fundamentals.revenueGrowth;
  const debtToEquity = fundamentals.debtToEquity;
  const epsGrowth = fundamentals.epsGrowth;

  data.roe = roe;
  data.revenueGrowth = revenueGrowth;
  data.debtToEquity = debtToEquity;
  data.epsGrowth = epsGrowth;
  data.dataSource = fundamentals.source || 'unknown';

  // Count strong/weak metrics
  let strongCount = 0;
  let weakCount = 0;

  // ROE assessment
  if (roe !== null && roe !== undefined) {
    if (roe > 15) {
      strongCount++;
      reasons.push(`ROE ${roe.toFixed(1)}% (Strong > 15%)`);
    } else if (roe >= 8) {
      reasons.push(`ROE ${roe.toFixed(1)}% (Decent 8-15%)`);
    } else {
      weakCount++;
      reasons.push(`ROE ${roe.toFixed(1)}% (Weak < 8%)`);
    }
  }

  // Revenue Growth assessment
  if (revenueGrowth !== null && revenueGrowth !== undefined) {
    if (revenueGrowth > 10) {
      strongCount++;
      reasons.push(`Revenue Growth ${revenueGrowth.toFixed(1)}% (Strong > 10%)`);
    } else if (revenueGrowth >= 0) {
      reasons.push(`Revenue Growth ${revenueGrowth.toFixed(1)}% (Decent 0-10%)`);
    } else {
      weakCount++;
      reasons.push(`Revenue Growth ${revenueGrowth.toFixed(1)}% (Weak < 0%)`);
    }
  }

  // Debt/Equity assessment
  if (debtToEquity !== null && debtToEquity !== undefined) {
    if (debtToEquity < 1.0 && debtToEquity >= 0) {
      strongCount++;
      reasons.push(`Debt/Equity ${debtToEquity.toFixed(2)} (Strong < 1.0)`);
    } else if (debtToEquity <= 2.0) {
      reasons.push(`Debt/Equity ${debtToEquity.toFixed(2)} (Decent 1.0-2.0)`);
    } else {
      weakCount++;
      reasons.push(`Debt/Equity ${debtToEquity.toFixed(2)} (Weak > 2.0)`);
    }
  }

  // If no metrics were evaluated, mark as unknown
  if (reasons.length === 0) {
    return {
      assessment: 'Unknown',
      reasons: ['No fundamental metrics available for evaluation'],
      data: { ...data, noData: true },
      color: 'gray'
    };
  }

  // Determine overall assessment
  let assessment = 'Decent';
  if (strongCount >= 2 && weakCount === 0) {
    assessment = 'Strong';
  } else if (weakCount >= 2) {
    assessment = 'Weak';
  }

  return {
    assessment,
    reasons,
    data,
    color: assessment === 'Strong' ? 'green' : assessment === 'Decent' ? 'yellow' : 'red'
  };
}

/**
 * Assess Sentiment (Fear & Greed Index)
 *
 * Criteria:
 * - Strong: 55-75 (Greed but not extreme - good for momentum)
 * - Neutral: 45-55 (Neutral zone)
 * - Weak: 0-25 (Extreme Fear) OR 75-100 (Extreme Greed - contrarian risk)
 *
 * @param {object} fearGreedData - Fear & Greed Index data from backend
 * @returns {object} { assessment, reasons, data }
 */
export function assessSentiment(fearGreedData) {
  const reasons = [];
  const data = {};

  // Default to neutral if no data
  if (!fearGreedData || fearGreedData.error) {
    return {
      assessment: 'Neutral',
      reasons: ['Fear & Greed data unavailable - defaulting to neutral'],
      data: { value: 50, rating: 'Neutral', source: 'default' },
      color: 'gray'
    };
  }

  const value = fearGreedData.value || 50;
  const rating = fearGreedData.rating || 'Neutral';

  data.value = value;
  data.rating = rating;
  data.source = fearGreedData.source || 'CNN Fear & Greed Index';

  let assessment = 'Neutral';

  // Strong: Greed but not extreme (55-75) - good for momentum trades
  if (value >= 55 && value <= 75) {
    assessment = 'Strong';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Positive sentiment without extreme greed');
    reasons.push('Good conditions for momentum/pullback trades');
  }
  // Neutral: Middle range (45-55) - balanced sentiment
  else if (value >= 45 && value < 55) {
    assessment = 'Neutral';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Market sentiment is balanced');
    reasons.push('Neither fear nor greed dominant');
  }
  // Weak: Fear zone (25-45) - pullback setups often fail
  else if (value >= 25 && value < 45) {
    assessment = 'Weak';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Fear present - pullback setups risky');
    reasons.push('Consider waiting for sentiment improvement');
  }
  // Weak: Extreme fear (<25) - capitulation risk
  else if (value < 25) {
    assessment = 'Weak';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Extreme fear - potential capitulation');
    reasons.push('Caution: pullback setups often fail in fearful markets');
  }
  // Weak: Extreme greed (>75) - contrarian risk
  else if (value > 75) {
    assessment = 'Weak';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Extreme greed - contrarian risk');
    reasons.push('Caution: market may be overextended');
  }

  return {
    assessment,
    reasons,
    data,
    color: assessment === 'Strong' ? 'green' : assessment === 'Neutral' ? 'gray' : 'red'
  };
}

/**
 * Assess Risk/Macro Environment
 *
 * Criteria:
 * - Favorable: VIX < 20, SPY > 200 EMA (Bull regime)
 * - Neutral: VIX 20-30, SPY near 200 EMA
 * - Unfavorable: VIX > 30 OR SPY < 200 EMA (Bear regime)
 *
 * @param {object} vixData - VIX data from backend
 * @param {object} spyData - SPY data from backend
 * @returns {object} { assessment, reasons, data }
 */
export function assessRiskMacro(vixData, spyData) {
  const reasons = [];
  const data = {};

  const vix = vixData?.current || 20;
  const spyAbove200EMA = spyData?.aboveSma200 || false;

  data.vix = vix;
  data.vixRegime = vixData?.regime || 'unknown';
  data.spyAbove200EMA = spyAbove200EMA;

  let assessment = 'Neutral';

  // Check for unfavorable conditions first (either condition triggers)
  if (vix > 30 || !spyAbove200EMA) {
    assessment = 'Unfavorable';
    if (vix > 30) {
      reasons.push(`VIX at ${vix.toFixed(1)} (Extreme volatility > 30)`);
    }
    if (!spyAbove200EMA) {
      reasons.push('SPY below 200 EMA (Bear regime)');
      reasons.push('Caution: Most pullback setups fail in bear markets');
    }
  }
  // Favorable: Low VIX AND bull regime
  else if (vix < 20 && spyAbove200EMA) {
    assessment = 'Favorable';
    reasons.push(`VIX at ${vix.toFixed(1)} (Low volatility < 20)`);
    reasons.push('SPY above 200 EMA (Bull regime)');
    reasons.push('Favorable conditions for swing trades');
  }
  // Neutral: Elevated VIX but still bull regime
  else {
    assessment = 'Neutral';
    reasons.push(`VIX at ${vix.toFixed(1)} (Elevated 20-30)`);
    if (spyAbove200EMA) {
      reasons.push('SPY above 200 EMA (Bull regime intact)');
    }
    reasons.push('Proceed with caution');
  }

  return {
    assessment,
    reasons,
    data,
    color: assessment === 'Favorable' ? 'green' : assessment === 'Neutral' ? 'yellow' : 'red'
  };
}

/**
 * Determine Overall Verdict
 *
 * Logic:
 * - BUY: 2+ Strong categories AND Favorable/Neutral Risk
 * - HOLD: 1 Strong OR (Decent Tech + Decent Fund) with no Unfavorable Risk
 * - AVOID: Weak Technical OR (Weak Fundamental + Weak Sentiment) OR Unfavorable Risk override
 *
 * @param {string} technical - Technical assessment
 * @param {string} fundamental - Fundamental assessment
 * @param {string} sentiment - Sentiment assessment
 * @param {string} riskMacro - Risk/Macro assessment
 * @returns {object} { verdict, reason, color }
 */
export function determineVerdict(technical, fundamental, sentiment, riskMacro) {
  // Count strong assessments (excluding Risk which uses different scale)
  const assessments = [technical, fundamental, sentiment];
  const strongCount = assessments.filter(a => a === 'Strong').length;
  const weakCount = assessments.filter(a => a === 'Weak').length;

  // AVOID conditions (highest priority)

  // 1. Technical Weak = AVOID (can't fight bad technicals)
  if (technical === 'Weak') {
    return {
      verdict: 'AVOID',
      reason: 'Weak technical setup',
      color: 'red'
    };
  }

  // 2. Unfavorable Risk = HOLD at best (regime override)
  if (riskMacro === 'Unfavorable') {
    return {
      verdict: 'HOLD',
      reason: 'Unfavorable market conditions (regime caution)',
      color: 'yellow'
    };
  }

  // 3. Both Fundamental AND Sentiment are Weak = AVOID
  if (fundamental === 'Weak' && sentiment === 'Weak') {
    return {
      verdict: 'AVOID',
      reason: 'Weak fundamentals and negative sentiment',
      color: 'red'
    };
  }

  // BUY conditions
  // Need 2+ Strong with Favorable or Neutral risk
  if (strongCount >= 2 && (riskMacro === 'Favorable' || riskMacro === 'Neutral')) {
    return {
      verdict: 'BUY',
      reason: `${strongCount} strong categories with ${riskMacro.toLowerCase()} conditions`,
      color: 'green'
    };
  }

  // HOLD conditions (default for mixed signals)
  if (strongCount >= 1) {
    return {
      verdict: 'HOLD',
      reason: 'Mixed signals - wait for better setup',
      color: 'yellow'
    };
  }

  // Decent across the board with favorable risk = HOLD (borderline)
  if (technical === 'Decent' && riskMacro === 'Favorable') {
    return {
      verdict: 'HOLD',
      reason: 'Decent setup - consider with proper position sizing',
      color: 'yellow'
    };
  }

  // Default: AVOID
  return {
    verdict: 'AVOID',
    reason: 'Insufficient strength across categories',
    color: 'red'
  };
}

/**
 * Run Full Categorical Assessment
 *
 * Main entry point that runs all assessments and returns complete result
 *
 * @param {object} stockData - Stock data from backend
 * @param {object} spyData - SPY data
 * @param {object} vixData - VIX data
 * @param {object} fearGreedData - Fear & Greed Index data
 * @param {object} trendTemplate - Trend Template from pattern detection
 * @param {object} technicalResult - Technical scoring result (from scoringEngine)
 * @param {object} fundamentalResult - Fundamental scoring result
 * @param {string} ticker - Stock ticker symbol
 * @returns {object} Complete categorical assessment
 */
export function runCategoricalAssessment(
  stockData,
  spyData,
  vixData,
  fearGreedData,
  trendTemplate,
  technicalResult,
  fundamentalResult,
  ticker
) {
  // Get RSI from technical indicators or calculate
  const rsi = technicalResult?.indicators?.rsi || stockData?.technicals?.rsi14 || 50;

  // Run individual assessments
  const technical = assessTechnical(technicalResult, trendTemplate, rsi);
  const fundamental = assessFundamental(fundamentalResult || stockData?.fundamentals, ticker);
  const sentiment = assessSentiment(fearGreedData);
  const riskMacro = assessRiskMacro(vixData, spyData);

  // Determine overall verdict
  const verdict = determineVerdict(
    technical.assessment,
    fundamental.assessment,
    sentiment.assessment,
    riskMacro.assessment
  );

  return {
    technical,
    fundamental,
    sentiment,
    riskMacro,
    verdict,
    timestamp: new Date().toISOString()
  };
}
