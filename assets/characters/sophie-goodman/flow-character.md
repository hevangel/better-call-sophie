# Sophie Goodman — Google Flow character record

**Status:** the Flow character exists (created by hand during the tutorial); the **repo copy is not synced yet**. Info text and voice are **not set in Flow**, as the showrunner reported on 2026-11-22.

This file mirrors Sophie's character in Google Flow, so the repo stays the source of truth for what that character should be. The canon itself is in [spec/canon.md](../../../spec/canon.md) and [story/characters/sophie-goodman.md](../../../story/characters/sophie-goodman.md).

## Synced from Flow

Fill this in only from a real read of Flow (a command or the showrunner). Never guess.

```yaml
flow_project_title: null        # tutorial suggested "Better Call Sophie - Flow Experiments"; unverified
flow_project_id: null
flow_character_id: null
flow_character_name: null       # expected "Sophie Goodman"
reference_images: []            # Flow media names, plus repo/local copies once downloaded
info_text_in_flow: null         # currently empty, per the showrunner
voice_in_flow: null             # currently not set, per the showrunner
last_synced: null
synced_by: null                 # aao command, or "showrunner by hand"
```

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
