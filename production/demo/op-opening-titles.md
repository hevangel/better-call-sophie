# OP — opening title sequence

**Status:** PROPOSED concept, song and shots; not generated.

**Length:** 30 s for the pilot. Optionally a 60 s full-song version for YouTube. This matches a 5–8 minute episode: long enough to have a real song, short enough not to eat the runtime.

## Concept: "Arguments as objects"

A music-driven montage with no dialogue. Ordinary objects act out philosophical problems, cut to the beat, ending on Sophie and the title. Silent stylized shots are what Flow produces most reliably, so the OP needs little character continuity. Only the last two shots show Sophie.

| Shot | Beat | Image (text, if any, added in post) |
| --- | --- | --- |
| `demo-op-sh01` | 0:00–0:03 | Macro shot: chalk scrapes across a slate board in a puff of dust |
| `demo-op-sh02` | 0:03–0:06 | A toy train on a desk reaches a track switch; a hand in a burgundy sleeve hovers over the lever (trolley problem) |
| `demo-op-sh03` | 0:06–0:09 | Brass scales on the walnut desk tip back and forth between a thick law book and a worn green paperback |
| `demo-op-sh04` | 0:09–0:13 | Timelapse of the Albuquerque skyline at dusk, the Sandia Mountains turning pink |
| `demo-op-sh05` | 0:13–0:16 | A stack of Goodman business cards fans out across the desk in slow motion |
| `demo-op-sh06` | 0:16–0:19 | A small Socrates bust on a bookshelf, with sunlight sweeping across it |
| `demo-op-sh07` | 0:19–0:23 | The yellow-red storefront decal flickers on at dusk, seen from the parking lot |
| `demo-op-sh08` | 0:23–0:26 | Sophie, backlit in silhouette in the office doorway, turns her head toward the camera |
| `demo-op-sh09` | 0:26–0:30 | Title card in post: "BETTER CALL SOPHIE" over a slow push-in on the empty client chair |

## Theme song (Flow Music, PROPOSED)

```text
An original upbeat theme song for a dark-comedy TV show about a witty philosopher in Albuquerque. Desert surf-rock twang guitar, upright bass, brushed drums, a little lounge-jazz organ; dry, playful, a little dangerous. Female lead vocal, conversational and sly. 30-second TV edit with a strong hook at the end on the words "Better call Sophie." Original melody, not in the style of any existing TV theme.
```

Proposed lyrics (original). AAO cannot pass lyrics separately yet (gap 6), so they go in the prompt text, or are entered by hand in Flow Music:

```text
Somebody says that you've done something wrong,
somebody's certain, and the crowd is strong.
Don't call a lawyer — the law's not the why...
Better call Sophie. She'll tell you why.
```

Generate several songs; the showrunner picks the theme. The chosen song then becomes the **theme music** reference for all later cues (a new decision to record in `spec/canon.md`).

## Technical pieces tested

- Song generation and selection in Flow Music, and download through `aao web audio flow-music`
- Shots with no characters, macro shots and timelapse
- Cutting to the beat (find beat times with ffmpeg or an audio tool, then cut on them)
- Animated title typography (Remotion), kept as a reusable title template
- The burgundy sleeve and the office props match the location pack

## Pass criteria

The song works as a theme the showrunner would actually keep. The cuts land on beats. The title card text is correct. The two Sophie shots are believable as her.
