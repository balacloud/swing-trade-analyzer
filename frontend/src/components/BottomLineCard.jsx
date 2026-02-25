/**
 * Bottom Line Card - v4.13 Holding Period Selector
 *
 * Consolidated "What's Good / What's Risky / Action Plan" card
 * that replaces the fragmented Actionable Recommendation card.
 *
 * Adapts messaging based on holding period signal weighting.
 * ADX regime determines RSI interpretation (unchanged from v4.6.2).
 *
 * Research basis:
 * - arXiv 2512.00280: Short-horizon = technical, Long-horizon = fundamental (~40 bps alpha)
 * - UX research: Consolidated views reduce cognitive load
 * - Day 51: RSI thresholds by period INVALIDATED, signal weighting VALIDATED
 */

import React from 'react';

const HOLDING_PERIODS = {
  quick: { label: '5-10 days', name: 'Quick Swing', techWeight: 0.7, fundWeight: 0.3 },
  standard: { label: '15-30 days', name: 'Standard Swing', techWeight: 0.5, fundWeight: 0.5 },
  position: { label: '1-3 months', name: 'Position Trade', techWeight: 0.3, fundWeight: 0.7 },
};

/**
 * Generate "What's Good" points from categorical assessment data
 */
function getWhatsGood(categoricalResult, srData, currentPrice, holdingPeriod) {
  const points = [];
  const tech = categoricalResult?.technical;
  const fund = categoricalResult?.fundamental;
  const sentiment = categoricalResult?.sentiment;
  const riskMacro = categoricalResult?.riskMacro;
  const adxData = categoricalResult?.adxData;

  // Technical positives
  if (tech?.assessment === 'Strong') {
    const ttScore = tech.data?.trendTemplateScore;
    if (ttScore) points.push(`Stage 2 Uptrend (${ttScore} TT) - ideal for swing trades`);
    const rs = tech.data?.rs52Week;
    if (rs && rs >= 1.1) points.push(`RS ${rs.toFixed(2)} - outperforming market`);
  } else if (tech?.assessment === 'Decent') {
    const ttScore = tech.data?.trendTemplateScore;
    if (ttScore) points.push(`Trend Template ${ttScore} - acceptable setup`);
  }

  // RSI in good range
  const rsi = tech?.data?.rsi;
  if (rsi && rsi >= 40 && rsi <= 65) {
    points.push(`RSI ${rsi.toFixed(1)} - in optimal entry range`);
  }

  // ADX confirmation
  if (adxData?.adx >= 25) {
    points.push(`ADX ${adxData.adx} - strong trend confirmed`);
  }

  // Fundamental positives
  if (fund?.assessment === 'Strong') {
    const reasons = fund.reasons || [];
    const strongReasons = reasons.filter(r => r.includes('Strong'));
    if (strongReasons.length > 0) {
      points.push(`Strong fundamentals (${strongReasons.map(r => r.split(' ')[0]).join(', ')})`);
    } else {
      points.push('Strong fundamentals across metrics');
    }
  } else if (fund?.assessment === 'Decent' && holdingPeriod === 'position') {
    points.push('Decent fundamentals - acceptable for position trade');
  }

  // Sentiment positives
  if (sentiment?.assessment === 'Strong') {
    points.push(`Positive sentiment (F&G: ${sentiment.data?.value}) supports momentum`);
  }

  // Risk/Macro positives
  if (riskMacro?.assessment === 'Favorable') {
    points.push(`Favorable market conditions (VIX ${riskMacro.data?.vix?.toFixed(1)}, SPY bullish)`);
  }

  // S&R positives
  if (srData?.meta?.tradeViability?.viable === 'YES') {
    const rr = srData.meta?.tradeViability?.riskRewardRatio;
    if (rr) points.push(`Trade setup viable with ${rr} R:R`);
  }

  return points;
}

/**
 * Generate "What's Risky" points from categorical assessment data
 */
