# Part 0 media runbook

Three source-video excerpts: OpenAI GPT-Realtime-2 06:58–07:28 (30 s), Genie 3 00:07–00:31 (24 s), Runway Gen-4.5 00:06–00:26 (20 s). Total video time: 74 seconds. These are publisher demonstrations; detailed provenance belongs in notes, not on the capability overview slide.

| Source | Start | End |
|---|---|---|
| [OpenAI](https://www.youtube.com/watch?v=qGS9Ghnq1RU) | 418 s | 448 s |
| [Google DeepMind](https://www.youtube.com/watch?v=PDKhUknuQDg) | 7 s | 31 s |
| [Runway](https://www.youtube.com/watch?v=ei2PsDpPbB4) | 6 s | 26 s |

## Preferred rehearsal workflow

1. Open the deck in the actual presentation browser. Press V to open Video setup, or add `?presenter=1` to expose the setup button.
2. Select a video file you have permission to use. Choose full source video or already-trimmed excerpt. Files are local object URLs only: not uploaded, persisted or added to the public repository.
3. Play the excerpt. For a full source file, playback seeks to the recorded start and pauses at the end. A trimmed excerpt starts at zero and plays up to the specified excerpt length or the shorter file duration. Native controls allow pausing; Replay restarts the excerpt.
4. Re-select files after reloading. Leaving a slide stops playback. Keep a fallback sentence rather than debugging audio or streaming on stage.

## External player

The default uses standard youtube.com embeds. Timestamp parameters do not bypass sign-in, age, anti-bot, region, network or embedding restrictions. An iframe alone cannot identify why a particular user was asked to sign in. Changing from youtube-nocookie.com is an alternative, not a confirmed fix.

The Watch on YouTube link opens the original video at the starting timestamp. It does not enforce the ending timestamp; pause it manually. Use the same signed-in browser if needed. Do not weaken browser security or suggest circumvention.

No third-party video is downloaded or redistributed by this repository. Local player mechanics and external URL construction are testable; actual YouTube playback and campus audio/network remain rehearsal tasks.

[Official player parameters](https://developers.google.com/youtube/player_parameters) · [Presenter guide](presenter-guide.md)
