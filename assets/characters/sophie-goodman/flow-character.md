# Sophie Goodman — Google Flow character record

**Status:** the Flow character exists (created by hand during the tutorial). On **2026-11-23** its Portrait and Body images were replaced with the **approved age-27 face** (portrait v02) and the approved info text was entered (block below). The voice **Kore** (attached since the tutorial) was **approved by the showrunner on 2026-11-23** after the voice shortlist below.

This file mirrors Sophie's character in Google Flow, so the repo stays the source of truth for what that character should be. The canon itself is in [spec/canon.md](../../../spec/canon.md) and [story/characters/sophie-goodman.md](../../../story/characters/sophie-goodman.md).

## Synced from Flow

Fill this in only from a real read of Flow (a command or the showrunner). Never guess.

```yaml
flow_project_title: "Better Call Sophie - Flow Experiments"
flow_project_id: c9df3f16-dbf1-459b-a447-b20fbd978552
flow_character_id: 63d772dc-71bc-4c69-b14c-6b28a68d9cfe
flow_character_name: "Sophie Goodman"
reference_images:
  - view: Portrait
    made_with: >-
      Character page edit box, 2026-11-23T01:23:53-07:00, Nano Banana 2.1: attached
      sophie-portrait-age27-v02.jpg (show project media) with the prompt "Replace the portrait with the
      attached image: use the attached photo of the woman exactly as it is, the same face, hair, earrings,
      cream blouse, burgundy blazer, light gray background, framing and lighting. Do not change her face or
      age." Flow also passed the old portrait in as an input. Selected in the history panel and saved with Done.
    size: 1376x768 JPEG
    local_copy: production/exports/characters/sophie-goodman/flow-character-portrait-age27.jpg  # gitignored
    sha256: F68F741FC7CEBAD73355BC3020E8B5BF591E5CB11F81462F2648BB22145E91DA
    repo_copy: assets/characters/sophie-goodman/reference-front.webp   # WebP of portrait v02, the approved source image
    approved_as_canonical_face: true   # showrunner chose portrait v02, 2026-11-23
  - view: Body
    made_with: >-
      Character page edit box, 2026-11-23T01:25:23-07:00, Nano Banana 2.1: attached
      sophie-portrait-age27-v02.jpg with the prompt "Redo this full-body triptych with the woman from the
      attached portrait: her exact face, age, dark wavy hair loosely pinned up and gold hoop earrings. Keep the
      three views (front facing, 3/4 side view and back view), the deep burgundy tailored pantsuit, the cream
      blouse, dark shoes, flat studio lighting and a plain light gray background. Same woman in all three
      views." Selected in the history panel and saved with Done.
    size: 1376x768 JPEG
    local_copy: production/exports/characters/sophie-goodman/flow-character-body-age27.jpg  # gitignored
    sha256: 73F337C7B4BCAC731DA5548F38F07DE0FD7CBA6CC4ACEAC06409C8136E8FD264
    repo_copy: assets/characters/sophie-goodman/reference-body.webp
previous_images:   # still in the character's history panel
  - "Portrait: tutorial image, 'Medium studio shot of a 33-year-old woman ...', sha256 5FC1EE6107C534C7F901BAB62B53B43797AC236F372812035248E278312C78E6 (flow-character-portrait-original.jpg)"
  - "Body: tutorial triptych, 'Full-body triptych, three distinct views: front facing, 3/4 side view and back view ...' (not downloaded)"
info_text_in_flow: approved info text below + blank line + approved voice paragraph below; entered 2026-11-23 and read back after a reload (1,034 characters, exact match)
voice_in_flow: kore             # shown on the character page; Flow lists it as "Kore — Female, firm, mid pitch"; approved by the showrunner 2026-11-23 ("Keep kore")
model_shown_on_character_page: "Nano Banana 2.1"   # model picker in the character's edit box
last_synced: 2026-11-23
synced_by: "playwright-cli -s=aao-web-gemini on the character page (edit, then reload and read back); images fetched at =s0 in the signed-in session"
```

**Gotcha:** generating in the character's edit box adds the result to the history panel, but after a reload the character still shows the old image. Click the new history entry, then **Done**, for each view (Portrait and Body separately), and reload to check.

The project also holds a second character, **The Client** (ID not read). AAO's `aao flow download` timed out on the character tile, so the portrait was fetched from the URL the character page shows (`=s0`, the original size) inside the signed-in browser.

### Age check (2026-11-22)

**Result: does not read as 26–28.** The face reads early-to-mid thirties (fine lines at the eyes and mouth), which matches the "33-year-old" in its generation prompt. Wardrobe, hair, earrings and skin tone match the canon. Next: generate a new portrait with the age-27 prompt below and replace the character image before the voice is chosen.

