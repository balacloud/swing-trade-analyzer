/**
 * Categorical Assessment System for Swing Trade Analyzer
 * v4.5: Replaces 75-point numerical scoring with categorical assessments
 * v4.6: Perplexity research recommendations (Day 45)
 *       - F&G thresholds: Neutral zone 40-55 (Bug 0G narrowed from original 35-60)
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
 *
 * EQUAL-WEIGHT PRINCIPLE (Tier 1B, Day 69):
 * All 4 categories are computed independently — never optimize category weights.
 * DeMiguel et al. (2009): equal weights beat optimized weights out-of-sample.
 * 238 trades is insufficient to optimize 4+ weights without overfitting.
 * Verdict logic (Day 70 revision — see determineVerdict()): only Technical and
 * Fundamental are counted toward strongCount → BUY/HOLD/AVOID. Sentiment is
 * informational-only (backtest never validated a live sentiment signal).
 * Risk/Macro acts as a gate/cap on the verdict, not a counted vote.
 */

// Known ETF tickers - these don't have traditional fundamentals
const ETF_TICKERS = ['SPY', 'QQQ', 'IWM', 'DIA', 'VOO', 'VTI', 'VEA', 'VWO', 'VNQ',
                     'BND', 'AGG', 'GLD', 'SLV', 'USO', 'XLF', 'XLK', 'XLE', 'XLV',
                     'XLI', 'XLP', 'XLY', 'XLB', 'XLU', 'ARKK', 'ARKG', 'ARKW'];

// Day 125: getActionablePatterns / measured-move / VCP targets removed with the
// Pattern Detection card (their only caller). The pattern payload still feeds
// trendTemplate into the verdict via runCategoricalAssessment().

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
/**
 * The Strong rule's thresholds (Day 123). Single frontend definition, read by
 * assessTechnical() below and by deriveStrongCriteria() for the tiles.
 * Mirrored in backend/backtest/categorical_engine.py (parity-tested).
 */
export const STRONG_RULE = {
  minTrendChecks: 7,  // of 8 Trend Template criteria
  rsiMin: 50,
  rsiMax: 70,
  rsMin: 1.0          // rs52Week, stock growth ÷ S&P 500 growth over 52 weeks
};

