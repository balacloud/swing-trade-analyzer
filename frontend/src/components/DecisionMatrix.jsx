/**
 * Decision Matrix - Synthesis & Interpretation Layer
 * Day 53: Surfaces 10+ computed-but-hidden fields into a 3-step trader workflow
 *
 * Step 1: "Should I Trade This?" - Assessment synthesis with interpretations
 * Step 2: "When Should I Enter?" - Pattern + timing + ADX guidance
 * Step 3: "Does The Math Work?" - R:R comparison with contradiction resolution
 * Final: "What Should I Do?" - Contextual action items
 */

import React from 'react';
import { calculateRiskReward, hasViabilityContradiction } from '../utils/riskRewardCalc';

const ASSESSMENT_COLORS = {
  Strong: { bg: 'bg-green-900/40', border: 'border-green-600', text: 'text-green-400', badge: 'bg-green-600' },
  Decent: { bg: 'bg-yellow-900/40', border: 'border-yellow-600', text: 'text-yellow-400', badge: 'bg-yellow-600' },
  Weak:   { bg: 'bg-red-900/40', border: 'border-red-600', text: 'text-red-400', badge: 'bg-red-600' },
  Favorable: { bg: 'bg-green-900/40', border: 'border-green-600', text: 'text-green-400', badge: 'bg-green-600' },
  Neutral: { bg: 'bg-yellow-900/40', border: 'border-yellow-600', text: 'text-yellow-400', badge: 'bg-yellow-600' },
  Unfavorable: { bg: 'bg-red-900/40', border: 'border-red-600', text: 'text-red-400', badge: 'bg-red-600' },
  'N/A': { bg: 'bg-gray-800', border: 'border-gray-600', text: 'text-gray-400', badge: 'bg-gray-600' },
};

const HOLDING_LABELS = {
  quick: { name: 'Quick Swing', days: '5-10 days', techPct: 70, fundPct: 30 },
  standard: { name: 'Standard Swing', days: '15-30 days', techPct: 50, fundPct: 50 },
  position: { name: 'Position Trade', days: '1-3 months', techPct: 30, fundPct: 70 },
};

function formatCurrency(val) {
  if (val == null) return 'N/A';
  return '$' + Number(val).toFixed(2);
}

