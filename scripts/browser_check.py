"""Chromium regression tests. Authenticated AI and external streaming are excluded."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import argparse, base64, json, math, re
from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser()
parser.add_argument('--site', default='_site')
parser.add_argument('--materials-only', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
site = (root / args.site).resolve()
out = root / 'test-results'; out.mkdir(exist_ok=True)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(site)))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
report = {'external_services_tested': False, 'failures': [], 'checks': []}

def contrast_ratio(first, second):
    def luminance(color):
        values = [float(v) / 255 for v in re.findall(r'[\d.]+', color)[:3]]
        linear = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in values]
        return sum(v*w for v,w in zip(linear, (.2126,.7152,.0722)))
    a,b = sorted((luminance(first), luminance(second)))
    return (b+.05)/(a+.05)

js_errors = []
try:
    with sync_playwright() as pw:
        executable = '/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None
        browser = pw.chromium.launch(headless=True, executable_path=executable, args=['--no-sandbox'])
        context = browser.new_context(viewport={'width':1280,'height':720}, permissions=['clipboard-read','clipboard-write'])
        page = context.new_page()
        page.on('pageerror', lambda error: js_errors.append(str(error)))
        context.route('**/*youtube*/*', lambda route: route.fulfill(status=200,content_type='text/html',body='<p>External streaming excluded.</p>'))
        if not args.materials_only:
            # Keep the original dark-theme regression; the preferences suite checks both palettes.
            page.goto(base+'?theme=dark', wait_until='networkidle'); page.wait_for_function('window.Reveal && Reveal.isReady()')
            ids = page.evaluate('Reveal.getSlides().map(s=>s.id)'); assert len(ids)==52, len(ids)
            assert page.locator('.slides > section > section').count()==0
            assert 'Wenxin Jiang' in page.locator('#start').inner_text()
            assert 'PART 0' not in page.locator('#start').inner_text()
            assert page.locator('#agenda .break-band').count()==1
            bg = page.evaluate('getComputedStyle(document.body).backgroundColor'); assert bg=='rgb(11, 20, 36)', bg
            for width,height in [(1280,720),(1440,900)]:
                page.set_viewport_size({'width':width,'height':height})
                for i,ident in enumerate(ids):
                    page.evaluate('i=>Reveal.slide(i)', i); page.wait_for_timeout(90)
                    assert page.evaluate('Boolean(Reveal.getSlideNotes()?.trim())'), ident
                    color = page.locator(f'#{ident} h2').first.evaluate('(el)=>getComputedStyle(el).color')
                    assert contrast_ratio(color,bg)>=4.5, ('Heading contrast',ident)
                    for footer in page.locator(f'#{ident} > .footer').all():
                        assert contrast_ratio(footer.evaluate('(el)=>getComputedStyle(el).color'),bg)>=4.5, ident
                    box = page.locator(f'#{ident}').bounding_box()
                    if box and (box['y'] < -2 or box['y']+box['height'] > height+2): report['failures'].append(f'Slide bounds: {ident} at {width}x{height}: {box}')
                    if width==1280: page.screenshot(path=str(out/f'slide-{i:02d}-{ident}.png'))
                    for button in page.locator(f'#{ident} button.copy').all():
                        expected = button.locator('..').locator('pre').inner_text(); button.click()
                        actual = page.evaluate('navigator.clipboard.readText()')
                        assert actual==expected and '\\n' not in actual, ident
            report['checks'] += ['52 Reveal slides at two desktop sizes','cover, outline, notes, contrast and exact clipboard text']
            page.set_viewport_size({'width':1280,'height':720})
            page.evaluate("Reveal.slide(Reveal.getSlides().findIndex(s=>s.id==='voice-demo'))")
            page.locator('#voice-demo .play-clip').click()
            url = page.locator('#voice-demo iframe').get_attribute('src')
            assert 'youtube.com/embed/' in url and 'start=420' in url and 'end=450' in url, url
            page.evaluate('Reveal.next()'); assert page.locator('#voice-demo iframe').count()==0
            report['checks'].append('YouTube URL bounds and unloading; external streaming mocked')
            # Wait for observable state, not 1.2 seconds close to a 1-second/250-ms boundary.
            for ident,start in [('first-demo','04:00'),('exercise1','10:00')]:
                page.evaluate('(id)=>Reveal.slide(Reveal.getSlides().findIndex(s=>s.id===id))',ident)
                toggle=page.locator(f'#{ident} [data-timer="toggle"]')
                output=page.locator(f'#{ident} output')
                page.locator(f'#{ident} [data-timer="reset"]').click()
                expect(output).to_have_text(start)
                toggle.click(); expect(toggle).to_have_text('Pause')
                expect(output).not_to_have_text(start, timeout=6000)
                toggle.click(); expect(toggle).to_have_text('Start')
                paused=output.inner_text(); page.wait_for_timeout(600)
                assert output.inner_text()==paused, ('Paused timer changed',ident)
                page.locator(f'#{ident} [data-timer="reset"]').click(); expect(output).to_have_text(start)
            report['checks'].append('Four-minute and ten-minute timers: start, countdown, pause and reset')
            with page.expect_popup() as pop: page.locator('[data-notes]').click()
            notes=pop.value; notes.wait_for_timeout(800); assert not notes.is_closed(); notes.close()
            page.bring_to_front()
            report['checks'].append('Speaker-view popup')
            # Generate our own recording; no third-party video file is used.
            recording = page.evaluate('''async () => {
                const c=document.createElement('canvas');c.width=160;c.height=90;
                const g=c.getContext('2d');const stream=c.captureStream(12);
                const rec=new MediaRecorder(stream,{mimeType:'video/webm'});const chunks=[];
                rec.ondataavailable=e=>chunks.push(e.data);
                const finished=new Promise(resolve=>rec.onstop=resolve);rec.start();
                for(let i=0;i<18;i++){g.fillStyle=i%2?'black':'white';g.fillRect(0,0,160,90);await new Promise(r=>setTimeout(r,90));}
                rec.stop();await finished;stream.getTracks().forEach(t=>t.stop());
                return await new Promise(resolve=>{const f=new FileReader();f.onload=()=>resolve(f.result.split(',')[1]);f.readAsDataURL(new Blob(chunks,{type:'video/webm'}));});
            }''')
            page.evaluate("Reveal.slide(Reveal.getSlides().findIndex(s=>s.id==='voice-demo'))")
            page.evaluate("document.querySelector('#voice-demo .video-stage').dataset.start='0.1';document.querySelector('#voice-demo .video-stage').dataset.end='0.6'")
            page.keyboard.press('v'); expect(page.locator('dialog.media-settings')).to_be_visible()
            page.locator('dialog .media-row input[type=file]').first.set_input_files({'name':'test.webm','mimeType':'video/webm','buffer':base64.b64decode(recording)})
            page.get_by_role('button',name='Close setup').click(); page.locator('#voice-demo .play-clip').click()
            page.wait_for_function("document.querySelector('#voice-demo video')?.readyState >= 2")
            page.wait_for_function("(()=>{const v=document.querySelector('#voice-demo video');return v && v.paused && v.currentTime>=.6;})()",timeout=6000)
            result=page.locator('#voice-demo video').evaluate('(v)=>({time:v.currentTime,paused:v.paused})')
            assert result['paused'] and .6 <= result['time'] <= 1.1, result
            replay=page.locator('#voice-demo .play-again'); expect(replay).to_be_visible(); replay.click()
            page.wait_for_function("(()=>{const v=document.querySelector('#voice-demo video');return v && v.paused && v.currentTime>=.6;})()",timeout=6000)
            page.evaluate('Reveal.next()'); assert page.locator('#voice-demo video').count()==0
            report['checks'].append('Local test-video excerpt stops, can replay, and unloads on slide change')
        page.goto(base+'/prompts/index.html'); page.wait_for_function("document.querySelectorAll('#library details').length===20")
        page.locator('#search').fill('glossary'); assert page.locator('#library details:visible').count()==1
        page.locator('#library details:visible summary').click()
        button=page.locator('#library details:visible .copy'); expected=button.locator('..').locator('pre').inner_text(); button.click()
        assert page.evaluate('navigator.clipboard.readText()')==expected
        page.locator('#search').fill(''); page.locator('#mode').select_option('Practice'); assert page.locator('#library details:visible').count()>0
        page.goto(base+'/demo-materials/stem/eigenvectors.html')
        for matrix,x,y,eigen,lam,valid in [('stretch',1,0,True,2,True),('stretch',1,1,False,None,True),('reflect',1,0,True,-1,True),('project',0,1,True,0,True),('stretch',0,0,False,None,False)]:
            page.locator('#matrix').select_option(matrix); page.locator('#vx').fill(str(x)); page.locator('#vy').fill(str(y)); page.locator('#reveal-result').click()
            result=page.evaluate('window.labResult'); assert result['eigen']==eigen and result['valid']==valid,result
            if lam is not None: assert math.isclose(result['lambda'],lam,abs_tol=1e-9),result
        page.screenshot(path=str(out/'eigenvector-lab.png'))
        page.goto(base+'/demo-materials/medicine/ppv-lab.html')
        for preset,expected in [('baseline',.5),('rare',1/12),('none',None)]:
            page.locator(f'[data-preset="{preset}"]').click(); assert not page.locator('#result').is_visible(); page.locator('#reveal-result').click()
            result=page.evaluate('window.labResult'); assert math.isclose(sum(result[k] for k in ('tp','fn','fp','tn')),10000,abs_tol=1e-6),result
            if expected is None: assert result['ppv'] is None
            else: assert math.isclose(result['ppv'],expected,abs_tol=1e-9),result
        page.screenshot(path=str(out/'ppv-lab.png'))
        paths=['materials.html','prompts/index.html','demo-materials/stem/eigenvectors.html','demo-materials/medicine/ppv-lab.html','demo-materials/business/price-elasticity.html','demo-materials/humanities/argument-structure.html','demo-materials/assignment-warmup.html','resources/interactive-guide.html']
        for path in paths:
            page.set_viewport_size({'width':390,'height':844}); page.goto(base+'/'+path); page.wait_for_timeout(180)
            if page.evaluate('document.documentElement.scrollWidth > innerWidth+1'): report['failures'].append('Mobile overflow: '+path)
        report['checks'] += ['20 prompt templates and search/filter','eigenvector boundary cases','PPV independent reference values','eight student pages at 390px']
        browser.close()
except Exception as error:
    report['failures'].append(f'{type(error).__name__}: {error}')
    raise
finally:
    report['failures'] += js_errors
    server.shutdown()
    (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))
if report['failures']: raise SystemExit(1)
