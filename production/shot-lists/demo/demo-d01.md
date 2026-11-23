# D01 commercial — shot record

Script and plan: [production/demo/d01-commercial-30s.md](../../demo/d01-commercial-30s.md). Prompts: [production/prompts/d01-commercial.md](../../prompts/d01-commercial.md). First test run: **2026-11-23**, one take per shot, all in the show project with Omni 1.2 Flash, 720p, 8 s.

The agent may mark takes `generated` or `rejected`; only the showrunner sets `selected` or `final`.

| Shot | Take | Status | Flow name | Line (Whisper) | Agent notes | Log |
| --- | --- | --- | --- | --- | --- | --- |
| `demo-d01-sh01` | v01 | generated | Woman at chalkboard holding chalk | word-perfect | Office matches the wide master well; she walks toward the camera after turning | [log](../../generation-logs/demo-d01-sh01-v01.yaml) |
| `demo-d01-sh02` | v01 | generated | Man staring at phone | silent (buzz only) | One-shot cameo, no references by design; screen faces away | [log](../../generation-logs/demo-d01-sh02-v01.yaml) |
| `demo-d01-sh03` | v01 | generated | Woman speaking at desk | word-perfect | Sophie consistent; **office restyled** against cam-a (plants, globe, clock; no laptop or bust) | [log](../../generation-logs/demo-d01-sh03-v01.yaml) |
| `demo-d01-sh04a` | v01 | generated | Woman tapping chalkboard with text | word-perfect | Version A: Flow's chalk text correct and stable, plus an unasked underline | [log](../../generation-logs/demo-d01-sh04a-v01.yaml) |
| `demo-d01-sh04b` | v01 | generated | Woman tapping chalkboard with chalk | word-perfect | Version B: clean board; text added in post with `scripts/chalk_overlay.py` | [log](../../generation-logs/demo-d01-sh04b-v01.yaml) |
| `demo-d01-sh05` | v01 | generated | Woman pointing and speaking | word-perfect | Points at the lens, wry smile and a wink | [log](../../generation-logs/demo-d01-sh05-v01.yaml) |

## Rough cut v01 (2026-11-23)

`production/exports/demo-d01-roughcut/demo-d01-roughcut-v01.mp4` (gitignored), 25.0 s: sh01 0.8–5.8 s, sh02 0–4 s, sh03 0–6 s, sh04b with the post overlay 1.0–6.0 s, sh05 0–5 s. Each clip keeps its own audio with 30 ms fades. No jingle, no end card and no mix yet. Encoded with libopenh264 8 Mb/s because this ffmpeg build has no libx264.

Still to do for D01: the showrunner picks takes (and A or B for shot 4); the Flow Music jingle; the end card in post; the mix; the YouTube upload.
