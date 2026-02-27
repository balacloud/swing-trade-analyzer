/**
 * Categorical Assessment System for Swing Trade Analyzer
 * v4.5: Replaces 75-point numerical scoring with categorical assessments
 * v4.6: Perplexity research recommendations (Day 45)
 *       - F&G thresholds: Expanded neutral zone (35-60) to eliminate cliff at 45
 *       - Structure > Sentiment hierarchy: Risk/Macro determines IF, Sentiment determines HOW
 *       - Entry preference guidance: Pullback vs Momentum based on sentiment
 * v4.6.2: ADX-based entry preference (Day 47)
 *       - ADX > 25: Momentum entry viable (strong trend)
 *       - ADX 20-25: Pullback preferred (moderate trend)
 *       - ADX < 20: Wait for trend (no trend/choppy)
 * v4.13: Holding Period Selector (Day 53)
 *       - Signal weighting by horizon (arXiv 2512.00280 validated)
 *       - Quick (5-10d): 70% Technical / 30% Fundamental
 *       - Standard (15-30d): 50% / 50%
 *       - Position (1-3mo): 30% Technical / 70% Fundamental
 *       - RSI thresholds by period INVALIDATED - only weighting changes
 *
 * Day 44: Initial implementation
 * Day 45: v4.6 updates based on Perplexity research
 * Day 47: v4.6.2 ADX-based entry preference (Recommendation #2)
 * Day 53: v4.13 Holding Period signal weighting
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

// v4.6.2 (Day 47): Minimum confidence threshold for actionable patterns
// Day 56: Lowered from 80 to 60 per Perplexity research + backtest validation
// Config C at 60%: 238 trades, 53.78% WR, PF 1.61, p=0.002
const PATTERN_ACTIONABILITY_THRESHOLD = 60;

/**
 * Get Actionable Patterns
 *
 * v4.6.2 (Day 47): Filter patterns to only show those above confidence threshold
 * Day 56: Lowered from 80% to 60% — backtest validated (Config C: PF 1.61)
 *
 * @param {object} patternsData - Raw patterns data from backend
 * @param {number} atr - ATR value for stop calculation
 * @returns {object} { actionablePatterns, summary }
 */
