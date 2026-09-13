"""Real Chromium tests. External streaming and authenticated AI services excluded."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import argparse, json, math
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument("--site", default="_site")
parser.add_argument("--materials-only", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
site = (root / args.site).resolve()
out = root / "test-results"; out.mkdir(exist_ok=True)
server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(site)))
Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"
report = {"external_services_tested": False, "failures": [], "checks": []}
with sync_playwright() as pw:
    executable = "/usr/bin/chromium" if Path("/usr/bin/chromium").exists() else None
    browser = pw.chromium.launch(headless=True, executable_path=executable, args=["--no-sandbox"])
    context = browser.new_context(viewport={"width":1280,"height":720}, permissions=["clipboard-read","clipboard-write"])
    page = context.new_page(); js_errors=[]
    page.on("pageerror", lambda e: js_errors.append(str(e)))
    # Deliberately do not treat external streaming as a tested local capability.
    context.route("**/*youtube*/*", lambda route: route.fulfill(status=200, content_type="text/html", body="<p>External video playback is excluded from this test.</p>"))
    if not args.materials_only:
        page.goto(base, wait_until="networkidle")
        page.wait_for_function("window.Reveal && Reveal.isReady()")
        count=page.evaluate("Reveal.getSlides().length"); assert count==51,count
        assert page.locator('.slides > section > section').count()==0
        ids=page.evaluate("Reveal.getSlides().map(s=>s.id)")
        for width,height in [(1280,720),(1440,900)]:
            page.set_viewport_size({"width":width,"height":height})
            for i,ident in enumerate(ids):
                page.evaluate("i=>Reveal.slide(i)",i); page.wait_for_timeout(80)
                assert page.evaluate("Boolean(Reveal.getSlideNotes()?.trim())"),ident
                box=page.locator(f'#{ident}').bounding_box()
                if box and (box['y'] < -2 or box['y']+box['height']>height+2):
                    report['failures'].append(f"Slide bounds {ident} at {width}x{height}: {box}")
                if width==1280:
                    page.screenshot(path=str(out/f"slide-{i:02d}-{ident}.png"))
                copies=page.locator(f'#{ident} button.copy')
                for j in range(copies.count()):
                    b=copies.nth(j);expected=b.locator('..').locator('pre').inner_text();b.click();
                    actual=page.evaluate("navigator.clipboard.readText()")
                    assert actual==expected,(ident,repr(actual),repr(expected))
                    assert '\\n' not in actual,ident
        page.set_viewport_size({"width":1280,"height":720})
        page.evaluate("Reveal.slide(Reveal.getSlides().findIndex(s=>s.id==='voice-demo'))")
        page.locator('#voice-demo .play-clip').click()
        url=page.locator('#voice-demo iframe').get_attribute('src');assert 'start=418' in url and 'end=448' in url
        page.evaluate("Reveal.next()")
        assert page.locator('#voice-demo iframe').count()==0
        page.evaluate("Reveal.slide(Reveal.getSlides().findIndex(s=>s.id==='exercise1'))")
        page.locator('#exercise1 [data-timer="toggle"]').click();page.wait_for_timeout(1200)
        assert page.locator('#exercise1 output').inner_text()!='10:00'
        page.locator('#exercise1 [data-timer="toggle"]').click();page.locator('#exercise1 [data-timer="reset"]').click()
        assert page.locator('#exercise1 output').inner_text()=='10:00'
        with page.expect_popup() as pop:
            page.locator('[data-notes]').click()
        notes=pop.value;notes.wait_for_timeout(1000);assert not notes.is_closed();notes.close()
        report['checks']+=['51 real Reveal slides at 1280×720 and 1440×900','all slide notes and copy buttons','speaker popup','timer start/pause/reset','video timestamp bounds and unloading']
    page.goto(base+'/prompts/index.html');page.wait_for_function("document.querySelectorAll('#library details').length===20")
    page.locator('#search').fill('glossary');assert page.locator('#library details:visible').count()==1
    page.locator('#library details:visible summary').click()
    b=page.locator('#library details:visible .copy');expected=b.locator('..').locator('pre').inner_text();b.click();assert page.evaluate('navigator.clipboard.readText()')==expected
    page.locator('#search').fill('');page.locator('#mode').select_option('Practice');assert page.locator('#library details:visible').count()>0
    page.goto(base+'/demo-materials/stem/eigenvectors.html')
    for matrix,x,y,eigen,lam,valid in [('stretch',1,0,True,2,True),('stretch',1,1,False,None,True),('reflect',1,0,True,-1,True),('project',0,1,True,0,True),('stretch',0,0,False,None,False)]:
        page.locator('#matrix').select_option(matrix);page.locator('#vx').fill(str(x));page.locator('#vy').fill(str(y));page.locator('#reveal-result').click();r=page.evaluate('window.labResult');assert r['eigen']==eigen and r['valid']==valid,r
        if lam is not None:assert math.isclose(r['lambda'],lam,abs_tol=1e-9),r
    page.screenshot(path=str(out/'eigenvector-lab.png'))
    page.goto(base+'/demo-materials/medicine/ppv-lab.html')
    for preset,expected in [('baseline',.5),('rare',1/12),('none',None)]:
        page.locator(f'[data-preset="{preset}"]').click();assert not page.locator('#result').is_visible();page.locator('#reveal-result').click();r=page.evaluate('window.labResult');assert math.isclose(sum(r[k] for k in ('tp','fn','fp','tn')),10000,abs_tol=1e-6),r
        if expected is None:assert r['ppv'] is None
        else:assert math.isclose(r['ppv'],expected,abs_tol=1e-9),r
    page.screenshot(path=str(out/'ppv-lab.png'))
    for path in ['materials.html','prompts/index.html','demo-materials/stem/eigenvectors.html','demo-materials/medicine/ppv-lab.html','demo-materials/business/price-elasticity.html','demo-materials/humanities/argument-structure.html']:
        page.set_viewport_size({'width':390,'height':844});page.goto(base+'/'+path);page.wait_for_timeout(150)
        if page.evaluate('document.documentElement.scrollWidth > innerWidth+1'):report['failures'].append('Mobile horizontal overflow: '+path)
    report['checks']+=['20 searchable/filterable templates and exact clipboard text','eigenvector non-eigenvector / sign / zero cases','PPV known values, conservation of expected counts and undefined denominator','six companion pages at 390 px']
    report['failures']+=js_errors;browser.close()
server.shutdown()
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
if report['failures']:raise SystemExit(1)
