# Workshop QA scope

## Automated checks

`python scripts/check_sources.py` checks 52 slide anchors, one notes block per slide, no nested slide sections or duplicated clipboard content, selected reader-facing regressions, and local links.

`npm run build` copies the pinned Reveal.js 5.2.1 runtime into the site. It does not copy font files or third-party videos.

`python scripts/browser_check.py` uses a real Chromium browser against the bundled site. It checks:

- 52 slides at 1280×720 and 1440×900, notes, selected text contrast and vertical slide bounds; saves screenshots for visual review.
- Exact visible prompt text on the clipboard, speaker popup, four-minute and ten-minute timer start/pause/reset.
- YouTube URL time ranges and player unloading. The external player response is mocked; this does **not** test actual YouTube streaming or login behavior.
- Local video controls using a short recording created by the test itself: bounded playback, Replay and unload. It does not use or redistribute a third-party clip.
- Twenty prompt-library templates, search/filter, numerical eigenvector and PPV reference cases.
- Eight student companion pages at 390 px for horizontal overflow.

Timing assertions wait for observable state changes rather than assuming a rendering callback will run within a narrow fixed interval. A stalled timer or failed player still fails the test. See `test-results/report.json` in the workflow artifact for the checks that actually completed; a successful build alone is not a browser-test pass.

## Not automatically verified

Authenticated Gemini / Notebook output, in-chat visualization availability, school account permissions, generation times, host academic-integrity policy, live YouTube playback, campus network, audio and projector conditions require rehearsal with the lecturer's account and venue. The prompts for Gemini interactive visualizations are proposed requests, not a verified transcript. The site includes prepared browser labs as alternatives, and these must not be presented as newly generated Gemini results.

See the [presenter guide](presenter-guide.md) and [media runbook](part0-media.md).
