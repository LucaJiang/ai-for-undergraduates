"""Regression coverage for bilingual reading pages; no external AI or streaming."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import json
import re
from playwright.sync_api import sync_playwright, expect

root = Path(__file__).resolve().parents[1]
site = root / '_site'
out = root / 'test-results'
out.mkdir(exist_ok=True)
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(site)))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
report = {'checks': [], 'failures': [], 'external_services_tested': False}
errors = []
paths = [str(p.relative_to(site)) for p in sorted(site.rglob('*.html')) if 'vendor' not in p.parts and '.zh.' not in p.name and '<body class="source-page">' in p.read_text()]
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None, args=['--no-sandbox'])
        context = browser.new_context(viewport={'width':1280,'height':900}, permissions=['clipboard-read','clipboard-write'])
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        for lang in ('en','zh'):
            for theme in ('light','dark'):
                for path in paths:
                    page.goto(f'{base}/{path}?lang={lang}&theme={theme}', wait_until='networkidle')
                    page.wait_for_function('window.WorkshopPreferences?.ready')
                    assert page.locator('html').get_attribute('lang') == ('zh-CN' if lang == 'zh' else 'en'), path
                    assert page.locator('html').get_attribute('data-theme') == theme, path
                    assert page.locator('[data-language-toggle]').is_visible(), path
                    title = page.locator('h1').inner_text()
                    if lang == 'zh': assert re.search('[\u4e00-\u9fff]', title), (path, title)
                    else: assert re.search('[a-zA-Z]', title), (path, title)
                    # This is the same palette as the presentation, including panels.
                    bg = page.evaluate('getComputedStyle(document.body).backgroundColor')
                    assert bg == ('rgb(248, 250, 252)' if theme == 'light' else 'rgb(11, 20, 36)'), (path,bg)
                    for button in page.locator('.copy').all():
                        if button.is_visible():
                            expected = button.locator('..').locator('pre').inner_text()
                            button.click()
                            assert page.evaluate('navigator.clipboard.readText()') == expected, path
                report['checks'].append(f'{len(paths)} reading pages: {lang}/{theme}, titles, controls, palette and clipboard')
        # Search in either language; keep selection and expanded cards on switching.
        page.goto(base+'/prompts/index.html?lang=zh&theme=light', wait_until='networkidle')
        page.wait_for_selector('#library[data-ready="true"]')
        assert page.locator('#library details').count() == 20
        page.locator('#search').fill('术语表')
        assert page.locator('#library details:visible').count() == 1
        page.locator('#prompt-12 summary').click()
        before = page.locator('#prompt-12 pre').inner_text()
        assert '角色：' in before
        page.locator('#prompt-12 .copy').click()
        assert page.evaluate('navigator.clipboard.readText()') == before
        page.locator('[data-language-toggle]').click()
        expect(page.locator('#prompt-12')).to_have_attribute('open','')
        assert page.locator('#library details:visible').count() == 1
        assert page.locator('#search').input_value() == '术语表'
        assert 'Role:' in page.locator('#prompt-12 pre').inner_text()
        page.locator('#search').fill('glossary')
        assert page.locator('#library details:visible').count() == 1
        page.locator('#search').fill('')
        page.locator('#category').select_option('Materials')
        page.locator('#mode').select_option('Explain')
        assert page.locator('#library details:visible').count() == 3
        page.locator('[data-language-toggle]').click()
        assert page.locator('#category').input_value() == 'Materials'
        assert page.locator('#mode').input_value() == 'Explain'
        assert page.locator('#library details:visible').count() == 3
        page.screenshot(path=str(out/'materials-zh-prompt-library.png'), full_page=True)
        report['checks'].append('20 translated templates, bilingual search, stable category/mode filters, open cards and exact copy')
        # Ensure every translated prompt is readable/copyable, not only the glossary.
        page.locator('#category').select_option('');page.locator('#mode').select_option('')
        for card in page.locator('#library details').all():
            if card.get_attribute('open') is None: card.locator('summary').click()
            assert '角色：' in card.locator('pre').inner_text()
            card.locator('.copy').click()
            assert page.evaluate('navigator.clipboard.readText()') == card.locator('pre').inner_text()
        report['checks'].append('All 20 Chinese prompt bodies copied and compared byte-for-byte')
        # The selected language/theme travels from the presentation into reading pages.
        page.goto(base+'/?lang=zh&theme=dark#/start', wait_until='networkidle')
        page.wait_for_function('window.Reveal?.isReady() && WorkshopPreferences.ready')
        href = page.locator('.deck-nav a[href*="materials.html"]').get_attribute('href')
        assert 'lang=zh' in href and 'theme=dark' in href
        page.goto(href, wait_until='networkidle')
        assert page.locator('html').get_attribute('lang') == 'zh-CN'
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        page.locator('[data-theme-toggle]').click()
        page.screenshot(path=str(out/'materials-zh-light.png'), full_page=True)
        notebook_link = page.locator('#notebook a').first.get_attribute('href')
        assert '.zh.html' in notebook_link
        response = context.request.get(notebook_link)
        assert '课程讲义：诊断检测' in response.text()
        assert '在真正患病的人群中' in response.text()
        for path in sorted((site/'demo-materials/notebook').glob('*.zh.html')):
            static_context=browser.new_context(java_script_enabled=False)
            static_page=static_context.new_page();static_page.goto(base+'/'+str(path.relative_to(site)))
            assert re.search('[\u4e00-\u9fff]', static_page.locator('h1').inner_text())
            static_context.close()
        assert '敏感度以全部患病者' in (site/'resources/answer-keys.zh.md').read_text()
        report['checks'].append('Slide-to-material preference inheritance; three static Chinese Notebook sources and Chinese answer-key download')
        # Lab inputs and already revealed results survive language changes.
        page.goto(base+'/demo-materials/medicine/ppv-lab.html?lang=zh', wait_until='networkidle')
        page.locator('[data-preset="rare"]').click();page.locator('#reveal-result').click()
        assert abs(page.evaluate('labResult.ppv') - 1/12) < 1e-10
        page.locator('[data-language-toggle]').click()
        expect(page.locator('#result')).to_be_visible();assert page.locator('#p').input_value() == '1'
        page.locator('[data-preset="none"]').click();page.locator('#reveal-result').click()
        assert page.evaluate('labResult.ppv') is None
        page.locator('[data-language-toggle]').click()
        assert '未定义' in page.locator('#ppv').inner_text()
        page.goto(base+'/demo-materials/stem/eigenvectors.html?lang=zh', wait_until='networkidle')
        page.locator('#matrix').select_option('reflect');page.locator('#reveal-result').click()
        assert '是特征向量' in page.locator('#result').inner_text()
        page.locator('[data-language-toggle]').click()
        assert 'Eigenvector' in page.locator('#result').inner_text()
        assert page.locator('#matrix').input_value() == 'reflect'
        report['checks'].append('Standalone PPV/eigenvector state preservation and boundary cases')
        for width in (390,768):
            page.set_viewport_size({'width':width,'height':844})
            for path in paths:
                page.goto(f'{base}/{path}?lang=zh&theme=light',wait_until='networkidle')
                assert not page.evaluate('document.documentElement.scrollWidth>innerWidth+1'), (width,path)
                if path == 'materials.html':page.screenshot(path=str(out/f'materials-zh-mobile-{width}.png'),full_page=True)
        report['checks'].append('All 16 Chinese reading pages at 390px and 768px; no document overflow')
        restricted=browser.new_context()
        restricted.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('blocked')}})")
        p=restricted.new_page();p.goto(base+'/materials.html?lang=zh&theme=dark',wait_until='networkidle')
        p.locator('[data-language-toggle]').click();assert p.locator('html').get_attribute('lang') == 'en'
        assert 'lang=en' in p.locator('a[href*="price-elasticity.html"]').get_attribute('href')
        restricted.close()
        report['checks'].append('Storage-blocked URL settings and working toggles')
        page.goto(base+'/materials.html?lang=zh&theme=light',wait_until='networkidle');page.emulate_media(media='print')
        assert not page.locator('.deck-preferences').is_visible()
        report['checks'].append('Reading controls hidden in print')
        browser.close()
except Exception as error:
    report['failures'].append(f'{type(error).__name__}: {error}')
    raise
finally:
    report['failures'] += errors
    server.shutdown()
    (out/'materials-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))
if report['failures']: raise SystemExit(1)
