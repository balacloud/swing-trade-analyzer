/**
 * PullbackPlan — Trade Setup card body (Analyze Page Redesign Step 3, Day 123)
 *
 * One plan only: buy at the nearest support, stop 2×ATR below it, target the
 * nearest resistance. Plain arithmetic for the user's judgment — it gates
 * nothing and is not a tested system (decisions doc, Day 123; mockup v0.14).
 * No pass/fail colouring on the ratio: the engine has no reward:risk
 * threshold here, and adding one would disagree with the others on the page
 * (Golden Rule 59). The rules of thumb are shown as reference text only.
 */
import React from 'react';
import { calculateRiskReward } from '../utils/riskRewardCalc';
import useMissingInputWarning from '../hooks/useMissingInputWarning';

const money = (v) => (v == null || !Number.isFinite(v) ? '—' : `$${v.toFixed(2)}`);
const pct = (v) => `${v >= 0 ? '+' : '−'}${Math.abs(v).toFixed(1)}%`;

// Day 123: each non-ok state says why, in plain words (no silent hide).
const EMPTY_MESSAGES = {
  no_data: "Couldn't load support and resistance levels for this ticker, so there's no pullback plan. The rest of the page is unaffected.",
  no_support: "No support level below today's price, so there's no pullback plan to show.",
  no_price: "Today's price didn't load, so the plan can't be placed against it.",
};

