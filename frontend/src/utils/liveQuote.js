/**
 * Live price for the Analyze header (Day 126). Display only: nothing here
 * feeds an indicator, a verdict or a stop. Plan: docs/claude/design/LIVE_QUOTE_PLAN_DAY126.md.
 *
 * `describeLiveQuote` turns the backend answer (GET /api/quote/<ticker>) into
 * the words and numbers the header shows. It never invents a price: with no
 * usable price it returns state 'unavailable' or 'closed' and no `price`.
 * Pure, never throws.
 */
const ET = 'America/New_York';

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);

/** The quote is only usable for the ticker on screen (a late reply for the previous ticker is dropped). */
export function acceptQuote(resp, ticker) {
  if (!resp || typeof resp !== 'object') return null;
  if (typeof resp.ticker !== 'string' || typeof ticker !== 'string') return null;
  return resp.ticker.toUpperCase() === ticker.toUpperCase() ? resp : null;
}

/** "2:51pm ET" from an ISO time, or null when it cannot be read. */
export function formatTradeTime(iso) {
  const d = new Date(iso);
  if (typeof iso !== 'string' || Number.isNaN(d.getTime())) return null;
  const t = new Intl.DateTimeFormat('en-US', { timeZone: ET, hour: 'numeric', minute: '2-digit', hour12: true }).format(d);
  return `${t.replace(/\s/g, '').toLowerCase()} ET`;
}

/** "Nov 13" (adds the year when it is not this year, New York time). */
export function formatCloseDate(dateStr, now = new Date()) {
  if (typeof dateStr !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) return null;
  const d = new Date(`${dateStr}T12:00:00`);
  if (Number.isNaN(d.getTime())) return null;
  const nowYear = new Intl.DateTimeFormat('en-US', { timeZone: ET, year: 'numeric' }).format(now);
  return d.toLocaleDateString('en-US', dateStr.slice(0, 4) === nowYear
    ? { month: 'short', day: 'numeric' }
    : { month: 'short', day: 'numeric', year: 'numeric' });
}

/**
 * @returns {{state:'none'|'live'|'recent'|'pre'|'post'|'closed'|'unavailable',
 *   price:?number, change:?number, changePct:?number, tradeTime:?string,
 *   statusText:string, lastClose:?{price:number,date:string,dateLabel:?string}, reason:?string}}
 */
export function describeLiveQuote(quote, now = new Date()) {
  const base = { price: null, change: null, changePct: null, tradeTime: null, ageText: null, lastClose: null, reason: null };
  if (!quote || typeof quote !== 'object') return { ...base, state: 'none', statusText: '' };

  const lc = quote.last_close;
  const lastClose = lc && isNum(lc.price) && lc.price > 0 && typeof lc.date === 'string'
    ? { price: lc.price, date: lc.date, dateLabel: formatCloseDate(lc.date, now) } : null;

  if (quote.available !== true) {
    const reason = typeof quote.reason === 'string' && quote.reason ? quote.reason : 'source down';
    return { ...base, state: 'unavailable', reason, statusText: `Live price unavailable (${reason})` };
  }
  if (quote.session === 'closed') {
    return { ...base, state: 'closed', lastClose, statusText: 'Market closed, last close shown' };
  }
  if (!isNum(quote.price) || quote.price <= 0) {
    return { ...base, state: 'unavailable', reason: 'bad price', statusText: 'Live price unavailable (bad price)' };
  }

  const tradeTime = formatTradeTime(quote.last_trade_at);
  if (!tradeTime) {
    // a price with no readable time is not shown as live
    return { ...base, state: 'unavailable', reason: 'no trade time', statusText: 'Live price unavailable (no trade time)' };
  }
  const age = isNum(quote.age_minutes) ? Math.max(0, quote.age_minutes) : null;
  let state = 'recent';
  let statusText;
  if (quote.session === 'pre') { state = 'pre'; statusText = 'Pre-market'; }
  else if (quote.session === 'post') { state = 'post'; statusText = 'After hours'; }
  else if (age !== null && age <= 2) { state = 'live'; statusText = 'Live'; }
  else { statusText = age === null ? 'Last trade time shown' : `Last trade ${Math.round(age)} min ago`; }

  return {
    state,
    price: quote.price,
    change: isNum(quote.change) ? quote.change : null,
    changePct: isNum(quote.change_pct) ? quote.change_pct : null,
    tradeTime,
    ageText: state === 'recent' && age !== null ? `${Math.round(age)} min ago` : null,
    lastClose,
    reason: null,
    statusText,
  };
}

/** Wait before the next ask: a minute while a session is open, five while closed or failing. */
export function nextPollDelayMs(state) {
  return state === 'live' || state === 'recent' || state === 'pre' || state === 'post' ? 60000 : 300000;
}

/** Signed percent for the header: "-4.18%" / "+1.20%" (true minus sign). */
export function signedPct(v) {
  return isNum(v) ? `${v >= 0 ? '+' : '−'}${Math.abs(v).toFixed(2)}%` : '';
}
