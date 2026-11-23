# Sophie Goodman — Google Flow character record

**Status:** the Flow character exists (created by hand during the tutorial) and was **synced read-only on 2026-11-22** (block below). Flow shows **no info text** and a voice named **kore** already attached; that voice was not chosen against the brief below, so the voice decision is still open. The current portrait **does not read as 26–28** (see the age check below).

This file mirrors Sophie's character in Google Flow, so the repo stays the source of truth for what that character should be. The canon itself is in [spec/canon.md](../../../spec/canon.md) and [story/characters/sophie-goodman.md](../../../story/characters/sophie-goodman.md).

## Synced from Flow

Fill this in only from a real read of Flow (a command or the showrunner). Never guess.

```yaml
flow_project_title: "Better Call Sophie - Flow Experiments"
flow_project_id: c9df3f16-dbf1-459b-a447-b20fbd978552
flow_character_id: 63d772dc-71bc-4c69-b14c-6b28a68d9cfe
flow_character_name: "Sophie Goodman"
reference_images:
  - flow_media: 'project media #10, "Character thumbnail" (Portrait view; a Body view tab also exists, not read)'
    size: 1376x768 JPEG
    local_copy: production/exports/characters/sophie-goodman/flow-character-portrait-original.jpg  # gitignored
    sha256: 5FC1EE6107C534C7F901BAB62B53B43797AC236F372812035248E278312C78E6
    flow_generation_prompt_head: "Medium studio shot of a 33-year-old woman, perfectly centered and forward-facing. ..."  # from the character's History panel
    approved_as_canonical_face: false
info_text_in_flow: ""           # "Character info (optional)" box is empty
voice_in_flow: kore             # shown on the character page; not chosen by the showrunner against the voice brief
model_shown_on_character_page: "Nano Banana 2.1"   # model picker in the character's edit box
last_synced: 2026-11-22
synced_by: "aao flow read + playwright-cli -s=aao-web-gemini (read-only character page); image fetched in the signed-in session"
```

The project also holds a second character, **The Client** (ID not read). AAO's `aao flow download` timed out on the character tile, so the portrait was fetched from the URL the character page shows (`=s0`, the original size) inside the signed-in browser.

### Age check (2026-11-22)

**Result: does not read as 26–28.** The face reads early-to-mid thirties (fine lines at the eyes and mouth), which matches the "33-year-old" in its generation prompt. Wardrobe, hair, earrings and skin tone match the canon. Next: generate a new portrait with the age-27 prompt below and replace the character image before the voice is chosen.

### Age-27 portrait takes (2026-11-23)

Made in the work project `d0b10764-5004-4f27-9269-a447a70807fe` with the prompts in [production/prompts/sophie-portrait-age27.md](../../../production/prompts/sophie-portrait-age27.md). None has replaced the character image yet. **Decision needed:** pick a take to become Sophie's face, or ask for more.

| Take | Route | Agent verdict | Log |
| --- | --- | --- | --- |
| v01 | Approved prompt, no reference | Reads late twenties to about thirty; a new, calmer face that matches neither the poster nor the current portrait | [log](../../../production/generation-logs/sophie-portrait-age27-v01.yaml) |
| v02 | Approved prompt + the poster concept art as reference | Closest to the concept art (strong brows, loose curls, wry half-smile); reads late twenties, upper end | [log](../../../production/generation-logs/sophie-portrait-age27-v02.yaml) |
| v03 | Approved prompt + the current Flow portrait as reference, asked to be younger | Rejected by the agent: almost unchanged, still early thirties | [log](../../../production/generation-logs/sophie-portrait-age27-v03.yaml) |

Once a take is approved: replace the Flow character's image (by hand, since AAO cannot edit characters; gap 4), enter the approved info text, keep a small copy here as `reference-front.webp`, then shortlist voices. The poster and business card will be regenerated with the approved face.

**How to sync:** AAO cannot read characters yet (gap 3 in [spec/flow-automation.md](../../../spec/flow-automation.md)). Until it can, either:

- the showrunner copies the fields above from Flow's Characters page, or
- an agent on the showrunner's computer opens the character page with playwright-cli (`playwright-cli -s=aao-web-gemini …`, read-only) and records what it shows.

Also download the character's reference image(s) with `aao flow download <project> <media>`. Keep a small copy here as `reference-front.png` once the showrunner approves it as the canonical face.

## APPROVED — info text to put into Flow (showrunner, 2026-11-22)

Short, visual and voice-focused, so Flow can use it. Story backstory stays in the repo.

```text
Dr. Sophie Goodman, late twenties, a young PhD moral philosopher who runs a small, loudly advertised "philosophical advocacy" practice in Albuquerque in 2030. Dark brown wavy hair loosely pinned up, warm light-medium skin, small gold hoop earrings, cream blouse under a deep burgundy tailored pantsuit. Confident, quick, theatrical when selling, quiet and precise when thinking. Wry half-smile; rarely raises her voice. Speaks American English, fast but clear, with dry humor.
```

Approved, with her age updated to late twenties to match the age lock. Next: enter it in Flow (by hand, because AAO cannot edit characters yet; gap 4).

**Check the portrait first.** The existing Flow portrait was generated from the tutorial prompt, which said "age about 33". If it doesn't read as late twenties, generate a new portrait with the prompt below. Then rebuild the character, or replace its image, before choosing the voice. Keep the old image only as a record.

```text
A realistic television casting reference photograph of a fictional woman named Sophie Goodman, age about 27. Dark brown wavy hair loosely pinned up, confident intelligent eyes, warm light-medium skin tone, subtle makeup, small gold hoop earrings, cream blouse and deep burgundy tailored blazer. Neutral light gray studio background, soft even lighting, camera at eye level, shoulders and face unobscured, natural expression. No writing, posters, props, extra people, watermarks or stylization. This is a consistent original fictional character design, not a portrait of a real actor.
```

## PROPOSED — voice selection

Pick one of Flow's built-in voices by name, and use it for every Sophie shot from then on.

- **Listen for:** a female voice that sounds late twenties, with a clear mid-range pitch, warm, fast and articulate. Not breathy, not announcer-like, and no accent beyond General American.
- **Test line** (read in two moods, salesy and serious): *"Legality is your lawyer's problem. Morality? That's mine."*
- Record the chosen voice name here and in `voice_in_flow`. Do not use a real person's voice or a sound-alike.

**Decision needed:** which voice. This is the showrunner's ear; an agent can shortlist voices, but not choose one.

## Other demo characters (PROPOSED, not created)

| Character | Needed for | Look anchor |
| --- | --- | --- |
| The Client (tech executive) | Commercial, consultation test | Man in his late forties, navy suit, pale blue shirt, tired expression |
| Daniel Park | Walk-and-talk test | Korean American, about 30, AI engineer/marketer, casual blazer, sneakers, tablet |
| Integrity Index panelist | Hearing test | Woman in her fifties, gray bob, charcoal suit, reading glasses |

Use original fictional people only, never real actors' likenesses. Each one gets a record like this file once it is created in Flow.