export default function DecisionMatrix({
  categoricalResult,
  analysisResult,
  srData,
  patternsData,
  holdingPeriod = 'standard',
  currentPrice,
}) {
  if (!categoricalResult) return null;

  const verdict = categoricalResult.verdict || {};
  const holdingConfig = HOLDING_LABELS[holdingPeriod] || HOLDING_LABELS.standard;

  // ─── R:R Calculations (Day 61: shared utility — single source of truth) ───
  const rr = calculateRiskReward(srData, currentPrice);
  const { pullbackRR, momentumRR, pullbackViable, momentumViable, anyViable, nearestSupport, target, atr, momentumStop } = rr;

  // Backend viability vs frontend R:R contradiction
  const hasContradiction = hasViabilityContradiction(srData, rr);

  return (
    <div className="space-y-1">
      {/* Header */}
      <div className="text-center mb-2">
        <h2 className="text-xl font-bold text-indigo-400">Decision Matrix</h2>
        <p className="text-xs text-gray-500">
          {holdingConfig.name} ({holdingConfig.days}) &middot; Tech {holdingConfig.techPct}% / Fund {holdingConfig.fundPct}%
        </p>
      </div>

      {/* ━━━ STEP 1: Should I Trade This? ━━━ */}
      <StepContainer number={1} title="Should I Trade This?" subtitle="Assessment Synthesis">
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-4">
          <AssessmentCard
            label="Technical"
            icon="📊"
            assessment={categoricalResult.technical?.assessment}
            reasons={categoricalResult.technical?.reasons}
            interpretation={analysisResult?.rsData?.interpretation}
            metrics={[
              { label: 'RS Rating', value: analysisResult?.rsData?.rsRating, suffix: '/99' },
              { label: 'RS Trend', value: analysisResult?.rsData?.rsTrend },
              { label: 'Above 200 SMA', value: categoricalResult.technical?.data?.priceAbove200SMA != null
                ? (categoricalResult.technical.data.priceAbove200SMA ? 'Yes' : 'No') : null },
            ]}
          />
          <AssessmentCard
            label="Fundamental"
            icon="💰"
            assessment={categoricalResult.fundamental?.assessment}
            reasons={categoricalResult.fundamental?.reasons}
            metrics={[
              { label: 'ROE', value: categoricalResult.fundamental?.data?.roe != null
                ? (categoricalResult.fundamental.data.roe * 100).toFixed(1) + '%' : null },
              { label: 'Rev Growth', value: categoricalResult.fundamental?.data?.revenueGrowth != null
                ? (categoricalResult.fundamental.data.revenueGrowth * 100).toFixed(1) + '%' : null },
              { label: 'D/E', value: categoricalResult.fundamental?.data?.debtToEquity?.toFixed(2) },
              { label: 'EPS Growth', value: categoricalResult.fundamental?.data?.epsGrowth != null
                ? (categoricalResult.fundamental.data.epsGrowth * 100).toFixed(1) + '%' : null },
            ]}
          />
          <AssessmentCard
            label="Sentiment"
            icon="🧠"
            assessment={categoricalResult.sentiment?.assessment}
            reasons={categoricalResult.sentiment?.reasons}
            interpretation={categoricalResult.sentiment?.data?.subLabel}
            metrics={[
              { label: 'F&G Index', value: categoricalResult.sentiment?.data?.value },
              { label: 'Mood', value: categoricalResult.sentiment?.data?.subLabel },
            ]}
          />
          <AssessmentCard
            label="Risk / Macro"
            icon="🛡️"
            assessment={categoricalResult.riskMacro?.assessment}
            reasons={categoricalResult.riskMacro?.reasons}
            metrics={[
              { label: 'VIX', value: categoricalResult.riskMacro?.data?.vix?.toFixed(1) },
              { label: 'SPY > 200 EMA', value: categoricalResult.riskMacro?.data?.spyAbove200EMA != null
                ? (categoricalResult.riskMacro.data.spyAbove200EMA ? 'Yes' : 'No') : null },
            ]}
          />
        </div>

        {/* Verdict Bar */}
        <div className={`rounded-lg p-4 ${
          verdict.verdict === 'BUY' ? 'bg-green-900/30 border border-green-700' :
          verdict.verdict === 'HOLD' ? 'bg-yellow-900/30 border border-yellow-700' :
          'bg-red-900/30 border border-red-700'
        }`}>
          <div className="flex justify-between items-center">
            <div>
              <span className={`text-lg font-bold ${
                verdict.verdict === 'BUY' ? 'text-green-400' :
                verdict.verdict === 'HOLD' ? 'text-yellow-400' : 'text-red-400'
              }`}>
                {verdict.verdict || 'N/A'}
              </span>
              <span className="text-gray-400 text-sm ml-3">{verdict.reason}</span>
            </div>
            {verdict.signalWeights && (
              <div className="text-xs text-gray-500 text-right">
                <div>Tech {Math.round(verdict.signalWeights.technical * 100)}% / Fund {Math.round(verdict.signalWeights.fundamental * 100)}%</div>
                <div className="text-indigo-400">{holdingConfig.name}</div>
              </div>
            )}
          </div>
          {verdict.entryPreference && (
            <div className="mt-2 text-xs text-gray-400 border-t border-gray-700 pt-2">
              Entry: {verdict.entryPreference}
            </div>
          )}
        </div>
      </StepContainer>

      {/* ━━━ STEP 2: When Should I Enter? ━━━ */}
      <StepContainer number={2} title="When Should I Enter?" subtitle="Pattern + Timing">
        {/* Trend Template */}
        {patternsData?.trendTemplate && (
          <div className="bg-gray-800/60 rounded-lg p-4 mb-3">
            <div className="flex justify-between items-center mb-2">
              <span className="text-sm font-medium text-blue-400">Trend Template</span>
              <span className={`text-sm font-bold ${
                patternsData.trendTemplate.criteria_met >= 7 ? 'text-green-400' :
                patternsData.trendTemplate.criteria_met >= 5 ? 'text-yellow-400' : 'text-red-400'
              }`}>
                {patternsData.trendTemplate.criteria_met}/8 criteria
              </span>
            </div>
            {patternsData.trendTemplate.in_stage2_uptrend && (
              <span className="text-xs bg-green-700 text-green-100 px-2 py-0.5 rounded mr-2">Stage 2 Uptrend</span>
            )}
            <div className="text-xs text-gray-500 mt-1">
              {patternsData.trendTemplate.criteria_met >= 7
                ? 'Strong institutional-quality setup meeting most Minervini criteria'
                : patternsData.trendTemplate.criteria_met >= 5
                ? 'Developing setup — some criteria met, monitor for improvement'
                : 'Weak template — multiple criteria failing, not ready for entry'}
            </div>
          </div>
        )}

        {/* Pattern Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-3">
          {patternsData?.patterns && Object.entries(patternsData.patterns).map(([key, pattern]) => (
            <PatternCard key={key} name={key} pattern={pattern} />
          ))}
          {(!patternsData?.patterns || Object.keys(patternsData.patterns).length === 0) && (
            <div className="col-span-3 text-center text-gray-500 py-4 text-sm">
              No patterns detected for this stock
            </div>
          )}
        </div>

        {/* ADX Trend Guidance */}
        {verdict.adxAnalysis && (
          <div className={`rounded-lg p-3 text-sm ${
            verdict.adxAnalysis.value >= 25 ? 'bg-green-900/20 border border-green-800' :
            verdict.adxAnalysis.value >= 20 ? 'bg-yellow-900/20 border border-yellow-800' :
            'bg-red-900/20 border border-red-800'
          }`}>
            <div className="flex justify-between items-center">
              <span className="font-medium text-gray-300">
                ADX {verdict.adxAnalysis.value} — {verdict.adxAnalysis.interpretation}
              </span>
              <span className={`text-xs px-2 py-0.5 rounded ${
                verdict.adxAnalysis.value >= 25 ? 'bg-green-700 text-green-100' :
                verdict.adxAnalysis.value >= 20 ? 'bg-yellow-700 text-yellow-100' :
                'bg-red-700 text-red-100'
              }`}>
                {verdict.adxAnalysis.value >= 25 ? 'TREND' :
                 verdict.adxAnalysis.value >= 20 ? 'DEVELOPING' : 'NO TREND'}
              </span>
            </div>
            <div className="text-xs text-gray-400 mt-1">
              {verdict.adxAnalysis.recommendation}
            </div>
          </div>
        )}
      </StepContainer>

      {/* ━━━ STEP 3: Does The Math Work? ━━━ */}
      <StepContainer number={3} title="Does The Math Work?" subtitle="Risk / Reward Analysis">
        {srData ? (
          <>
            {/* Support Quality */}
            <div className="bg-gray-800/60 rounded-lg p-4 mb-3">
              <div className="text-sm font-medium text-blue-400 mb-2">Support & Target</div>
              <div className="grid grid-cols-3 gap-4 text-sm">
                <div>
                  <div className="text-gray-500 text-xs">Nearest Support</div>
                  <div className="font-semibold text-white">
                    {nearestSupport ? formatCurrency(nearestSupport) : 'None found'}
                  </div>
                  {nearestSupport && currentPrice && (
                    <div className="text-xs text-gray-500">
                      {((currentPrice - nearestSupport) / currentPrice * 100).toFixed(1)}% below price
                    </div>
                  )}
                </div>
                <div>
                  <div className="text-gray-500 text-xs">Target</div>
                  <div className="font-semibold text-white">{formatCurrency(target)}</div>
                  {currentPrice && (
                    <div className="text-xs text-gray-500">
                      {((target - currentPrice) / currentPrice * 100).toFixed(1)}% upside
                    </div>
                  )}
                </div>
                <div>
                  <div className="text-gray-500 text-xs">ATR</div>
                  <div className="font-semibold text-white">{formatCurrency(atr)}</div>
                  {currentPrice && atr > 0 && (
                    <div className="text-xs text-gray-500">
                      {(atr / currentPrice * 100).toFixed(1)}% of price
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* R:R Comparison */}
            <div className="grid grid-cols-2 gap-3 mb-3">
              <RRCard
                title="Pullback Entry"
                entry={nearestSupport}
                stop={nearestSupport ? nearestSupport - atr * 2 : null}
                target={target}
                rr={pullbackRR}
                viable={pullbackViable}
                currentPrice={currentPrice}
              />
              <RRCard
                title="Momentum Entry"
                entry={currentPrice}
                stop={momentumStop || null}
                target={target}
                rr={momentumRR}
                viable={momentumViable}
                currentPrice={currentPrice}
              />
            </div>

            {/* Contradiction Resolution */}
            {hasContradiction && (
              <div className="bg-yellow-900/20 border border-yellow-700 rounded-lg p-3 mb-3">
                <div className="text-sm font-medium text-yellow-400 mb-1">
                  Why "structurally sound" but R:R fails
                </div>
                <div className="text-xs text-yellow-300/80">
                  Backend confirms support is within 10% (structural stop works).
                  However, the reward side is insufficient — target at {formatCurrency(target)} is too close
                  relative to the risk. {currentPrice && nearestSupport && currentPrice > nearestSupport * 1.08
                    ? 'Price is extended from support, increasing risk without proportional reward.'
                    : 'The target-to-stop ratio doesn\'t justify the trade at current levels.'}
                  {' '}Wait for a pullback closer to {formatCurrency(nearestSupport)} for better R:R.
                </div>
              </div>
            )}
          </>
        ) : (
          <div className="text-center text-gray-500 py-6 text-sm">
            No support/resistance data available for R:R analysis
          </div>
        )}
      </StepContainer>

      {/* ━━━ FINAL: What Should I Do? ━━━ */}
      <ActionSection
        verdict={verdict}
        anyViable={anyViable}
        pullbackViable={pullbackViable}
        momentumViable={momentumViable}
        pullbackRR={pullbackRR}
        momentumRR={momentumRR}
        nearestSupport={nearestSupport}
        target={target}
        currentPrice={currentPrice}
        holdingConfig={holdingConfig}
        hasContradiction={hasContradiction}
        patternsData={patternsData}
        categoricalResult={categoricalResult}
      />
    </div>
  );
}

// ─── Sub-Components ───

function StepContainer({ number, title, subtitle, children }) {
  return (
    <div className="bg-gray-800 rounded-lg p-5 relative">
      <div className="flex items-center gap-3 mb-4">
        <div className="w-8 h-8 rounded-full bg-indigo-600 flex items-center justify-center text-white font-bold text-sm flex-shrink-0">
          {number}
        </div>
        <div>
          <h3 className="text-base font-semibold text-white">{title}</h3>
          <p className="text-xs text-gray-500">{subtitle}</p>
        </div>
      </div>
      {children}
    </div>
  );
}

function AssessmentCard({ label, icon, assessment, reasons, interpretation, metrics }) {
  const colors = ASSESSMENT_COLORS[assessment] || ASSESSMENT_COLORS['N/A'];

  return (
    <div className={`rounded-lg p-3 ${colors.bg} border ${colors.border}`}>
      <div className="flex justify-between items-center mb-2">
        <span className="text-xs text-gray-400">{icon} {label}</span>
        <span className={`text-xs font-bold px-2 py-0.5 rounded ${colors.badge} text-white`}>
          {assessment || 'N/A'}
        </span>
      </div>

      {/* Key metric */}
      {metrics && metrics.filter(m => m.value != null).length > 0 && (
        <div className="space-y-1 mb-2">
          {metrics.filter(m => m.value != null).slice(0, 3).map((m, i) => (
            <div key={i} className="flex justify-between text-xs">
              <span className="text-gray-500">{m.label}</span>
              <span className={colors.text}>{m.value}{m.suffix || ''}</span>
            </div>
          ))}
        </div>
      )}

      {/* Interpretation */}
      {interpretation && (
        <div className="text-xs text-gray-400 italic border-t border-gray-700 pt-1 mt-1">
          {interpretation}
        </div>
      )}

      {/* Top reason */}
      {reasons && reasons.length > 0 && (
        <div className="text-[10px] text-gray-500 mt-1 truncate" title={reasons.join('; ')}>
          {reasons[0]}
        </div>
      )}
    </div>
  );
}

function PatternCard({ name, pattern }) {
  const detected = pattern?.detected;
  const confidence = pattern?.confidence || 0;
  const actionable = confidence >= 80;
  const displayName = name === 'vcp' ? 'VCP' :
                      name === 'cupAndHandle' ? 'Cup & Handle' :
                      name === 'flatBase' ? 'Flat Base' :
                      name.charAt(0).toUpperCase() + name.slice(1);

  const traderMeaning = name === 'vcp'
    ? 'Sellers exhausted — each pullback smaller. Lowest risk breakout entry.'
    : name === 'cupAndHandle'
    ? 'Institutional accumulation. Handle shakes out weak hands before real move.'
    : name === 'flatBase'
    ? 'Digesting gains in tight range. Compression before next leg up.'
    : '';

  return (
    <div className={`rounded-lg p-3 border ${
      detected
        ? actionable ? 'bg-green-900/30 border-green-700' : 'bg-yellow-900/20 border-yellow-700'
        : 'bg-gray-800/60 border-gray-700'
    }`}>
      <div className="flex justify-between items-center mb-1">
        <span className="text-sm font-medium text-gray-300">{displayName}</span>
        <span className={`text-xs px-1.5 py-0.5 rounded ${
          detected ? 'bg-green-700 text-green-100' : 'bg-gray-700 text-gray-400'
        }`}>
          {detected ? `${confidence}%` : 'Not found'}
        </span>
      </div>

      {detected && (
        <div className="text-xs text-gray-400 mt-1">
          {actionable
            ? 'Pattern ACTIONABLE — check trigger price'
            : 'Pattern forming — add to watchlist, check back in 2-3 days'}
        </div>
      )}

      {/* Confidence bar */}
      {detected && (
        <div className="mt-2 h-1 bg-gray-700 rounded-full overflow-hidden">
          <div
            className={`h-full rounded-full ${actionable ? 'bg-green-500' : 'bg-yellow-500'}`}
            style={{ width: `${Math.min(confidence, 100)}%` }}
          />
        </div>
      )}

      {/* Trader context */}
      {traderMeaning && (
        <div className="text-xs text-gray-500 mt-2 italic border-t border-gray-700 pt-1.5">
          {traderMeaning}
        </div>
      )}
    </div>
  );
}

function RRCard({ title, entry, stop, target, rr, viable }) {
  const risk = entry && stop ? Math.abs(entry - stop) : 0;
  const reward = entry && target ? target - entry : 0;

  return (
    <div className={`rounded-lg p-4 border ${
      viable ? 'bg-green-900/20 border-green-700' : 'bg-red-900/20 border-red-700'
    }`}>
      <div className="flex justify-between items-center mb-3">
        <span className="text-sm font-medium text-gray-300">{title}</span>
        <span className={`text-sm font-bold px-2 py-0.5 rounded ${
          viable ? 'bg-green-600 text-white' : 'bg-red-600 text-white'
        }`}>
          R:R {rr.toFixed(2)}
        </span>
      </div>

      <div className="space-y-1.5 text-xs">
        <div className="flex justify-between">
          <span className="text-gray-500">Entry</span>
          <span className="text-white">{entry ? formatCurrency(entry) : 'N/A'}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-gray-500">Stop</span>
          <span className="text-red-400">{stop ? formatCurrency(stop) : 'N/A'}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-gray-500">Target</span>
          <span className="text-green-400">{formatCurrency(target)}</span>
        </div>
        <div className="border-t border-gray-700 pt-1.5 mt-1.5">
          <div className="text-gray-400">
            Risking {formatCurrency(risk)} to make {formatCurrency(reward)}
          </div>
        </div>
      </div>
    </div>
  );
}

function ActionSection({
  verdict, anyViable, pullbackViable, momentumViable,
  pullbackRR, momentumRR, nearestSupport, target, currentPrice,
  holdingConfig, hasContradiction, patternsData, categoricalResult,
}) {
  const v = verdict.verdict;

  let bgColor = 'bg-gray-800';
  let borderColor = 'border-gray-700';
  let icon = '📋';
  let heading = 'Action Plan';

  if (v === 'BUY' && anyViable) {
    bgColor = 'bg-green-900/30';
    borderColor = 'border-green-700';
    icon = '✅';
    heading = 'Ready to Trade';
  } else if (v === 'BUY' && !anyViable) {
    bgColor = 'bg-yellow-900/30';
    borderColor = 'border-yellow-700';
    icon = '⏳';
    heading = 'Wait for Better Entry';
  } else if (v === 'HOLD') {
    bgColor = 'bg-yellow-900/30';
    borderColor = 'border-yellow-700';
    icon = '⏸️';
    heading = 'On Watch';
  } else if (v === 'AVOID') {
    bgColor = 'bg-red-900/30';
    borderColor = 'border-red-700';
    icon = '🚫';
    heading = 'Do Not Trade';
  }

  return (
    <div className={`rounded-lg p-5 border ${bgColor} ${borderColor}`}>
      <div className="flex items-center gap-2 mb-3">
        <span className="text-lg">{icon}</span>
        <h3 className="text-base font-bold text-white">{heading}</h3>
        <span className="text-xs text-gray-500 ml-auto">{holdingConfig.name}</span>
      </div>

      <div className="space-y-2 text-sm">
        {v === 'BUY' && anyViable && (
          <>
            {pullbackViable && (
              <ActionItem
                label="Pullback Entry"
                detail={`Enter near ${formatCurrency(nearestSupport)} with R:R ${pullbackRR.toFixed(2)}`}
                color="text-green-400"
              />
            )}
            {momentumViable && (
              <ActionItem
                label="Momentum Entry"
                detail={`Enter at ${formatCurrency(currentPrice)} with R:R ${momentumRR.toFixed(2)}`}
                color="text-blue-400"
              />
            )}
            <ActionItem
              label="Target"
              detail={formatCurrency(target)}
              color="text-gray-300"
            />
            {verdict.entryPreference && (
              <ActionItem
                label="ADX Guidance"
                detail={verdict.entryPreference}
                color="text-indigo-400"
              />
            )}
          </>
        )}

        {v === 'BUY' && !anyViable && (
          <>
            <ActionItem
              label="Wait for pullback"
              detail={nearestSupport
                ? `Price needs to come down to ${formatCurrency(nearestSupport)} area for acceptable R:R`
                : 'No clear support level — wait for one to form'}
              color="text-yellow-400"
            />
            {hasContradiction && (
              <ActionItem
                label="Why not now"
                detail="Support structure is sound but current price is too extended — reward doesn't justify risk"
                color="text-yellow-300"
              />
            )}
          </>
        )}

        {v === 'HOLD' && (
          <>
            <ActionItem
              label="What needs to change"
              detail={verdict.reason || 'Mixed signals — wait for clarity'}
              color="text-yellow-400"
            />
            {verdict.adxAnalysis && verdict.adxAnalysis.value < 20 && (
              <ActionItem
                label="Trend watch"
                detail={`ADX at ${verdict.adxAnalysis.value} — needs to rise above 20 for trend confirmation`}
                color="text-gray-400"
              />
            )}
            {patternsData?.trendTemplate && patternsData.trendTemplate.criteria_met < 7 && (
              <ActionItem
                label="Template progress"
                detail={`${patternsData.trendTemplate.criteria_met}/8 trend criteria met — needs 7+ for strong setup`}
                color="text-gray-400"
              />
            )}
          </>
        )}

        {v === 'AVOID' && (
          <>
            <ActionItem
              label="Why"
              detail={verdict.reason || 'Conditions not favorable'}
              color="text-red-400"
            />
            <ActionItem
              label="Re-evaluate when"
              detail={getReEvalTriggers(categoricalResult, verdict)}
              color="text-gray-400"
            />
          </>
        )}
      </div>
    </div>
  );
}

function ActionItem({ label, detail, color }) {
  return (
    <div className="flex gap-2">
      <span className={`font-medium ${color} flex-shrink-0 min-w-[120px]`}>{label}:</span>
      <span className="text-gray-300">{detail}</span>
    </div>
  );
}

function getReEvalTriggers(categoricalResult, verdict) {
  const triggers = [];

  if (categoricalResult?.technical?.assessment === 'Weak') {
    triggers.push('technical setup improves (RS, moving averages)');
  }
  if (categoricalResult?.fundamental?.assessment === 'Weak') {
    triggers.push('earnings or revenue growth accelerates');
  }
  if (categoricalResult?.riskMacro?.assessment === 'Unfavorable') {
    triggers.push('VIX drops below 20, SPY reclaims 200 EMA');
  }
  if (verdict.adxAnalysis && verdict.adxAnalysis.value < 20) {
    triggers.push('ADX rises above 20 (trend develops)');
  }

  return triggers.length > 0
    ? triggers.join('; ')
    : 'Fundamental or technical conditions improve significantly';
}
