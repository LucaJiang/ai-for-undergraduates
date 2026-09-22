/* Presentation preferences: local-only, no reloads, no DOM replacement.
 * URL options override saved choices. First visit: English, light theme.
 * Keep this small script in <head> so the correct palette paints immediately. */
(function () {
  'use strict';
  const root = document.documentElement;
  const keys = { lang: 'ai-study-language', theme: 'ai-study-theme' };
  function read(key) { try { return localStorage.getItem(key); } catch (_) { return null; } }
  function save(key, value) { try { localStorage.setItem(key, value); } catch (_) { /* Private/restricted browser. */ } }
  const query = new URLSearchParams(location.search);
  function choice(name, allowed, fallback) {
    const requested = query.get(name), saved = read(keys[name]);
    return allowed.includes(requested) ? requested : allowed.includes(saved) ? saved : fallback;
  }
  let language = choice('lang', ['en', 'zh'], 'en');
  let theme = choice('theme', ['light', 'dark'], 'light');
  root.lang = language === 'zh' ? 'zh-CN' : 'en';
  root.dataset.theme = theme;
  root.style.colorScheme = theme;

  const normalize = text => text.trim().replace(/\s+/g, ' ');
  const textCache = new WeakMap();
  const attributeCache = new WeakMap();
  const observers = new Map();
  const frameListeners = new WeakSet();
  const excluded = 'script,style,textarea,aside.notes,[data-no-translate],.deck-preferences,#presentation-status';
  let dictionary, reverse, initialized = false;
  function dictionaries() {
    if (dictionary) return;
    dictionary = new Map(); reverse = new Map();
    Object.entries(window.WorkshopChinese || {}).forEach(([en, zh]) => {
      const pair = { en, zh };
      dictionary.set(normalize(en), pair);
      if (!reverse.has(normalize(zh))) reverse.set(normalize(zh), pair);
    });
  }
  function translatedPair(text) {
    dictionaries();
    const normalized = normalize(text);
    const english = dictionary.get(normalized);
    const chinese = reverse.get(normalized);
    if (english) return { en: text, zh: text.replace(text.trim(), english.zh) };
    if (chinese) return { en: text.replace(text.trim(), chinese.en), zh: text };
    // Presenter video labels contain a runtime-generated time range.
    const range = normalized.match(/^(.*) \(([\d.]+–[\d.]+) (seconds|秒)\)$/);
    if (range) return { en: `${range[1]} (${range[2]} seconds)`, zh: `${range[1]} (${range[2]} 秒)` };
    const vector = normalized.match(/^(Av = \([^)]+\))\. (.+)$/);
    if (vector) {
      const result = vector[2].match(/^Eigenvector: λ = (.+)\.$/);
      const conclusion = result ? `是特征向量：λ = ${result[1]}。` : dictionary.get(vector[2])?.zh;
      if (conclusion) return { en: text, zh: `${vector[1]}。${conclusion}` };
    }
    const excerpt = normalized.match(/^(OpenAI · GPT-Realtime-2|Runway · Gen-4\.5) excerpt$/);
    if (excerpt) return { en: text, zh: `${excerpt[1]} 片段` };
    return null;
  }
  function t(text) {
    if (language !== 'zh') return text;
    dictionaries();
    return dictionary.get(normalize(text))?.zh || text;
  }
  function updateText(node) {
    const parent = node.parentElement;
    if (!parent || parent.closest(excluded) || !node.nodeValue.trim()) return;
    const value = node.nodeValue;
    let pair = textCache.get(node);
    if (!pair || (value !== pair.en && value !== pair.zh)) pair = translatedPair(value);
    if (!pair) return;
    textCache.set(node, pair);
    const next = pair[language];
    if (next !== value) node.nodeValue = next;
  }
  function updateAttributes(element) {
    if (element.closest(excluded)) return;
    let cache = attributeCache.get(element);
    if (!cache) { cache = new Map(); attributeCache.set(element, cache); }
    ['title', 'aria-label', 'placeholder', 'alt'].forEach(name => {
      const value = element.getAttribute(name);
      if (!value) return;
      let pair = cache.get(name);
      if (!pair || (value !== pair.en && value !== pair.zh)) pair = translatedPair(value);
      if (!pair) return;
      cache.set(name, pair);
      if (value !== pair[language]) element.setAttribute(name, pair[language]);
    });
  }
  function translateSubtree(target) {
    if (!target) return;
    if (target.nodeType === Node.TEXT_NODE) { updateText(target); return; }
    if (target.nodeType !== Node.ELEMENT_NODE && target.nodeType !== Node.DOCUMENT_NODE) return;
    if (target.nodeType === Node.ELEMENT_NODE && target.closest(excluded)) return;
    const doc = target.ownerDocument || target;
    const walker = doc.createTreeWalker(target, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) updateText(node);
    if (target.nodeType === Node.ELEMENT_NODE) updateAttributes(target);
    target.querySelectorAll('[title],[aria-label],[placeholder],[alt]').forEach(updateAttributes);
  }
  const observeOptions = { subtree: true, childList: true, characterData: true, attributes: true,
    attributeFilter: ['title', 'aria-label', 'placeholder', 'alt'] };
  function withObserverPaused(doc, action) {
    const observer = observers.get(doc);
    observer?.disconnect();
    try { action(); } finally { if (observer && doc.body) observer.observe(doc.body, observeOptions); }
  }
  function observeDocument(doc) {
    if (observers.has(doc) || !doc.body) return;
    const observer = new MutationObserver(records => {
      withObserverPaused(doc, () => {
        for (const record of records) {
          if (record.type === 'childList') record.addedNodes.forEach(translateSubtree);
          else if (record.type === 'characterData') updateText(record.target);
          else updateAttributes(record.target);
        }
      });
      if (doc === document) connectLabs();
    });
    observers.set(doc, observer);
    observer.observe(doc.body, observeOptions);
  }
  function connectLabs() {
    document.querySelectorAll('iframe.lab-frame').forEach(frame => {
      if (frameListeners.has(frame)) return;
      frameListeners.add(frame);
      const translate = () => {
        // Only our same-origin teaching labs. Never inspect third-party video frames.
        try {
          const src = frame.getAttribute('src');
          if (!src || new URL(src, location.href).origin !== location.origin) return;
          const doc = frame.contentDocument;
          if (!doc?.body) return;
          doc.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
          withObserverPaused(doc, () => translateSubtree(doc.body));
          observeDocument(doc);
        } catch (_) { /* A sandboxed or cross-origin frame keeps its own interface. */ }
      };
      frame.addEventListener('load', translate);
      translate();
    });
  }
  function refresh() {
    withObserverPaused(document, () => translateSubtree(document.body));
    observers.forEach((_, doc) => {
      if (doc === document) return;
      doc.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
      withObserverPaused(doc, () => translateSubtree(doc.body));
    });
    document.title = language === 'zh' ? '用 AI 提高学习效率 · Wenxin Jiang' : 'Boost Your Study Skills with AI · Wenxin Jiang';
  }
  function updateURL(name, value) {
    try {
      const url = new URL(location.href);
      url.searchParams.set(name, value);
      history.replaceState(history.state, '', url);
    } catch (_) { /* Controls also work in a restricted/file preview. */ }
  }
  function updateControls() {
    const chinese = language === 'zh';
    const languageButton = document.querySelector('[data-language-toggle]');
    const themeButton = document.querySelector('[data-theme-toggle]');
    const group = document.querySelector('.deck-preferences');
    group?.setAttribute('aria-label', chinese ? '演示设置' : 'Presentation settings');
    if (languageButton) {
      const label = chinese ? 'Switch to English' : '切换为中文';
      languageButton.setAttribute('aria-label', label);
      languageButton.title = label;
      languageButton.dataset.language = language;
    }
    if (themeButton) {
      const dark = theme === 'dark';
      const label = chinese ? (dark ? '切换为浅色主题' : '切换为深色主题') : (dark ? 'Switch to light theme' : 'Switch to dark theme');
      themeButton.setAttribute('aria-label', label);
      themeButton.title = label;
      themeButton.querySelector('[data-theme-label]').textContent = chinese ? (dark ? '浅色' : '深色') : (dark ? 'Light' : 'Dark');
      themeButton.querySelector('[data-light-icon]').hidden = !dark;
      themeButton.querySelector('[data-dark-icon]').hidden = dark;
    }
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'light' ? '#f8fafc' : '#0b1424');
  }
  function announce() {
    const status = document.getElementById('presentation-status');
    if (status) status.textContent = language === 'zh' ? `中文 · ${theme === 'light' ? '浅色' : '深色'}主题` : `English · ${theme} theme`;
  }
  function setLanguage(value) {
    if (!['en', 'zh'].includes(value)) return;
    language = value; root.lang = value === 'zh' ? 'zh-CN' : 'en';
    save(keys.lang, value); updateURL('lang', value);
    refresh(); updateControls();
    document.dispatchEvent(new CustomEvent('workshoplanguagechange', { detail: { language } }));
    // Recalculate centering without replacing slides, fragments, timers or videos.
    window.Reveal?.layout(); announce();
  }
  function setTheme(value) {
    if (!['light', 'dark'].includes(value)) return;
    theme = value; root.dataset.theme = value; root.style.colorScheme = value;
    save(keys.theme, value); updateURL('theme', value); updateControls(); announce();
  }
  function init() {
    if (initialized) return;
    initialized = true;
    refresh(); updateControls(); observeDocument(document); connectLabs();
    document.querySelector('[data-language-toggle]')?.addEventListener('click', () => setLanguage(language === 'en' ? 'zh' : 'en'));
    document.querySelector('[data-theme-toggle]')?.addEventListener('click', () => setTheme(theme === 'light' ? 'dark' : 'light'));
    window.Reveal?.layout();
  }
  window.WorkshopPreferences = Object.freeze({ init, setLanguage, setTheme, t,
    get language() { return language; }, get theme() { return theme; }, get ready() { return initialized; } });
})();