function getWhatsRisky(categoricalResult, srData, currentPrice, holdingPeriod) {
  const points = [];
  const tech = categoricalResult?.technical;
  const fund = categoricalResult?.fundamental;
  const sentiment = categoricalResult?.sentiment;
  const riskMacro = categoricalResult?.riskMacro;
  const adxData = categoricalResult?.adxData;

  // RSI overbought + ADX context (v4.6.2 logic)
  const rsi = tech?.data?.rsi;
  const adx = adxData?.adx;
  if (rsi && rsi > 70) {
    if (adx && adx < 20) {
      points.push(`RSI ${rsi.toFixed(1)} + ADX ${adx} - overbought in WEAK trend = pullback likely`);
    } else if (adx && adx >= 25) {
      // In strong trend, overbought RSI is less risky but still worth noting
      if (rsi > 80) {
        points.push(`RSI ${rsi.toFixed(1)} extremely overbought - even strong trends pull back from here`);
      }
    } else {
      points.push(`RSI ${rsi.toFixed(1)} overbought - watch for reversal`);
    }
  }

  // RSI oversold
  if (rsi && rsi < 30) {
    points.push(`RSI ${rsi.toFixed(1)} deeply oversold - avoid catching falling knives`);
  }

  // Weak technicals
  if (tech?.assessment === 'Weak') {
    if (tech.data?.trendTemplateScore) {
      const ttParts = tech.data.trendTemplateScore.split('/');
      const ttNum = parseInt(ttParts[0]) || 0;
      if (ttNum >= 7) {
        points.push(`Trend Template: ${tech.data.trendTemplateScore} - in Stage 2 but weak RS/RSI drags technicals down`);
      } else {
        points.push(`Trend Template: ${tech.data.trendTemplateScore} - not in Stage 2 uptrend`);
      }
    }
    if (tech.data?.rs52Week && tech.data.rs52Week < 1.0) {
      points.push(`RS ${tech.data.rs52Week.toFixed(2)} - underperforming market`);
    }
  }

  // ADX no trend
  if (adx && adx < 20) {
    points.push(`ADX ${adx} - no clear trend (choppy market increases failure rate)`);
  }

  // Weak fundamentals (especially relevant for position trades)
  if (fund?.assessment === 'Weak') {
    const weakReasons = (fund.reasons || []).filter(r => r.includes('Weak'));
    if (weakReasons.length > 0) {
      points.push(`Weak fundamentals: ${weakReasons.map(r => r.split('(')[0].trim()).join(', ')}`);
    } else {
      points.push('Weak fundamentals - risky for longer holds');
    }
  }

  // Sentiment risk
  if (sentiment?.assessment === 'Weak') {
    const fgValue = sentiment.data?.value;
    if (fgValue && fgValue > 80) {
      points.push(`Extreme greed (F&G: ${fgValue}) - contrarian risk elevated`);
    } else if (fgValue && fgValue < 35) {
      points.push(`Fear in market (F&G: ${fgValue}) - pullback setups risky`);
    }
  }

  // Risk/Macro
  if (riskMacro?.assessment === 'Unfavorable') {
    const vix = riskMacro.data?.vix;
    if (vix && vix > 30) points.push(`High VIX (${vix.toFixed(1)}) - extreme volatility`);
    if (!riskMacro.data?.spyAbove200EMA) points.push('SPY below 200 EMA - bear regime');
  }

  // Extended from support (use highest support = nearest to price)
  if (srData?.support?.length > 0 && currentPrice) {
    const nearestSupport = Math.max(...srData.support);
    const pctFromSupport = ((currentPrice - nearestSupport) / nearestSupport) * 100;
    if (pctFromSupport > 15) {
      points.push(`${pctFromSupport.toFixed(1)}% above nearest support - extended entry`);
    }
  }

  return points;
}

/**
 * Generate action plan based on verdict + holding period
 */
function getActionPlan(categoricalResult, srData, currentPrice, holdingPeriod) {
  const verdict = categoricalResult?.verdict?.verdict;
  const nearestSupport = srData?.support?.length > 0 ? Math.max(...srData.support) : null;
  const viability = srData?.meta?.tradeViability;
  const adx = categoricalResult?.adxData?.adx;
  const steps = [];

  if (verdict === 'BUY') {
    if (viability?.viable === 'YES') {
      // Day 59 fix: Use R:R viability to recommend entry type (not just ADX)
      const entryLabel = getEntryTypeLabel(categoricalResult, srData, currentPrice);
      if (entryLabel === 'MOMENTUM ENTRY') {
        steps.push(`Momentum entry viable at current price ($${currentPrice?.toFixed(2)})`);
      } else {
        steps.push(`Consider pullback entry near $${nearestSupport?.toFixed(2) || 'support'} for better R:R`);
      }
      if (viability.suggestedStop) {
        steps.push(`Stop: $${parseFloat(viability.suggestedStop).toFixed(2)}`);
      }
      if (viability.suggestedTarget) {
        steps.push(`Target: $${parseFloat(viability.suggestedTarget).toFixed(2)}`);
      }
      if (viability.riskRewardRatio) {
        steps.push(`R:R = ${viability.riskRewardRatio}`);
      }
    } else if (nearestSupport) {
      const pctBelow = ((currentPrice - nearestSupport) / currentPrice * 100).toFixed(1);
      steps.push(`Set alert at $${nearestSupport.toFixed(2)} (${pctBelow}% below)`);
      steps.push('Entry at support offers better R:R');
      if (viability?.suggestedStop) steps.push(`Stop: $${parseFloat(viability.suggestedStop).toFixed(2)}`);
    }
  } else if (verdict === 'HOLD') {
    if (nearestSupport) {
      steps.push(`Set alert at $${nearestSupport.toFixed(2)} for pullback entry`);
    }
    steps.push('Wait for improving technicals or sentiment');
    if (holdingPeriod === 'position') {
      steps.push('Monitor quarterly earnings for fundamental confirmation');
    }
  } else {
    // AVOID
    steps.push('Look for stocks with stronger setup');
    if (categoricalResult?.technical?.assessment === 'Weak') {
      const ttScore = categoricalResult?.technical?.data?.trendTemplateScore;
      const ttNum = ttScore ? parseInt(ttScore.split('/')[0]) || 0 : 0;
      if (ttNum >= 7) {
        steps.push('In Stage 2 but RS/RSI weak - wait for relative strength to improve');
      } else {
        steps.push('Wait for Stage 2 uptrend before considering');
      }
    }
    if (categoricalResult?.riskMacro?.assessment === 'Unfavorable') {
      steps.push('Market conditions need to improve first');
    }
  }

  return steps;
}

