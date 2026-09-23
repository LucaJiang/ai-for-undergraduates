"""Bilingual/theme regressions on the real bundled Reveal deck (no external AI)."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import json, re
from playwright.sync_api import sync_playwright, expect

root = Path(__file__).resolve().parents[1]
out = root / 'test-results'
out.mkdir(exist_ok=True)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(root / '_site')))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
report = {'checks': [], 'failures': [], 'external_services_tested': False}
errors = []

def ready(page):
    page.wait_for_function('window.Reveal?.isReady() && window.WorkshopPreferences?.ready')

def slide(page, ident):
    page.evaluate('(id)=>Reveal.slide(Reveal.getSlides().findIndex(s=>s.id===id))', ident)
    page.wait_for_timeout(60)

def contrast(first, second):
    def luminance(value):
        if value.startswith('#'):
            rgb = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
        else:
            rgb = [float(x) / 255 for x in re.findall(r'[\d.]+', value)[:3]]
        values = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in rgb]
        return sum(x*w for x, w in zip(values, (.2126, .7152, .0722)))
    a, b = sorted([luminance(first), luminance(second)])
    return (b + .05) / (a + .05)

try:
    with sync_playwright() as pw:
        executable = '/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None
        browser = pw.chromium.launch(headless=True, executable_path=executable, args=['--no-sandbox'])
        context = browser.new_context(viewport={'width': 1280, 'height': 720}, permissions=['clipboard-read', 'clipboard-write'])
        context.route('**/*youtube*/*', lambda route: route.fulfill(status=200, content_type='text/html', body='External streaming excluded.'))
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(base, wait_until='networkidle'); ready(page)
        assert page.locator('html').get_attribute('lang') == 'en'
        assert page.locator('html').get_attribute('data-theme') == 'light'
        assert page.evaluate('getComputedStyle(document.body).backgroundColor') == 'rgb(248, 250, 252)'
        ids = page.evaluate('Reveal.getSlides().map(s=>s.id)')
        assert len(ids) == 54
        report['checks'].append('First visit defaults to English + light; 54 original slide IDs')

        # Require complete translation coverage, with only intentional proper names retained.
        missing = page.evaluate('''() => {
          const norm = t => t.trim().replace(/\\s+/g, ' ');
          const keys = new Set(Object.keys(WorkshopChinese).map(norm));
          const names = new Set(['Wenxin Jiang','Gemini','DeepSeek','NotebookLM','FaceNet','AlphaGo','ChatGPT',
            'OpenAI · GPT-Realtime-2','Runway · Gen-4.5']);
          const result = [];
          for (const s of Reveal.getSlides()) {
            const walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
            let n;
            while ((n=walker.nextNode())) {
              if(n.parentElement.closest('aside.notes,svg,script,style')) continue;
              const text=norm(n.nodeValue);
              if (/[A-Za-z]/.test(text) && !keys.has(text) && !names.has(text)) result.push({slide:s.id,text});
            }
          }
          return result;
        }''')
        report['untranslated_nodes'] = missing
        assert not missing, f'Untranslated slide text: {missing}'
        report['checks'].append('Every English slide text node has reviewed Chinese copy or is an intentional proper name')
        original = page.evaluate('''() => {
          window.originalSlideNodes = Reveal.getSlides();
          return Reveal.getSlides().map(s=>({id:s.id, notes:s.querySelector('aside.notes')?.innerHTML,
            text:[...s.childNodes].filter(n=>n.nodeName!=='ASIDE').map(n=>n.textContent).join('')}));
        }''')

        # All four presentation combinations, including Chinese line lengths.
        for lang in ['en', 'zh']:
            page.evaluate('(lang)=>WorkshopPreferences.setLanguage(lang)', lang)
            for theme in ['light', 'dark']:
                page.evaluate('(theme)=>WorkshopPreferences.setTheme(theme)', theme)
                palette = page.evaluate('''() => {
                  const s=getComputedStyle(document.documentElement), result={};
                  for (const n of ['bg','panel','ink','muted','accent','warn','bad','button-ink']) result[n]=s.getPropertyValue('--'+n).trim();
                  return result;
                }''')
                for name in ['ink', 'muted', 'accent', 'warn', 'bad']:
                    assert contrast(palette[name], palette['bg']) >= 4.5, (theme, name, palette)
                assert contrast(palette['button-ink'], palette['accent']) >= 4.5, theme
                for ident in ids:
                    slide(page, ident)
                    box = page.locator('#'+ident).bounding_box()
                    assert box and box['y'] >= -2 and box['y']+box['height'] <= 722, (lang, theme, ident, box)
                    assert not page.locator('#'+ident).evaluate('(el)=>el.scrollWidth>el.clientWidth+2'), (lang, theme, ident, 'horizontal overflow')
                    assert page.evaluate('Reveal.getCurrentSlide() === originalSlideNodes[Reveal.getIndices().h]')
                    if ident in ['start','evidence-warning','specific-question','part6']:
                        page.screenshot(path=str(out / f'preferences-{lang}-{theme}-{ident}.png'))
        report['checks'].append('All 54 slides fit at 1280×720 in EN/中文 × light/dark; both palettes meet 4.5:1 text contrast')

        # Chinese prompts copy the actual displayed text; changing language does not replace nodes.
        slide(page, 'specific-question')
        page.evaluate('WorkshopPreferences.setLanguage("zh")')
        code = page.locator('#specific-question pre code').inner_text()
        assert '统计学入门导师' in code
        page.locator('#specific-question .copy').click()
        assert page.evaluate('navigator.clipboard.readText()') == code
        page.evaluate('WorkshopPreferences.setLanguage("en")')
        expect(page.locator('#specific-question .copy')).to_have_text('Copy prompt', timeout=3000)
        assert 'Role: Act as an introductory statistics tutor.' in page.locator('#specific-question pre code').inner_text()
        report['checks'].append('Exact Chinese clipboard text and correct button reset when switching languages during copy feedback')

        # Fragment state, current slide, notes and active timers survive both switches.
        slide(page, 'notebook-quiz'); page.evaluate('Reveal.navigateFragment(0)')
        before = page.evaluate('Reveal.getIndices()')
        page.locator('[data-language-toggle]').click(); page.locator('[data-theme-toggle]').click()
        assert page.evaluate('Reveal.getIndices()') == before
        expect(page.locator('#notebook-quiz .fragment')).to_have_class(re.compile('visible'))
        slide(page, 'future-reflection')
        toggle=page.locator('#future-reflection [data-timer="toggle"]')
        output=page.locator('#future-reflection output')
        toggle.click(); expect(output).not_to_have_text('01:00', timeout=6000)
        page.locator('[data-language-toggle]').click(); page.locator('[data-theme-toggle]').click()
        assert output.inner_text() != '01:00'
        expect(toggle).to_have_text('Pause')
        toggle.click(); paused=output.inner_text(); page.wait_for_timeout(600); assert output.inner_text()==paused
        notes = page.evaluate('Reveal.getSlides().map(s=>s.querySelector("aside.notes")?.innerHTML)')
        assert notes == [s['notes'] for s in original]
        report['checks'].append('Current slide, revealed fragment, running/paused timer, original DOM nodes and speaker notes survive switching')

        slide(page, 'voice-demo'); page.locator('#voice-demo .play-clip').click()
        page.evaluate('window.playingFrame=document.querySelector("#voice-demo iframe")')
        page.locator('[data-language-toggle]').click(); page.locator('[data-theme-toggle]').click()
        assert page.evaluate('playingFrame===document.querySelector("#voice-demo iframe")')
        page.keyboard.press('v')
        expect(page.locator('dialog h2')).to_have_text('讲者视频设置')
        page.get_by_role('button', name='关闭设置', exact=True).click()
        report['checks'].append('Language/theme switches do not unload media; dynamically created presenter controls are translated')

        slide(page, 'ppv-demo')
        lab=page.frame_locator('#ppv-demo iframe')
        expect(lab.locator('h1')).to_have_text('分母里是哪一群人？')
        lab.locator('[data-preset="rare"]').click(); lab.locator('#reveal-result').click()
        expect(lab.locator('#ppv')).to_have_text('PPV = 8.3%')
        page.locator('[data-language-toggle]').click()
        expect(lab.locator('h1')).to_have_text('Who is in the denominator?')
        expect(lab.locator('#p')).to_have_value('1')
        expect(lab.locator('#ppv')).to_have_text('PPV = 8.3%')
        slide(page, 'vector-predict'); page.evaluate('WorkshopPreferences.setLanguage("zh")')
        lab=page.frame_locator('#vector-predict iframe')
        lab.locator('[data-vector="1,1"]').click(); lab.locator('#reveal-result').click()
        expect(lab.locator('#result')).to_contain_text('不是特征向量')
        page.evaluate('WorkshopPreferences.setLanguage("en")')
        expect(lab.locator('#result')).to_contain_text('Not an eigenvector')
        report['checks'].append('Embedded PPV/eigenvector labels and dynamic results switch language without changing inputs or results')

        page.evaluate('WorkshopPreferences.setLanguage("zh");WorkshopPreferences.setTheme("dark")')
        saved_hash=page.evaluate('location.hash'); page.reload(); ready(page)
        assert page.locator('html').get_attribute('lang')=='zh-CN'
        assert page.locator('html').get_attribute('data-theme')=='dark'
        assert page.evaluate('location.hash')==saved_hash
        page.goto(base); ready(page)
        assert page.locator('html').get_attribute('lang')=='zh-CN'
        assert page.locator('html').get_attribute('data-theme')=='dark'
        page.goto(base+'?lang=en&theme=light#/specific-question'); ready(page)
        assert page.locator('html').get_attribute('lang')=='en'
        assert page.locator('html').get_attribute('data-theme')=='light'
        assert page.evaluate('Reveal.getCurrentSlide().id')=='specific-question'
        report['checks'].append('Saved preferences survive refresh/new visits; explicit URL options override them and keep deep links')

        for width, height in [(1440,900),(1024,768),(768,1024),(390,844)]:
            page.set_viewport_size({'width':width,'height':height})
            for lang in ['en','zh']:
                page.evaluate('(lang)=>WorkshopPreferences.setLanguage(lang)',lang)
                nav=page.locator('.deck-nav').bounding_box(); controls=page.locator('.deck-preferences').bounding_box()
                assert nav['x']+nav['width']<=controls['x'], (width, lang, nav, controls)
                assert controls['x']>=0 and controls['x']+controls['width']<=width, (width,controls)
                assert not page.evaluate('document.documentElement.scrollWidth>innerWidth+1')
            page.screenshot(path=str(out/f'preferences-controls-{width}.png'))
        page.locator('[data-language-toggle]').focus(); page.keyboard.press('Enter')
        assert page.locator('html').get_attribute('lang')=='en'
        page.emulate_media(media='print'); expect(page.locator('.deck-preferences')).not_to_be_visible()
        report['checks'].append('Non-overlapping controls on desktop/tablet/mobile, keyboard activation and print-hidden controls')
        context.close()

        restricted=browser.new_context()
        restricted.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('Storage unavailable')}})")
        page=restricted.new_page(); page.on('pageerror',lambda error:errors.append(str(error)))
        page.goto(base+'?lang=zh&theme=light'); ready(page)
        page.locator('[data-language-toggle]').click(); page.locator('[data-theme-toggle]').click()
        assert page.locator('html').get_attribute('lang')=='en'
        assert page.locator('html').get_attribute('data-theme')=='dark'
        report['checks'].append('Controls work when browser storage is unavailable')
        browser.close()
except Exception as error:
    report['failures'].append(f'{type(error).__name__}: {error}')
    raise
finally:
    report['failures']+=errors
    server.shutdown()
    (out/'preferences-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))
if report['failures']:
    raise SystemExit(1)
