# D01 commercial — shot record

Script and plan: [production/demo/d01-commercial-30s.md](../../demo/d01-commercial-30s.md). Prompts: [production/prompts/d01-commercial.md](../../prompts/d01-commercial.md). First test run: **2026-11-23**, one take per shot, all in the show project with Omni 1.2 Flash, 720p, 8 s.

The agent may mark takes `generated` or `rejected`; only the showrunner sets `selected` or `final`.

| Shot | Take | Status | Flow name | Line (Whisper) | Agent notes | Log |
| --- | --- | --- | --- | --- | --- | --- |
| `demo-d01-sh01` | v01 | **selected** (showrunner, 2026-11-23) | Woman at chalkboard holding chalk | word-perfect | Office matches the wide master well; she walks toward the camera after turning | [log](../../generation-logs/demo-d01-sh01-v01.yaml) |
| `demo-d01-sh02` | v01 | **selected** (showrunner, 2026-11-23) | Man staring at phone | silent (buzz only) | One-shot cameo, no references by design; screen faces away | [log](../../generation-logs/demo-d01-sh02-v01.yaml) |
| `demo-d01-sh03` | v01 | rejected (re-roll asked) | Woman speaking at desk | word-perfect | Sophie consistent; **office restyled** against cam-a (plants, globe, clock; no laptop or bust) | [log](../../generation-logs/demo-d01-sh03-v01.yaml) |
| `demo-d01-sh03` | v02 | **selected** (showrunner, 2026-11-23) | Woman leaning forward talking | word-perfect | Re-roll with the room spelled out: cam-a angle over the wingback, bookcases, bust, diplomas, lamp all right; still a small plant and globe, no laptop, cooler light | [log](../../generation-logs/demo-d01-sh03-v02.yaml) |
| `demo-d01-sh04a` | v01 | **selected** (showrunner, 2026-11-23) | Woman tapping chalkboard with text | word-perfect | Version A: Flow's chalk text correct and stable, plus an unasked underline | [log](../../generation-logs/demo-d01-sh04a-v01.yaml) |
| `demo-d01-sh04b` | v01 | rejected (not chosen) | Woman tapping chalkboard with chalk | word-perfect | Version B: clean board; text added in post with `scripts/chalk_overlay.py` | [log](../../generation-logs/demo-d01-sh04b-v01.yaml) |
| `demo-d01-sh05` | v01 | **selected** (showrunner, 2026-11-23) | Woman pointing and speaking | word-perfect | Points at the lens, wry smile and a wink | [log](../../generation-logs/demo-d01-sh05-v01.yaml) |

## Rough cut v01 (2026-11-23)

`production/exports/demo-d01-roughcut/demo-d01-roughcut-v01.mp4` (gitignored), 25.0 s: sh01 0.8–5.8 s, sh02 0–4 s, sh03 0–6 s, sh04b with the post overlay 1.0–6.0 s, sh05 0–5 s. Each clip keeps its own audio with 30 ms fades. No jingle, no end card and no mix yet. Encoded with libopenh264 8 Mb/s because this ffmpeg build has no libx264.

## Rough cut v02 (2026-11-23)