/**
 * Get the weighted verdict label and explanation
 */
function getWeightedVerdictInfo(categoricalResult, holdingPeriod) {
  const tech = categoricalResult?.technical?.assessment;
  const fund = categoricalResult?.fundamental?.assessment;

  // Determine how weighting affected the verdict
  let weightNote = null;
  if (holdingPeriod === 'quick' && tech === 'Strong' && fund === 'Weak') {
    weightNote = 'Technical strength emphasized for short-term trade';
  } else if (holdingPeriod === 'position' && fund === 'Strong' && tech === 'Weak') {
    weightNote = 'Strong fundamentals matter most for position trades, but weak technicals still risky';
  } else if (holdingPeriod === 'position' && fund === 'Strong' && tech === 'Decent') {
    weightNote = 'Strong fundamentals weighted heavily for position trade horizon';
  } else if (holdingPeriod === 'quick' && tech === 'Weak') {
    weightNote = 'Weak technicals are non-negotiable for short-term trades';
  }

  return { weightNote };
}

/**
 * Determine entry type label for Bottom Line card header.
 * Uses R:R viability from S&R data (same math as Trade Setup card).
 * Day 59 fix: Previously used ADX >= 30 which contradicted Trade Setup's
 * R:R-based preference. Now uses actual R:R viability — if pullback R:R
 * is better, says PULLBACK even when ADX is high.
 */
function getEntryTypeLabel(categoricalResult, srData, currentPrice) {
  const nearestSupport = srData?.support?.length > 0 ? Math.max(...srData.support) : null;
  const atr = srData?.meta?.atr || 0;
  const target = srData?.suggestedTarget || (currentPrice ? currentPrice * 1.10 : 0);

  if (nearestSupport && currentPrice && atr > 0) {
    // Calculate R:R for both entry types (mirrors Trade Setup card logic in App.jsx)
    const pullbackEntry = nearestSupport;
    const pullbackStop = pullbackEntry - (atr * 2);
    const pullbackRisk = pullbackEntry - pullbackStop;
    const pullbackReward = target - pullbackEntry;
    const pullbackRR = pullbackRisk > 0 ? pullbackReward / pullbackRisk : 0;

    const momentumStop = nearestSupport - (atr * 1.5);
    const momentumRisk = currentPrice - momentumStop;
    const momentumReward = target - currentPrice;
    const momentumRR = momentumRisk > 0 ? momentumReward / momentumRisk : 0;

    const pullbackViable = pullbackRR >= 1.0;
    const momentumViable = momentumRR >= 1.0;

    // Prefer whichever entry type has better R:R
    if (pullbackViable && momentumViable) {
      return pullbackRR > momentumRR ? 'PULLBACK ENTRY' : 'MOMENTUM ENTRY';
    } else if (pullbackViable) {
      return 'PULLBACK ENTRY';
    } else if (momentumViable) {
      return 'MOMENTUM ENTRY';
    }
  }

  // Fallback to ADX-based entry preference from categorical assessment
  const entryPref = categoricalResult?.verdict?.entryPreference || '';
  if (entryPref.includes('Momentum')) return 'MOMENTUM ENTRY';
  if (entryPref.includes('Pullback')) return 'PULLBACK ENTRY';
  return 'PULLBACK ENTRY';  // Default conservative
}

/**
 * Get verdict display styling
 */
function getVerdictStyle(verdict) {
  switch (verdict) {
    case 'BUY':
      return {
        bg: 'bg-gradient-to-r from-green-600 to-emerald-600',
        border: 'border-green-400',
        text: 'text-white',
        label: 'READY',
        icon: 'checkmark',
      };
    case 'HOLD':
      return {
        bg: 'bg-gradient-to-r from-amber-600 to-yellow-600',
        border: 'border-amber-400',
        text: 'text-white',
        label: 'WATCHLIST',
        icon: 'eye',
      };
    case 'AVOID':
      return {
        bg: 'bg-gradient-to-r from-red-700 to-rose-700',
        border: 'border-red-500',
        text: 'text-white',
        label: 'PASS',
        icon: 'x',
      };
    default:
      return {
        bg: 'bg-gray-700',
        border: 'border-gray-600',
        text: 'text-gray-300',
        label: 'N/A',
        icon: 'question',
      };
  }
}