export function assessTechnical(technicalData, trendTemplate, rsi) {
  const reasons = [];
  const data = {};

  // Get trend template pass count (API returns criteria_met, not criteria_passed)
  const passCount = trendTemplate?.criteria_met || trendTemplate?.criteria_passed || 0;
  const totalCriteria = trendTemplate?.total_criteria || 8;
  const hasTrendTemplate = trendTemplate !== null && trendTemplate !== undefined;
  data.trendTemplateScore = `${passCount}/${totalCriteria}`;
  data.trendTemplateAvailable = hasTrendTemplate;
  data.trendTemplatePassCount = passCount;  // Day 123: numeric, for the Strong tiles

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
  // Day 78 (Fable Remediation Task 3.3): do not fabricate RS=1.0 when the
  // value is missing. Silently substituting a neutral value let a stock
  // with no RS data qualify for "Strong" — an invisible lie (Golden Rule:
  // "Return null, not a plausible fake", Day 54). Missing RS now visibly
  // caps the assessment below Strong instead of silently passing.
  const rs52WeekRaw = technicalData?.rsData?.rs52Week;
  const rs52WeekAvailable = rs52WeekRaw !== null && rs52WeekRaw !== undefined;
  const rs52Week = rs52WeekAvailable ? rs52WeekRaw : null;
  data.rs52Week = rs52Week;
  data.rs52WeekAvailable = rs52WeekAvailable;

  // Determine assessment
  let assessment = 'Weak';

  // Strong: 7-8/8 trend template, RSI 50-70, good RS (RS must be available)
  // Day 123: literals moved to STRONG_RULE so deriveStrongCriteria() (the
  // Technical Read tiles) reads the same numbers. Values unchanged.
  if (passCount >= STRONG_RULE.minTrendChecks && rsiValue >= STRONG_RULE.rsiMin && rsiValue <= STRONG_RULE.rsiMax
      && rs52WeekAvailable && rs52Week >= STRONG_RULE.rsMin) {
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
    if (!rs52WeekAvailable) {
      reasons.push('RS data unavailable — Strong rating requires RS ≥ 1.0');
    } else if (rsiValue < 50) {
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

    // RS issues (guard: only evaluate if RS is available — Day 78)
    if (!rs52WeekAvailable) {
      reasons.push('RS data unavailable — Strong rating requires RS ≥ 1.0');
    } else if (rs52Week < 0.8) {
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

  // Strong: Greed but not extreme (55-80) - good for momentum trades
  // Bug 0G: Widened from 60-80 to 55-80 (narrowing neutral zone from 35-60 to 40-55)
  if (value >= 55 && value <= 80) {
    assessment = 'Strong';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Positive sentiment supports momentum entries');
    reasons.push('Good conditions for both pullback and momentum trades');
  }
  // Neutral (Optimistic): Mild greed (50-55) - supports momentum
  else if (value >= 50 && value < 55) {
    assessment = 'Neutral';
    subLabel = 'Optimistic';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Mild greed - sentiment slightly positive');
    reasons.push('Focus on stock-specific technicals');
  }
  // Neutral (Cautious): Mild fear (40-50) - neither extreme
  // Bug 0G: Narrowed from 35-50 to 40-50 (35-40 is now Weak)
  else if (value >= 40 && value < 50) {
    assessment = 'Neutral';
    subLabel = 'Cautious';
    reasons.push(`Fear & Greed: ${value} (${rating})`);
    reasons.push('Mild fear - sentiment cautious but not extreme');
    reasons.push('Pullback entries still viable if structure is bullish');
  }
  // Weak: Fear zone (<40) - pullback setups often fail
  // Bug 0G: Raised from <35 to <40 (moderate fear is now Weak, not Neutral)
  else if (value < 40) {
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
 * - Favorable: VIX < 20, SPY > 200 SMA (Bull regime)
 * - Neutral: VIX 20-30, SPY near 200 SMA
 * - Unfavorable: VIX > 30 OR SPY < 200 SMA (Bear regime)
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
  // Day 123: additive, display only. A missing SPY reading becomes `false`
  // above and so reads as "below its 200-day" (engine bug logged; verdict
  // unchanged). The Regime band uses this to say the data is missing.
  data.spyAvailable = spyData?.aboveSma200 != null;

  let assessment = 'Neutral';

  // If VIX unavailable, assess based on SPY alone
  if (vix === null) {
    reasons.push('VIX data unavailable');
    if (!spyAbove200EMA) {
      assessment = 'Unfavorable';
      reasons.push('SPY below 200 SMA (Bear regime)');
      reasons.push('Caution: Most pullback setups fail in bear markets');
    } else {
      assessment = 'Neutral';
      reasons.push('SPY above 200 SMA (Bull regime intact)');
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
      reasons.push('SPY below 200 SMA (Bear regime)');
      reasons.push('Caution: Most pullback setups fail in bear markets');
    }
  }
  // Favorable: Low VIX AND bull regime
  else if (vix < 20 && spyAbove200EMA) {
    assessment = 'Favorable';
    reasons.push(`VIX at ${vix.toFixed(1)} (Low volatility < 20)`);
    reasons.push('SPY above 200 SMA (Bull regime)');
    reasons.push('Favorable conditions for swing trades');
  }
  // Neutral: Elevated VIX but still bull regime
  else {
    assessment = 'Neutral';
    reasons.push(`VIX at ${vix.toFixed(1)} (Elevated 20-30)`);
    if (spyAbove200EMA) {
      reasons.push('SPY above 200 SMA (Bull regime intact)');
    }
    reasons.push('Proceed with caution');
  }

  // Day 57: Early bear regime cap — SPY above 200 SMA but 50 SMA declining >1%
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
  // Count strong assessments (T + F only — Sentiment is informational, Risk is gate)
  // Day 70: Removed sentiment from verdict. Backtest hardcoded sentiment='Neutral' (never validated).
  // Removing aligns live system with validated backtest. Sentiment still passed & displayed in UI.
  const assessments = [technical, fundamental];
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

  // Decent across the board = HOLD (not AVOID) as long as risk isn't Unfavorable
  // Neutral risk + all Decent is not ideal but not a rejection — wait for breakout
  if (technical === 'Decent' && (riskMacro === 'Favorable' || riskMacro === 'Neutral')) {
    return buildResult('HOLD', 'Decent setup - wait for a strong catalyst or breakout', 'yellow');
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
  // Day 123: additive. The `|| 50` above hides a missing RSI from the display;
  // record it so the Technical Read can say "RSI unavailable, engine assumed
  // 50" instead of showing 50 as real. Engine behavior unchanged (logged as a
  // known issue: the assumed 50 counts as a pass toward Strong).
  technical.data.rsiAvailable = Boolean(technicalResult?.indicators?.rsi || stockData?.technicals?.rsi14);
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

// ============================================================================
// Analyze Page Redesign — display-layer reads (Day 121, Phase 1 of
// docs/claude/design/ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md).
//
// Everything below is additive and display-only. Nothing above this line was
// changed, and none of these functions feeds determineVerdict(), the Simple
// Checklist's criteria, or the parity grid (test_verdict_parity.py /
// scripts/verdict_grid.mjs). They only re-describe results the assess*()
// functions have already computed.
// ============================================================================

/**
 * ADX "no confirmed trend" line. Mirrors the literal 20 already used in
 * determineVerdict() (the `adxValue < 20` HOLD branch) and
 * simplifiedScoring.js — not a new threshold. Kept as its own constant here
 * so that line inside determineVerdict() (parity-tested) doesn't have to be
 * edited to share it.
 */
export const ADX_NO_TREND_THRESHOLD = 20;

const TECHNICAL_READ_PLAIN = {
  Strong: 'This stock is in a healthy uptrend and beating the market — the classic "leader" pattern.',
  StrongUnconfirmed: 'The setup checks out on paper, but the move hasn\'t shown real conviction yet — could still take off, could also fizzle. Worth a tighter entry or a little patience.',
  Developing: 'Some of the uptrend boxes are checked, not all — this could turn into a leader, but it isn\'t one yet.',
  Weak: 'This doesn\'t look like a market leader right now — either the trend or the relative performance is lagging.',
  Unavailable: 'We couldn\'t run the trend read for this ticker — try again in a moment.'
};

/**
 * Technical Read (redesign item 12): assessTechnical()'s result relabeled
 * Strong / Developing / Weak, plus a 4th Unavailable state (item 1) and the
 * ADX<20 modifier (item 2). Never influenced by regime or fundamentals.
 *
 * @param {object} technicalAssessment - assessTechnical() return value
 * @param {object} adxData - { adx: number, ... } or null
 * @returns {object} { read, detail, adx, adxModifier, plainEnglish, color }
 */
export function deriveTechnicalRead(technicalAssessment, adxData = null) {
  const data = technicalAssessment?.data || {};
  const adxRaw = adxData?.adx;
  const adx = Number.isFinite(adxRaw) ? adxRaw : null;

  // Display-layer branch only: assessTechnical() reports a missing trend
  // template as 'Weak', which would read as a real Stage-4 call.
  if (!technicalAssessment || data.trendTemplateAvailable === false) {
    return {
      read: 'Unavailable',
      detail: 'pattern detection didn\'t return for this ticker',
      adx,
      adxModifier: null,
      plainEnglish: TECHNICAL_READ_PLAIN.Unavailable,
      color: 'gray'
    };
  }

  const read = technicalAssessment.assessment === 'Strong' ? 'Strong'
    : technicalAssessment.assessment === 'Decent' ? 'Developing'
    : 'Weak';

  const rsiText = Number.isFinite(data.rsi) ? data.rsi.toFixed(1) : 'n/a';
  const rsText = data.rs52WeekAvailable && Number.isFinite(data.rs52Week) ? data.rs52Week.toFixed(2) : 'n/a';
  const detail = `Trend Template ${data.trendTemplateScore}, RSI ${rsiText}, RS ${rsText}`;

  const unconfirmed = adx !== null && adx < ADX_NO_TREND_THRESHOLD;
  // Day 122 wording (decisions doc): "taking a breather", not "not yet confirmed".
  const adxModifier = unconfirmed ? `taking a breather: moving sideways for now (ADX ${adx.toFixed(1)})` : null;

  return {
    read,
    detail,
    adx,
    adxModifier,
    plainEnglish: read === 'Strong' && unconfirmed
      ? TECHNICAL_READ_PLAIN.StrongUnconfirmed
      : TECHNICAL_READ_PLAIN[read],
    color: read === 'Strong' ? 'green' : read === 'Developing' ? 'yellow' : 'red'
  };
}

/**
 * "Strong needs all three" tiles (Day 123). Splits the Strong rule in
 * assessTechnical() into its three parts using the same STRONG_RULE numbers
 * and the same engine values (data.rsi is the engine's RSI, including its
 * assumed 50 when RSI is missing). `consistent` is false if the tiles would
 * disagree with the engine's own Strong call — the card then warns rather
 * than show tiles that contradict the read.
 *
 * @param {object} technicalAssessment - assessTechnical() return value
 * @param {object} rsData - scoringEngine rsData ({ stock52wReturn, spy52wReturn }), optional
 * @returns {object} { state, trend, momentum, rs, allPass, consistent } or { state: 'unavailable', reason }
 */
export function deriveStrongCriteria(technicalAssessment, rsData = null) {
  const data = technicalAssessment?.data;
  if (!data) return { state: 'unavailable', reason: 'technical assessment missing' };

  const isNum = (v) => typeof v === 'number' && Number.isFinite(v);
  const count = isNum(data.trendTemplatePassCount) ? data.trendTemplatePassCount : 0;
  const trend = {
    available: data.trendTemplateAvailable !== false,
    count,
    total: 8,
    pass: count >= STRONG_RULE.minTrendChecks
  };

  const rsi = isNum(data.rsi) ? data.rsi : null;
  const momentum = {
    rsi,
    rsiAvailable: data.rsiAvailable !== false,
    pass: rsi !== null && rsi >= STRONG_RULE.rsiMin && rsi <= STRONG_RULE.rsiMax
  };

  const stockReturn = isNum(rsData?.stock52wReturn) ? rsData.stock52wReturn : null;
  const spyReturn = isNum(rsData?.spy52wReturn) ? rsData.spy52wReturn : null;
  const rs = {
    available: data.rs52WeekAvailable === true && isNum(data.rs52Week),
    ratio: isNum(data.rs52Week) ? data.rs52Week : null,
    stockReturn,
    spyReturn,
    pass: data.rs52WeekAvailable === true && isNum(data.rs52Week) && data.rs52Week >= STRONG_RULE.rsMin
  };

  const allPass = trend.pass && momentum.pass && rs.pass;
  return {
    state: 'ok',
    trend,
    momentum,
    rs,
    allPass,
    consistent: allPass === (technicalAssessment.assessment === 'Strong')
  };
}

/**
 * Red-flag triggers (redesign §5). Deliberately not the scoring bands:
 * revenue moved out to -10% (the 0% line is where TTM vs. annualized
 * quarterly data flip sign), D/E reused as-is, ROE changed to a fact
 * (negative) rather than a quality judgment. Negative EPS was checked and
 * declined (Day 119 plan, C4: epsGrowth is a growth rate, not a level).
 */
export const RED_FLAG_THRESHOLDS = {
  revenueGrowthMax: -10,  // flag when revenue growth <= -10% YoY
  debtToEquityMin: 2.0,   // flag when D/E > 2.0
  roeMax: 0               // flag when ROE < 0%
};

/**
 * Fundamentals red-flag screen (redesign item 5 / §5). Four states, never
 * collapsed (§5 display rule 1): a missing feed must not read as "no flags."
 * Consumes assessFundamental()'s output only.
 *
 * Limitation (Day 119 plan, C8): 'not_applicable' relies on
 * assessFundamental()'s hardcoded ETF_TICKERS list. An ETF outside it falls
 * through to the fundamentals path; the card must say so.
 *
 * @param {object} fundamentalResult - assessFundamental() return value
 * @returns {object} { state, flags: [{metric, value, text}], checked: [], missing: [] }
 */
export function screenFundamentalRedFlags(fundamentalResult) {
  const empty = { flags: [], checked: [], missing: [] };

  if (fundamentalResult?.assessment === 'N/A' || fundamentalResult?.data?.isETF) {
    return { state: 'not_applicable', ...empty };
  }
  if (!fundamentalResult || fundamentalResult.assessment === 'Unknown') {
    return { state: 'unavailable', ...empty };
  }

  const { roe, revenueGrowth, debtToEquity } = fundamentalResult.data || {};
  const flags = [];
  const checked = [];
  const missing = [];
  const isNum = (v) => v != null && Number.isFinite(v);

  if (isNum(revenueGrowth)) {
    checked.push('revenueGrowth');
    if (revenueGrowth <= RED_FLAG_THRESHOLDS.revenueGrowthMax) {
      flags.push({ metric: 'revenueGrowth', value: revenueGrowth, text: `Revenue declining ${revenueGrowth.toFixed(1)}% YoY` });
    }
  } else {
    missing.push('revenueGrowth');
  }

  if (isNum(debtToEquity)) {
    checked.push('debtToEquity');
    if (debtToEquity > RED_FLAG_THRESHOLDS.debtToEquityMin) {
      flags.push({ metric: 'debtToEquity', value: debtToEquity, text: `Debt/Equity ${debtToEquity.toFixed(2)} (above 2.0)` });
    }
  } else {
    missing.push('debtToEquity');
  }

  if (isNum(roe)) {
    checked.push('roe');
    if (roe < RED_FLAG_THRESHOLDS.roeMax) {
      flags.push({ metric: 'roe', value: roe, text: `Negative ROE ${roe.toFixed(1)}%` });
    }
  } else {
    missing.push('roe');
  }

  return { state: flags.length > 0 ? 'flags' : 'no_flags', flags, checked, missing };
}
