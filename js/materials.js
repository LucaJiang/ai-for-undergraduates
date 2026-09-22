/* Reading pages reuse the deck's language and theme without replacing content. */
(function () {
  'use strict';
  function init() {
    const prefs = window.WorkshopPreferences;
    if (!prefs) return;
    // Embedded labs remain under the deck's existing observer so inputs/results
    // are not reset or translated twice by conflicting observers.
    try { if (window.frameElement?.classList.contains('lab-frame') && parent.WorkshopPreferences) return; } catch (_) { /* Standalone page. */ }
    function sources() {
      const chinese = prefs.language === 'zh';
      document.querySelectorAll('a[data-source-en]').forEach(link => {
        const url = new URL(chinese ? link.dataset.sourceZh : link.dataset.sourceEn, document.baseURI);
        if (url.pathname.endsWith('.html')) { url.searchParams.set('lang', prefs.language); url.searchParams.set('theme', prefs.theme); }
        link.href = url.href;
      });
    }
    prefs.init();
    sources();
    document.addEventListener('workshoplanguagechange', sources);
    document.addEventListener('workshopthemechange', sources);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true }); else init();
})();
