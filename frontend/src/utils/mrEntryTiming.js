/**
 * When was / is the tested MR entry? (Day 123, redesign Step 5)
 *
 * The tested system bought at the open of the session after the signal
 * close. If that open has already happened (signal from a prior close and
 * the market opened today), buying now is not the tested entry, and the card
 * must say so instead of "buy at the next open".
 * Weekends are handled; market holidays are not (treated as sessions).
 *
 * @param {string} asOf - signal bar date, YYYY-MM-DD (completed close)
 * @param {Date} now - injectable for tests
 * @returns {{ state: 'next_open'|'tomorrow_open'|'passed', text: string }}
 */
export function mrEntryTiming(asOf, now = new Date()) {
  const parts = Object.fromEntries(
    new Intl.DateTimeFormat('en-CA', {
      timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit',
      hour: '2-digit', minute: '2-digit', hourCycle: 'h23', weekday: 'short',
    }).formatToParts(now).map((p) => [p.type, p.value])
  );
  const today = `${parts.year}-${parts.month}-${parts.day}`;
  const minutes = Number(parts.hour) * 60 + Number(parts.minute);
  const weekday = !['Sat', 'Sun'].includes(parts.weekday);
  const openedToday = weekday && minutes >= 9 * 60 + 30;

  if (asOf === today) {
    return { state: 'tomorrow_open', text: "at the next session's open (the signal is from today's close)" };
  }
  // Only claim "already passed" for a recent signal; an old asOf (stale
  // provider data, delisted ticker) gets the neutral wording. Holidays aside,
  // within 4 calendar days covers a Friday signal read on Monday or Tuesday.
  const ageDays = asOf ? (Date.parse(`${today}T00:00:00Z`) - Date.parse(`${asOf}T00:00:00Z`)) / 86400000 : null;
  if (asOf && asOf < today && openedToday && ageDays <= 4) {
    return {
      state: 'passed',
      text: `at the open after the ${asOf} close, which has already passed. Buying now isn't the tested entry`,
    };
  }
  return { state: 'next_open', text: "at the next session's open" };
}
