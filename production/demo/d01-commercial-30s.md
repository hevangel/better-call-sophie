# D01 — "Better Call Sophie" 30-second commercial

**Status:** PROPOSED script and shots; not generated.

An in-world local TV ad for Goodman Philosophical Consulting, in the spirit of grandpa's ads: earnest, a little cheesy, very sure of itself. It also works as the show's teaser. The ad shows her **mixed** starting stance: she's openly selling, but what she sells is a real principle.

**Needs first:** the Sophie character (with voice), the Client reference, and the office pack's golden-hour views.

## Script and shots

| Shot | Time | Camera / location | Action and dialogue | Audio |
| --- | --- | --- | --- | --- |
| `demo-d01-sh01` | 0:00–0:05 | `cam-c` wide, office, golden hour | Sophie turns from the chalkboard to face the camera, chalk in hand. **SOPHIE:** "Has the internet decided you're a bad person?" | Jingle bed starts |
| `demo-d01-sh02` | 0:05–0:09 | The Client's kitchen at night, medium close | The Client stares at his phone, its glow on his face (no readable screen), and winces as it buzzes again and again. Silent | Phone buzz SFX over the bed |
| `demo-d01-sh03` | 0:09–0:15 | `cam-a`, Sophie at her desk | She leans forward. **SOPHIE:** "Your lawyer handles what's legal. I handle what's *defensible*." | Bed |
| `demo-d01-sh04` | 0:15–0:20 | `cam-d`, at the chalkboard | She taps "IS ≠ OUGHT". **SOPHIE:** "I won't say you're right. I'll make sure you get a *good argument*." | Bed |
| `demo-d01-sh05` | 0:20–0:25 | `cam-a` close-up | She points at the lens and gives a wry smile. **SOPHIE:** "Morally questionable? Philosophically defensible." | Bed builds |
| `demo-d01-sh06` | 0:25–0:30 | End card, made in post over the `office-exterior-dusk` plate | Animated yellow-red title "BETTER CALL SOPHIE", phone **505-555-0148**, and fine print: *"Dr. Goodman is not a lawyer. Nothing in this ad is legal advice. Or moral advice. Probably."* | Sung tag "Better call Sophie!" and a button chord |

The total is 30 s, cut to exactly 30.0 s in the edit. The lines are new and PROPOSED. The tagline and phone number come from the existing concept art (fictional 555 number).

## Prompt pattern (for each speaking shot)

```text
@Sophie Goodman in her Albuquerque philosophical consulting office, matching the office reference image: [camera position], golden-hour light through half-open blinds, banker's lamp on. Same deep burgundy pantsuit, cream blouse, gold hoops and loosely pinned dark wavy hair as her character reference. Shot in the style of a slightly cheesy, confident local TV commercial, looking straight into the lens. She says clearly in English: "[line]". Exactly one speaker. Static camera. No subtitles, no on-screen text, no logos, no extra people.
```

Ingredients for each shot: the Sophie character (or her portrait), plus the matching office view from the location pack.

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
- The final file is 30.0 s, and the end-card text is correct (made in post).
