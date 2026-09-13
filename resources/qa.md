# QA scope and commands

Run source checks with `python scripts/check_sources.py`.

Install the pinned Reveal runtime using `npm install --ignore-scripts --no-audit --no-fund`, then `npm run build`. For the browser suite install `playwright==1.55.0` and Chromium with `python -m playwright install --with-deps chromium`; run `python scripts/browser_check.py`.

The publishing workflow builds locally bundled Reveal assets, runs the browser suite, uploads `workshop-qa` screenshots/report, and deploys only if checks pass. It checks 51 slides, notes, copies, timers, player parameters/unloading, two desktop viewports, two numeric labs, template search/filter/copy and six mobile companion pages. Source checks reject nested Markdown sections and broken local paths.

Local material-only command: `python scripts/browser_check.py --site . --materials-only`. This does **not** validate the actual Reveal engine.

Not covered: authenticated Notebook sessions, generated Quiz quality/latency, actual school-account options, third-party video streaming, ads/audio/captions or optimal excerpt frames, the venue projector/network, or the host's policy. Media requests are mocked in automated tests to avoid claiming streaming has been verified. Run a final venue rehearsal. A successful Pages deployment is not evidence these external conditions work.