export default function PullbackPlan({ srData, ticker }) {
  const plan = calculateRiskReward(srData);
  const now = srData?.currentPrice;
  const state = plan.state === 'no_data' || plan.state === 'no_support' ? plan.state
    : !Number.isFinite(now) ? 'no_price'
    : plan.state;

  useMissingInputWarning('TradeSetup', ticker, {
    no_data: ['/api/sr returned nothing'],
    no_price: ['srData.currentPrice missing'],
    no_atr: ['srData.meta.atr missing, stop not placed'],
  }[state] || []);

  if (EMPTY_MESSAGES[state]) {
    return (
      <div className="mb-4 p-3 rounded-lg text-sm bg-gray-700/30 border border-gray-600 text-gray-400">
        {EMPTY_MESSAGES[state]}
      </div>
    );
  }

  if (state === 'no_atr') {
    return (
      <div className="mb-4 p-3 rounded-lg text-sm bg-gray-700/30 border border-gray-600 text-gray-300">
        <div>Buy near support at <b className="text-gray-100">{money(plan.entry)}</b>
          {plan.target != null && <>, target <b className="text-gray-100">{money(plan.target)}</b>{plan.targetProjected ? ' (projected)' : ''}</>}.</div>
        <div className="mt-1 text-gray-400">ATR (the stock's normal daily move) didn't load, so the stop can't be placed and there's no reward:risk.</div>
      </div>
    );
  }

  const { entry, stop, target, risk, reward, rr, targetProjected } = plan;
  const entryVsNow = ((entry - now) / now) * 100;
  const stopPct = ((stop - entry) / entry) * 100;
  const targetPct = target != null ? ((target - entry) / entry) * 100 : null;

  // One price scale for the bar: lowest of stop, highest of target/now, 4% padding.
  const lo = Math.min(stop, now);
  const hi = Math.max(target ?? now, now, entry);
  const pad = (hi - lo) * 0.04 || 1;
  const pos = (v) => ((v - (lo - pad)) / ((hi + pad) - (lo - pad))) * 100;
  const pStop = pos(stop);
  const pEntry = pos(entry);
  const pTarget = target != null ? pos(target) : null;
  const pNow = pos(now);
  const nowNearEntry = Math.abs(pNow - pEntry) < 12;

  return (
    <div className="mb-4">
      <div className="flex justify-between items-baseline gap-2 flex-wrap">
        <span className="font-semibold text-gray-200">
          Pullback plan <span className="font-normal text-gray-400 text-sm ml-1">wait for a dip to support</span>
        </span>
        <span className="font-mono text-lg text-gray-200">
          {rr != null ? `${rr.toFixed(1)} : 1` : '—'}
          <span className="text-xs text-gray-400 ml-1.5">reward : risk</span>
        </span>
      </div>

      {/* risk (red) = stop → buy, reward (green) = buy → target, "now" tick */}
      <div className="relative h-3 mt-8 mb-7 rounded-full bg-gray-700/50">
        <span className="absolute inset-y-0 rounded-l-full bg-red-500/40" style={{ left: `${pStop}%`, width: `${pEntry - pStop}%` }} />
        {pTarget != null && (
          <span
            className={`absolute inset-y-0 rounded-r-full ${targetProjected ? 'border border-dashed border-green-400 bg-green-500/15' : 'bg-green-500/40'}`}
            style={{ left: `${pEntry}%`, width: `${pTarget - pEntry}%` }}
          />
        )}
        <span className="absolute -top-1.5 -bottom-1.5 w-0.5 bg-gray-400" style={{ left: `${pNow}%` }} />
        <span className="absolute bottom-4 -translate-x-1/2 whitespace-nowrap text-[11px] font-mono text-gray-400" style={{ left: `${pEntry}%` }}>
          <span className="font-sans font-semibold text-[10px] text-gray-500 mr-1">BUY</span>{money(entry)}
        </span>
        {!nowNearEntry && (
          <span className="absolute bottom-4 -translate-x-1/2 text-[10px] font-semibold text-gray-500" style={{ left: `${pNow}%` }}>NOW</span>
        )}
        <span className="absolute top-4 -translate-x-1/2 whitespace-nowrap text-[11px] font-mono text-gray-400" style={{ left: `${pStop}%` }}>{money(stop)}</span>
        {pTarget != null && (
          <span className="absolute top-4 -translate-x-1/2 whitespace-nowrap text-[11px] font-mono text-gray-400" style={{ left: `${pTarget}%` }}>
            {money(target)}{targetProjected ? '?' : ''}
          </span>
        )}
      </div>

      <div className="grid grid-cols-3 gap-2">
        <div className="rounded-lg bg-gray-700/40 border border-gray-700 p-2.5">
          <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold">Buy</div>
          <div className="font-mono text-gray-100 mt-0.5">{money(entry)}</div>
          <div className="text-xs text-gray-400 mt-0.5">support, {Math.abs(entryVsNow).toFixed(1)}% {entryVsNow <= 0 ? 'below' : 'above'} now</div>
        </div>
        <div className="rounded-lg bg-gray-700/40 border border-gray-700 p-2.5">
          <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold">Stop</div>
          <div className="font-mono text-red-400 mt-0.5">{money(stop)}</div>
          <div className="text-xs text-gray-400 mt-0.5">{pct(stopPct)} from the buy · {stop <= 0.01 ? 'floored at $0.01' : '2 ATR below'}</div>
        </div>
        <div className="rounded-lg bg-gray-700/40 border border-gray-700 p-2.5">
          <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold">Target</div>
          <div className="font-mono text-green-400 mt-0.5">{money(target)}</div>
          <div className="text-xs text-gray-400 mt-0.5">
            {target == null
              ? 'no resistance level found'
              : targetProjected
                ? 'projected, not a real level'
                : `${pct(targetPct)} from the buy · nearest resistance`}
          </div>
        </div>
      </div>

      <div className="text-sm text-gray-300 mt-3">
        {reward != null ? (
          <>Risk <b className="text-gray-100">{money(risk)}</b> to make <b className="text-gray-100">{money(reward)}</b> a share{targetProjected ? <>, <i>if</i> the projection is reached</> : ''}.</>
        ) : (
          <>Risk <b className="text-gray-100">{money(risk)}</b> a share. No resistance target was found, so there's no reward:risk to show.</>
        )}
      </div>

      <div className="mt-3 text-xs text-gray-400 bg-gray-700/30 rounded-lg px-3 py-2">
        Common rules of thumb, for reference: most traders want the reward to be at least <b>2×</b> the risk, and won't let a
        stop sit more than <b>7–8%</b> below their buy (O'Neil). This card doesn't judge; you do.
      </div>

      <details className="mt-3 text-xs text-gray-400">
        <summary className="cursor-pointer text-blue-400">How this setup was formed</summary>
        <div className="mt-2 space-y-2">
          <p><b className="text-gray-300">Levels:</b> support and resistance are the nearest real price levels where buyers or sellers showed up before. The target is the nearest resistance above today's price.</p>
          <p><b className="text-gray-300">Buy and stop:</b> buy at the nearest support, stop 2 ATR below it (ATR is how much the stock normally moves in a day). Buying a pullback near support is the canon low-risk entry (Minervini, Livermore's pivots); stops below support with an ATR buffer follow the Turtles.</p>
          <p><b className="text-gray-300">At an all-time high</b> there's no resistance above, so the target is a projection from recent moves, drawn dashed with a "?". It is not a price where sellers have actually appeared.</p>
          <p><b className="text-gray-300">Why there is no "buy now" plan:</b> STA's momentum system failed every backtest and the forward test, so the card doesn't show it. The pullback plan hasn't been tested by STA either; it's shown because it matches how the one tested edge works (the Mean-Reversion signal buys dips inside an uptrend).</p>
        </div>
      </details>
    </div>
  );
}
