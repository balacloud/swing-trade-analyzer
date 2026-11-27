#!/usr/bin/env node
/**
 * Data Sources tab, rare states in the REAL page (Day 136). Plan: docs/claude/design/DATA_SOURCES_PROVENANCE_PLAN_DAY136.md Part D.
 * Puppeteer request interception: the app runs for real, but the four Data Sources requests are answered with planted payloads
 * (the real payloads, captured once, then changed). Every other request is continued untouched. Separate from ui-verify-checklist.js
 * on purpose: A1-A18 never see planted data.
 * Run: cd frontend && STA_HEADLESS=shell node scripts/test_data_sources_rare_states.js [TICKER]   (backend :5001 and frontend :3000 up)
 * Exit 1 when any expectation fails.
 */
const puppeteer = require('puppeteer');
const { readTabInPage } = require('./lib/readDataSourcesTab');

const FRONTEND = process.env.STA_FRONTEND || 'http://localhost:3000';
const TICKER = (process.argv[2] || 'AAPL').toUpperCase();
const PATHS = { prov: `/api/provenance/${TICKER}`, health: '/api/health', cache: '/api/cache/status', cov: '/api/data-sources/coverage' };

let pass = 0, fail = 0;
const expect = (c, m) => { if (c) { pass++; console.log(`ok   ${m}`); } else { fail++; console.log(`FAIL ${m}`); } };
const clone = (x) => JSON.parse(JSON.stringify(x));

async function openTab(browser, plants) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 1000 });
  const captured = {};
  await page.setRequestInterception(true);
  page.on('request', (req) => {
    let p; try { p = new URL(req.url()).pathname; } catch { return req.continue(); }
    const key = Object.keys(PATHS).find((k) => PATHS[k] === p);
    if (key && plants && plants[key]) {
      const pl = plants[key];
      if (pl.abort) return req.abort();
      return req.respond({ status: pl.status || 200, contentType: 'application/json', headers: { 'Access-Control-Allow-Origin': '*' }, body: JSON.stringify(pl.body) });
    }
    return req.continue();   // never leave a request hanging
  });
  page.on('response', async (res) => {
    try {
      const p = new URL(res.url()).pathname; const key = Object.keys(PATHS).find((k) => PATHS[k] === p);
      if (key && res.status() === 200 && !(plants && plants[key])) captured[key] = await res.json();
    } catch { /* ignore */ }
  });
  await page.goto(FRONTEND, { waitUntil: 'networkidle2', timeout: 60000 });
  const input = await page.waitForSelector('input[placeholder*="ticker"]', { timeout: 8000 });
  await input.click({ clickCount: 3 }); await input.type(TICKER, { delay: 25 }); await page.keyboard.press('Enter');
  await page.waitForSelector('[data-testid="card-technical-read"], [data-testid="analysis-error"]', { timeout: 120000 });
  await new Promise((r) => setTimeout(r, 1500));
  await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((x) => x.textContent.includes('Data Sources')); if (b) b.click(); });
  await page.waitForSelector('[data-testid="data-sources-tab"]', { timeout: 8000 });
  await page.waitForNetworkIdle({ idleTime: 800, timeout: 30000 }).catch(() => {});
  await new Promise((r) => setTimeout(r, 500));
  return { page, captured };
}
const read = (page) => page.evaluate(readTabInPage);

