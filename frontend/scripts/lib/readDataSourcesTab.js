/** The ONE reader of what the Data Sources tab shows (Day 136). Used by dump_data_sources_tab.js (statement audit) and
 *  test_data_sources_rare_states.js, so both read the same DOM the same way. Runs inside the page. */
function readTabInPage() {
    document.querySelectorAll('[data-testid="data-sources-tab"] details').forEach((d) => { d.open = true; });
    const q = (s) => document.querySelector(`[data-testid="${s}"]`);
    const t = (el) => (el ? el.textContent.trim().replace(/\s+/g, ' ') : null);
    const all = (s) => [...document.querySelectorAll(`[data-testid="${s}"]`)];
    const root = q('data-sources-tab');
    const staticLine = [...root.querySelectorAll('p')].find((p) => p.textContent.includes('Prices are cached'));
    const tvLine = [...root.querySelectorAll('p')].find((p) => p.textContent.includes('Market scanning'));
    const disabledLine = [...root.querySelectorAll('p')].find((p) => p.textContent.includes('Disabled:'));
    const grid = [...root.querySelectorAll('.grid > div')].map((d) => t(d));
    return {
      fullText: t(root),
      symbol: t(q('ds-symbol')), exchange: t(q('ds-exchange')), currency: t(q('ds-currency')), cls: t(q('ds-class')),
      basis: q('ds-class') ? q('ds-class').getAttribute('title') : null,
      dataFrom: t(q('ds-datafrom')), cacheState: t(q('ds-cachestate')),
      attempt: t(q('ds-attempt')),
      identityText: t(q('ds-identity')),
      qualityVerdict: q('ds-quality-verdict') ? q('ds-quality-verdict').dataset.level : null,
      qualityHeader: t(q('ds-quality-header')), allPass: t(q('ds-quality-allpass')),
      qualityRows: all('ds-quality-row').map((r) => ({ level: r.dataset.level, text: t(r) })),
      splitNotes: all('ds-split-note').map(t), audit: t(q('ds-audit')), fundamentals: t(q('ds-fundamentals')),
      error: t(q('ds-error')), qualityBoxText: t(q('ds-quality')),
      coverageLine: t(q('ds-coverage')),
      chainRows: all('ds-chain-row').map((r) => ({ group: r.dataset.group, provider: r.dataset.provider, text: t(r) })),
      disabledLine: t(disabledLine), tvLine: t(tvLine),
      otherChains: [...root.querySelectorAll('details .space-y-1 > div')].map(t),
      cacheGrid: grid, staticCacheLine: t(staticLine),
      indicatorRows: [...root.querySelectorAll('[data-testid="ds-indicators"] tbody tr')].map((r) => [...r.children].map((td) => td.textContent.trim())),
    };
}
module.exports = { readTabInPage };
