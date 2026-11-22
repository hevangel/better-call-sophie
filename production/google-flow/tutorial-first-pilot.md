# Google Flow: First Pilot Runs for *Better Call Sophie*

**Audience:** First-time Google Flow user. **Verified:** 2026-11-14 against Google's public Flow Help pages. **Status:** Production tutorial; sample prompts and examples are proposals, not show canon.  
> **Update 2026-11-22:** Sophie's age is now LOCKED at 26–28, and the era at 2030. The prompts below are kept as they were run. For new work, use the approved character record `assets/characters/sophie-goodman/flow-character.md`, not the "about 33" / "early thirties" wording here.

**Goal:** Make a convincing 20–30-second *technical proof of concept* before attempting a full episode of the show.  
**Starting tool:** [Google Flow](https://flow.google.com/) in Chrome or Edge on desktop.

> **The most important principle:** Test **one problem at a time**. First make Sophie appear; then give her a stable face and voice; then make a two-person exchange; finally edit the best shots together. Do **not** try to create a full pilot episode with one prompt.

## 0. What you will have at the end

1. A short Goodman-style **direct-to-camera commercial** for Sophie.
2. A consistent visual/voice **Sophie Goodman character** in two different shots.
3. A **three-shot dialogue scene** with a client, assembled in Flow's Scenebuilder.
4. Downloaded clip/scene files, their exact prompts, a shot log, and a list of observed problems.

You should be able to judge whether Flow is viable for this show based on **character identity, reliable spoken dialogue, lip synchronization, spatial continuity, and editability**.

This first run does **not** need courtroom-scale scenes, elaborate stunts, 4K, or an entire episode. All story details below are fictional rehearsal material, not locked canon.

## 1. First setup, with exact UI steps

1. On a desktop, open [https://flow.google.com/](https://flow.google.com/) in Chrome or Edge and sign in to your subscribed Google account.
2. Click **+ New project**.
3. Name it `Better Call Sophie - Flow Experiments` (a separate space from future approved episode work).
4. In the project's prompt box, click the current model/generation selector. **Select Video**, not Image.
5. Select a model, output count (**1**), aspect ratio (**16:9 landscape**), duration (normally **6–8 seconds**), and resolution. The control labels can change as Flow evolves; check the current settings immediately before generating.
6. Check the remaining credits under your profile icon. Also examine the active model's **credit cost per generation** in the generation-settings menu.

**Recommended learning order:** text-to-video → character creation/references → separate dialogue shots → Scenebuilder → downloads. Do not begin with the Flow Agent, complex editing or video extension: those are useful later, but obscure what the underlying generation can do.

For guidance on where the UI controls are, see:
- [Google: Get started with Flow](https://support.google.com/flow/answer/16353333)
- [Google: Create videos in Flow](https://support.google.com/flow/answer/16353334)
- [Google: Models and feature support](https://support.google.com/flow/answer/16352836)

### Models and a small experimental budget (as documented 2026-11-14)

| Model | Recommended role | Current published credit cost | Important limits |
| --- | --- | --- | --- |
| **Omni Flash 1.2 360p** | Lowest-cost composition/continuity tests | **1 credit per second** | Subscribers can generate 3–15s; all users 3–10s |
| **Omni Flash 1.2 720p** | Dialogue and better-quality candidate takes | **3 credits per second** | Same duration tiers as above |
| **Veo 3.1 Lite 720p** | Alternative low-cost 720p baseline | **10 credits per 4/6/8s generation** for non-Ultra; 5 for Ultra | Ingredients mode is limited to 8s; no video-to-video edits or Extend |
| **Veo 3.1 Fast/Quality or Omni Flash 1.1** | Do not build a new workflow around these | Varies | Google says they retire **2026-12-05** |

Check your current menu before using any number: model costs, durations, entitlement and regions can change. Google also documents 50 daily trial credits plus monthly credits by subscription tier; your actual balances are account-specific.

**Example budget:** Six **6-second** draft generations with Omni Flash 1.2 at 360p are **36 credits** if charged at the published one-credit/second rate (and if each generation makes one output). Six matching 720p attempts would be **108 credits**. This is for learning and iteration, not an estimate of a completed episode.

Official pricing: [Flow credits](https://support.google.com/flow/answer/16526234). Credits are **per output generation**, not necessarily per button press: requesting two outputs may cost twice as much.

## 2. Experiment A — Sophie’s eight-second TV advertisement

**Goal:** Test basic action, shot framing, fictional performance, speech accuracy and tone without continuity requirements.

1. Confirm **Video**, **16:9**, **one output**, and **8 seconds** (or nearest supported option).
2. For the very first attempt, select **Omni Flash 1.2** at **360p** or a low-cost option visible in your account.
3. Paste this prompt in the standard Flow prompt box:

```text
A fictional prestige television dark-comedy commercial, 16:9 landscape.

Sophie Goodman, a charismatic female philosophical consultant in her early thirties, has dark loosely pinned wavy hair and wears an elegant deep burgundy pantsuit with a cream blouse. She stands in a modest Albuquerque consulting office with a bookshelf of philosophy texts, a chalkboard of hand-drawn ethical diagrams, and a bright yellow-red advertising accent. Warm afternoon light, realistic faces, carefully composed medium shot, static camera.

She smiles directly at the viewer and speaks clearly in English:
"Legality is your lawyer's problem. Morality? That's mine."

After speaking, she gives a tiny mischievous smile. Dry, confident, witty professional delivery. Natural room tone. Exactly one speaker.

No subtitles, no titles, no logos, no extra people, no cutaways, no camera shake.
```

4. Generate **one** result and watch it twice: once for storytelling, once for technical flaws.
5. Write down: did the correct words appear? Was the voice understandable? Did Sophie look like an appropriate television protagonist? Was her face/hair consistent throughout? Were hands, mouth movements, book spines and background stable?
6. If the first result fails, change **one variable** (e.g., shorten the line, change the camera framing, or use a character reference in Experiment B), then generate a second take. Avoid rewriting all details simultaneously.

**Failure is useful evidence.** If spoken dialogue keeps failing, make an equally good **silent** image-to-video performance and add synthetic dialogue as a separate post-production layer later. Do not let audio problems prevent evaluation of shot quality.

**Do not ask the video model to render perfect Goodman business-card typography.** Add the large slogan and phone number later as a title overlay; your existing business-card concept art is a brand reference, not an accurate text-generation template.

## 3. Experiment B — Build Sophie as a reusable character

**Goal:** The *same fictional actor* must plausibly appear in different shots. Do not treat the face in the poster as automatically stable across generations.

### Step B1: Make a clean character reference image

Your existing README artwork establishes visual direction:
- [TV poster](../../assets/marketing/poster-tv-4x3.webp)
- [Business-card front](../../assets/marketing/business-card-front.webp)

These contain lots of advertising text, props and backgrounds, so they are **not ideal primary character references**. Create a cleaner portrait inside Flow instead:

1. In the project, change the generation type to **Image** (Flow supports Nano Banana image models).
2. Enter:

```text
A realistic television casting reference photograph of a fictional woman named Sophie Goodman, age about 33. Dark brown wavy hair loosely tied up, confident intelligent eyes, warm light-medium skin tone, subtle makeup, small gold hoop earrings, cream blouse and deep burgundy tailored blazer. Neutral light gray studio background, soft even lighting, camera at eye level, shoulders and face unobscured, natural expression. No writing, posters, props, extra people, watermarks or stylization. This is a consistent original fictional character design, not a portrait of a real actor.
```

3. Inspect the result. If satisfied, save it as a reference asset in the Flow project.
4. Optionally generate a **second** matched reference (three-quarter profile or full-body) with the *same identity and outfit*. Do not use a differently generated face as an independent "reference" unless you confirm they match.

### Step B2: Use Flow's Characters feature

As of November 2026, Google's Flow Help documents a dedicated **Characters** section that can bundle one or two visual references and a selected voice.

1. Open the left-side **Characters** section.
2. Choose **New Character**, or the equivalent character-creation control.
3. Add the approved Sophie portrait (one image is sufficient) and, if available, the matching second image.
4. Name the character **Sophie Goodman**.
5. Choose a voice, listening to the available samples. For later tests, stick to the same voice.
6. Save the character and use `@Sophie Goodman` in subsequent generation prompts where the UI supports character references.

Google's character guide: [Manage projects, assets and characters](https://support.google.com/flow/answer/16935308). Also see [Add visual and voice references](https://support.google.com/flow/answer/16353334).

If a specific character or voice feature is missing on your account, use **Video → Ingredients** and the clean portrait as a visual reference. To add an ingredient, click **Add Image** or drag the image into the prompt and say how it should be used. Avoid combining too many incompatible reference photos.

### Step B3: Generate two continuity shots

Run these as separate generations using the **same Sophie character reference** and selected voice when supported.

**Shot B1 — Reception office, 6–8s**

```text
@Sophie Goodman enters her modest philosophical consulting office in Albuquerque. She wears the same deep burgundy pantsuit, cream blouse, hairstyle and jewelry as her character reference. Medium-wide locked-off cinematic shot; she sets a worn philosophy book on a desk, surveys the room, and raises one eyebrow with a restrained smile. Late-afternoon warm light. No dialogue. Natural office room tone. No added text or new characters.
```

**Shot B2 — Seated at desk, 6–8s**

```text
@Sophie Goodman sits behind her desk in the same office, wearing exactly the same burgundy suit, cream blouse, hairstyle and gold earrings. Medium-close eye-level shot. She opens a worn philosophy book, marks a line with a pencil, then looks up at someone just off-camera. Cinematic realism, warm light, restrained confident body language. No dialogue. No titles, subtitles or logos.
```

**Compare B1 and B2** side by side. Check face shape, hair, age, wardrobe, jewelry, color palette and office architecture. If they don't match, refine the *reference set and prompting strategy*, not just add more adjectives.

> **Optional frame trick:** Pause on a good frame of a generated clip and choose **Save frame**. The frame can be used as a new ingredient, **start frame** or **end frame** for the next shot. This is documented in Flow's [editing guide](https://support.google.com/flow/answer/16935718).

## 4. Experiment C — A genuine two-person philosophical scene

**Goal:** Test narrative continuity and spoken exchanges. Use separate close-ups: two speakers in one short generation is a harder problem and can confuse who is speaking.

**Rehearsal scenario:** A technology executive wants philosophical help justifying his replacement of employees with AI.

Create a fictional second character, **The Client**, with a stable reference image: male executive in his late forties, navy suit, pale blue shirt, tired expression. Avoid naming a real person. If a character asset is available, use it. Keep both shots in the same small office, same day and lighting.

**C1 — Client asks for help**

```text
A fictional television drama shot in Sophie Goodman's Albuquerque philosophical consulting office. Medium close-up on a worried male corporate executive in his late forties, navy suit, seated opposite Sophie. Camera from Sophie's shoulder; only the edge of her burgundy sleeve is visible in the foreground. Warm late-afternoon lighting, steady camera, natural office ambience.

The executive says clearly in English:
"Can you prove I'm a good person?"

He pauses and waits. Exactly one visible speaker. No subtitles or text.
```

**C2 — Sophie answers**

```text
@Sophie Goodman in the same Albuquerque philosophical consulting office and same deep burgundy suit. Reverse medium close-up from the client's eyeline, matching the previous shot's warm light and camera height. Sophie studies the client, leans forward slightly and says clearly in English:

"No. But I can make your critics regret calling you a bad one."

Then she smiles briefly. Only Sophie speaks. No subtitles, logos or text.
```

**C3 — Client reaction (silent)**

```text
Matching close-up of the same male executive in the same office, navy suit, same lighting and camera axis. He pauses in disbelief, glances down at the Goodman business card in his hand, then looks up with a cautious smile. No speech, no titles or subtitles. Natural office room tone.
```

If you cannot obtain a coherent two-person scene after several attempts, record the reasons. A **successful short silent shot** with separately recorded voice can be more useful than a beautifully rendered but unusable line of dialogue.

## 5. Assemble the scene inside Google Flow

Google Flow includes **Scenebuilder** for ordering, trimming, previewing and downloading a clip sequence.

1. Hover over the chosen clip; select **More → Add to Scene**.
2. Add shots **C1 → C2 → C3** in order.
3. Use the scene controls to move shots or trim their beginnings/ends.
4. Preview the sequence, especially the conversational rhythm, cut on speaker and sound transitions.
5. Download the scene as a single video. Also download the **individual selected clips** separately as your recoverable sources.

See [Google: Edit videos and build scenes](https://support.google.com/flow/answer/16935718) and [Google: Download assets](https://support.google.com/flow/answer/16935308).

Your *first* useful result should be a **roughly 18–24 second exchange**, not a polished television episode. Keep silent pauses short but intelligible.

## 6. Optional: Extend a successful shot

If you have a good clip that ends too soon, open it, choose **Extend**, select added duration, and prompt the next action. Google's current documentation limits **Extend** to eligible subscribers using **Omni Flash 1.2** (as of Nov. 2026); some edit modes cannot be applied afterward. Test this only after you have already saved the original clip.

Example:

```text
Continue the existing shot in the same office with the same Sophie Goodman appearance and locked-off camera. After her line, Sophie silently places the philosophy book down, waits for the client's reaction, then gives a tiny knowing smile. Do not introduce another person, costume change or camera cut.
```

Refer to [Google: Extend and edit](https://support.google.com/flow/answer/16935718). Do not use extensions to hide a weak initial shot; fix the source first.

## 7. Download, name and log everything

Google Flow's project screen supports **More → Download** on an asset; you can also download project content. When choosing formats, prefer a standard video file for editing rather than a GIF. Keep the original downloaded file intact.

Use this structure in your *local working directory* (large videos should not be committed to Git):

```text
BetterCallSophie-Flow-Tests/
  references/
    sophie-clean-portrait.png
    client-clean-portrait.png
  exports/
    s01e01-test-a-commercial-v01.mp4
    s01e01-test-b1-office-v01.mp4
    s01e01-test-b2-desk-v01.mp4
    s01e01-test-c1-client-v01.mp4
    s01e01-test-c2-sophie-v01.mp4
    s01e01-test-c3-reaction-v01.mp4
    test-c-scene-assembly-v01.mp4
  notes/
    shots.csv
    observations.md
```

Filename extensions reflect your **actual** downloaded file formats; don't rename a file merely to pretend it is MP4.

When you have real outputs, log text metadata in the GitHub repository under `production/generation-logs/`. For each generation, use a record like:

```yaml
id: s01e01-test-c2-sophie-v01
status: generated
tool: Google Flow
model: "Omni Flash 1.2"     # replace with the actual model selected
aspect_ratio: "16:9"
duration_seconds: 8         # actual output duration, not target
resolution: "360p"          # replace with observed value
references:
  - "Sophie Goodman character (Flow asset ID if available)"
export: "LOCAL_PATH_NOT_IN_GIT"
prompt_file: "SEE_TUTORIAL_C2"
dialogue_match: unreviewed
face_consistency: unreviewed
lip_sync: unreviewed
accepted: false
notes: "Fill in only after examining the exported clip"
```

Don't fabricate generation IDs, credits charged, durations or model versions. Git is the source of truth for prompts and decisions; Flow and local production storage hold actual generated assets.

## 8. Troubleshooting: what to change first

| Symptom | First thing to try |
| --- | --- |
| Sophie looks like a new actor in each shot | Use a clean approved Character or Ingredients reference; stop using a text-heavy poster as the only identity anchor |
| Dialogue is incorrect or garbled | Cut dialogue length in half and use exactly one speaker per shot; consider separate voice production |
| Mouth movement doesn't match | Try a closer shot and simpler line; evaluate voice-reference features in Omni Flash; if it remains poor, choose a non-speaking shot |
| Advertising words are misspelled | Add exact text in editing software, not in the video prompt |
| Camera moves unpredictably | Describe a locked-off or very slow single movement and remove competing camera instructions |
| Clothing or props shift | State exact wardrobe and props and reuse visual references/frames |
| Two-person conversation is inconsistent | Generate individual single-speaker close-ups and bridge with a reaction shot |
| Results eat too many credits | Switch draft work to 360p Omni, one output, short duration; check per-generation price before each batch |
| Flow gives a content-policy block | Simplify/replace material, inspect current policies; do not attempt to evade safety restrictions |
| Finished clip cannot be found | Open project's **Videos** list, search its prompt text, inspect History/collections, and download assets promptly |

Google specifically recommends clean reference images, consistent styling across ingredients, and prompts that don't contradict those images: [Creating Flow videos](https://support.google.com/flow/answer/16353334).

## 9. Scorecard: decide whether we are ready for a scripted pilot

Score each category from **0 (failure)** to **5 (production-ready for a rough cut)**:

| Criterion | 0–5 | What you examine |
| --- | --- | --- |
| Sophie identity across shots | ___ | Same face, age, hair, outfit |
| Dialogue transcription | ___ | Exact words and intelligibility |
| Lip synchronization | ___ | Does speech visually match? |
| Cinematography | ___ | Camera, lighting, useful framing |
| Physical continuity | ___ | Props, layout, eyelines, gestures |
| Editing usability | ___ | Can the shots be cut together naturally? |
| Cost efficiency | ___ | Quality obtained per credit spent |

**Practical milestone:** At least **4/5** for Sophie identity and editability and **3/5** for dialogue/lip sync before we scale up. These are project-created editorial thresholds, not Google's published metrics.

Write a conclusion after testing:
- What can Flow reliably produce?
- Which shots still need manual editing or another AI model?
- How many credits did the tests actually cost?
- Which reference images and voices are worth locking?
- Which single problem should we solve before writing a full pilot?

## 10. What's next after the first tests?

1. **Approve a canonical Sophie reference** (face, clothing, voice; include a reusable character ID and export).
2. **Choose the exact pilot format** (runtime, language, aspect ratio and editorial target).
3. Write the real `S01E01` screenplay, not merely a prompt.
4. Translate it into shots and separate dialogue performances, then generate scene by scene.
5. Assemble and mix in Flow or in a dedicated editor/automation system. This repo already pins optional third-party tools under `external/`; using any of them requires separate setup and licensing review.

## Sources (official Google documentation, checked 2026-11-14)

- https://support.google.com/flow/answer/16353333 — access, browser and account requirements.
- https://support.google.com/flow/answer/16353334 — create videos, Frames, Ingredients, character/voice references.
- https://support.google.com/flow/answer/16352836 — model capabilities, duration and retirement notes.
- https://support.google.com/flow/answer/16526234 — current credit schedule and account balance.
- https://support.google.com/flow/answer/16935308 — project management, character creation, downloading.
- https://support.google.com/flow/answer/16935718 — editing, frame extraction, extension and Scenebuilder.

**Rights reminder:** This is an unofficial fan-made concept involving Saul Goodman. Keep experiments private during technical development unless rights and publication decisions are reviewed. Do not use actual actor likenesses, franchise footage, unlicensed voices, or soundtracks.