/**
 * BottomLineCard Component
 */
export default function BottomLineCard({
  categoricalResult,
  srData,
  currentPrice,
  holdingPeriod = 'standard',
}) {
  if (!categoricalResult) return null;

  const verdict = categoricalResult.verdict?.verdict;
  const verdictReason = categoricalResult.verdict?.reason;
  const periodConfig = HOLDING_PERIODS[holdingPeriod];
  const style = getVerdictStyle(verdict);
  const { weightNote } = getWeightedVerdictInfo(categoricalResult, holdingPeriod);

  const whatsGood = getWhatsGood(categoricalResult, srData, currentPrice, holdingPeriod);
  const whatsRisky = getWhatsRisky(categoricalResult, srData, currentPrice, holdingPeriod);
  const actionPlan = getActionPlan(categoricalResult, srData, currentPrice, holdingPeriod);

  // Signal weight indicator
  const techPct = Math.round(periodConfig.techWeight * 100);
  const fundPct = Math.round(periodConfig.fundWeight * 100);

  return (
    <div className={`rounded-xl shadow-lg border-2 ${style.bg} ${style.border} overflow-hidden`}>
      {/* Header */}
      <div className="px-5 pt-4 pb-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <span className="text-3xl">
              {verdict === 'BUY' ? '\u{1F3AF}' : verdict === 'HOLD' ? '\u{1F4CB}' : '\u{1F6AB}'}
            </span>
            <div>
              <div className={`text-xl font-bold ${style.text}`}>
                {style.label} - {verdict === 'BUY' ? getEntryTypeLabel(categoricalResult, srData, currentPrice) :
                 verdict === 'HOLD' ? 'WAIT FOR PULLBACK' : 'SKIP THIS ONE'}
              </div>
              <div className={`text-sm ${style.text} opacity-80`}>
                for {periodConfig.name} ({periodConfig.label})
              </div>
            </div>
          </div>
          {/* Signal weight badge */}
          <div className="text-right">
            <div className="text-xs text-white/60 uppercase tracking-wide">Signal Weight</div>
            <div className="flex gap-1 mt-1">
              <span className="px-2 py-0.5 rounded text-xs font-medium bg-blue-500/40 text-blue-100">
                T:{techPct}%
              </span>
              <span className="px-2 py-0.5 rounded text-xs font-medium bg-purple-500/40 text-purple-100">
                F:{fundPct}%
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Content sections */}
      <div className="bg-black/20 px-5 py-4 space-y-4">
        {/* Weight note */}
        {weightNote && (
          <div className="text-xs text-white/60 italic bg-white/5 rounded px-3 py-2">
            {weightNote}
          </div>
        )}

        {/* What's Good */}
        {whatsGood.length > 0 && (
          <div>
            <div className="text-xs font-semibold text-green-300 uppercase tracking-wider mb-2">
              What's Good
            </div>
            <ul className="space-y-1">
              {whatsGood.map((point, i) => (
                <li key={i} className="text-sm text-white/90 flex items-start gap-2">
                  <span className="text-green-400 mt-0.5 flex-shrink-0">+</span>
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* What's Risky */}
        {whatsRisky.length > 0 && (
          <div>
            <div className="text-xs font-semibold text-red-300 uppercase tracking-wider mb-2">
              What's Risky
            </div>
            <ul className="space-y-1">
              {whatsRisky.map((point, i) => (
                <li key={i} className="text-sm text-white/90 flex items-start gap-2">
                  <span className="text-red-400 mt-0.5 flex-shrink-0">-</span>
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Action Plan */}
        {actionPlan.length > 0 && (
          <div>
            <div className="text-xs font-semibold text-blue-300 uppercase tracking-wider mb-2">
              Action Plan
            </div>
            <ol className="space-y-1">
              {actionPlan.map((step, i) => (
                <li key={i} className="text-sm text-white/90 flex items-start gap-2">
                  <span className="text-blue-400 font-mono text-xs mt-0.5 flex-shrink-0">{i + 1}.</span>
                  <span>{step}</span>
                </li>
              ))}
            </ol>
          </div>
        )}

        {/* Verdict reason */}
        {verdictReason && (
          <div className="text-xs text-white/50 border-t border-white/10 pt-2 mt-2">
            {verdictReason}
          </div>
        )}
      </div>
    </div>
  );
}

export { HOLDING_PERIODS };
