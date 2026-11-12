/**
 * Date label for the stock header price (Day 124, follow-up to Analyze Redesign Step 8).
 * The header price is the last bar's close in /api/stock (backend.py current_price),
 * and newestDate is that bar's date. The route doesn't drop today's unfinished bar,
 * so a bar dated today before the 16:30 ET cutoff (backend/market_time.py
 * MARKET_CLOSE_HOUR/MIN, matching the OHLCV cache expiry) is labelled intraday,
 * never "close".
 * Pure, never throws; a missing or bad date returns null (no label, no guess).
 */
const CUTOFF_MINUTES = 16 * 60 + 30; // 16:30 New York, same as market_time.py

function nyParts(now) {
  const f = new Intl.DateTimeFormat('en-US', {
    timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', hourCycle: 'h23',
  });
  const p = Object.fromEntries(f.formatToParts(now).map(x => [x.type, x.value]));
  return { date: `${p.year}-${p.month}-${p.day}`, year: p.year, minutes: Number(p.hour) * 60 + Number(p.minute) };
}

export function describePriceAsOf(newestDate, now = new Date()) {
  if (typeof newestDate !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(newestDate)) return null;
  const d = new Date(`${newestDate}T12:00:00`);
  if (Number.isNaN(d.getTime())) return null;
  const ny = nyParts(now);
  const sameYear = newestDate.slice(0, 4) === ny.year;
  const label = d.toLocaleDateString('en-US', sameYear
    ? { month: 'short', day: 'numeric' }
    : { month: 'short', day: 'numeric', year: 'numeric' });
  const forming = newestDate === ny.date && ny.minutes < CUTOFF_MINUTES;
  return forming ? `${label} · intraday, not a close` : `${label} close`;
}