export function getActionablePatterns(patternsData, atr = null) {
  if (!patternsData || !patternsData.patterns) {
    return {
      actionablePatterns: [],
      summary: { count: 0, hasActionable: false }
    };
  }

  const actionablePatterns = [];

  // Check VCP
  const vcp = patternsData.patterns.vcp;
  if (vcp?.detected && vcp.confidence >= PATTERN_ACTIONABILITY_THRESHOLD) {
    const pivotPrice = vcp.pivot_price;
    const stopPrice = atr
      ? pivotPrice - (atr * 2)  // 2 ATR below pivot
      : pivotPrice * 0.93;     // 7% below pivot as fallback
    const targetPrice = pivotPrice * 1.15; // 15% above pivot

    // Day 47: Breakout quality assessment
    const breakout = vcp.breakout || {};
    const breakoutQuality = breakout.quality || 'Unknown';
    const volumeConfirmed = breakout.volume_confirmed || false;
    const isTradeable = breakout.tradeable || false;

    actionablePatterns.push({
      name: 'VCP',
      fullName: 'Volatility Contraction Pattern',
      confidence: vcp.confidence,
      status: vcp.status,
      triggerPrice: pivotPrice,
      stopPrice: Math.round(stopPrice * 100) / 100,
      targetPrice: Math.round(targetPrice * 100) / 100,
      riskReward: ((targetPrice - pivotPrice) / (pivotPrice - stopPrice)).toFixed(1),
      description: `${vcp.contractions_count} contractions with ${vcp.base_tightness_pct}% base tightness`,
      action: vcp.status === 'at_pivot' ? 'Ready to buy on breakout above pivot' :
              vcp.status === 'broken_out' ? 'Already broken out - use pullback entry' :
              'Wait for price to reach pivot zone',
      breakout: {
        quality: breakoutQuality,
        volumeConfirmed,
        volumeRatio: breakout.volume_ratio,
        isTradeable,
        reasons: breakout.reasons || []
      },
      raw: vcp
    });
  }

  // Check Cup & Handle (note: API transforms to camelCase)
  const cupHandle = patternsData.patterns.cupHandle;
  if (cupHandle?.detected && cupHandle.confidence >= PATTERN_ACTIONABILITY_THRESHOLD) {
    const pivotPrice = cupHandle.pivot_price;
    const stopPrice = atr
      ? pivotPrice - (atr * 2)
      : pivotPrice * 0.93;
    const targetPrice = pivotPrice * 1.20; // 20% above pivot (C&H targets are higher)

    // Day 47: Breakout quality assessment
    const breakout = cupHandle.breakout || {};
    const breakoutQuality = breakout.quality || 'Unknown';
    const volumeConfirmed = breakout.volume_confirmed || false;
    const isTradeable = breakout.tradeable || false;

    actionablePatterns.push({
      name: 'Cup & Handle',
      fullName: 'Cup and Handle Pattern',
      confidence: cupHandle.confidence,
      status: cupHandle.status,
      triggerPrice: pivotPrice,
      stopPrice: Math.round(stopPrice * 100) / 100,
      targetPrice: Math.round(targetPrice * 100) / 100,
      riskReward: ((targetPrice - pivotPrice) / (pivotPrice - stopPrice)).toFixed(1),
      description: `Cup depth ${cupHandle.cup?.depth_pct}%, ${cupHandle.handle?.days || 0} day handle`,
      action: cupHandle.status === 'complete' ? 'Ready to buy on handle breakout' :
              cupHandle.status === 'broken_out' ? 'Already broken out - use pullback entry' :
              'Cup forming - wait for handle',
      breakout: {
        quality: breakoutQuality,
        volumeConfirmed,
        volumeRatio: breakout.volume_ratio,
        isTradeable,
        reasons: breakout.reasons || []
      },
      raw: cupHandle
    });
  }

  // Check Flat Base (note: API transforms to camelCase)
  const flatBase = patternsData.patterns.flatBase;
  if (flatBase?.detected && flatBase.confidence >= PATTERN_ACTIONABILITY_THRESHOLD) {
    const pivotPrice = flatBase.pivot_price;
    const stopPrice = atr
      ? pivotPrice - (atr * 2)
      : pivotPrice * 0.93;
    const targetPrice = pivotPrice * 1.12; // 12% above pivot (flat base targets are modest)

    // Day 47: Breakout quality assessment
    const breakout = flatBase.breakout || {};
    const breakoutQuality = breakout.quality || 'Unknown';
    const volumeConfirmed = breakout.volume_confirmed || false;
    const isTradeable = breakout.tradeable || false;

    actionablePatterns.push({
      name: 'Flat Base',
      fullName: 'Flat Base Consolidation',
      confidence: flatBase.confidence,
      status: flatBase.status,
      triggerPrice: pivotPrice,
      stopPrice: Math.round(stopPrice * 100) / 100,
      targetPrice: Math.round(targetPrice * 100) / 100,
      riskReward: ((targetPrice - pivotPrice) / (pivotPrice - stopPrice)).toFixed(1),
      description: `${flatBase.base?.range_pct}% range, ${flatBase.prior_uptrend?.pct}% prior uptrend`,
      action: flatBase.status === 'forming' ? 'Ready to buy on breakout above range' :
              flatBase.status === 'broken_out' ? 'Already broken out - use pullback entry' :
              'Wait for base to complete',
      breakout: {
        quality: breakoutQuality,
        volumeConfirmed,
        volumeRatio: breakout.volume_ratio,
        isTradeable,
        reasons: breakout.reasons || []
      },
      raw: flatBase
    });
  }

  // Summary
  const bestPattern = actionablePatterns.length > 0
    ? actionablePatterns.reduce((best, p) => p.confidence > best.confidence ? p : best)
    : null;

  return {
    actionablePatterns,
    summary: {
      count: actionablePatterns.length,
      hasActionable: actionablePatterns.length > 0,
      bestPattern: bestPattern?.name || null,
      bestConfidence: bestPattern?.confidence || 0,
      threshold: PATTERN_ACTIONABILITY_THRESHOLD
    },
    // Also include patterns below threshold for transparency
    belowThreshold: [
      vcp?.detected && vcp.confidence < PATTERN_ACTIONABILITY_THRESHOLD ? {
        name: 'VCP',
        confidence: vcp.confidence,
        reason: `${vcp.confidence}% < ${PATTERN_ACTIONABILITY_THRESHOLD}% threshold`
      } : null,
      cupHandle?.detected && cupHandle.confidence < PATTERN_ACTIONABILITY_THRESHOLD ? {
        name: 'Cup & Handle',
        confidence: cupHandle.confidence,
        reason: `${cupHandle.confidence}% < ${PATTERN_ACTIONABILITY_THRESHOLD}% threshold`
      } : null,
      flatBase?.detected && flatBase.confidence < PATTERN_ACTIONABILITY_THRESHOLD ? {
        name: 'Flat Base',
        confidence: flatBase.confidence,
        reason: `${flatBase.confidence}% < ${PATTERN_ACTIONABILITY_THRESHOLD}% threshold`
      } : null
    ].filter(Boolean)
  };
}

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
  // Day 61: Sanitize NaN values — NaN passes !== null checks but breaks scoring
  const _sanitize = (v) => (v != null && !Number.isNaN(v) && Number.isFinite(v)) ? v : null;
  const roe = _sanitize(fundamentals.roe);
  const revenueGrowth = _sanitize(fundamentals.revenueGrowth);
  const debtToEquity = _sanitize(fundamentals.debtToEquity);
  const epsGrowth = _sanitize(fundamentals.epsGrowth);

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
 * v4.6 Update (Day 45): Expanded neutral zone to eliminate cliff at 45
 * Based on Perplexity research analysis - see docs/research/Perplexity_STA_Analysis_result_Feb5_2026
 *
 * Criteria (UPDATED):
 * - Strong: 60-80 (Greed but not extreme - good for momentum)
 * - Neutral (Optimistic): 50-60 (Mild greed, supports momentum)
 * - Neutral (Cautious): 35-50 (Mild fear, neither extreme)
 * - Weak: <35 (Fear - pullback setups risky)
 * - Weak: >80 (Extreme Greed - contrarian risk)
 *
 * Key Change: F&G 44.7 is now Neutral (was Weak), eliminating cliff at 45
 *
 * @param {object} fearGreedData - Fear & Greed Index data from backend
 * @returns {object} { assessment, reasons, data }
 */