`production/exports/demo-d01-roughcut/demo-d01-roughcut-v02.mp4` (gitignored), 25.0 s: the same as v01, except that shot 4 is **version A** (the showrunner's pick, "Version A (Flow)"), trimmed to 2.5–7.5 s so it covers the line (speech 3.44–7.4 s).

## Rough cut v03 (2026-11-23)

`production/exports/demo-d01-roughcut/demo-d01-roughcut-v03.mp4` (local; it was in Git LFS until the final cut replaced it), 25.0 s: as v02, with shot 3 **v02** trimmed to 1.0–7.0 s (speech 1.72–6.5 s).

**All picture takes are selected** (showrunner, 2026-11-23: "Accept all four", after "Version A (Flow)" for shot 4). Rough cut v03 is the picture lock candidate.

**Storage (showrunner, 2026-11-23):** the golden versions are committed with Git LFS: the five selected takes (`<shot>-<take>.mp4` beside each shot's exports) and the current cut, now the final commercial `demo-d01-v01.mp4` (rough cut v03 was removed from the tree when the final replaced it; its LFS object stays in history). Rejected takes, the 4B overlay and rough cuts v01–v02 stay local only; their logs keep the checksums.

## Music (2026-11-23)

Made in Google Flow Music with `aao web audio flow-music` (prompt only; AAO gap 6). Prompts: [production/prompts/d01-commercial.md](../../prompts/d01-commercial.md#music-google-flow-music-via-aao-web-audio-flow-music).

| Take | Status | Flow Music title | Length | Agent notes | Log |
| --- | --- | --- | --- | --- | --- |
| `demo-d01-jingle` v01 | rejected (agent) | Better Call Sophie | 103.3 s | Full song with invented handyman lyrics; the tag is unclear | [log](../../generation-logs/demo-d01-jingle-v01.yaml) |
| `demo-d01-jingle` v02 | **selected** (showrunner, 2026-11-23) | Prime Time Commercial Jingle | 61.6 s | Instrumental, no vocals: the bed | [log](../../generation-logs/demo-d01-jingle-v02.yaml) |
| `demo-d01-jingle-tag` v01 | **selected** (showrunner, 2026-11-23) | Better Call Sophie! (Jingle) | 60.2 s | Opens with exactly "Better call Sophie!" and a chord (0–3.6 s used) | [log](../../generation-logs/demo-d01-jingle-tag-v01.yaml) |

Flow Music ignored the requested lengths every time; trimming in the edit solves it.

## Mix v01 (2026-11-23)

`production/exports/demo-d01-mix/demo-d01-mix-v01.mp4`, **30.0 s, −14.5 LUFS**, **approved by the showrunner** (2026-11-23, "Approve, do end card"):

- Picture: rough cut v03 (25.0 s), then 5.0 s of the approved exterior plate `office-exterior-dusk` as the end card background. The end-card lettering is not made yet.
- Dialogue: each shot's own audio.
- Bed: jingle v02, 1.85–26.85 s, at 0.55 gain, faded, ducked under the dialogue with ffmpeg `sidechaincompress`.
- Tag: tag v01, 0–3.6 s, placed at 26.2 s so the chord ends just before 30 s.
- Master: ffmpeg `loudnorm` to −14 LUFS, true peak −1.5 dB.
- Whisper on the mix: all four lines word-perfect over the music; the tail alone reads "Better call Sophie!".
## End card and final cut v01 (2026-11-23)

- **End card** (`demo-d01-sh06` v01, [record](../../generation-logs/demo-d01-sh06-v01.yaml)): made in post with [scripts/end_card.py](../../../scripts/end_card.py) over the approved exterior plate, in the poster's colors. "BETTER CALL" slides in, "SOPHIE" lands on the sung "Sophie!", then the swoosh, the phone number 505-555-0148 and the fine print.
- **Commercial** `production/exports/demo-d01-final/demo-d01-v01.mp4`, **FINAL** (showrunner, 2026-11-23, "Approve as final"), **in Git LFS**: mix v01's picture for 0–25 s, then the end card, with mix v01's sound unchanged. **30.0 s, −14.5 LUFS, 1280x720, 24 fps.**
- Rebuild: the mix with [scripts/d01_mix.ps1](../../../scripts/d01_mix.ps1), the end card with `scripts/end_card.py`, then the ffmpeg concat in the end-card record.
**D01 is final** (2026-11-23) and **published** (2026-11-24): https://www.youtube.com/watch?v=iZbO5J0NBl4. Uploaded with youtube-mcp: private upload, then tags, category, not made for kids and the altered or synthetic content flag, then public; each step approved by the showrunner. Details in the [end-card record](../../generation-logs/demo-d01-sh06-v01.yaml).