(async () => {
  const browser = await puppeteer.launch({ headless: process.env.STA_HEADLESS || 'shell' });
  // base: the real payloads
  const base = await openTab(browser, null);
  const real = base.captured;
  await base.page.close();
  for (const k of Object.keys(PATHS)) if (!real[k]) { console.log(`FAIL base payload ${k} not captured (is the backend up?)`); process.exit(2); }
  const prov = () => clone(real.prov), health = () => clone(real.health), cov = () => clone(real.cov), cache = () => clone(real.cache);
  const P = (b) => ({ body: b });

  const scenarios = [
    ['real payloads (control): no error, a verdict shows', null, (t) => {
      expect(!t.error && !!t.qualityVerdict && t.chainRows.length > 0, 'control: renders with the real payloads');
    }],
    ['provenance 500: an error with Retry, no stale verdict', { prov: { status: 500, body: { error: 'boom' } } }, (t) => {
      expect(!!t.error && /Couldn't load data quality/.test(t.error) && /Retry/.test(t.error), 'prov 500: error text and Retry button');
      expect(t.qualityVerdict === null, 'prov 500: no verdict pill is shown');
    }],
    ['provenance request aborted (network down)', { prov: { abort: true } }, (t) => {
      expect(!!t.error || /Loading data quality|Couldn't/.test(t.qualityBoxText || ''), 'prov aborted: an error or loading state, never a blank or a verdict');
      expect(t.qualityVerdict === null, 'prov aborted: no verdict pill');
    }],
    ['nothing cached for the ticker', (() => { const b = prov(); b.quality = { state: 'not_cached' }; b.ohlcv = { source: 'unknown', cached: false, status: 'live', attempt: { state: 'never' } }; return { prov: P(b) }; })(), (t) => {
      expect(/Nothing is cached/.test(t.qualityBoxText || '') && t.qualityVerdict === null, 'not cached: says nothing is cached, no verdict');
      expect(/not cached, will fetch/.test(t.cacheState || ''), 'not cached: cache label says it will fetch');
      expect(/no provider check recorded/.test(t.attempt || ''), 'not cached + never: the attempt line says no check recorded');
    }],
    ['expired cache', (() => { const b = prov(); b.quality.expired = true; return { prov: P(b) }; })(), (t) => {
      expect(/expired, will refetch/.test(t.cacheState || ''), 'expired: label says expired');
    }],
    ['last check failed, saved data shown', (() => { const b = prov(); b.ohlcv.attempt = { state: 'failed', last_fail_ts: Date.now() / 1000 - 60, detail: 'alpaca:RateLimitError; yfinance:ProviderError', served_stale: true, last_ok_ts: Date.now() / 1000 - 86400 * 2, last_ok_provider: 'alpaca' }; return { prov: P(b) }; })(), (t) => {
      expect(/failed at /.test(t.attempt || '') && /alpaca:RateLimitError/.test(t.attempt) && /Saved data was shown instead/.test(t.attempt), 'failed: time, reason names and the saved-data fact');
      expect(/Last success: [A-Z][a-z]{2} \d/.test(t.attempt || ''), 'failed: the last success from two days ago shows its DATE');
    }],
    ['attempt record unreadable', (() => { const b = prov(); b.ohlcv.attempt = { state: 'never', error: 'OperationalError' }; return { prov: P(b) }; })(), (t) => {
      expect(/could not be read \(OperationalError\)/.test(t.attempt || ''), 'unreadable record is said, not shown as "no check yet"');
    }],
    ['old backend: no attempt block', (() => { const b = prov(); delete b.ohlcv.attempt; delete b.fundamentals.attempt; return { prov: P(b) }; })(), (t) => {
      expect(t.attempt === null && !/this session/.test(t.identityText || ''), 'old backend: no attempt line and no old session line');
    }],
    ['quality FAIL with rows', (() => { const b = prov(); b.quality.level = 'FAIL'; b.quality.checks.integrity = { level: 'FAIL', note: '100% of bars flat' }; return { prov: P(b) }; })(), (t) => {
      expect(t.qualityVerdict === 'FAIL' && t.qualityRows.some((r) => r.level === 'FAIL' && /flat/.test(r.text)), 'FAIL: pill and the failing row');
    }],
    ['breaker open, quota 0, a provider with no key', (() => {
      const h = health(); const ps = h.providers.providers;
      ps.twelvedata.health = 'open'; ps.twelvedata.daily_remaining = 0; ps.tradier.configured = false; ps.tradier.health = 'ok';
      return { health: P(h) };
    })(), (t) => {
      const row = (n) => (t.chainRows.find((r) => r.provider === n) || {}).text || '';
      expect(/circuit open/.test(row('twelvedata')), 'breaker open: the row says circuit open');
      expect(/0 calls left today/.test(row('twelvedata')), 'quota 0: "0 calls left today" is shown, not hidden');
      expect(/no key/.test(row('tradier')) && !/\bok\b/.test(row('tradier')), 'no API key: "no key", not a green ok');
    }],
    ['every provider down', (() => { const h = health(); for (const p of Object.values(h.providers.providers)) if (p.health) p.health = 'open'; return { health: P(h) }; })(), (t) => {
      const rows = t.chainRows.filter((r) => r.group === 'price');
      expect(rows.length > 0 && rows.every((r) => /circuit open/.test(r.text)), 'all down: every price row says circuit open');
    }],
    ['/api/health 500', { health: { status: 500, body: { error: 'x' } } }, (t) => {
      expect(/Provider health unavailable/.test(t.fullText || ''), 'health 500: "Provider health unavailable." instead of a blank chain');
    }],
    ['coverage 500', { cov: { status: 500, body: { error: 'coverage file unreadable' } } }, (t) => {
      expect(/Coverage table unavailable/.test(t.coverageLine || ''), 'coverage 500: says the table is unavailable');
      expect(!/works|partial|not tested/.test((t.chainRows[0] || {}).text || ''), 'coverage 500: no invented coverage chips');
    }],
    ['cache status 500', { cache: { status: 500, body: { error: 'db' } } }, (t) => {
      expect(/Cache status unavailable|Loading cache status/.test(t.fullText || ''), 'cache 500: says so, no fake "0 KB"');
      expect(!/\b0 KB\b/.test(t.fullText || ''), 'cache 500: no fake 0 KB');
    }],
    ['the static cache line is honest about exceptions', null, (t) => {
      expect(/expires sooner/.test(t.staticCacheLine || ''), 'static line names the shorter-lived cases');
    }],
  ];

  for (const [name, plants, check] of scenarios) {
    console.log(`\n# ${name}`);
    let page;
    try {
      ({ page } = await openTab(browser, plants));
      check(await read(page));
    } catch (e) {
      fail++; console.log(`FAIL scenario threw: ${e.message}`);
    } finally { if (page) await page.close(); }
  }
  // the Retry button in the error state actually asks again (planted 500 once, then real)
  console.log('\n# Retry after a planted 500 fetches again');
  {
    let calls = 0; const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 1000 });
    await page.setRequestInterception(true);
    page.on('request', (req) => {
      let p; try { p = new URL(req.url()).pathname; } catch { return req.continue(); }
      if (p === PATHS.prov) { calls++; if (calls === 1) return req.respond({ status: 500, contentType: 'application/json', headers: { 'Access-Control-Allow-Origin': '*' }, body: JSON.stringify({ error: 'boom' }) }); }
      return req.continue();
    });
    try {
      await page.goto(FRONTEND, { waitUntil: 'networkidle2', timeout: 60000 });
      const input = await page.waitForSelector('input[placeholder*="ticker"]', { timeout: 8000 });
      await input.click({ clickCount: 3 }); await input.type(TICKER, { delay: 25 }); await page.keyboard.press('Enter');
      await page.waitForSelector('[data-testid="card-technical-read"]', { timeout: 120000 });
      await new Promise((r) => setTimeout(r, 1500));
      await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((x) => x.textContent.includes('Data Sources')); if (b) b.click(); });
      await page.waitForSelector('[data-testid="ds-retry"]', { timeout: 10000 });
      await page.evaluate(() => document.querySelector('[data-testid="ds-retry"]').click());   // the button re-renders; a handle would detach
      await page.waitForSelector('[data-testid="ds-quality-verdict"]', { timeout: 15000 });
      expect(calls >= 2, `Retry asked /api/provenance again (${calls} calls) and the verdict appeared`);
    } catch (e) { fail++; console.log(`FAIL retry scenario: ${e.message}`); }
    await page.close();
  }
  await browser.close();
  console.log(`\n${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})();
