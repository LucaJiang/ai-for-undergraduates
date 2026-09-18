"""Browser checks for the visual revision and its new resource pages."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import json
from playwright.sync_api import sync_playwright, expect

root = Path(__file__).resolve().parents[1]
site = root / '_site'
out = root / 'test-results'; out.mkdir(exist_ok=True)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(site)))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
report = {'external_services_tested': False, 'checks': [], 'failures': []}
errors = []
try:
    with sync_playwright() as pw:
        executable = '/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None
        browser = pw.chromium.launch(headless=True, executable_path=executable, args=['--no-sandbox'])
        context = browser.new_context(viewport={'width':1280,'height':720}, permissions=['clipboard-read','clipboard-write'])
        page = context.new_page(); page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(base, wait_until='networkidle')
        page.wait_for_function('window.Reveal && Reveal.isReady()')
        hosts = page.locator('.reveal [data-icon]').count()
        assert hosts > 60, hosts
        assert page.locator('.reveal [data-icon] svg path').count() == hosts
        assert page.locator('.reveal [data-icon]:not([aria-hidden="true"])').count() == 0
        page.get_by_role('link', name='Part 6', exact=True).click()
        page.wait_for_function('Reveal.getCurrentSlide().id === "part6"')
        page.screenshot(path=str(out / 'part6-navigation.png'))
        report['checks'].append(f'{hosts} local SVG icons and Part 6 navigation')
        page.evaluate("Reveal.slide(Reveal.getSlides().findIndex(s=>s.id==='future-reflection'))")
        output = page.locator('#future-reflection output')
        toggle = page.locator('#future-reflection [data-timer="toggle"]')
        toggle.click(); expect(output).not_to_have_text('01:00', timeout=6000)
        toggle.click(); paused = output.inner_text(); page.wait_for_timeout(500)
        assert output.inner_text() == paused
        page.locator('#future-reflection [data-timer="reset"]').click()
        expect(output).to_have_text('01:00')
        report['checks'].append('One-minute reflection timer')
        page.goto(base + '/resources/google-study-tools.html', wait_until='networkidle')
        button = page.locator('.copy').first
        expected = button.locator('..').locator('pre').inner_text(); button.click()
        assert page.evaluate('navigator.clipboard.readText()') == expected
        report['checks'].append('Google resource-page prompt copying')
        for path in ['resources/google-study-tools.html', 'references/future.html', 'references/index.html']:
            page.set_viewport_size({'width':390,'height':844})
            page.goto(base + '/' + path, wait_until='networkidle')
            assert not page.evaluate('document.documentElement.scrollWidth > innerWidth+1'), path
            page.screenshot(path=str(out / ('mobile-' + path.replace('/', '-').replace('.html', '') + '.png')), full_page=True)
        report['checks'].append('Three revised resource pages at 390px')
        browser.close()
except Exception as error:
    report['failures'].append(f'{type(error).__name__}: {error}')
    raise
finally:
    report['failures'] += errors
    server.shutdown()
    (out / 'visual-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2))
if report['failures']: raise SystemExit(1)
