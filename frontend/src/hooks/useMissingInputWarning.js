/**
 * useMissingInputWarning — Day 123 (Analyze redesign engineering standard)
 *
 * Logs one console.warn when a card renders without an input it needs, so a
 * missing field is visible in the console as well as on the card. Fires once
 * per distinct ticker + reason set, not on every re-render.
 *
 * @param {string} card - card name, e.g. 'TradeSetup'
 * @param {string} ticker
 * @param {string[]} reasons - what is missing; empty array logs nothing
 */
import { useEffect } from 'react';

export default function useMissingInputWarning(card, ticker, reasons) {
  const message = reasons && reasons.length > 0
    ? `[STA][${card}] ${ticker || '?'}: ${reasons.join('; ')}`
    : null;

  useEffect(() => {
    if (message) console.warn(message);
  }, [message]);
}
