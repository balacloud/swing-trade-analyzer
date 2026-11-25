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
import { zoneSpan, formatZoneRange } from '../utils/keyLevels';
import useMissingInputWarning from '../hooks/useMissingInputWarning';
import { formatMoney, roundMoney } from '../utils/formatMoney';

const money = (v) => formatMoney(v);
const pct = (v) => `${v >= 0 ? '+' : '−'}${Math.abs(v).toFixed(1)}%`;

// Day 123: each non-ok state says why, in plain words (no silent hide).
const EMPTY_MESSAGES = {
  no_data: "Couldn't load support and resistance levels for this ticker, so there's no pullback plan. The rest of the page is unaffected.",
  no_support: "No support level below the last close, so there's no pullback plan to show.",
  no_price: "The last close didn't load, so the plan can't be placed against it.",
};

// Day 126: onSizePlan(entry, stop) opens the position-size calculator with this card's own
// Buy and Stop (rounded to cents, Golden Rule 63). Moved here from the removed Simple Checklist,
// where it only showed on a 9/9 TRADE. Shown whenever the plan has a buy and a stop; no verdict.
// Day 133: `status` = utils/planStatus.planStatusFromSr(srData, live), computed once in App.jsx. When the live price is already below the
// nearest support zone (or the stop), the plan is "void": the card says so in numbers, mutes the plan, and stops offering it for sizing.
// The plan's own numbers never move with the live price (Day 126 decision). A pre-market / after-hours price only adds a muted fact line.
export default function PullbackPlan({ srData, ticker, onSizePlan, status }) {
  const plan = calculateRiskReward(srData);
  const voided = status?.void === true;
  const factOnly = status?.factOnly === true;
  // Day 126 (Statement Audit): the card says "last close", so it measures from the last COMPLETED close. /api/sr's currentPrice is today's
  // live bar mid-session (it differed from the completed close for 5 of 7 audited tickers); prevBar is the last complete bar while today forms.
  const now = srData?.meta?.candle?.barComplete === false && Number.isFinite(srData?.meta?.prevBar?.close) ? srData.meta.prevBar.close : srData?.currentPrice;
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

  // The words are facts only (a print below a zone is not a confirmed break). They never start with "Price is" (audit_cards.py reads that as the Key Levels line).
  let liveNote = null;
  if ((voided || factOnly) && Number.isFinite(status?.livePrice)) {
    const lead = voided ? 'Last trade' : (status.basis === 'pre-market' ? 'Pre-market price' : 'After-hours price');
    const when = status.tradeTime ? ` (${status.tradeTime})` : '';
    const where = status.reason === 'below_support'
      ? ` is below the support zone (${formatZoneRange(status.zoneLow, status.zoneHigh)}).${status.belowStop && Number.isFinite(plan.stop) ? ` It is also below the stop (${money(plan.stop)}).` : ''}`
      : ` is below this plan's stop (${money(plan.stop)}).`;
    const closeText = Number.isFinite(status.close?.price) ? `${money(status.close.price)}${status.close.dateLabel ? `, ${status.close.dateLabel}` : ''}` : null;
    const buyAbove = Number.isFinite(plan.entry) && plan.entry > status.livePrice;
    const tail = voided && closeText ? ` This plan was set at the last close (${closeText})${buyAbove ? '; its Buy is above the price now' : ''}.` : '';
    liveNote = voided
      ? <div data-testid="plan-void" className="mb-3 p-3 rounded-lg text-sm bg-red-900/20 border border-red-500/40 text-red-200">{`${lead} ${money(status.livePrice)}${when}${where}${tail}`}</div>
      : <div data-testid="plan-live-fact" className="mb-3 text-xs text-gray-400">{`${lead} ${money(status.livePrice)}${when}${where}`}</div>;
  }

  if (state === 'no_atr') {
    return (
      <div className="mb-4 p-3 rounded-lg text-sm bg-gray-700/30 border border-gray-600 text-gray-300">
        {liveNote}
        <div>Buy near support at <b className="text-gray-100">{money(plan.entry)}</b>
          {plan.target != null && <>, target <b className="text-gray-100">{money(plan.target)}</b></>}.</div>
        <div className="mt-1 text-gray-400">ATR (the stock's normal daily move) didn't load, so the stop can't be placed, there's no reward:risk, and the trade can't be sized.</div>
      </div>
    );
  }

  const { entry, stop, target, risk, reward, rr } = plan;
  const entryVsNow = ((entry - now) / now) * 100;
  const stopPct = ((stop - entry) / entry) * 100;
  const targetPct = target != null ? ((target - entry) / entry) * 100 : null;

  // One price scale for the bar: lowest of stop, highest of target/now, 4% padding.
  // Day 133: when the plan is void, the live price joins the scale so the "now" tick shows where price fell to (below the stop/zone).
  const liveTick = voided && Number.isFinite(status?.livePrice) ? status.livePrice : null;
  const lo = Math.min(stop, now, liveTick ?? Infinity);
  const hi = Math.max(target ?? now, now, entry);
  const pad = (hi - lo) * 0.04 || 1;
  const pos = (v) => ((v - (lo - pad)) / ((hi + pad) - (lo - pad))) * 100;
  const pStop = pos(stop);
  const pEntry = pos(entry);
  const pTarget = target != null ? pos(target) : null;
  const pNow = pos(now);
  // Day 126: the nearest support / resistance zones, shaded on the same price scale (no new numbers).
  const zones = Array.isArray(srData?.meta?.zones) ? srData.meta.zones : [];
  const scaleLo = lo - pad, scaleHi = hi + pad;
  const supportBand = zoneSpan(zones.find((z) => z.nearest && z.side === 'support'), scaleLo, scaleHi);
  const resistanceBand = zoneSpan(zones.find((z) => z.nearest && z.side === 'resistance'), scaleLo, scaleHi);
  const atHigh = target == null && srData?.meta?.nearHigh52w === true;
  // Day 127: the wording follows the backend's entry basis (the Buy IS the last close when that close is inside the nearest support zone). A payload without
  // entryBasis (an old response) keeps the previous wording.
  const buyIsLastClose = srData?.meta?.entryBasis === 'last_close_inside_zone';
  const insideSupport = buyIsLastClose || (srData?.meta?.entryBasis == null && zones.some((z) => z.nearest && z.side === 'support' && z.insideZone === true));
  const nowNearEntry = Math.abs(pNow - pEntry) < 12;
  const pLive = liveTick != null ? pos(liveTick) : null;
  // keep the live label inside the bar: left-aligned near the left edge, right-aligned near the right edge
  const liveAlign = pLive == null ? '' : pLive < 18 ? '' : pLive > 82 ? '-translate-x-full' : '-translate-x-1/2';
  const muted = voided ? 'opacity-50' : '';

  return (
    <div className="mb-4">
      {liveNote}
      <div className="flex justify-between items-baseline gap-2 flex-wrap">
        <span className="font-semibold text-gray-200">
          Pullback plan <span className="font-normal text-gray-400 text-sm ml-1">{voided ? 'set at the last close' : buyIsLastClose ? 'price is already at support' : 'wait for a dip to support'}</span>
        </span>
        <span className={`font-mono text-lg text-gray-200 ${muted}`}>
          {rr != null ? `${rr.toFixed(1)} : 1` : '—'}
          <span className="text-xs text-gray-400 ml-1.5">reward : risk</span>
        </span>
      </div>

      {/* risk (red) = stop → buy, reward (green) = buy → target, "now" tick */}
      <div className={`relative mt-8 ${liveTick != null ? 'mb-12' : 'mb-7'}`}>
      <div className={`relative h-3 rounded-full bg-gray-700/50 ${muted}`}>
        {supportBand && <span aria-hidden="true" className="absolute -top-1 -bottom-1 rounded-sm bg-green-400/25 border-x border-green-400/50" style={{ left: `${supportBand.left}%`, width: `${supportBand.width}%` }} />}
        {resistanceBand && <span aria-hidden="true" className="absolute -top-1 -bottom-1 rounded-sm bg-red-400/25 border-x border-red-400/50" style={{ left: `${resistanceBand.left}%`, width: `${resistanceBand.width}%` }} />}
        <span className="absolute inset-y-0 rounded-l-full bg-red-500/40" style={{ left: `${pStop}%`, width: `${pEntry - pStop}%` }} />
        {pTarget != null && (
          <span
            className="absolute inset-y-0 rounded-r-full bg-green-500/40"
            style={{ left: `${pEntry}%`, width: `${pTarget - pEntry}%` }}
          />
        )}
        <span className="absolute -top-1.5 -bottom-1.5 w-0.5 bg-gray-400" style={{ left: `${pNow}%` }} />
        <span className="absolute bottom-4 -translate-x-1/2 whitespace-nowrap text-[11px] font-mono text-gray-400" style={{ left: `${pEntry}%` }}>
          <span className="font-sans font-semibold text-[10px] text-gray-500 mr-1">BUY</span>{money(entry)}
        </span>
        {!nowNearEntry && (
          <span className="absolute bottom-4 -translate-x-1/2 text-[10px] font-semibold text-gray-500" style={{ left: `${pNow}%` }}>CLOSE</span>
        )}
        <span className="absolute top-4 -translate-x-1/2 whitespace-nowrap text-[11px] font-mono text-gray-400" style={{ left: `${pStop}%` }}>{money(stop)}</span>
        {pTarget != null && (
          <span className="absolute top-4 -translate-x-1/2 whitespace-nowrap text-[11px] font-mono text-gray-400" style={{ left: `${pTarget}%` }}>
            {money(target)}
          </span>
        )}
      </div>
      {/* Day 133: the live-price tick and its label are an overlay AFTER the (muted) bar, so they stay bright and come LAST in the DOM: the audit's
          BUY/CLOSE/stop/target text pattern still reads in order. The label sits on its own row below the stop/target labels, so it cannot overlap
          them or the BUY label at 390 px. */}
      {pLive != null && (
        <div aria-hidden="true" className="absolute top-0 left-0 right-0 h-3 pointer-events-none">
          <span data-testid="plan-live-tick" className="absolute -top-1.5 -bottom-1.5 w-0.5 bg-amber-400" style={{ left: `${pLive}%` }} />
          <span data-testid="plan-live-label" className={`absolute top-9 whitespace-nowrap text-[10px] font-semibold text-amber-400 ${liveAlign}`} style={{ left: `${pLive}%` }}>{status.basis}</span>
        </div>
      )}
      </div>

      <div className={`grid grid-cols-3 gap-2 ${muted}`}>
        <div className="rounded-lg bg-gray-700/40 border border-gray-700 p-2.5">
          <div className="text-[10px] uppercase tracking-wider text-gray-500 font-semibold">Buy</div>
          <div data-testid="plan-buy-value" className="font-mono text-gray-100 mt-0.5">{money(entry)}</div>
          <div className="text-xs text-gray-400 mt-0.5">{buyIsLastClose ? 'the last close, inside the support zone' : insideSupport ? 'top of the support zone; price is inside it at the last close' : `support, ${Math.abs(entryVsNow).toFixed(1)}% ${entryVsNow <= 0 ? 'below' : 'above'} the last close`}</div>
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
              ? (atHigh ? 'no resistance above, the stock is near its 52-week high (within 3%)' : `no resistance within ${Math.round((srData?.meta?.proximityFilter?.resistancePct ?? 0.3) * 100)}% above`)
              : `${pct(targetPct)} from the buy · nearest resistance`}
          </div>
        </div>
      </div>

      <div className="text-sm text-gray-300 mt-3">
        {reward != null ? (
          <>Risk <b className="text-gray-100">{money(risk)}</b> to make <b className="text-gray-100">{money(reward)}</b> a share.</>
        ) : (
          <>Risk <b className="text-gray-100">{money(risk)}</b> a share. {atHigh ? 'The stock is near its 52-week high (within 3%) with no resistance above, so no target is shown and there is no reward:risk.' : 'No resistance target was found, so there is no reward:risk to show.'}</>
        )}
        {onSizePlan && voided && (
          <span data-testid="size-plan-off" className="ml-2 text-gray-500">Sizing is off: the Buy is above the live price.</span>
        )}
        {onSizePlan && !voided && (
          <button
            type="button"
            data-testid="size-this-plan"
            onClick={() => onSizePlan(roundMoney(entry), roundMoney(stop))}
            className="ml-2 text-blue-400 hover:text-blue-300 focus:outline-none focus-visible:underline"
          >
            Size this plan →
          </button>
        )}
      </div>

      <div className="mt-3 text-xs text-gray-400 bg-gray-700/30 rounded-lg px-3 py-2">
        Common rules of thumb, for reference: most traders want the reward to be at least <b>2×</b> the risk, and won't let a
        stop sit more than <b>7–8%</b> below their buy (O'Neil). This card doesn't judge; you do.
      </div>

      <details className="mt-3 text-xs text-gray-400">
        <summary className="cursor-pointer text-blue-400">How this setup was formed</summary>
        <div className="mt-2 space-y-2">
          <p><b className="text-gray-300">Levels:</b> support and resistance are zones where price turned before (swing highs and lows over the last year). The buy is the top of the nearest support zone (or, when the last close is already inside that zone, the last close itself) and the target is the bottom of the nearest resistance zone above the last close.</p>
          <p><b className="text-gray-300">Buy and stop:</b> buy at the nearest support (the last close when price is already inside the support zone), stop 2 ATR below the buy (ATR is how much the stock normally moves in a day). Buying a pullback near support is the canon low-risk entry (Minervini, Livermore's pivots); stops below support with an ATR buffer follow the Turtles.</p>
          <p><b className="text-gray-300">Zones on the bar:</b> the faint green band is the nearest support zone and the red band the nearest resistance zone, drawn on the same price scale. A zone outside the bar's range isn't drawn; its row below still lists it.</p>
          <p><b className="text-gray-300">At a high with no resistance above</b> there is no target. STA doesn't invent one.</p>
          <p><b className="text-gray-300">Why there is no "buy now" plan:</b> STA's momentum system failed every backtest and the forward test, so the card doesn't show it. The pullback plan hasn't been tested by STA either; it's shown because it matches how the one tested edge works (the Mean-Reversion signal buys dips inside an uptrend).</p>
        </div>
      </details>
    </div>
  );
}