export function assessSentiment(fearGreedData) {
  const reasons = [];
  const data = {};

  // Default to neutral if no data or if backend returned a fallback
  if (!fearGreedData || fearGreedData.error || fearGreedData.fallback) {
    return {
      assessment: 'Neutral',
      reasons: ['Fear & Greed data unavailable - defaulting to neutral'],
      data: { value: null, rating: 'Unavailable', source: 'default' },
      color: 'gray'
    };
  }

  const value = fearGreedData.value || 50;
  const rating = fearGreedData.rating || 'Neutral';

  data.value = value;
  data.rating = rating;
  data.source = fearGreedData.source || 'CNN Fear & Greed Index';

  let assessment = 'Neutral';
  let subLabel = ''; // For more nuanced messaging

  // Strong: Greed but not extreme (60-80) - good for momentum trades
  // Tightened from 55-75 to require more confident greed
  if (value >= 60 && value <= 80) {
    assessment = 'Strong';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Positive sentiment supports momentum entries');
    reasons.push('Good conditions for both pullback and momentum trades');
  }
  // Neutral (Optimistic): Mild greed (50-60) - supports momentum
  else if (value >= 50 && value < 60) {
    assessment = 'Neutral';
    subLabel = 'Optimistic';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Mild greed - sentiment slightly positive');
    reasons.push('Focus on stock-specific technicals');
  }
  // Neutral (Cautious): Mild fear (35-50) - neither extreme
  // KEY FIX: 44.7 is now Neutral, not Weak (eliminates cliff at 45)
  else if (value >= 35 && value < 50) {
    assessment = 'Neutral';
    subLabel = 'Cautious';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Mild fear - sentiment cautious but not extreme');
    reasons.push('Pullback entries still viable if structure is bullish');
  }
  // Weak: Fear zone (<35) - pullback setups often fail
  else if (value < 35) {
    assessment = 'Weak';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    if (value < 20) {
      reasons.push('Extreme fear - potential capitulation');
      reasons.push('Contrarian opportunity possible, but high risk');
    } else {
      reasons.push('Fear present - pullback setups risky');
      reasons.push('Consider waiting for sentiment improvement');
    }
  }
  // Weak: Extreme greed (>80) - contrarian risk
  else if (value > 80) {
    assessment = 'Weak';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Extreme greed - contrarian risk elevated');
    reasons.push('Caution: market may be overextended');
  }

  // Add sub-label to data for UI to optionally display
  data.subLabel = subLabel;

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

  const vix = vixData?.current != null ? vixData.current : null;
  const spyAbove200EMA = spyData?.aboveSma200 || false;
  // Day 57: Early bear detection — mirrors backtest categorical_engine.assess_risk_macro()
  const sma50Declining = spyData?.sma50Declining || false;

  data.vix = vix;
  data.vixRegime = vixData?.regime || 'unknown';
  data.spyAbove200EMA = spyAbove200EMA;
  data.sma50Declining = sma50Declining;
  data.vixUnavailable = vix === null;

  let assessment = 'Neutral';

  // If VIX unavailable, assess based on SPY alone
  if (vix === null) {
    reasons.push('VIX data unavailable');
    if (!spyAbove200EMA) {
      assessment = 'Unfavorable';
      reasons.push('SPY below 200 EMA (Bear regime)');
      reasons.push('Caution: Most pullback setups fail in bear markets');
    } else {
      assessment = 'Neutral';
      reasons.push('SPY above 200 EMA (Bull regime intact)');
      reasons.push('VIX unknown — proceed with caution');
    }
  }
  // Check for unfavorable conditions first (either condition triggers)
  else if (vix > 30 || !spyAbove200EMA) {
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

  // Day 57: Early bear regime cap — SPY above 200 EMA but 50 SMA declining >1%
  // Catches 2022-style slow deterioration before 200 SMA crosses
  // Mirrors backtest categorical_engine.py lines 219-221
  if (sma50Declining && assessment === 'Favorable') {
    assessment = 'Neutral';
    reasons.push('SPY 50 SMA declining (early bear signal — capped at Neutral)');
  }

  return {
    assessment,
    reasons,
    data,
    color: assessment === 'Favorable' ? 'green' : assessment === 'Neutral' ? 'yellow' : 'red'
  };
}

/**
 * Get signal weights based on holding period
 *
 * v4.13 (Day 53): Research-validated signal weighting by horizon
 * - arXiv 2512.00280: Short-horizon = technical signals, Long-horizon = fundamental
 * - This changes category IMPORTANCE in verdict, not individual thresholds
 * - RSI thresholds by period were INVALIDATED (Day 51) - we only change weights
 *
 * @param {string} holdingPeriod - 'quick', 'standard', or 'position'
 * @returns {object} { technical, fundamental }
 */
export function getSignalWeight(holdingPeriod) {
  switch (holdingPeriod) {
    case 'quick':    // 5-10 days - Technical dominates
      return { technical: 0.7, fundamental: 0.3 };
    case 'position': // 1-3 months - Fundamental dominates
      return { technical: 0.3, fundamental: 0.7 };
    case 'standard': // 15-30 days - Balanced (default)
    default:
      return { technical: 0.5, fundamental: 0.5 };
  }
}

/**
 * Determine Overall Verdict
 *
 * v4.6 Update (Day 45): Structure > Sentiment Hierarchy
 * Based on Elder's Triple Screen and Perplexity research:
 * - Structure (Risk/Macro) determines IF you trade
 * - Sentiment determines HOW you enter (pullback vs momentum)
 *
 * v4.6.2 Update (Day 47): ADX-based Entry Preference
 * - ADX > 25: Momentum entry viable (strong confirmed trend)
 * - ADX 20-25: Pullback preferred (trend developing)
 * - ADX < 20: Wait for trend (no trend/choppy market)
 *
 * v4.13 Update (Day 53): Holding Period Signal Weighting
 * - Quick: Technical 70% / Fundamental 30% (short-term = technicals matter more)
 * - Standard: 50/50 balanced
 * - Position: Technical 30% / Fundamental 70% (long-term = fundamentals matter more)
 * - Affects verdict when categories disagree (e.g., Strong tech + Weak fund)
 *
 * Logic:
 * - BUY: Strong Tech + Strong Fund + Favorable/Neutral Risk (ADX guides entry type)
 * - BUY: 2+ Strong with Favorable Risk (even if Sentiment is Weak)
 * - HOLD: Mixed signals or Unfavorable Risk override
 * - AVOID: Weak Technical (non-negotiable) OR Weak Fundamental with no Strong to offset
 *
 * Key Change: ADX now determines entry preference instead of sentiment alone.
 *             ADX < 20 suggests waiting for trend development.
 *             Holding period weights influence borderline decisions.
 *
 * @param {string} technical - Technical assessment
 * @param {string} fundamental - Fundamental assessment
 * @param {string} sentiment - Sentiment assessment
 * @param {string} riskMacro - Risk/Macro assessment
 * @param {object} adxData - ADX data { adx: number, trend_strength: string }
 * @param {string} holdingPeriod - 'quick', 'standard', or 'position'
 * @returns {object} { verdict, reason, color, entryPreference, adxAnalysis, holdingPeriod, signalWeights }
 */
export function determineVerdict(technical, fundamental, sentiment, riskMacro, adxData = null, holdingPeriod = 'standard') {
  // Count strong assessments (excluding Risk which uses different scale)
  const assessments = [technical, fundamental, sentiment];
  const strongCount = assessments.filter(a => a === 'Strong').length;

  // v4.13: Get signal weights for this holding period
  const signalWeights = getSignalWeight(holdingPeriod);

  // v4.6.2: ADX-based entry preference (replaces sentiment-based logic)
  // ADX measures trend strength - determines HOW to enter, not IF to enter
  const adxValue = adxData?.adx || null;
  // trendStrength available for future use: adxData?.trend_strength

  let entryPreference = 'Either';
  let adxAnalysis = null;

  if (adxValue !== null) {
    if (adxValue >= 25) {
      // Strong trend confirmed - momentum entries work well
      entryPreference = 'Momentum viable (ADX ' + adxValue + ' - strong trend)';
      adxAnalysis = {
        value: adxValue,
        interpretation: 'Strong trend confirmed',
        recommendation: 'Momentum entry viable - trend is established'
      };
    } else if (adxValue >= 20) {
      // Moderate/developing trend - prefer pullback entries
      entryPreference = 'Pullback preferred (ADX ' + adxValue + ' - moderate trend)';
      adxAnalysis = {
        value: adxValue,
        interpretation: 'Trend developing',
        recommendation: 'Wait for pullback to support - better risk/reward'
      };
    } else {
      // No trend/choppy - wait for trend development
      entryPreference = 'Wait for trend (ADX ' + adxValue + ' - choppy/no trend)';
      adxAnalysis = {
        value: adxValue,
        interpretation: 'No clear trend',
        recommendation: 'Avoid entries - wait for trend to develop (ADX > 20)'
      };
    }
  } else {
    // Fallback to sentiment-based if no ADX data
    if (sentiment === 'Weak') {
      entryPreference = 'Pullback preferred (fearful sentiment, no ADX data)';
    } else if (sentiment === 'Strong') {
      entryPreference = 'Momentum viable (positive sentiment, no ADX data)';
    }
  }

  // Helper to build return object with v4.13 fields
  const buildResult = (verdict, reason, color, includeEntry = true) => ({
    verdict,
    reason,
    color,
    entryPreference: includeEntry ? entryPreference : null,
    adxAnalysis,
    holdingPeriod,
    signalWeights,
  });

  // AVOID conditions (highest priority - non-negotiable)

  // 1. Technical Weak = AVOID (can't fight bad technicals for ANY holding period)
  if (technical === 'Weak') {
    return buildResult('AVOID', 'Weak technical setup', 'red', false);
  }

  // 2. Unfavorable Risk = HOLD at best (structure override)
  // This is the highest-level filter - bearish structure = don't trade
  if (riskMacro === 'Unfavorable') {
    return buildResult('HOLD', 'Unfavorable market conditions (regime caution)', 'yellow', false);
  }

  // 3. Weak Fundamental handling - v4.13: depends on holding period
  if (fundamental === 'Weak') {
    if (holdingPeriod === 'position') {
      // Position trades: weak fundamentals = AVOID (fundamentals are 70% weight)
      return buildResult('AVOID', 'Weak fundamentals - critical for position trades (70% weight)', 'red', false);
    } else if (holdingPeriod === 'quick' && technical === 'Strong') {
      // Quick trades: strong technicals can offset weak fundamentals (tech is 70% weight)
      // Don't AVOID - let it fall through to BUY/HOLD logic below
    } else if (strongCount === 0) {
      return buildResult('AVOID', 'Weak fundamentals with no offsetting strengths', 'red', false);
    }
  }

  // v4.6.2: ADX < 20 suggests caution - downgrade to HOLD if no strong trend
  // Even with good categories, choppy markets increase failure rate
  if (adxValue !== null && adxValue < 20) {
    // Strong categories but no trend - still tradeable but prefer to wait
    if (strongCount >= 2) {
      return buildResult(
        'HOLD',
        `${strongCount} strong categories but ADX ${adxValue} < 20 (no trend) - wait for trend development`,
        'yellow'
      );
    }
  }

  // BUY conditions (Structure > Sentiment applied here)

  // Strong Tech + Strong Fund = BUY regardless of Sentiment (Structure determines IF)
  // ADX guides entry type via entryPreference
  if (technical === 'Strong' && fundamental === 'Strong') {
    let reason = '2 strong categories (Technical + Fundamental)';
    if (sentiment === 'Weak') {
      reason += ' - structure bullish despite fearful sentiment';
    }
    if (adxValue !== null && adxValue >= 25) {
      reason += ` - ADX ${adxValue} confirms trend`;
    }
    return buildResult('BUY', reason, 'green');
  }

  // 2+ Strong with Favorable/Neutral risk = BUY
  if (strongCount >= 2 && (riskMacro === 'Favorable' || riskMacro === 'Neutral')) {
    return buildResult('BUY', `${strongCount} strong categories with ${riskMacro.toLowerCase()} conditions`, 'green');
  }

  // v4.13: Strong Tech + Weak Fund in Quick mode = BUY (tech dominates at 70%)
  if (holdingPeriod === 'quick' && technical === 'Strong' && fundamental === 'Weak' &&
      (riskMacro === 'Favorable' || riskMacro === 'Neutral')) {
    return buildResult('BUY', 'Strong technicals (70% weight for quick swing) offset weak fundamentals', 'green');
  }

  // Strong Tech + Decent Fund + Favorable Risk = BUY (upgraded from HOLD)
  // v4.13: Also BUY for quick swings even without Favorable risk (tech is 70%)
  if (technical === 'Strong' && fundamental === 'Decent') {
    if (riskMacro === 'Favorable') {
      return buildResult('BUY', 'Strong technicals with favorable macro conditions', 'green');
    }
    if (holdingPeriod === 'quick' && riskMacro === 'Neutral') {
      return buildResult('BUY', 'Strong technicals (70% weight for quick swing) with neutral conditions', 'green');
    }
  }

  // v4.13: Decent Tech + Strong Fund in Position mode = BUY (fund dominates at 70%)
  if (holdingPeriod === 'position' && technical === 'Decent' && fundamental === 'Strong' &&
      (riskMacro === 'Favorable' || riskMacro === 'Neutral')) {
    return buildResult('BUY', 'Strong fundamentals (70% weight for position trade) with decent technicals', 'green');
  }

  // HOLD conditions (default for mixed signals)
  if (strongCount >= 1) {
    let reason = 'Mixed signals - wait for better setup';
    // v4.13: Add context about which signal matters more for this period
    if (holdingPeriod === 'quick' && technical === 'Strong') {
      reason = 'Strong technicals but other signals mixed - consider with tight stop';
    } else if (holdingPeriod === 'position' && fundamental === 'Strong') {
      reason = 'Strong fundamentals but technicals need improvement for entry timing';
    }
    return buildResult('HOLD', reason, 'yellow');
  }

  // Decent across the board with favorable risk = HOLD (borderline)
  if (technical === 'Decent' && riskMacro === 'Favorable') {
    return buildResult('HOLD', 'Decent setup - consider with proper position sizing', 'yellow');
  }

  // Default: AVOID
  return buildResult('AVOID', 'Insufficient strength across categories', 'red', false);
}

/**
 * Run Full Categorical Assessment
 *
 * Main entry point that runs all assessments and returns complete result
 *
 * v4.6.2 (Day 47): Added ADX data parameter for entry preference logic
 * v4.13 (Day 53): Added holdingPeriod parameter for signal weighting
 *
 * @param {object} stockData - Stock data from backend
 * @param {object} spyData - SPY data
 * @param {object} vixData - VIX data
 * @param {object} fearGreedData - Fear & Greed Index data
 * @param {object} trendTemplate - Trend Template from pattern detection
 * @param {object} technicalResult - Technical scoring result (from scoringEngine)
 * @param {object} fundamentalResult - Fundamental scoring result
 * @param {string} ticker - Stock ticker symbol
 * @param {object} adxData - ADX data { adx: number, trend_strength: string } (optional)
 * @param {string} holdingPeriod - 'quick', 'standard', or 'position' (default: 'standard')
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
  ticker,
  adxData = null,
  holdingPeriod = 'standard'
) {
  // Get RSI from technical indicators or calculate
  const rsi = technicalResult?.indicators?.rsi || stockData?.technicals?.rsi14 || 50;

  // Run individual assessments (these don't change with holding period)
  const technical = assessTechnical(technicalResult, trendTemplate, rsi);
  const fundamental = assessFundamental(fundamentalResult || stockData?.fundamentals, ticker);
  const sentiment = assessSentiment(fearGreedData);
  const riskMacro = assessRiskMacro(vixData, spyData);

  // Determine overall verdict (v4.13: now includes holdingPeriod for signal weighting)
  const verdict = determineVerdict(
    technical.assessment,
    fundamental.assessment,
    sentiment.assessment,
    riskMacro.assessment,
    adxData,
    holdingPeriod
  );

  return {
    technical,
    fundamental,
    sentiment,
    riskMacro,
    verdict,
    adxData,  // Include raw ADX data in result
    holdingPeriod,  // v4.13: Include holding period in result
    timestamp: new Date().toISOString()
  };
}
