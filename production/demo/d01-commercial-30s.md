# D01 — "Better Call Sophie" 30-second commercial

**Status:** PROPOSED script; **first takes of every shot generated on 2026-11-23** (shot record: [production/shot-lists/demo/demo-d01.md](../shot-lists/demo/demo-d01.md)). No take is selected yet; the jingle, end card and mix are not made. Showrunner decisions on 2026-11-23: shot 4 is made in two versions (generated chalk text vs text added in post), and the end card matches the approved poster's colors.

An in-world local TV ad for Goodman Philosophical Consulting, in the spirit of grandpa's ads: earnest, a little cheesy, very sure of itself. It also works as the show's teaser. The ad shows her **mixed** starting stance: she's openly selling, but what she sells is a real principle.

**Needs first:** the Sophie character (with voice) and the office pack's golden-hour views. The Client and his kitchen in shot 2 are a **throwaway one-shot cameo** (showrunner, 2026-11-23): no reference image, no Flow character and no continuity check; describe them in the prompt and take what Flow gives.

## Script and shots

| Shot | Time | Camera / location | Action and dialogue | Audio |
| --- | --- | --- | --- | --- |
| `demo-d01-sh01` | 0:00–0:05 | `cam-c` wide, office, golden hour | Sophie turns from the chalkboard to face the camera, chalk in hand. **SOPHIE:** "Has the internet decided you're a bad person?" | Jingle bed starts |
| `demo-d01-sh02` | 0:05–0:09 | A client's kitchen at night, medium close (one-shot cameo, no references) | A tired man in his late forties stares at his phone, its glow on his face (no readable screen), and winces as it buzzes again and again. Silent | Phone buzz SFX over the bed |
| `demo-d01-sh03` | 0:09–0:15 | `cam-a`, Sophie at her desk | She leans forward. **SOPHIE:** "Your lawyer handles what's legal. I handle what's *defensible*." | Bed |
| `demo-d01-sh04` | 0:15–0:20 | `cam-d`, at the chalkboard | She taps "IS ≠ OUGHT" chalked on the board beside the trolley drawing. **SOPHIE:** "I won't say you're right. I'll make sure you get a *good argument*." Made two ways and compared (see [Shot 4 test](#shot-4-test-chalk-text-generated-vs-added-in-post)) | Bed |
| `demo-d01-sh05` | 0:20–0:25 | `cam-a` close-up | She points at the lens and gives a wry smile. **SOPHIE:** "Morally questionable? Philosophically defensible." | Bed builds |
| `demo-d01-sh06` | 0:25–0:30 | End card, made in post over the `office-exterior-dusk` plate | Animated title "BETTER CALL SOPHIE" in the approved poster's colors and lettering style (see [End card](#end-card)), phone **505-555-0148**, and fine print: *"Dr. Goodman is not a lawyer. Nothing in this ad is legal advice. Or moral advice. Probably."* | Sung tag "Better call Sophie!" and a button chord |

The total is 30 s, cut to exactly 30.0 s in the edit. The lines are new and PROPOSED. The tagline and phone number come from the existing concept art (fictional 555 number).

## Prompt pattern (for each speaking shot)

```text
@Sophie Goodman in her Albuquerque philosophical consulting office, matching the office reference image: [camera position], golden-hour light through half-open blinds, banker's lamp on. Same deep burgundy pantsuit, cream blouse, gold hoops and loosely pinned dark wavy hair as her character reference. Shot in the style of a slightly cheesy, confident local TV commercial, looking straight into the lens. She says clearly in English: "[line]". Exactly one speaker. Static camera. No subtitles, no on-screen text, no logos, no extra people.
```

Ingredients for each shot: the Sophie character (or her portrait), plus the matching office view from the location pack.

## Shot 4 test: chalk text generated vs added in post

**Showrunner direction (2026-11-23):** in the test run, generate the chalk text in the video and use that take as the reference; also generate the shot without the text, and experiment with adding the text onto the board surface reliably with traditional editing tools.

This is a deliberate exception to the demo rule that readable text is added in post: it measures how far Flow can be trusted with text, against the post route.

| Version | Shot ID | How | Board in the prompt |
| --- | --- | --- | --- |
| **A — generated text (reference)** | `demo-d01-sh04a` | Flow generates the chalk text | The trolley drawing plus "IS ≠ OUGHT" in white chalk capitals to its right; the prompt's "no on-screen text" clause becomes "no other text" |
| **B — clean plate + post** | `demo-d01-sh04b` | Flow generates the shot with a blank area on the board; the text is composited afterwards | Only the trolley drawing, and an empty, clean patch of slate to its right where she taps |

**Version B overlay, with traditional tools only.** No AI regeneration, inpainting or video-to-video for the text. Try these in order, simplest first, and log what was used:

1. **Static camera (the shot's default):** pick the four board corners of the blank patch on one frame. Warp a chalk-text image onto them with ffmpeg (`perspective` filter, or `overlay` after an OpenCV `warpPerspective`), for the whole clip.
2. **If the camera drifts:** track the board with OpenCV (feature tracking on the board's frame and the trolley drawing, then `findHomography` per frame) and warp the text with that homography. Blender's motion tracker with a plane track is the fallback.
3. **When her hand crosses the text:** build the text's matte from the board itself. Show the text only where the frame is dark slate (a luminance key on the board area), so her hand and sleeve, which are lighter than the board, cover the text naturally. Fall back to a hand-drawn roto mask for the frames where the key fails.
4. **Make it look like chalk:** use a chalk-style text image (rough edges, slight transparency, a hint of dust), blend it with screen or lighten so the board texture shows through, match the shot's warm grade, and add a little blur and grain.

**Text source for B:** "IS ≠ OUGHT" rendered from a font (scripted, so the spelling is exact) or written in chalk on a real board and photographed. Record which.

**Compare A and B on:** spelling in every frame; whether the text stays put on the board (no swimming or flicker); whether her hand covers it correctly; whether it looks like chalk on that board; time and number of retries. The comparison goes in the shot records and decides the rule for the OP, T4 and the pilot.

### First results (2026-11-23, one take each)

| | A — generated ([log](../generation-logs/demo-d01-sh04a-v01.yaml)) | B — clean plate + post ([log](../generation-logs/demo-d01-sh04b-v01.yaml)) |
| --- | --- | --- |
| Spelling | Correct in every sampled frame, plus an underline under "IS" that was not asked for | Exact by construction (rendered from a font) |
| Stays on the board | Yes | Yes: OpenCV tracking, corners within 3.4 px of the pinned position over 192 frames |
| Hand over the text | Not tested: she taps the switch figure, not the words | Not tested: she taps the trolley, not the empty corner |
| Looks like chalk | Yes; Flow's chalk is bolder and matches the drawing | Convincing in the slate texture and sun stripes; strokes thinner than the drawing's |
| Effort | 1 generation, about 45 s | 1 generation plus one script run (a few seconds) after picking the four corners by eye |
| Line (Whisper) | Word-perfect | Word-perfect |

Both routes worked on the first try for a static camera. B gives exact control of wording and lettering and needs only four corner points per shot; A needs no post work but cannot guarantee spelling, and added an underline unasked. Neither take tested a hand crossing the text; a third take where she writes or taps on the words would test the matte.

Tools: [scripts/chalk_overlay.py](../../scripts/chalk_overlay.py) (overlay) and [scripts/check_lines.py](../../scripts/check_lines.py) (Whisper line check).

## End card

**Showrunner direction (2026-11-23):** match the colors of the approved poster ([poster-tv-4x3.webp](../../assets/marketing/poster-tv-4x3.webp)). "BETTER CALL" in white bold italic sans-serif capitals and "SOPHIE" larger, in golden-yellow bold italic with a gold swoosh underline, as on the poster. The phone number and the fine print go in the poster's cream serif italic. All of it is made in post. The poster's lettering was generated by Flow, so there is no font file: use the closest fonts, or cut the lettering out of the poster art; record which.

## Music (Flow Music, PROPOSED prompt)

```text
A 30-second original retro local-TV commercial jingle: bright brass stabs, cheesy electric organ, slap bass and handclaps, optimistic and slightly over-the-top. Instrumental bed for 25 seconds, then a short group vocal tag singing "Better call Sophie!" ending on a big button chord. Original melody; not in the style of any existing TV theme.
```

Generate several takes and pick one. Trim it to the cut in the edit. If the sung words come out wrong, use the instrumental and add the tag as a separate generation.

## Post-production

1. Assemble sh01–sh05 and the end card with ffmpeg (scripted) or Remotion (`external/remotion`) for the animated title. Also try Flow's Scenebuilder as a comparison.
2. Mix: dialogue first, jingle bed lowered under speech, end at about −14 LUFS for YouTube.
3. Check with Whisper that each line matches the script word for word.
4. Upload to [@better-call-sophie](https://www.youtube.com/@better-call-sophie) with the AI-generated and unofficial-fan-work disclosure.

## Pass criteria

- Sophie reads as the same person in sh01, sh03, sh04 and sh05.
- The office is recognizably the same room across three camera positions.
- All four lines are word-perfect and lip sync is acceptable.
- Shot 4: versions A and B are both made and compared; the cut uses whichever the showrunner picks.
- The final file is 30.0 s, and the end-card text is correct (made in post).
