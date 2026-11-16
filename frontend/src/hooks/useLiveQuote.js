/**
 * useLiveQuote - polls /api/quote/<ticker> for the Analyze header (Day 126).
 * Display only. Asks on load, then every minute while a session is open and the
 * tab is visible; every 5 minutes when the market is closed or the source is
 * failing; and straight away when the tab becomes visible again (a page left
 * open over the weekend wakes up at the open). A reply for a ticker that is no
 * longer on screen is dropped. Returns the described state (utils/liveQuote.js).
 */
import { useEffect, useState } from 'react';
import { fetchLiveQuote } from '../services/api';
import { acceptQuote, describeLiveQuote, nextPollDelayMs } from '../utils/liveQuote';

export default function useLiveQuote(ticker) {
  const [quote, setQuote] = useState(null);

  useEffect(() => {
    setQuote(null);
    if (!ticker) return undefined;
    let alive = true;
    let timer = null;
    let ctrl = null;

    const schedule = (state) => {
      if (!alive) return;
      clearTimeout(timer);
      timer = setTimeout(tick, nextPollDelayMs(state));
    };

    async function tick() {
      if (!alive) return;
      if (typeof document !== 'undefined' && document.hidden) return; // resumed by visibilitychange
      ctrl?.abort();
      ctrl = new AbortController();
      try {
        const resp = await fetchLiveQuote(ticker, ctrl.signal);
        if (!alive) return;
        const accepted = acceptQuote(resp, ticker);
        if (!accepted) { console.warn(`[STA] live quote: dropped a reply that is not for ${ticker}`); schedule('unavailable'); return; }
        setQuote(accepted);
        schedule(describeLiveQuote(accepted).state);
      } catch (e) {
        if (e && e.name === 'AbortError') return;
        console.warn(`[STA] live quote ${ticker}: ${e && e.message}`);
        schedule('unavailable');
      }
    }

    const onVisible = () => { if (!document.hidden) { clearTimeout(timer); tick(); } };
    document.addEventListener('visibilitychange', onVisible);
    tick();
    return () => {
      alive = false;
      clearTimeout(timer);
      ctrl?.abort();
      document.removeEventListener('visibilitychange', onVisible);
    };
  }, [ticker]);

  return describeLiveQuote(quote);
}