### Age-27 portrait takes (2026-11-23)

Made in the work project `d0b10764-5004-4f27-9269-a447a70807fe` with the prompts in [production/prompts/sophie-portrait-age27.md](../../../production/prompts/sophie-portrait-age27.md). **The showrunner chose v02 on 2026-11-23** as Sophie's canonical face. It is uploaded to the show project as `sophie-portrait-age27-v02.jpg` and is now the character's image (see the block above). Repo copies: [reference-front.webp](reference-front.webp) (portrait v02) and [reference-body.webp](reference-body.webp) (the character's new Body triptych).

| Take | Route | Agent verdict | Log |
| --- | --- | --- | --- |
| v01 | Approved prompt, no reference | Reads late twenties to about thirty; a new, calmer face that matches neither the poster nor the current portrait | [log](../../../production/generation-logs/sophie-portrait-age27-v01.yaml) |
| v02 | Approved prompt + the poster concept art as reference | **Approved (canonical face).** Closest to the concept art (strong brows, loose curls, wry half-smile); reads late twenties, upper end | [log](../../../production/generation-logs/sophie-portrait-age27-v02.yaml) |
| v03 | Approved prompt + the current Flow portrait as reference, asked to be younger | Rejected by the agent: almost unchanged, still early thirties | [log](../../../production/generation-logs/sophie-portrait-age27-v03.yaml) |

Done on 2026-11-23: character image replaced, info text entered, repo copies made. Next: shortlist voices, and regenerate the poster and business card with this face.

**How to sync:** AAO cannot read characters yet (gap 3 in [spec/flow-automation.md](../../../spec/flow-automation.md)). Until it can, either:

- the showrunner copies the fields above from Flow's Characters page, or
- an agent on the showrunner's computer opens the character page with playwright-cli (`playwright-cli -s=aao-web-gemini …`, read-only) and records what it shows.

Also download the character's reference image(s) with `aao flow download <project> <media>`. Keep a small copy here as `reference-front.png` once the showrunner approves it as the canonical face.

## APPROVED — info text to put into Flow (showrunner, 2026-11-22)

Short, visual and voice-focused, so Flow can use it. Story backstory stays in the repo.

```text
Dr. Sophie Goodman, late twenties, a young PhD moral philosopher who runs a small, loudly advertised "philosophical advocacy" practice in Albuquerque in 2030. Dark brown wavy hair loosely pinned up, warm light-medium skin, small gold hoop earrings, cream blouse under a deep burgundy tailored pantsuit. Confident, quick, theatrical when selling, quiet and precise when thinking. Wry half-smile; rarely raises her voice. Speaks American English, fast but clear, with dry humor.
```

Approved, with her age updated to late twenties to match the age lock. **Entered in Flow on 2026-11-23** with playwright-cli (AAO cannot edit characters yet; gap 4).

**Check the portrait first.** The existing Flow portrait was generated from the tutorial prompt, which said "age about 33". If it doesn't read as late twenties, generate a new portrait with the prompt below. Then rebuild the character, or replace its image, before choosing the voice. Keep the old image only as a record.

```text
A realistic television casting reference photograph of a fictional woman named Sophie Goodman, age about 27. Dark brown wavy hair loosely pinned up, confident intelligent eyes, warm light-medium skin tone, subtle makeup, small gold hoop earrings, cream blouse and deep burgundy tailored blazer. Neutral light gray studio background, soft even lighting, camera at eye level, shoulders and face unobscured, natural expression. No writing, posters, props, extra people, watermarks or stylization. This is a consistent original fictional character design, not a portrait of a real actor.
```

## APPROVED — voice description added to the info text (showrunner, 2026-11-23)

The showrunner asked for more description of the voice in Flow. The character page has no separate voice-description field: it has the voice picker and one **Character info** box ("Describe how your character acts…", no length limit in the page). So the voice description goes there, appended after the approved text above, which stays unchanged.

```text
Voice (Kore): a firm, clear, mid-pitched woman's voice in her late twenties, General American accent. She talks fast but crisply and lands the key word of each argument with a short pause. Selling, she is bright and theatrical, with a local TV-ad rhythm and a smile you can hear. Thinking or arguing, she drops lower and quieter: short sentences, precise, a deliberate pause before a conclusion. Her dry humor is deadpan; the joke is in the timing. When angry she gets quieter and slower, never louder. Never breathy, whispery, sing-song or announcer-like.
```

Why these lines:

- Kore's own label is "firm, mid pitch"; the text names it, so the description and the picked voice agree.
- The two modes (selling and thinking) come from the approved info text and the series bible's "theatrical" persona. Flow can then match the delivery to the scene.
- "Quieter when angry" gives the director a consistent rule for confrontation scenes, and follows "rarely raises her voice".
- The "never" list repeats the voice brief's exclusions, which are the common failure modes of generated voices.
- No real person, actor or character is named, so it cannot drift into a sound-alike.

**Approved** by the showrunner on 2026-11-23 ("Good add it"). **Entered in Flow on 2026-11-23** with playwright-cli: the Character info box now holds the approved info text, a blank line, then this paragraph (1,034 characters). Saved with Done; after a reload the box matched the entered text exactly and the voice still showed kore.

## Voice selection — Kore (APPROVED 2026-11-23)

The showrunner kept **Kore** ("Keep kore", 2026-11-23). Use it for every Sophie shot. The brief and shortlist below are kept as the record of the choice.

- **Listen for:** a female voice that sounds late twenties, with a clear mid-range pitch, warm, fast and articulate. Not breathy, not announcer-like, and no accent beyond General American.
- **Test line** (read in two moods, salesy and serious): *"Legality is your lawyer's problem. Morality? That's mine."*
- Record the chosen voice name here and in `voice_in_flow`. Do not use a real person's voice or a sound-alike.

**Decided:** Kore, by the showrunner on 2026-11-23.

### Shortlist (PROPOSED, 2026-11-23)

Read from the character page's **Select a voice** dialog (click the voice name) in the show project on 2026-11-23. The dialog lists 30 built-in voices, each with a one-line description. The agent did not select anything; the character still has **kore**. The agent has not listened to the voices, so this shortlist goes by Flow's descriptions only.

To listen, use the play button in that dialog, or open the sample file Flow plays. These are public files on `gstatic.com`, which Flow loads when you preview a voice (pattern seen in the page: `https://www.gstatic.com/aitestkitchen/voices/samples/<Name>.wav`).

| Voice | Flow's description | Shortlist | Why | Sample |
| --- | --- | --- | --- | --- |
| Kore | Female, firm, mid pitch | **yes** (current) | Firm and mid pitch fit "confident, quick, rarely raises her voice" | [Kore.wav](https://www.gstatic.com/aitestkitchen/voices/samples/Kore.wav) |
| Erinome | Female, clear, mid pitch | **yes** | "Clear" fits "fast but clear, articulate" | [Erinome.wav](https://www.gstatic.com/aitestkitchen/voices/samples/Erinome.wav) |
| Sulafat | Female, warm, mid pitch | **yes** | "Warm" is in the brief | [Sulafat.wav](https://www.gstatic.com/aitestkitchen/voices/samples/Sulafat.wav) |
| Autonoe | Female, bright, mid pitch | **yes** | Bright and mid pitch suit the salesy side | [Autonoe.wav](https://www.gstatic.com/aitestkitchen/voices/samples/Autonoe.wav) |
| Despina | Female, smooth, mid pitch | **yes** | Smooth and mid pitch suit the quiet, precise side | [Despina.wav](https://www.gstatic.com/aitestkitchen/voices/samples/Despina.wav) |
| Callirrhoe | Female, easy-going, mid pitch | maybe | Mid pitch, but "easy-going" may be too relaxed for fast talk | [Callirrhoe.wav](https://www.gstatic.com/aitestkitchen/voices/samples/Callirrhoe.wav) |
| Aoede | Female, breezy, mid pitch | no | "Breezy" risks the breathy sound the brief rules out | |
| Achernar | Female, soft, high pitch | no | High pitch and soft | |
| Gacrux | Female, mature, mid pitch | no | "Mature" works against late twenties | |
| Laomedeia | Female, upbeat, mid-high pitch | no | Above mid pitch | |
| Leda | Female, youthful, mid-high pitch | no | Above mid pitch; may read younger than 27 | |
| Zephyr | Female, bright, mid-high pitch | no | Above mid pitch | |
| Vindemiatrix | Female, gentle, mid pitch | no | "Gentle" undersells the theatrical sales mode | |
| Pulcherrima | Ungendered, forward, mid-high pitch | no | Brief asks for a female voice | |

The other 16 voices are listed as male: Achird, Algenib, Algieba, Alnilam, Charon, Enceladus, Fenrir, Iapetus, Orus, Puck, Rasalgethi, Sadachbia, Sadaltager, Schedar, Umbriel and Zubenelgenubi.

## Other demo characters (PROPOSED, not created)

| Character | Needed for | Look anchor |
| --- | --- | --- |
| The Client (tech executive) | Commercial, consultation test | Man in his late forties, navy suit, pale blue shirt, tired expression |
| Daniel Park | Walk-and-talk test | Korean American, about 30, AI engineer/marketer, casual blazer, sneakers, tablet |
| Integrity Index panelist | Hearing test | Woman in her fifties, gray bob, charcoal suit, reading glasses |

Use original fictional people only, never real actors' likenesses. Each one gets a record like this file once it is created in Flow.
